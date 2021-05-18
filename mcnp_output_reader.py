"""
Reads MCNP output file
"""
import argparse
import logging
import numpy as np
import pandas as pd
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


class MCNP_tally_data():
    """ generic tally object for data common to all tally types """
    def __init__(self):
        # general
        self.number = 1
        self.type = 1
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


class MCNP_surface_tally(MCNP_tally_data):
    """ specific tally object for a type 1 or 2 surface tally"""
    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 1 or 2
        self.surfaces = None
        self.areas = None
        self.ang_bins = None


class MCNP_cell_tally(MCNP_tally_data):
    """ specific tally object for a type 4 cell tally"""
    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 4
        self.cells = None
        self.vols = None


class MCNP_pulse_tally(MCNP_tally_data):
    """ specific tally object for a type 8 pulse height tally"""
    def __init__(self):
        MCNP_tally_data.__init__(self)
        # for type 8
        self.cells = None


class MCNP_summary_data():
    """ data for the summary table """
    def __init__(self):
        self.number = 1
        self.type = 1


def read_version(lines):
    """ from 1st line of output get the MCNP version"""
    version = None
    line = lines[0]
    if line[:29] == "          Code Name & Version":
        version = line.split("=")[1]
        version = version.strip()
    logging.debug("Version: %s", version)
    return version


def read_run_date(lines):
    """ finds the start date and time of the run """
    date = None
    time = None
    if len(lines) > 101:
        lines = lines[:100]
    data_line = lines[ut.find_line("1mcnp", lines, 5)]
    data_line = ut.string_cleaner(data_line)
    data_line = data_line.split(" ")
    date = data_line[-2]
    time = data_line[-1]

    logging.debug("Start date: %s", date)
    logging.debug("Start time: %s", time)

    return date, time


def read_cell_mass(data):
    """ """
    return 1


def read_surface_area(data):
    """ """
    return 1


def read_comments_warnings(lines):
    """ extracts all comments and warnings in the output file """
    comments = []
    warnings = []
    for line in lines:
        if line[:10] == "  comment.":
            comments.append(line)
        elif line[:10] == "  warning.":
            warnings.append(line)
    return comments, warnings


def get_tally_nums(lines):
    """ finds the tally numbers used in the problem"""
    tal_num_list = []
    for line in lines:
        if line[0:11] == "1tally     ":
            line = ut.string_cleaner(line)
            line = line.split(" ")[1]
            tal_num_list.append(line)
    tal_num_list = set(tal_num_list)
    logging.debug("tally numbers:")
    logging.debug(tal_num_list)

    return tal_num_list


def get_rendevous_index(data):
    """ returns the line index of the rendevous line """
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
    """ converts the tally string describing the angualr bin edges into
        a single float value for the angle """
    line = line.strip()
    ang_string = line.split(":")[1]
    ang_float = float(ang_string.split()[-2])
    return ang_float


def read_summary(data, ptype, rnum):
    """ reads the summary tables in the output file """
    return 1


def read_table60(lines):
    """ read table 60
       input a list of strings
       returns a reduced list with just the lines in table 60
    """

    # first check there is a table 60,  might not be if it is a continue run
    try:
        start_line = ut.find_line("1cells", lines, 6)
    except ValueError:
        return None

    term_line = ut.find_line("    minimum source weight", lines, 25)
    lines = lines[start_line:term_line]

    return lines


def print_tally_lines_to_file(lines, fname, tnum):
    """ prints tally section to a file for debugging """
    if logging.getLogger().getEffectiveLevel() == 10:
        fname = fname + str(tnum)+".txt"
        logging.debug("writing " + fname)
        ut.write_lines(fname, lines)


def process_e_t_userbin(data):
    """ processes energy time bins in a tally """
    time_bins = []
    erg_bins = []

    # first find time bins
    for line in data:
        if "time" in line:
            line = " ".join(line.split())
            line = line.split(" ")[1:]
            for t in line:
                time_bins.append(t)

    # find energy bins
    in_data = False
    for line in data:
        if in_data:
            if "total" in line:
                in_data = False
                break
            line = " ".join(line.split())
            erg = line.split(" ")[0]
            erg_bins.append(erg)
        elif not in_data:
            if "energy" in line:
                in_data = True

    erg_bins.append("total")
    # create data arrays
    res_data = np.zeros((len(time_bins), len(erg_bins)))
    err_data = np.zeros((len(time_bins), len(erg_bins)))
    # now try get the data
    tcol = 0
    erow = 0
    len_tcol = 0
    in_data = False
    for j, line in enumerate(data):
        if in_data:
            if "total" in line:
                in_data = False

            line = " ".join(line.split())
            line = line.split(" ")[1:]
            tvals = line[::2]
            ervals = line[1::2]
            len_tcol = 0
            for i, val in enumerate(tvals):
                res_data[tcol+len_tcol, erow] = val
                err_data[tcol+len_tcol, erow] = ervals[i]
                len_tcol = len_tcol + 1
            erow = erow + 1

        elif not in_data:
            if "energy" in line:
                in_data = True
                tcol = tcol + len_tcol
                erow = 0
    try:
        res_df = pd.DataFrame(res_data, index=time_bins, columns=erg_bins)
    except ValueError:
        logging.debug("cannot convert to dataframe ")
        res_df = res_data

    return time_bins, erg_bins, res_df, err_data


