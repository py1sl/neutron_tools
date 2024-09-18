# -*- coding: utf-8 -*-
"""
Fispact output file reader
S Lilley
March 2019

Amended from the pyne version i wrote some time ago

Module for parsing FISPACT output data
FISPACT and FISPACT-II are bateman equation solvers for transmutation
and fission product yield calculations.  FISPACT-II is developed and maintained
by the UKAEA.
it supports not only neutron irradiation but gamma, proton, deuteron and triton
irradiation. it has support for self shielding and can read endf format nuclear
data
this module has methods for parsing the fispact output file,
extracting data, processing the data

"""
import argparse
import neut_utilities as ut
import numpy as np
import pandas as pd


class FispactOutput():
    """ fispact output data"""

    def __init__(self):
        """ define data"""
        self.file_name = ""
        self.sumdat = []
        self.timestep_data = []
        self.num_cool_step = 0   # number of steps after zero keyword
        self.num_irrad_step = 0  # number of steps with flux > 0
        self.version = ""
        self.isFisII = False
        self.cpu_time = 0.0
        self.tot_irrad_time = 0.0
        self.tot_fluence = 0.0
        self.ave_flux = 0.0
        self.time_days = []


class FispactTimeStep():
    """ data for an individual time step can be heating or cooling """

    def __init__(self):
        self.step_num = 1
        self.step_length = 0
        self.flux_amp = 0
        self.is_cooling = False
        self.num_nuclides = 0
        self.alpha_act = 0     # bq
        self.beta_act = 0      # bq
        self.gamma_act = 0     # bq
        self.total_act = 0     # bq
        self.total_act_no_trit = 0   # bq
        self.alpha_heat = 0    # kw
        self.beta_heat = 0     # kw
        self.gamma_heat = 0    # kw
        self.total_heat = 0    # kw
        self.total_heat_no_trit = 0   # kw
        self.num_fissions = 0
        self.neutron_flux = 0   # n/cm**2/s
        self.initial_mass = 0   # kg
        self.total_mass = 0     # kg
        self.density = 0        # g/cc
        self.actinide_burn = 0   # %
        self.appm_h1 = 0
        self.appm_h2 = 0
        self.appm_h3 = 0
        self.appm_he3 = 0
        self.appm_he4 = 0

        self.dom_data = []
        self.inventory = []
        self.gspec = []
        self.composition = []


def read_fis_out(path):
    """ parse a fispact output file
        returns fo, a fispact output object
    """

    fo = FispactOutput()
    fo.file_name = path
    lines = ut.get_lines(path)

    fo.version = check_fisp_version(lines)
    fo.isFisII = isFisII(lines)
    fo.sumdat = read_summary_data(lines)

    fo.ave_flux = read_parameter(lines, "Mean flux")
    fo.tot_irrad_time = read_parameter(lines, "Total irradiation time")
    fo.tot_fluence = read_parameter(lines, "Total fluence")
    fo.num_irrad_step = read_parameter(lines, "Number of on-times")

    if fo.isFisII:
        search_string = "fispact run time"
    else:
        search_string = "CPU Time used for case"
    fo.cpu_time = read_parameter(lines, search_string)

    # find where each time step starts
    time_step_inds = []
    for index, line in enumerate(lines):
        if len(line) > 0:
            if line[0:7] == "1 * * *":
                time_step_inds.append(index)

    # Parse time step data
    for i in range(1, len(time_step_inds)):
        start = time_step_inds[i]
        if i + 1 < len(time_step_inds):
            end = time_step_inds[i + 1]
        else:
            end = None
        data = lines[start:end]
        fo.timestep_data.append(read_time_step(data, i))

    return fo


