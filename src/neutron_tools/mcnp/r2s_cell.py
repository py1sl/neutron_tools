import json
import argparse
import pandas as pd
import os
import shutil
from pathlib import Path
import subprocess

from neutron_tools.mcnp import mcnp_output_reader as mor
from neutron_tools.mcnp import mcnp_input_reader as mir
from neutron_tools.fispact import fispact_output_reader as fisor
from neutron_tools.fispact import fispact_fluxes_writer as ffw
from neutron_tools.fispact import fispact_files_file_reader as ffr
from neutron_tools.utilities import neut_utilities as ut
from neutron_tools.utilities import neut_constants as nc



class usr_inputs:
    """ input from usr read from json file """
    def __init__(self):
        self.mc_input = None
        self.mc_ouput = None
        self.mc_gamma_input = None
        self.mc_code = "MCNP"
        self.files_file = None
        self.fispact_template = None
        self.tallies = None
        self.cells = None
        self.fispact_path = None
        self.cooling_step = 1
        self.norm_factor = 1.0


def read_config(config_fp):
    """ reads the json file and assigns values """
    if not Path(config_fp).exists():
        raise FileNotFoundError(f"config file {config_fp} not found")

    with open(config_fp) as f:
        config = json.load(f)

    inputs = usr_inputs()
    for key in config.keys():
        if key == "mc_input":
            inputs.mc_input = config["mc_input"]
        elif key == "mc_output":
            inputs.mc_output = config["mc_output"]
        elif key == "mc_gamma_input":
            inputs.mc_gamma_input = config["mc_gamma_input"]
        elif key == "mc_code":
            inputs.mc_code = config["mc_code"]
        elif key == "files_file":
            inputs.files_file = config["files_file"]
        elif key == "fispact_template":
            inputs.fispact_template = config["fispact_template"]
        elif key == "tallies":
            inputs.tallies = config["tallies"]
        elif key == "cells":
            inputs.cells = config["cells"]
        elif key == "fispact_path":
            inputs.fispact_path = config["fispact_path"]
        elif key == "cooling_step":
            inputs.cooling_step = config["cooling_step"]
        elif key == "norm_factor":
            inputs.norm_factor = config["norm_factor"]
        else:
            raise ValueError('input not recognised')

    return inputs


def get_cells_mcnp(mcnp_output, particle="neutrons", tallies=None):
    """ reads from mcnp output and gets cell numbers from tallies"""
    cell_numbers = {}
    tally_data = []
    for tal in mcnp_output.tally_data:
        if tal.tally_type == '4' and tal.particle == particle:
            if tallies is not None:
                if tal.number in tallies:
                    cell_numbers.update({cell: tal.number for cell in tal.cells})
                    tally_data.append(tal)
            else:
                cell_numbers.update({cell: tal.number for cell in tal.cells})
                tally_data.append(tal)

    cell_numbers = {int(k): v for k, v in cell_numbers.items()}
    return cell_numbers, tally_data


def get_cell_data(mc_input, tally_cell_list):
    """ get the cell material, mass and volume data"""
    cell_data = []
    for cell_num in tally_cell_list:
        if mir.check_cell_exists(cell_num, mc_input.cells):
            cell = mir.get_cell(cell_num, mc_input.cells)
            cell_data.append(cell)
        else:
            raise ValueError(f"Cell: {cell_num} not found in input")

    header = ["number", "material", "density"]
    cell_df = None
    for i, cell in enumerate(cell_data):
        cell_series = {"number": cell.number, "material": cell.mat, "density": cell.density}
        cell_series = pd.DataFrame(cell_series, columns=header, index=[i])
        if isinstance(cell_df, pd.DataFrame):
            cell_df = pd.concat([cell_df, cell_series])
        else:
            cell_df = cell_series

    return cell_df


def write_collapse(path, groups_count):
    """ writes the collapse stage fispact input file"""
    lines = [
        "<< -----collapse cross section data----- >>",
        "CLOBBER",
        f"GETXS 1 {groups_count}",
        "FISPACT",
        "* COLLAPSE",
        "END",
        "* END OF RUN",
    ]
    ut.write_lines(path, lines)
    return 0


def write_array(path):
    """ writes the array stage fispact input file"""
    lines = ["<< -----condense decay data----- >>",
             "CLOBBER",
             "SPEK",
             "GETDECAY 1",
             "FISPACT",
             "* CONDENSE",
             "END",
             "* END OF RUN"]
    ut.write_lines(path, lines)
    return 0