def find_term_line(lines):
    """ finds the term line or last dump """
    try:
        term_line = ut.find_line("      run terminated ", lines, 21)
    except ValueError:
        logging.debug("Term line not found ")
        term_line = None
    return term_line


def find_last_rendevous(lines):
    """ finds line index of last rendevous """
    indexes = get_rendevous_index(lines)

    # the last one is generally at the end of the file, if not a complete run
    # therefore index of last complete set is the second last one
    logging.debug("last index: %s", str(indexes[-2]))
    return indexes[-2]


def read_tally(lines, tnum, rnum=-1):
    """reads the lines and extracts the tally results"""

    # todo add ability to do all rendevous
    # reduce to only the final result set
    term_line = find_term_line(lines)
    if term_line is None:
        logging.debug("trying to find last complete rendevous")
        term_line = find_last_rendevous(lines)

    lines = lines[term_line:]

    # reduce to only the tally results section
    fline = "1tally" + ((9-len(str(tnum)))*" ")
    res_start_line = ut.find_line(fline + str(tnum), lines, 15)

    # add an error catch

    # check if tally comment
    if lines[res_start_line + 1][0] == "+":
        tal_comment_bool = True
    else:
        tal_comment_bool = False

    # find tally type and create appropriate class
    if tal_comment_bool:
        type = lines[res_start_line + 2][22]
    else:
        type = lines[res_start_line + 1][22]

    if type == '5':
        tally_data = MCNP_type5_tally()
    elif type == '4' or type == '6':
        tally_data = MCNP_cell_tally()
    elif type == '1' or type == '2':
        tally_data = MCNP_surface_tally()
    elif type == '8':
        tally_data = MCNP_pulse_tally()
    else:
        tally_data = MCNP_tally_data()

    # get basic common tally data
    tally_data.number = int(tnum)

    # get particle type
    if tal_comment_bool:
        tally_data.particle = lines[res_start_line+3][24:33]
    else:
        tally_data.particle = lines[res_start_line+2][24:33]

    tally_data.particle = ut.string_cleaner(tally_data.particle)
    tally_data.nps = ut.string_cleaner(lines[res_start_line][28:40])
    tally_data.nps = int(tally_data.nps)
    tally_data.type = type

    # limit lines to just the tally data
    lines = lines[res_start_line + 1:]
    tal_end_line = ut.find_line("1tally", lines, 6)
    lines = lines[:tal_end_line-1]

    # print tally test file
    print_tally_lines_to_file(lines, "tally_test", tnum)

    # debug
    logging.info('Reading tally %s', str(tnum))
    logging.debug('Run term line number: %s', str(term_line))
    logging.debug('Result start line number: %s', str(res_start_line))
    logging.debug('tally end line number: %s', str(tal_end_line))
    logging.debug('tally particle: %s', tally_data.particle)
    logging.debug('tally nps: %s', str(tally_data.nps))
    logging.debug('tally type: %s', str(tally_data.type))

    # depending on tally type choose what to do now
    if tally_data.type == "4" or tally_data.type == "6":
        tally_data = read_type_cell(tally_data, lines)
    elif tally_data.type == "5":
        tally_data = read_type_5(tally_data, lines)
    elif tally_data.type == "1" or tally_data.type == "2":
        tally_data = read_type_surface(tally_data, lines)
    elif tally_data.type == "8":
        tally_data = read_type_8(tally_data, lines)
    else:
        logging.info("Tally type not recognised or supported")

    # get statistical test outcomes
    # first check not all zeros
    # if np.array(tally_data.result).any():
    # tally_data.stat_tests = read_stat_tests(lines)

    return tally_data