def read_time_step(lines, i):
    """ reads a particular time step """
    ts = FispactTimeStep()
    ts.step_num = i + 1

    ts.step_length = float(lines[0][50:60])

    ind = ut.find_ind(lines, "TOTAL NUMBER OF NUCLIDES PRINTED IN INVENTORY")
    ts.num_nuclides = int(lines[ind][50:])

    ind = ut.find_ind(lines, "ALPHA BECQUERELS")
    ts.alpha_act = float(lines[ind][22:34])
    ts.beta_act = float(lines[ind][54:66])
    ts.gamma_act = float(lines[ind][87:99])

    ind = ut.find_ind(lines, "TOTAL ACTIVITY FOR ALL MATERIALS ")
    ts.total_act = float(lines[ind][40:51])

    ind = ut.find_ind(lines, "TOTAL ACTIVITY EXCLUDING TRITIUM ")
    ts.total_act_no_trit = float(lines[ind][40:51])

    ind = ut.find_ind(lines, "TOTAL ALPHA HEAT")
    ts.alpha_heat = float(lines[ind][40:51])
    ts.beta_heat = float(lines[ind + 1][40:51])
    ts.gamma_heat = float(lines[ind + 2][40:51])
    ts.total_heat = float(lines[ind + 2][90:101])
    ts.initial_mass = float(lines[ind + 3][40:51])
    ts.total_heat_no_trit = float(lines[ind + 3][90:101])
    ts.total_mass = float(lines[ind + 4][40:51])
    ts.neutron_flux = float(lines[ind + 5][40:51])

    ts.num_fissions = lines[ind + 6][39:51]
    # added check for E as if <=1E-100 the E is dropped
    if "E" in ts.num_fissions:
        ts.num_fissions = float(ts.num_fissions)

    ts.actinide_burn = float(lines[ind + 6][90:101])

    ind = ut.find_ind(lines, "DENSITY")
    ts.density = float(lines[ind][78:86])

    if ts.total_act > 0.0:
        # added check for E as if <=1E-100 the E is dropped
        ind = ut.find_ind(lines, "APPM OF He  4 ")
        ts.appm_he4 = lines[ind][23:33]
        if "E" in ts.appm_he4:
            ts.appm_he4 = float(ts.appm_he4)
        ts.appm_he3 = lines[ind + 1][23:33]
        if "E" in ts.appm_he3:
            ts.appm_he3 = float(ts.appm_he3)
        ts.appm_h3 = lines[ind + 2][23:33]
        if "E" in ts.appm_h3:
            ts.appm_h3 = float(ts.appm_h3)
        ts.appm_h2 = lines[ind + 3][23:33]
        if "E" in ts.appm_h2:
            ts.appm_h2 = float(ts.appm_h2)
        ts.appm_h1 = lines[ind + 4][23:33]
        if "E" in ts.appm_h1:
            ts.appm_h1 = float(ts.appm_h1)
        ind = 1

        ts.dom_data = parse_dominant(lines)
        ts.composition = parse_composition(lines)
        ts.gspec = parse_spectra(lines)
    ts.inventory = parse_inventory(lines)

    return ts


def check_fisp_version(data):
    """ Checks which version of fispact was used to produced data
        requires a list with each element being a line from the
        fispact output file
        returns a string of the version name
    """

    sub = "FISPACT VERSION 07.0/0"
    data = data[:50]
    if next((s for s in data if sub in s), None):
        v = "FISP07"
    else:
        v = "FISPACT-II"
    return v


def isFisII(data):
    """boolean check if file is fispact-ii output """
    v = check_fisp_version(data)
    if v == "FISPACT-II":
        return True
    else:
        return False


def find_summary_block(data, fisII):
    """
    Finds the start and end of the summary block in the data.
    """
    if fisII:
        cool_str = " -----Irradiation Phase-----"
    else:
        cool_str = "  COOLING STEPS"

    try:
        start_ind = data.index(cool_str)
        end_ind = next(i for i, line in enumerate(data) if "0 Mass" in line)
    except ValueError as e:
        raise ValueError("Summary data section could not be found in the file.") from e

    return start_ind, end_ind

