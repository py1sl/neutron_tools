"""
Reads MCNP output file
"""
import argparse
import logging as ntlogger
import numpy as np
import pandas as pd
import re
from collections import defaultdict
import neut_utilities as ut


class MCNPOutput():
    """ MCNP output data"""

    def __init__(self):
        """ define data"""
        self.file_name = ""
        self.version = ""
        self.date = ""
        self.start_time = ""
        self.cell_mass_volume = []
        self.surface_area = []
        self.num_tallies = 1
        self.num_rendevous = 1
        self.tally_data = []
        self.summary_data = []
        self.tfc_data = []
        self.t60 = None
        self.warnings = []
        self.comments = []
        self.tables = []
        self.fatal = False


class MCNP_tally_data():
    """ generic tally object for data common to all tally types """

    def __init__(self):
        # general data all tallies have
        self.number = 1
        self.tally_type = 1
        self.particle = "neutron"
        self.nps = 1
        self.result = []
        self.err = []
        self.eng = None
        self.stat_tests = None
        self.times = None
        self.user_bins = None


class MCNP_type5_tally(MCNP_tally_data):
    """ specific tally object for a type 5 point detector tally """

    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 5 tallies
        self.x = None
        self.y = None
        self.z = None
        self.cell_scores = None
        self.uncoll_flux = None
        self.uncoll_err = None
        self.diagnostics = None
        self.largest_score = 0.0
        self.largest_score_nps = 0.0
        self.average_per_history = 0.0
        self.misses = None

    def __str__(self):
        print_list = []
        print_list.append("Tally number: "+str(self.number))
        print_list.append("Particle: "+self.particle)
        print_list.append("X: "+str(self.x))
        print_list.append("Y: "+str(self.y))
        print_list.append("Z: "+str(self.z))
        if self.eng is not None:
            print_list.append("Energy Bins: True")
        else:
            print_list.append("Energy Bins: False")
        if self.times is not None:
            print_list.append("Time Bins: True")
        else:
            print_list.append("Time Bins: False")

        return "\n".join(print_list)


class MCNP_surface_tally(MCNP_tally_data):
    """ specific tally object for a type 1 or 2 surface tally"""

    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 1 or 2
        self.surfaces = None
        self.areas = None
        self.ang_bins = None

    def __str__(self):
        print_list = []
        print_list.append("Tally number: "+str(self.number))
        print_list.append("Particle: "+self.particle)
        print_list.append("Number of Surfaces: " + str(len(self.surfaces)))
        if self.eng is not None:
            print_list.append("Energy Bins: True")
        else:
            print_list.append("Energy Bins: False")
        if self.times is not None:
            print_list.append("Time Bins: True")
        else:
            print_list.append("Time Bins: False")
        if self.ang_bins is not None:
            print_list.append("Angular Bins: True")
        else:
            print_list.append("Angular Bins: False")
        return "\n".join(print_list)


class MCNP_cell_tally(MCNP_tally_data):
    """ specific tally object for a type 4 cell tally"""

    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 4
        self.cells = None
        self.vols = None

    def __str__(self):
        print_list = []
        print_list.append("Tally number: "+str(self.number))
        print_list.append("Particle: "+self.particle)
        print_list.append("Number of Cells: " + str(len(self.cells)))
        if self.eng is not None:
            print_list.append("Energy Bins: True")
        else:
            print_list.append("Energy Bins: False")
        if self.times is not None:
            print_list.append("Time Bins: True")
        else:
            print_list.append("Time Bins: False")
        return "\n".join(print_list)


class MCNP_pulse_tally(MCNP_tally_data):
    """ specific tally object for a type 8 pulse height tally"""

    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 8
        self.cells = None

    def __str__(self):
        print_list = []
        print_list.append("Tally number: "+str(self.number))
        print_list.append("Particle: "+self.particle)
        print_list.append("Number of Cells: " + str(len(self.cells)))
        if self.eng is not None:
            print_list.append("Energy Bins: True")
        else:
            print_list.append("Energy Bins: False")
        if self.times is not None:
            print_list.append("Time Bins: True")
        else:
            print_list.append("Time Bins: False")
        return "\n".join(print_list)


class MCNP_summary_data():
    """ data for the summary table """

    def __init__(self):
        self.number = 1
        self.summary_type = 1
        self.nps = 1
        self.particle = "Neutron"

    def __str__(self):
        print_list = []
        print_list.append(f"NPS: {self.nps}")
        print_list.append(f"Particle: {self.particle}")
        return "\n".join(print_list)