def read_type_8(tally_data, lines):
    """ process type 8 tally output data """
    logging.debug("pulse height tally")
    # TODO: fix this hard coded part
    tally_data.cells = ["2"]  # this should not be hard coded

    # loop for each cell
    for cell in tally_data.cells:
        cline = " cell  "
        cell_res_start = ut.find_line(cline + cell, lines,
                                      len(cell)+len(cline))
        if lines[cell_res_start + 1] == "      energy   ":
            logging.debug("noticed energy")
            tally_data.eng = []
            loc_line_id2 = ut.find_line("      total    ",
                                        lines[cell_res_start + 1:], 15)
            erg_lines = lines[cell_res_start + 2:cell_res_start +
                              1 + loc_line_id2]
            for line in erg_lines:
                line = line.strip()
                line = line.split(" ")
                tally_data.eng.append(float(line[0]))
                tally_data.result.append(float(line[3]))
                tally_data.err.append(float(line[4]))
        else:
            # single value result
            logging.debug('tally e bin count = 1')
            line = lines[cell_res_start + 1]
            line = line.strip()
            line = line.split(" ")
            tally_data.result.append(float(line[0]))
            tally_data.err.append(float(line[1]))

    if tally_data.eng is not None:
        logging.debug('tally e bin count: %s', len(tally_data.eng))

    return tally_data


def read_type_surface(tally_data, lines):
    """ process type 1 or type 2 tally output data"""
    logging.debug("Surface Tally")
    tally_data.areas = []
    tally_data.surfaces = []

    # TODO: if more than a single line of surfaces or areas
    # find areas
    # TODO: sort for type 1 tally with sd card
    if tally_data.type == "2":
        area_line_id = ut.find_line("           areas", lines, 16)
        area_val_line = lines[area_line_id + 2]
        area_val_line = " ".join(area_val_line.split())
        tally_data.areas = np.asarray(area_val_line.split(" "))
        # find surfaces
        suf_val_line = lines[area_line_id + 1]
        suf_val_line = " ".join(suf_val_line.split())
        suf_val_line = suf_val_line.split(":")[1]
        tally_data.surfaces = suf_val_line.split(" ")[1:]

        logging.debug("Tally surface numbers:")
        logging.debug(tally_data.surfaces)
        logging.debug("Tally surface areas:")
        logging.debug(tally_data.areas)

    first_surface_line_id = ut.find_line(" surface ", lines, 9)
    logging.debug("first surface id %s", first_surface_line_id)
    if tally_data.type == "1":
        tally_data.surfaces = lines[first_surface_line_id].strip()
        tally_data.surfaces = [tally_data.surfaces.split()[-1]]
        logging.debug("Tally surface numbers:")
        logging.debug(tally_data.surfaces)

    loc = 0
    surface_line_id = first_surface_line_id
    res_df = []
    rel_err_df = []
    if "energy" in lines[first_surface_line_id + 1]:
        logging.debug("energy bins only")

        for s in tally_data.surfaces:
            # find start and end points
            logging.debug("Reading Surface: %s", s)
            tot_line_id = ut.find_line("      total  ",
                                       lines[surface_line_id:], 13)
            erg_lines = lines[surface_line_id+2:surface_line_id+tot_line_id]

            surface_line_id = ut.find_line(" surface ", lines[loc:], 9)
            surface_line_id = surface_line_id + loc

            loc = tot_line_id + 1
            # set arrays
            erg = []
            res = []
            rel_err = []
            for line in erg_lines:
                line = line.strip()
                line = line.split(" ")
                erg.append(float(line[0]))
                res.append(float(line[3]))
                rel_err.append(float(line[4]))

            res_df.append(res)
            rel_err_df.append(rel_err)

        # simplfy if only one surface
        if len(res_df) == 1:
            tally_data.result = res
            tally_data.err = rel_err
        else:
            tally_data.result = res_df
            tally_data.err = rel_err_df

        # add energy data to tally object
        tally_data.eng = erg

    elif "angle" in lines[first_surface_line_id+1]:
        logging.debug("angle bins")

        if lines[first_surface_line_id+2] == "      energy   ":
            logging.debug("energy bins")
            angles_bins = [-1.0]

            ebin = []
            rel_err = []
            res = []
            in_res = False
            for line in lines[first_surface_line_id:]:
                if line[:11] == " angle  bin":
                    ang_float = process_ang_string(line)
                    angles_bins.append(ang_float)
                    logging.debug(ang_float)
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

            tally_data.result = res_df
            tally_data.err = rel_err_df
            tally_data.ang_bins = angles_bins

        else:
            logging.debug("angle bins only")
    elif "time" in lines[first_surface_line_id+1]:
        logging.debug("time bins")
        end_line_id = ut.find_line(" ===", lines, 4)
        tb, eb, res, err = process_e_t_userbin(
                           lines[first_surface_line_id+1:end_line_id])
        tally_data.times = tb
        tally_data.eng = eb
        tally_data.result = res
        tally_data.err = err

    else:
        logging.debug("single value only")
        line = lines[first_surface_line_id+1]
        line = line.strip()
        line = line.split(" ")
        tally_data.result = [float(line[0])]
        tally_data.err = [float(line[1])]

    return tally_data