def read_summary_data(data):
    """ Processes the summary block at the end of the file"""

    fisII = isFisII(data)
    start_ind, end_ind = find_summary_block(data, fisII)
    end_ind = [i for i, line in enumerate(data) if "0 Mass" in line]
    sum_lines = data[start_ind + 1:end_ind[0]]
    sum_data = []
    time_yrs = []
    act = []
    act_un = []
    dr = []
    dr_un = []
    heat = []
    heat_un = []
    ing = []
    ing_un = []
    inhal = []
    inhal_un = []
    trit = []
    cooling = []
    to = 0
    is_cooling = False

    for line in sum_lines:
        if fisII:
            if line[1] == "-":
                to = time_yrs[-1]
                is_cooling = True

            else:
                time_yrs.append(float(line[24:32]) + to)
                act.append(float(line[35:43]))
                dr.append(float(line[58:66]))
                heat.append(float(line[81:89]))
                ing.append(float(line[104:112]))
                inhal.append(float(line[127:135]))
                trit.append(float(line[150:158]))
                cooling.append(is_cooling)

        else:
            time_yrs.append(line[20:28])
            act.append(line[31:39])
            dr.append(line[54:62])
            heat.append(line[77:85])
            ing.append(line[100:108])
            inhal.append(line[123:131])
            trit.append(line[146:154])

    sum_data.append(time_yrs)
    sum_data.append(act)
    sum_data.append(dr)
    sum_data.append(heat)
    sum_data.append(ing)
    sum_data.append(inhal)
    sum_data.append(trit)
    sum_data.append(act_un)
    sum_data.append(dr_un)
    sum_data.append(heat_un)
    sum_data.append(ing_un)
    sum_data.append(inhal_un)
    sum_data.append(cooling)

    # convert to dataframe
    col_heads = ["time_years", "act", "dose_rate", "heating", "ingestion",
                 "inhalation", "tritium", "act_un", "dr_un", "heat_un",
                 "ing_un", "inhal_un", "is_cooling"]
    sum_data = pd.DataFrame(sum_data)
    sum_data = sum_data.transpose()
    sum_data.columns = col_heads

    # add columns for time in days, hrs, seconds
    sum_data["time_days"] = sum_data["time_years"] * 365.4
    sum_data["time_hours"] = sum_data["time_years"] * 365.4 * 24
    sum_data["time_secs"] = sum_data["time_years"] * 365.4 * 24 * 3600

    return sum_data


def retrieve_cooling_data(sum_data):
    """ filters the data summary to only include data from the cooling
    phase """
    cooling_data = sum_data[sum_data["is_cooling"] == True]
    return cooling_data


def parse_dominant(data):
    """parse dominant nuclides section and return a list of lists """
    p1_ind = ut.find_ind(data, "DOMINANT NUCLIDES")
    data = data[p1_ind:]
    d1_ind = ut.find_ind(data, "(Bq) ")
    d2_ind = ut.find_ind(data, "GAMMA HEAT")
    topset = data[d1_ind + 2:d2_ind - 1]
    topset = np.array(topset)
    lowerset = data[d2_ind + 3:]

    act_nuc = []
    act = []
    act_percent = []
    heat_nuc = []
    heat = []
    heat_percent = []
    dr_nuc = []
    dr = []
    dr_percent = []
    gheat_nuc = []
    gheat = []
    gheat_percent = []
    bheat_nuc = []
    bheat = []
    bheat_percent = []

    for tl in topset:
        act_nuc.append(tl[7:13].replace(" ", ""))
        act.append(float(tl[15:25]))
        act_percent.append(float(tl[27:36]))
        heat_nuc.append(tl[38:44].replace(" ", ""))
        heat.append(float(tl[46:56]))
        heat_percent.append(float(tl[58:67]))
        dr_nuc.append(tl[69:75].replace(" ", ""))
        dr.append(float(tl[77:87]))
        dr_percent.append(float(tl[89:98]))

    for ll in lowerset:
        if ll[0] == "1":
            break
        gheat_nuc.append(ll[7:13].replace(" ", ""))
        gheat.append(float(ll[15:25]))
        gheat_percent.append(float(ll[27:36]))
        bheat_nuc.append(ll[38:44].replace(" ", ""))
        bheat.append(float(ll[46:56]))
        bheat_percent.append(float(ll[58:67]))

    dom_data = pd.DataFrame()
    dom_data["act_nuc"] = act_nuc
    dom_data["act"] = act
    dom_data["act_percent"] = act_percent
    dom_data["heat_nuc"] = heat_nuc
    dom_data["heat"] = heat
    dom_data["heat_percent"] = heat_percent
    dom_data["dr_nuc"] = dr_nuc
    dom_data["dr"] = dr
    dom_data["dr_percent"] = dr_percent
    dom_data["gheat_nuc"] = gheat_nuc
    dom_data["gheat"] = gheat
    dom_data["gheat_percent"] = gheat_percent
    dom_data["bheat_nuc"] = bheat_nuc
    dom_data["bheat"] = bheat
    dom_data["bheat_percent"] = bheat_percent

    return dom_data