def read_version(lines):
    """ from 1st line of output get the MCNP version
    Parameters:
    - lines (list of str): List of lines containing information about the simulation.

    Returns:
    - str : The MCNP version.
    """
    version = None
    try:
        line = lines[0]
        if line[:29] == "          Code Name & Version":
            version = line.split("=")[1]
            version = version.strip()
        ntlogger.debug("Version: %s", version)
    except IndexError:
        ntlogger.debug("Version not found - are you sure this is an MCNP output file")
    return version


def read_run_date(lines):
    """ finds the start date and time of the run
    Parameters:
    - lines (list of str): List of lines containing information about the run.

    Returns:
    - tuple: A tuple containing the start date and start time.    """
    date = None
    time = None
    if len(lines) > 101:
        lines = lines[:100]
    data_line = lines[ut.find_line("1mcnp", lines, 5)]
    data_line = ut.string_clean_and_split(data_line)
    date = data_line[-2]
    time = data_line[-1]

    ntlogger.debug("Start date: %s", date)
    ntlogger.debug("Start time: %s", time)

    return date, time


def read_comments_warnings(lines):
    """ extracts all comments and warnings in the output file
    Parameters:
    - lines (list of str): List of lines containing information about comments and warnings.

    Returns:
    - tuple: A tuple containing two lists - comments and warnings.    """
    comments = [line for line in lines if line.startswith("  comment.")]
    warnings = [line for line in lines if line.startswith("  warning.")]

    return comments, warnings


def get_tally_nums(lines):
    """     Finds the tally numbers used in the problem.

    Parameters:
    - lines (list of str): List of lines containing information about tally numbers.

    Returns:
    - set: Set of unique tally numbers
    """
    tal_num_list = []
    for line in lines:
        if line[0:11] == "1tally     ":
            line = ut.string_clean_and_split(line)[1]
            tal_num_list.append(line)
    # remove duplicates
    tal_num_list = set(tal_num_list)
    #
    ntlogger.debug("Tally numbers: %s", tal_num_list)

    return tal_num_list


def get_rendevous_index(data):
    """ Returns the line indices of the rendezvous lines.

    Parameters:
    - data (list of str): List of lines containing information.

    Returns:
    - list of int: List of line indices where the rendezvous line is found.
    """
    indexes = []
    for i, line in enumerate(data):
        if "master set rendezvous nps" in line:
            indexes.append(i)

    return indexes


def count_rendevous(data):
    """ counts the number of rendevous in the file """
    indexes = get_rendevous_index(data)
    count = len(indexes)
    return count


def process_ang_string(line):
    """
    Converts the tally string describing angular bin edges into a single float value for the angle.

    Parameters:
    - line (str): The input line containing the angular information.

    Returns:
    - float: The extracted angle value.
    """
    line = line.strip()
    ang_string = line.split(":")[1]
    ang_float = float(ang_string.split()[-2])
    return ang_float


def read_summary(data, ptype, rnum):
    """ reads the summary tables in the output file """
    return 1


def read_table101(lines, start_line):
    """
    Read particle energy limits and table limits from print table 101.

    Parameters:
    - lines (list): List of lines containing the table data.
    - start_line (int): Index of the line where the table starts.

    Returns:
    - pd.DataFrame: DataFrame with the extracted data.
    """

    term_line = ut.find_line(" *******", lines[start_line:], 8)

    columns = ["particle_id", "particle_symbol", "particle_name",
               "cutoff_energy", "max_energy",
               "smallest_table_max", "largest_table_max", "always_table_below",
               "always_model_above"]

    table_lines = [ut.string_cleaner(line) for line in lines[start_line:start_line + term_line]][6:]
    data_lines = []

    for line in table_lines:
        if line == "":
            break
        else:
            line = line.split(" ")
            data_lines.append(line)

    t101df = pd.DataFrame(data_lines, columns=columns)
    return t101df


def read_table60(lines, start_line):
    """ read print table 60
        input a list of strings
        returns a dataframe with table 60 data
    """

    term_line = ut.find_line("    minimum source weight", lines, 25)

    table_lines = [ut.string_cleaner(line) for line in lines[start_line:term_line]]

    # header is split over two lines
    header1 = table_lines[2]
    header1 = header1.split(" ")
    header2 = table_lines[3]
    header2 = header2.split(" ")
    # density headings
    header2[2] = header1[0] + " " + header2[2]
    header2[3] = header1[1] + " " + header2[3]
    # importances -
    # TODO more than 1 importance
    header2[-1] = header1[-1] + " " + header2[-1]

    # process the data section
    datalines = table_lines[5:-3]
    data = []
    for line in datalines:
        dataline = line.split(" ")
        data.append(dataline[1:])

    t60df = pd.DataFrame(data, columns=header2)

    return t60df