def get_z_from_zaid(zaid):
    """ get the atomic number from a zaid """
    zaid = zaid.split(".")[0]  # remove any suffixes
    zaid = int(zaid)
    z = int(zaid / 1000)
    return z


def convert_comp_to_elements(mat):
    """ converts the material composition to elements for fispact input """
    elements = {}
    # loop over the isotopes in the material composition and convert to elements
    for iso in mat.composition:
        z = get_z_from_zaid(iso)
        z = next((k for k, v in nc.Z_dict().items() if v == z), None)
        if z not in elements:
            elements[z] = 0
        elements[z] += mat.composition[iso]
    
    # need to normalise the elements to 100 for fispact input
    total = sum(elements.values())
    for z in elements:
        elements[z] = elements[z] / total * 100

    return elements


def write_fispact(inputs, cell_data, material_data, tally_data, path):
    """ writes the main fispact runner """
    lines = ut.get_lines(inputs.fispact_template)
    mat_num = cell_data["material"]
    mat = material_data[mat_num]
    print(mat)
    density = cell_data["density"]
    density = abs(density)  # make sure density is positive for fispact input

    # extract and normalise the flux
    cell_result = get_cell_tally_data(cell_data, tally_data)
    total = cell_result.loc[cell_result["energy"] == "total", "result"].iloc[0]

    # replace the material data in the template with the material from the cell data
    for i, line in enumerate(lines):
        if line.lower().startswith("density"):
            lines[i] = f"density {density}"
        elif line.lower().startswith("fuel"):
            raise NotImplementedError("fuel line not implemented yet")
        elif line.lower().startswith("mass"):
            lines[i] = f"mass 1.0 {len(mat.elements)}"
            for j, comp in enumerate(mat.elements):
                lines.insert(i + j + 1, f"{comp.upper()} {mat.elements[comp]}")
            lines[i + len(mat.elements) + 1] = "* end of mat"
        elif line.lower().startswith('flux'):
            current_flux = float(line. split()[-1])
            new_flux = current_flux * inputs.norm_factor * total
            lines[i] = f"FLUX {new_flux}"

    ut.write_lines(path, lines)
    return 0


def copy_files_file(inputs, path):
    """ copy the files file into the folder for the current cell"""
    if not Path(inputs.files_file).exists():
        raise FileNotFoundError(f"Files file {inputs.files_file} not found")
    shutil.copyfile(inputs.files_file, f"{path}/FILES")
    return 0


def get_cell_tally_data(cell_data, tally_data):
    """ """
    # get the tally number for the current cell
    tally_number = cell_data["tally_number"]
    # get the tally data for the current cell
    tally = next((t for t in tally_data if t.number == tally_number), None)
    if tally is None:
        raise ValueError(f"Tally {tally_number} not found in tally data")
    
    return tally.result[cell_data["number"]] 


def write_fluxes(cell_data, tally_data, path):
    """ write the fluxes file for the current cell"""

    # process tally data to get the right  spectrum 
    cell_result = get_cell_tally_data(cell_data, tally_data)
    
    # drop the row with column "energy" the equals "total" from the tally result if it exists
    if "total" in cell_result["energy"].values:
        cell_result = cell_result[cell_result["energy"] != "total"]

    # extract the result column
    result_column = cell_result["result"].to_list()

    lines = ffw.convert_mcnp_spect_to_fispact_fluxes_format(result_column)
    ut.write_lines(path, lines)
    return 0


def check_files_file(files_file, ngroups_count):
    """ check the files file matches the data library with the current particle and group structure"""
    if not Path(files_file).exists():
        raise FileNotFoundError(f" Files file {files_file} not found")
    
    ff = ffr.read_fispact_files_file(files_file)

    if "xs_endf" not in ff.parameters:
        raise ValueError(f"Files file {files_file} does not contain xs_endf parameter")
    elif str(ngroups_count) not in ff.parameters["xs_endf"]:
        raise ValueError(f"Files file {files_file} does not contain xs_endf parameter for {ngroups_count} groups")
    
    if "prob_tab" not in ff.parameters:
        raise ValueError(f"Files file {files_file} does not contain prob_tab parameter")
    elif str(ngroups_count) not in ff.parameters["prob_tab"]:
        raise ValueError(f"Files file {files_file} does not contain prob_tab parameter for {ngroups_count} groups")

    return 0