def parse_composition(data):
    """ parse compostions section
        returns dataframe with two columns, one with name of element,
        one with the number of atoms
    """
    start = ut.find_ind(data, "COMPOSITION  OF  MATERIAL  BY  ELEMENT") + 5
    end = ut.find_ind(data, "GAMMA SPECTRUM AND ENERGIES/SECOND") - 3

    data = data[start:end]
    ele_list = []
    atoms = []

    for line in data:
        ele_list.append(line[12:14])
        atoms.append(float(line[20:30]))

    composition = pd.DataFrame()
    composition["element"] = ele_list
    composition["atoms"] = atoms
    
    # Calculate the total number of atoms
    total_atoms = sum(atoms)

    # Compute the atom fraction for each element
    composition["atom_fraction"] = composition["atoms"] / total_atoms

    return composition


def parse_spectra(data):
    """ reads gamma spectra data for each timestep
        returns list of length 24 corresponding to 24 gamma energy groups
        data is in gamma/s/cc
    """
    p1 = ut.find_ind(data, "GAMMA SPECTRUM AND ENERGIES/SECOND")
    
    # check data is long enough - checks for bad files
    if len(data) < p1 + 31:
        raise ValueError("data is too short for complete gamma spectra")
    
    data = data[p1 + 7:p1 + 31]
    spectra = []
    for line in data:
        try:
            spectra.append(float(line[130:141]))
        except ValueError as e:
            raise ValueError(f" Error parsing gamma spec line: {line} ") from e
    return spectra


def parse_inventory(data):
    """ parse inventory data
        returns a list of lists with all data from the inventory
        section of the times step in order:
        nuclide name,
        # of atoms,
        mass in grams,
        activity in bq,
        beta energy in kw
        alpha energy in kw
        gamma energy in kw
        dose rate in Sv/hr
    """
    inv = []
    p2 = ut.find_ind(data, "0  TOTAL NUMBER OF NUCLIDES PRINTED IN INVENTORY")
    data = data[4:p2]
    for nuc in data:
        nuc_data = [nuc[2:8], float(nuc[14:25]),
                    float(nuc[28:37]), float(nuc[40:49]),
                    float(nuc[52:61]), float(nuc[64:72]),
                    float(nuc[75:84]), float(nuc[87:96])]
        inv.append(nuc_data)

    col_heads = ["nuclide", "atoms", "mass", "act", "b_energy", "a_energy",
                 "g_energy", "dose_rate"]
    inv = pd.DataFrame(inv, columns=col_heads)
    inv["element"] = inv["nuclide"].astype(str).str[0:2]
    inv["element"] = inv["element"].str.strip()
    inv["A"] = inv["nuclide"].astype(str).str[2:]
    inv["A"] = inv["A"].str.strip()
    inv["nuclide"] = inv["nuclide"].str.replace(" ", "")

    return inv


def read_parameter(data, sub):
    """ finds and cleans integral values in each timestep"""
    ind = ut.find_ind(data, sub)
    line = data[ind]
    line = line.split("=")
    line = line[1].strip()
    line = line.split(" ")
    param = float(line[0])
    return param


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads fispact output file")
    parser.add_argument("input", help="path to the fispact output file")
    args = parser.parse_args()

    read_fis_out(args.input)