def print_tally_lines_to_file(lines, fname, tnum):
    """ prints tally section to a file for debugging

    Parameters:
    - lines (list of str): List of lines containing tally section information.
    - fname (str): Base filename for the output file.
    - tnum : Tally number to print
    """
    if ntlogger.getLogger().getEffectiveLevel() == ntlogger.DEBUG:
        ntlogger.debug(f"Writing {fname}{tnum}.txt")
        fname = f"{fname}{tnum}.txt"

        ut.write_lines(fname, lines)


def process_time_bin_only(lines):
    """ processes a tally with only times bins
        input a list of strings for the time bin section of the tally
    """
    time_bins = []
    errs = []
    results = []

    for line in lines:
        line = ut.string_cleaner(line)
        if "time" in line:
            line = line.split(" ")[1:]
            for t in line:
                time_bins.append(t)
        elif len(line) > 4:
            line = line.split(" ")
            line = [float(i) for i in line]
            errs += line[1::2]
            results += line[0::2]

    return time_bins, results, errs


def eng_time_get_time_bins(data):
    """ for an energy and time bin tally, get the time bin boundary values """
    time_bins = []
    for line in data:
        if "time" in line:
            line = " ".join(line.split())
            line = line.split(" ")[1:]
            for t in line:
                # need to avoid duplicates if multiple cells/surfaces etc
                if t not in time_bins:
                    time_bins.append(t)

    return time_bins


def eng_time_get_eng_bins(data):
    """ for an energy and time binned tally get the energy
        bin boundary values
    """
    energy_bins = []
    in_data = False
    for line in data:
        if in_data:
            if "total" in line:
                in_data = False
                break
            line = " ".join(line.split())
            erg = line.split(" ")[0]
            energy_bins.append(erg)
        elif not in_data:
            if "energy" in line:
                in_data = True

    # add the total line
    energy_bins.append("total")

    return energy_bins


def process_energy_lines(erg_lines):
    """ process the results section for a tally with only energy bins """
    erg = []
    res = []
    rel_err = []

    for line in erg_lines:
        line = line.strip()
        line = line.split(" ")
        erg.append(float(line[0]))
        res.append(float(line[3]))
        rel_err.append(float(line[4]))

    return erg, res, rel_err


def convert_energy_time_data_to_df(data, time_bins, energy_bins):
    """ converts the energy time results into a dataframe """
    try:
        df = pd.DataFrame(data, index=time_bins, columns=energy_bins)
        return df
    except ValueError as e:
        ntlogger.debug(f"cannot convert to dataframe: {e}")

        return data


def process_e_t_userbin(lines):
    """read and process a tally output with energy and time bins """
    times = []
    energies = []
    values = []
    uncerts = []
    current_times = []
    current_block_values = []
    current_block_uncert = []
    reading_data = False

    for line in lines:
        line = line.strip()
        if line.startswith('time:'):
            # Extract times from line
            current_times = [float(x) for x in re.findall(r'[\d.E+-]+', line)]
            times.extend(current_times)
            reading_data = True
        elif reading_data:
            if line.startswith('total') or line == '':
                if current_block_values:
                    values.append(np.array(current_block_values))
                    uncerts.append(np.array(current_block_uncert))
                    current_block_values = []
                    current_block_uncert = []
                reading_data = False
            elif not line.startswith('energy'):
                # Parse energy and values (value, uncertainty pairs)
                parts = re.findall(r'[\d.E+-]+', line)
                if not parts:
                    continue
                energy = float(parts[0])
                energies.append(energy)
                data_pairs = list(map(float, parts[1:]))
                row_vals = data_pairs[::2]
                current_block_values.append(row_vals)
                row_uncert = data_pairs[1::2]
                current_block_uncert.append(row_uncert)

    # Combine all blocks
    values = np.hstack(values)
    uncerts = np.hstack(uncerts)
    energies = sorted(set(energies))
    times = sorted(set(times))

    # Convert to numpy arrays
    energy_arr = np.array(energies)
    time_arr = np.array(times)
    value_matrix = np.array(values)
    uncerts_matrix = np.array(uncerts)

    return time_arr, energy_arr, value_matrix, uncerts_matrix


def find_term_line(lines):
    """ finds the term line or last dump
    Parameters:
    - lines (list of str): List of lines containing information about the simulation.

    Returns:
    - int or None: Index of the termination line if found, or None if not found.
    """
    try:
        term_line = ut.find_line("      run terminated ", lines, 21)
    except ValueError:
        ntlogger.debug("Term line not found ")
        term_line = None
    return term_line


def find_last_rendevous(lines):
    """ finds line index of last rendevous
    Parameters:
    - lines (list of str): List of lines containing information about rendezvous points.

    Returns:
    - int: Index of the last rendezvous line
    """
    indexes = get_rendevous_index(lines)

    # the last one is generally at the end of the file, if not a complete run
    # therefore index of last complete set is the second last one
    ntlogger.debug("last index: %s", str(indexes[-2]))
    return indexes[-2]