def check_fispact_errors(log_file):
    """ check the fispact log files for any fatal errors"""
    if not Path(log_file).exists():
        raise FileNotFoundError(f" Fispact log file {log_file} not found")

    log = ut.get_lines(log_file)
    return 0


def cleanup_fispact_run(path):
    """ remove the fispact files after the run """
    return 0


def run_fispact(fispath, path):
    """ run the three fispact runs for a cell """
    # change directory into folder
    # run collapse
    print(f"running {path}/collapse.i")
    col_path = path + "/collapse"
    # result = subprocess.run( [fispath, col_path],
    #                        capture_output=True, text=True, check=True  )

    # check collapse run
    # run array
    print(f"running {path}/array.i")
    # check array run

    # run fispact main
    print(f"running {path}/{path}.i")

    # check main run

    # remember to move out of folder

    return 0


def fispact_setup(path, inputs, cell_data, tally_data, material_data):
    """ set up the different the parts of the fispact runs for a cell """
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)

    ngroups_count = int(cell_data["ngroups"])
    print(f"ngroups_count: {ngroups_count}")
    write_collapse(f"{path}/collapse.i", ngroups_count)
    write_array(f"{path}/array.i")
    write_fispact(inputs, cell_data, material_data, tally_data, f"{path}/{path}.i")
    copy_files_file(inputs, path)
    check_files_file(f"{path}/FILES", ngroups_count)
    write_fluxes(cell_data, tally_data, f"{path}/fluxes")

    return 0


def check_tally_energy_bins(tally_data):
    """ get the number of energy groups for a given tally """
    # check the energy group structure is allowable for fispact
    all_ngroups = {}
    for tal in tally_data:
        ngroups = len(tal.eng)
        if not ffw.check_group_struct(ngroups):
            raise ValueError(f"Tally {tal.number} has an invalid number of energy groups: {ngroups}")
        all_ngroups[tal.number] = ngroups

    return all_ngroups
    

def read_data_from_mcnp_output(inputs):
    """ """
    if not Path(inputs.mc_output).exists():
        raise FileNotFoundError(f"MCNP output file {inputs.mc_output} not found")

    mc_output = mor.read_output_file(inputs.mc_output)
    if mc_output.fatal is True:
        raise ValueError('MCNP output contains a fatal error')

    cells, tally_data = get_cells_mcnp(mc_output)

    return cells, tally_data


def read_data_from_mcnp_input(inputs, tally_cell_list):
    """ reads the data from an mcnp input file """
    if not Path(inputs.mc_input).exists():
        raise FileNotFoundError(f"MCNP input file {inputs.mc_input} not found")

    mc_input = mir.read_mcnp_input(inputs.mc_input)
    cell_data = get_cell_data(mc_input, tally_cell_list)

    material_data = {}

    for mat_num in set(cell_data["material"]):

        mat = mir.read_material_lines(mat_num, mc_input.data_block)
        material_data[mat_num] = mat

    return cell_data, material_data


def main(config_fp):
    """  main calculation flow """
    # read config
    inputs = read_config(config_fp)

    # read mc output and input files
    if inputs.mc_code.upper() == "MCNP":
        # read mcnp output
        cells, tally_data = read_data_from_mcnp_output(inputs)
        # read mc input
        cell_data, material_data = read_data_from_mcnp_input(inputs, cells)
    else:
        raise NotImplementedError()
    
    # check the tally energy bins
    ngroups = check_tally_energy_bins(tally_data)

    # add the tally number and ngroups to the cell data dataframe
    cell_data["tally_number"] = cell_data["number"].map(cells)
    cell_data["ngroups"] = cell_data["tally_number"].map(ngroups)

    # process materials
    for mat_num, mat in material_data.items():
        mat.elements = convert_comp_to_elements(mat)

    # generate fispact inputs and run each one
    for _, row in cell_data.iterrows():
        cell = row["number"]
        path = f"cell{cell}"
        fispact_setup(path, inputs, row, tally_data, material_data)

        # run fispact
        fispath = inputs.fispact_path
        run_fispact(fispath, path)

    # read fispact outputs

    # generate new mc gamma source


if __name__ == "__main__":
    desc_txt1 = "Cell based 2 step activation script"
    desc_txt2 = " using fispact"
    parser = argparse.ArgumentParser(description=desc_txt1 + desc_txt2)
    parser.add_argument("input", help="path to the json input file")

    args = parser.parse_args()

    main(args.input)