def read_type_cell(tally_data, lines):
    """ process type 4 or type 6 tally output data """
    logging.debug("Volume tally")
    tally_data.vols = []
    tally_data.cells = []
    # find cells
    # find volumes/ masses

    # find line that the volumes or masses start at
    if tally_data.type == "4":
        line_id = ut.find_line("           volumes ", lines, 19)
    elif tally_data.type == "6":
        line_id = ut.find_line("           masses ", lines, 18)

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
                tally_data.cells.append(cell)
        else:
            vol_line = " ".join(line.split())
            vol_line = vol_line.split(" ")
            for vol in vol_line:
                tally_data.vols.append(vol)

    lines = lines[line_id:]
    # loop for each cell
    for cell in tally_data.cells:

        results = []
        errs = []
        cell_res_start = ut.find_ind(lines, cell)
        # energy binned data
        if lines[cell_res_start + 1] == "      energy   ":
            logging.debug("noticed energy")
            tally_data.eng = []
            loc_line_id2 = ut.find_line("      total    ",
                                        lines[cell_res_start + 1:], 15)
            erg_lines = lines[cell_res_start + 2:cell_res_start + 1 +
                              loc_line_id2]
            for line in erg_lines:
                line = line.strip()
                line = line.split(" ")
                tally_data.eng.append(float(line[0]))
                results.append(float(line[3]))
                errs.append(float(line[4]))
            tally_data.result.append(results)
            tally_data.err.append(errs)
        # time bins
        elif "time" in lines[cell_res_start+1]:            
            end_line_id = ut.find_line(" ===", lines, 4)
            # check if energy bins as well as time
            if "energy" in lines[cell_res_start+2]:
                logging.debug("energy & time bins")
                tb, eb, res, err = process_e_t_userbin(
                               lines[cell_res_start+1:end_line_id])
                tally_data.times = tb
                tally_data.eng = eb
                tally_data.result = res
                tally_data.err = err
            else:
                # just time bins
                logging.debug("time bins only")
                end_line_id = ut.find_ind(lines, "total") + 2
                lines = lines[cell_res_start+1:end_line_id]
                time_bins = []

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
                        
                tally_data.times = time_bins
                tally_data.result = results
                tally_data.err = errs
                           

        else:
            # single value per cell data
            data_line = lines[cell_res_start + 1]
            data_line = " ".join(data_line.split())
            data_line = data_line.split(" ")
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
    logging.debug("x: %s", tally_data.x)
    logging.debug("y: %s", tally_data.y)
    logging.debug("z: %s", tally_data.z)
    res_line = lines[loc_line_id + 1]

    # check if energy dependant
    if res_line == "      energy   ":
        logging.debug("energy dependant")
        tally_data.eng = []
        total_line_id2 = ut.find_line("      total", lines[loc_line_id+1:], 11)
        erg_lines = lines[loc_line_id + 2:loc_line_id + total_line_id2+1]

        for line in erg_lines:
            line = line.strip()
            line = line.split(" ")
            tally_data.eng.append(float(line[0]))
            tally_data.result.append(float(line[3]))
            tally_data.err.append(float(line[4]))
    elif "time" in res_line:
        logging.debug("found time")
        # add time counter
        times = []
        t1_res = []
        t1_err = []
        t2_res = []
        t2_err = []
        t3_res = []
        t3_err = []
        t4_res = []
        t4_err = []
        t5_res = []
        t5_err = []
        ergs = []

        tcount = 0
        loc_line_id2 = ut.find_line(" detector located",
                                    lines[loc_line_id+2:], 17)
        erg_lines = lines[loc_line_id + 1:loc_line_id + loc_line_id2-1]
        in_res = False
        for line in erg_lines:
            if ("total" in line) and ("time" not in line):
                in_res = False
                tally_data.result.append(t1_res)
                tally_data.result.append(t2_res)
                tally_data.result.append(t3_res)
                tally_data.result.append(t4_res)
                tally_data.result.append(t5_res)
                tally_data.err.append(t1_err)
                tally_data.err.append(t2_err)
                tally_data.err.append(t3_err)
                tally_data.err.append(t4_err)
                tally_data.err.append(t5_err)
                tally_data.eng = ergs
                t1_res = []
                t1_err = []
                t2_res = []
                t2_err = []
                t3_res = []
                t3_err = []
                t4_res = []
                t4_err = []
                t5_res = []
                t5_err = []
                ergs = []
            elif in_res:
                line = line.strip()
                line = " ".join(line.split())
                line = line.split(" ")
                ergs.append(float(line[0]))
                if tcount >= 1:
                    t1_res.append(float(line[1]))
                    t1_err.append(float(line[2]))
                if tcount >= 2:
                    t2_res.append(float(line[3]))
                    t2_err.append(float(line[4]))
                if tcount >= 3:
                    t3_res.append(float(line[5]))
                    t3_err.append(float(line[6]))
                if tcount >= 4:
                    t4_res.append(float(line[7]))
                    t4_err.append(float(line[8]))
                if tcount >= 5:
                    t5_res.append(float(line[9]))
                    t5_err.append(float(line[10]))

            elif "energy" in line:
                in_res = True
            elif "time" in line:
                line = line.strip()
                line = " ".join(line.split())
                line = line.split(" ")
                tcount = len(line[1:])
                logging.debug("tcount: %s", tcount)

                for t in line[1:]:
                    times.append(t)

        tally_data.times = times
    elif "user bin" in res_line:
        # user bins used
        # assumes if user bins then also energy and time bins
        # curently extracts total flux not uncollided
        logging.debug("Special user bin tally")
        user_bins = []
        user_bin_locs = []
        user_bin = res_line.split(" ")[-1]
        logging.debug("User bin: %s", user_bin)
        user_bins.append(user_bin)
        user_bin_locs.append(0)
        for i, line in enumerate(lines[loc_line_id+1:]):
            if "user bin" in line:
                user_bin = line.split(" ")[-1]
                user_bins.append(user_bin)
                user_bin_locs.append(i)
                if user_bin == "total":
                    break
        tally_data.user_bins = user_bins

        bin_data = lines[loc_line_id+1:]
        i = 0
        while i < len(user_bin_locs)-1:
            ubin_data = bin_data[user_bin_locs[i]:user_bin_locs[i+1]]
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
    ave_line = ut.string_cleaner(ave_line)
    ave_line = ave_line.split("=")
    tally_data.average_per_history = float(ave_line[1][1:13])
    tally_data.largest_score = float(ave_line[-1])
    n_line = lines[ave_line_id+1]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split("=")
    tally_data.largest_score_nps = float(n_line[-1])
    
    # read score misses data
    tally_data.misses = {}
    
    score_miss_line_id = ut.find_ind(lines, "score misses")
    n_line = lines[score_miss_line_id+1]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["russian roulette on pd"] = float(n_line[-1])
    
    n_line = lines[score_miss_line_id+2]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["psc=0"] = float(n_line[-1])
    
    n_line = lines[score_miss_line_id+3]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["russian roulette in transmission"] = float(n_line[-1])
    
    n_line = lines[score_miss_line_id+4]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["underflow in transmission"] = float(n_line[-1])
    
    n_line = lines[score_miss_line_id+5]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["hit a zero-importance cell"] = float(n_line[-1])
    
    n_line = lines[score_miss_line_id+6]
    n_line = ut.string_cleaner(n_line)
    n_line = n_line.split(" ")
    tally_data.misses["energy cutoff"] = float(n_line[-1])

    
    return tally_data


def read_stat_tests(lines):
    """ initial stat test reader"""
    stat_res_line_id = ut.find_line(" passed", lines, 7)
    stat_line = lines[stat_res_line_id]
    stat_line = ut.string_cleaner(stat_line)
    stat_line = stat_line.split(" ")[1:]
    return stat_line


def read_output_file(path):
    """ reads an mcnp output file
        input is a path the to an ouput file
        output is an mcnp output object
    """
    logging.info('Reading MCNP output file: %s', path)
    ofile_data = ut.get_lines(path)
    mc_data = MCNPOutput()

    # general
    mc_data.file_name = path
    mc_data.version = read_version(ofile_data)
    mc_data.date, mc_data.start_time = read_run_date(ofile_data)
    mc_data.comments, mc_data.warnings = read_comments_warnings(ofile_data)

    # read specific tables
    # mc_data.t60 = read_table60(ofile_data)

    # tallies
    tls = get_tally_nums(ofile_data)
    for tnum in tls:
        mc_data.tally_data.append(read_tally(ofile_data, tnum))

    return mc_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()

    read_output_file(args.input)