def read_tally(lines, tnum, rnum=-1):
    """ reads the lines and extracts the tally results"""

    # todo add ability to do all rendevous
    # reduce to only the final result set
    term_line = find_term_line(lines)
    if term_line is None:
        ntlogger.debug("trying to find last complete rendevous")
        term_line = find_last_rendevous(lines)

    lines = lines[term_line:]

    # reduce to only the tally results section
    fline = "1tally" + ((9 - len(str(tnum))) * " ")
    res_start_line = ut.find_line(fline + str(tnum), lines, 15)

    # add an error catch

    # Check if tally comment
    tal_comment_bool = lines[res_start_line + 1][0] == "+"

    # Find tally type and create an appropriate class
    type_index = 2 if tal_comment_bool else 1
    tally_type = lines[res_start_line+type_index][22]

    if tally_type == '5':
        tally_data = MCNP_type5_tally()
    elif tally_type == '4' or tally_type == '6':
        tally_data = MCNP_cell_tally()
    elif tally_type == '1' or tally_type == '2':
        tally_data = MCNP_surface_tally()
    elif tally_type == '8':
        tally_data = MCNP_pulse_tally()
    else:
        tally_data = MCNP_tally_data()

    # get basic common tally data
    tally_data.number = int(tnum)

    # get particle type
    particle_index = 3 if tal_comment_bool else 2
    tally_data.particle = lines[res_start_line+particle_index][24:33]

    tally_data.particle = ut.string_cleaner(tally_data.particle)
    tally_data.nps = ut.string_cleaner(lines[res_start_line][28:40])
    try:
        tally_data.nps = int(tally_data.nps)
    except ValueError:
        ntlogger.debug('NPS value not an int, could be large value')

    tally_data.tally_type = tally_type

    # limit lines to just the tally data
    lines = lines[res_start_line + 1:]
    tal_end_line = ut.find_line("1tally", lines, 6)
    lines = lines[:tal_end_line - 1]

    # print tally test file
    print_tally_lines_to_file(lines, "tally_test", tnum)

    # debug
    ntlogger.info('Reading tally %s', str(tnum))
    ntlogger.debug('Run term line number: %s', str(term_line))
    ntlogger.debug('Result start line number: %s', str(res_start_line))
    ntlogger.debug('tally end line number: %s', str(tal_end_line))
    ntlogger.debug('tally particle: %s', tally_data.particle)
    ntlogger.debug('tally nps: %s', str(tally_data.nps))
    ntlogger.debug('tally type: %s', str(tally_data.tally_type))

    # depending on tally type choose what to do now
    if tally_data.tally_type == "4" or tally_data.tally_type == "6":
        tally_data = read_type_cell(tally_data, lines)
    elif tally_data.tally_type == "5":
        tally_data = read_type_5(tally_data, lines)
    elif tally_data.tally_type == "1" or tally_data.tally_type == "2":
        tally_data = read_type_surface(tally_data, lines)
    elif tally_data.tally_type == "8":
        tally_data = read_type_8(tally_data, lines)
    else:
        ntlogger.info("Tally type not recognised or supported")

    # get statistical test outcomes
    # first check not all zeros
    # if np.array(tally_data.result).any():
    #    tally_data.stat_tests = read_stat_tests(lines)

    return tally_data


def read_type_8(tally_data, lines):
    """ process type 8 tally output data
        note: type 8 tally cannot have time bins
    """
    ntlogger.debug("pulse height tally")
    # TODO: fix this hard coded part
    tally_data.cells = ["2"]  # this should not be hard coded

    # loop for each cell
    for cell in tally_data.cells:
        cline = " cell  "
        cell_res_start = ut.find_line(cline + cell, lines,
                                      len(cell) + len(cline))
        if lines[cell_res_start + 1] == "      energy   ":
            ntlogger.debug("noticed energy")
            tally_data.eng = []
            loc_line_id2 = ut.find_line("      total    ",
                                        lines[cell_res_start + 1:], 15)
            erg_lines = lines[cell_res_start + 2:cell_res_start +
                              1 + loc_line_id2]
            tally_data.eng, tally_data.result, tally_data.err = process_energy_lines(erg_lines)
        else:
            # single value result
            ntlogger.debug('tally e bin count = 1')
            line = lines[cell_res_start + 1]
            line = line.strip()
            line = line.split(" ")
            tally_data.result.append(float(line[0]))
            tally_data.err.append(float(line[1]))

    if tally_data.eng is not None:
        ntlogger.debug('tally e bin count: %s', len(tally_data.eng))

    return tally_data


def get_type2_surface_areas(lines):
    """ extracts the surface areas for a type 2 surface tally"""
    # TODO: if more than a single line of areas
    areas = []
    area_line_id = ut.find_line("           areas", lines, 16)
    area_val_line = lines[area_line_id + 2]
    area_val_line = " ".join(area_val_line.split())
    areas = np.asarray(area_val_line.split(" "))

    return areas


def get_type2_surface_numbers(lines):
    """ extracts the surface numbers for a type2 surface tally"""
    # TODO: if more than a single line of areas
    surfaces = []
    area_line_id = ut.find_line("           areas", lines, 16)
    suf_val_line = lines[area_line_id + 1]
    suf_val_line = " ".join(suf_val_line.split())
    suf_val_line = suf_val_line.split(":")[1]
    surfaces = suf_val_line.split(" ")[1:]

    return surfaces


def get_type1_surface_numbers(lines):
    """ extract the surface numbers for a type 1 surface tally """
    surface_list = []
    for line in lines[2:]:
        if "surface" in line:
            line = line.strip()
            surface_list.append(line.split()[-1])

    return surface_list


def process_energy_angle_tally(tally_data, lines, first_surface_line_id):
    """ """

    ntlogger.debug("energy bins")
    angles_bins = [-1.0]

    ebin = []
    rel_err = []
    res = []
    res_df = []
    rel_err_df = []
    in_res = False

    for line in lines[first_surface_line_id:]:
        if line[:11] == " angle  bin":
            ang_float = process_ang_string(line)
            angles_bins.append(ang_float)

        if line[:13] == "      total  ":
            in_res = False
            ebin = np.array(ebin)
            tally_data.eng = ebin
            rel_err = np.array(rel_err)
            rel_err_df.append(rel_err)
            res = np.array(res)
            res_df.append(res)
            ebin = []
            rel_err = []
            res = []
        if in_res:
            line = line.strip()
            line = line.split(" ")
            ebin.append(float(line[0]))
            res.append(float(line[3]))
            rel_err.append(float(line[4]))
        if line == "      energy   ":
            in_res = True

    return res_df, rel_err_df, angles_bins


def process_energy_binned_surface_tally(lines):
    """ process a surface tally with energy bins """
    data_dict = defaultdict(list)
    total_dict = {}

    current_surface = None
    for line in lines:
        line = line.strip()

        # Detect new surface block
        surface_match = re.match(r"surface\s+(\d+)", line)
        if surface_match:
            current_surface = int(surface_match.group(1))
            continue

        if not current_surface:
            continue  # Skip until a surface block is found

        # Handle the "total" line
        if line.lower().startswith("total"):
            parts = line.lower().replace("total", "").split()
            if len(parts) == 2:
                total_result = float(parts[0])
                total_rel_err = float(parts[1])
                total_dict[current_surface] = {
                    "total_result": total_result,
                    "total_rel_err": total_rel_err
                }
            continue

        # Match data lines (starting with a number and having 3 parts)
        parts = line.split()
        if len(parts) == 3 and re.match(r"^\d", parts[0]):
            energy = float(parts[0])
            result = float(parts[1])
            rel_err = float(parts[2])
            data_dict[current_surface].append([energy, result, rel_err])
            
    # Convert lists to DataFrames
    for surface in data_dict:
        data_dict[surface] = pd.DataFrame(data_dict[surface], columns=["energy", "result", "rel_err"])
        
    return data_dict, total_dict


def read_type_surface(tally_data, lines):
    """ process type 1 or type 2 tally output data"""
    ntlogger.debug("Surface Tally")
    tally_data.areas = []
    tally_data.surfaces = []

    # TODO: if more than a single line of surfaces or areas
    # find areas
    # TODO: sort for type 1 tally with sd card
    if tally_data.tally_type == "2":
        tally_data.areas = get_type2_surface_areas(lines)
        tally_data.surfaces = get_type2_surface_numbers(lines)

        ntlogger.debug("Tally surface numbers:")
        ntlogger.debug(tally_data.surfaces)
        ntlogger.debug("Tally surface areas:")
        ntlogger.debug(tally_data.areas)

    if tally_data.tally_type == "1":
        surface_list = get_type1_surface_numbers(lines)
        tally_data.surfaces = list(set(surface_list))
        ntlogger.debug("Tally surface numbers:")
        ntlogger.debug(tally_data.surfaces)

    loc = 0
    first_surface_line_id = ut.find_line(" surface ", lines, 9)
    ntlogger.debug("first surface id %s", first_surface_line_id)

    surface_line_id = first_surface_line_id
    res_df = []
    rel_err_df = []

    if "energy" in lines[first_surface_line_id + 1]:
        ntlogger.debug("energy bins only")

        tally_data.result, tally_data.totals = process_energy_binned_surface_tally(lines)
        first_key = next(iter(tally_data.result))
        tally_data.eng = tally_data.result[first_key]["energy"].tolist()

    elif "angle" in lines[first_surface_line_id + 1]:
        ntlogger.debug("angle bins")

        if lines[first_surface_line_id + 2] == "      energy   ":
            tally_data.result, tally_data.err, tally_data.ang_bins = process_energy_angle_tally(tally_data, lines, first_surface_line_id)
        else:
            ntlogger.debug("angle bins only")

    elif "time" in lines[first_surface_line_id + 1]:
        end_line_id = ut.find_line(" ===", lines, 4)
        lines = lines[:end_line_id]
        # check if energy bins as well as time
        if "energy" in lines[first_surface_line_id + 2]:
            ntlogger.debug("energy & time bins")
            if len(tally_data.surfaces) > 1:
                res_list = []
                err_list = []
                for sur in tally_data.surfaces:
                # needs more work here change - try except to use the fact that it will be the last surface block, check via enumerate(tally_data.surfaces)
                    # print(f"Surface: {sur}")
                    try:
                        end_surface_block_line_id = ut.find_line(" surface ", lines[first_surface_line_id + 1:], 9)+ first_surface_line_id + 1
                    except:
                        end_surface_block_line_id = -1
                    # print(f"first surf id: {first_surface_line_id}")
                    # print(f"end surf id: {end_surface_block_line_id}")
                    tb, eb, res, err = process_e_t_userbin(
                        lines[first_surface_line_id + 1:end_surface_block_line_id])
                    
                    first_surface_line_id = end_surface_block_line_id

                    res_list.append(res)
                    err_list.append(err)
                tally_data.times = tb
                tally_data.eng = eb
                tally_data.result = res_list
                tally_data.err = err_list
            else:
                # energy and time bins only one surface
                tb, eb, res, err = process_e_t_userbin(
                    lines[first_surface_line_id + 1:end_line_id])
                tally_data.times = tb
                tally_data.eng = eb
                tally_data.result = res
                tally_data.err = err
        elif len(tally_data.surfaces) > 1:
            # times bins multiple surfaces
            ntlogger.debug("time bins and multiple surfaces")
            res_data = []
            err_data = []
            for sur in tally_data.surfaces:
                end_pos = ut.find_ind(lines[first_surface_line_id:], "total")
                end_line_id = end_pos + 2 + first_surface_line_id
                sur_lines = lines[first_surface_line_id + 1:end_line_id]
                time_bins, results, errs = process_time_bin_only(sur_lines)
                res_data.append(results)
                err_data.append(errs)
                first_surface_line_id = end_line_id + 1

            tally_data.times = time_bins
            tally_data.result = res_data
            tally_data.err = err_data

        else:
            # time bins - only one surface
            ntlogger.debug("time bins only, only one surface")
            end_line_id = ut.find_ind(lines, "total") + 2
            lines = lines[first_surface_line_id + 1:end_line_id]
            tally_data.times, tally_data.result, tally_data.err = process_time_bin_only(lines)

    elif len(tally_data.surfaces) > 1:
        for s in tally_data.surfaces:
            # find start and end points
            ntlogger.debug("Reading Surface: %s", s)
            surface_line_id = ut.find_line(" surface ", lines[loc:], 9)
            surface_line_id = surface_line_id + loc
            loc = surface_line_id + 1
            line = lines[surface_line_id + 1]
            line = line.strip()
            line = line.split(" ")
            tally_data.result.append(float(line[0]))
            tally_data.err.append(float(line[1]))

    else:
        ntlogger.debug("single value only")
        line = lines[first_surface_line_id + 1]
        line = line.strip()
        line = line.split(" ")
        tally_data.result = [float(line[0])]
        tally_data.err = [float(line[1])]

    return tally_data


def get_cell_data(lines, line_id):
    """ for cell tally retrieves the cell numbers and volumes """
    cells = []
    vols = []

    # extract the values of cell number and volumes
    while True:
        line_id = line_id + 1
        line = lines[line_id]
        if (line == " "):
            break
        elif "cell:" in line:
            cell_line = " ".join(line.split())
            cell_line = cell_line.split(":")[1]
            cell_line = cell_line.split(" ")[1:]
            for cell in cell_line:
                cells.append(cell)
        else:
            vol_line = " ".join(line.split())
            vol_line = vol_line.split(" ")
            for vol in vol_line:
                vols.append(vol)

    return cells, vols, line_id


def read_energy_bin_only_cell_tally(lines):
    """ """
    data_dict = defaultdict(list)
    total_dict = {}
    current_cell = None

    for line in lines:
        line = line.strip()
        cell_match = re.match(r"cell\s+(\d+)", line)
        if cell_match:
            current_cell = int(cell_match.group(1))
        if not current_cell:
            continue
        # Handle the "total" line
        if line.lower().startswith("total"):
            parts = line.lower().replace("total", "").split()
            if len(parts) == 2:
                total_result = float(parts[0])
                total_rel_err = float(parts[1])
                total_dict[current_cell] = {
                    "total_result": total_result,
                    "total_rel_err": total_rel_err
                }
            continue

        # Match data lines (starting with a number and having 3 columns -energy, result and rel err)
        parts = line.split()
        if len(parts) == 3 and re.match(r"^\d", parts[0]):
            energy = float(parts[0])
            result = float(parts[1])
            rel_err = float(parts[2])
            data_dict[current_cell].append([energy, result, rel_err])
    # Convert lists to DataFrames
    for cell in data_dict:
        data_dict[cell] = pd.DataFrame(data_dict[cell], columns=["energy", "result", "rel_err"])

    return data_dict, total_dict


def read_type_cell(tally_data, lines):
    """ process type 4 or type 6 tally output data """
    ntlogger.debug("Volume tally")

    # find line that the volumes or masses start at
    if tally_data.tally_type == "4":
        line_id = ut.find_line("           volumes ", lines, 19)
    elif tally_data.tally_type == "6":
        line_id = ut.find_line("           masses ", lines, 18)

    # find cells
    # find volumes/ masses
    tally_data.cells, tally_data.vols, line_id = get_cell_data(lines, line_id)

    lines = lines[line_id:]
    cell_res_start = ut.find_ind(lines, " " + tally_data.cells[0] + " ")
    tally_read = False

    # only energy binned data
    if "energy" in lines[cell_res_start + 1]:
        ntlogger.debug("noticed energy")
        tally_data.result, tally_data.totals = read_energy_bin_only_cell_tally(lines)
        first_key = next(iter(tally_data.result))
        tally_data.eng = tally_data.result[first_key]["energy"].tolist()
        tally_read = True


    # loop for each cell
    for cell in tally_data.cells:
        results = []
        errs = []

        cell_res_start = ut.find_ind(lines, " " + cell + " ")

        # time bins
        if "time" in lines[cell_res_start + 1]:
            end_line_id = ut.find_line(" ===", lines, 4)
            # check if energy bins as well as time
            if "energy" in lines[cell_res_start + 2]:
                ntlogger.debug("energy & time bins")
                tally_data.times, tally_data.eng, res, err = process_e_t_userbin(
                    lines[cell_res_start + 1:end_line_id])
                tally_data.result.append(res)
                tally_data.err.append(err)
            else:
                # just time bins
                ntlogger.debug("time bins only")

                end_line_id = ut.find_ind(lines, "total") + 2
                cell_block = lines[cell_res_start + 1:end_line_id]
                tally_data.times, results, errs = process_time_bin_only(cell_block)
                tally_data.result.append(results)
                tally_data.err.append(errs)

                lines = lines[end_line_id:]

        elif tally_read is False:
            # single value per cell data
            data_line = lines[cell_res_start + 1]
            data_line = " ".join(data_line.split())
            data_line = data_line.split(" ")
            if ("total" in data_line) or data_line[0] == "":
                ntlogger.debug("skipping total line")
            else:
                ntlogger.debug(data_line[0])
                tally_data.result.append(float(data_line[0]))
                tally_data.err.append(float(data_line[1]))

    return tally_data


def read_type_5(tally_data, lines):
    """ processes a type 5 (point detector tally output) """
    # read detector position
    loc_line_id = ut.find_line(" detector located", lines, 17)
    loc_line = lines[loc_line_id]
    loc_line = loc_line.split("=")[1]

    tally_data.x = loc_line[0:12]
    tally_data.x = float(tally_data.x.strip())
    tally_data.y = loc_line[12:24]
    tally_data.y = float(tally_data.y.strip())
    tally_data.z = loc_line[24:36]
    tally_data.z = float(tally_data.z.strip())
    ntlogger.debug("x: %s", tally_data.x)
    ntlogger.debug("y: %s", tally_data.y)
    ntlogger.debug("z: %s", tally_data.z)
    res_line = lines[loc_line_id + 1]

    # check if energy dependant
    if res_line == "      energy   ":
        ntlogger.debug("energy dependant")
        tally_data.eng = []
        total_line_id2 = ut.find_line(
            "      total", lines[loc_line_id + 1:], 11)
        erg_lines = lines[loc_line_id + 2:loc_line_id + total_line_id2 + 1]
        tally_data.eng, tally_data.result, tally_data.err = process_energy_lines(erg_lines)

    elif "time" in res_line:
        ntlogger.debug("found time")
        # TODO: sort out f5 time dep tally

    elif "user bin" in res_line:
        # user bins used
        # assumes if user bins then also energy and time bins
        # curently extracts total flux not uncollided
        ntlogger.debug("Special user bin tally")
        user_bins = []
        user_bin_locs = []
        user_bin = res_line.split(" ")[-1]
        ntlogger.debug("User bin: %s", user_bin)
        user_bins.append(user_bin)
        user_bin_locs.append(0)
        for i, line in enumerate(lines[loc_line_id + 1:]):
            if "user bin" in line:
                user_bin = line.split(" ")[-1]
                user_bins.append(user_bin)
                user_bin_locs.append(i)
                if user_bin == "total":
                    break
        tally_data.user_bins = user_bins

        bin_data = lines[loc_line_id + 1:]
        i = 0
        while i < len(user_bin_locs) - 1:
            ubin_data = bin_data[user_bin_locs[i]:user_bin_locs[i + 1]]
            tdata, edata, resdata, errdata = process_e_t_userbin(ubin_data)
            tally_data.result.append(resdata)
            tally_data.err.append(errdata)
            tally_data.times = tdata
            tally_data.eng = edata
            i = i + 1

    else:
        # single value and error result
        res_line = res_line.split(" ")[-2:]
        tally_data.result.append(float(res_line[0]))
        tally_data.err.append(float(res_line[1]))

    # read general f5 tally data
    ave_line_id = ut.find_ind(lines, " average tally per history")
    ave_line = lines[ave_line_id]
    ave_line = ut.string_clean_and_split(ave_line, "=")
    tally_data.average_per_history = float(ave_line[1][1:13])
    tally_data.largest_score = float(ave_line[-1])

    n_line = lines[ave_line_id+1]
    n_line = ut.string_clean_and_split(n_line, "=")
    tally_data.largest_score_nps = float(n_line[-1])

    # read score misses data
    tally_data.misses = {}

    score_miss_line_id = ut.find_ind(lines, "score misses")
    n_line = lines[score_miss_line_id+1]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["russian roulette on pd"] = float(n_line[-1])

    n_line = lines[score_miss_line_id+2]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["psc=0"] = float(n_line[-1])

    n_line = lines[score_miss_line_id+3]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["russian roulette in transmission"] = float(n_line[-1])

    n_line = lines[score_miss_line_id+4]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["underflow in transmission"] = float(n_line[-1])

    n_line = lines[score_miss_line_id+5]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["hit a zero-importance cell"] = float(n_line[-1])

    n_line = lines[score_miss_line_id+6]
    n_line = ut.string_clean_and_split(n_line)
    tally_data.misses["energy cutoff"] = float(n_line[-1])

    return tally_data


def read_stat_tests(lines):
    """ initial stat test reader"""
    try:
        stat_res_line_id = ut.find_line(" passed", lines, 7)
    except ValueError:
        return ["no"]

    stat_line = lines[stat_res_line_id]
    stat_line = ut.string_clean_and_split(stat_line)[1:]

    return stat_line


def get_table_dict(lines):
    """ finds all mcnp output table numerical identifiers in
        lines and the starting line for that table, returns dict """
    table_dict = {}

    for i, line in enumerate(lines):
        if "print table" in line:
            key = line.split(" ")[-1]
            if key == '160' or key == '161' or len(key) > 3:
                continue
            else:
                table_dict[key] = i

    return table_dict


def check_fatal(ofile_data):
    """ checks if there are any fatal errors in the output file """
    for line in ofile_data:
        if "fatal" in line.lower():
            return True
    return False


def read_output_file(path):
    """ reads an mcnp output file
        input is a path the to an ouput file
        output is an mcnp output object
    """
    ntlogger.info('Reading MCNP output file: %s', path)
    ofile_data = ut.get_lines(path)
    mc_data = MCNPOutput()

    # general
    mc_data.file_name = path
    mc_data.version = read_version(ofile_data)
    mc_data.date, mc_data.start_time = read_run_date(ofile_data)
    mc_data.comments, mc_data.warnings = read_comments_warnings(ofile_data)
    mc_data.num_rendevous = count_rendevous(ofile_data)
    mc_data.fatal = check_fatal(ofile_data)
    mc_data.tables = get_table_dict(ofile_data)

    # read specific tables
    if '60' in mc_data.tables:
        mc_data.t60 = read_table60(ofile_data, mc_data.tables['60'])
    if '101' in mc_data.tables:
        mc_data.t101 = read_table101(ofile_data, mc_data.tables['101'])

    # tallies
    tls = get_tally_nums(ofile_data)
    for tnum in tls:
        mc_data.tally_data.append(read_tally(ofile_data, tnum))

    mc_data.num_tallies = len(tls)

    return mc_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()

    read_output_file(args.input)
