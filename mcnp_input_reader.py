# -*- coding: utf-8 -*-
"""
MCNP input file reader
S Lilley
March 2019
"""
import argparse
import neut_utilities as ut
import re
import pandas as pd


class mcnp_cell():
    """ """
    def __init__(self):
        self.number = ""
        self.mat = ""
        self.density = None
        self.imp_p = 1.0
        self.imp_n = 1.0
        self.geom = ""
        self.surfaces = []
        self.param_list = []

    def __str__(self):
        cell_ls = """
        Cell number: {self.number},
        Cell material: {self.mat},
        Cell density: {self.density},
        Cell geom: {self.geom},
        Cell surfaces: {self.surfaces},
        Cell imp p: {self.imp_p},
        Cell imp n: {self.imp_n}.
        """
        return cell_ls


class mcnp_input():
    """ """
    def __init__(self):
        self.filename = ''
        self.cell_list = []
        self.surface_list = []
        self.tally_list = []
        self.mat_list = []

    def __str__(self):
        input_ls = """
        Input filename: {self.number},
        Input cell list: {self.cell_list},
        Input surface list: {self.surface_list},
        Input tally list: {self.tally_list},
        Input materials list: {self.mat_list}.
        """
        return input_ls


def long_line_index(lines):
    """ find index of lines longer than 80 characters"""
    long_lines = []
    for i, line in enumerate(lines):
        if len(line) > 79:
            long_lines.append(i)
    if len(long_lines) == 0:
        return None
    else:
        return long_lines


def read_mode_card(lines):
    """ finds the mode card and returns the particle identifiers"""
    mode = None
    for line in lines:
        if line[0:4].lower() == "mode":
            line = ut.string_cleaner(line)
            mode = line.split(" ")[1:]
    return mode


def check_mode_valid(mode):
    """ checks the particles on a mode card are valid particles identifiers """
    particle_list = ["n", "p", "h", "e"]
    for particle in mode:
        if particle.lower() not in particle_list:
            return False
    return True


def get_full_line_comments(lines):
    """  extracts all full line comments """
    comments = {}
    for i, line in enumerate(lines):
        if len(line) > 1 and line[0].lower() == "c" and line[1] == " ":
            comments.update({i+1: line})
    return comments


def get_material_numbers(lines):
    """ extracts all material numbers """
    mat_nums = []
    for line in lines:
        if len(line) > 1 and line[0].lower() == "m" and line[1].isdigit():
            line = ut.string_cleaner(line)
            line = line.split(" ")[0]
            mnum = line[1:]
            mat_nums.append(int(mnum))
    return mat_nums


def get_tally_numbers(lines):
    """ extracts all tally numbers """
    tal_nums = []
    for line in lines:
        if len(line) > 1 and line[0].lower() == "f" and line[1].isdigit():
            line = ut.string_cleaner(line)
            line = line.split(" ")[0]
            line = line.split(":")[0]
            tnum = line[1:]
            tal_nums.append(int(tnum))
    return tal_nums


def check_surfaces(df):
    """ check entries on surface card are valid"""

    types = df.loc[:, 'Type']
    parameters = df.loc[:, 'Parameters']
    count = 0
    incorrect_dict = {}

    for i, c in enumerate(types):
        # Planes
        if c == 'p':
            if 1 <= len(parameters[i]) <= 4:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'px':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'py':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i: c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'pz':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i: c}
                incorrect_dict.update(entry)
                count = +1
        # Spheres
        if c == 'so':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i: c}
                incorrect_dict.update(entry)
                count = +1
        if c == 's':
            if len(parameters[i]) == 4:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'sx':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'sy':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'sz':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        # Cylinders
        if c == 'c/x':
            if len(parameters[i]) == 3:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'c/y':
            if len(parameters[i]) == 3:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'c/z':
            if len(parameters[i]) == 3:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'cx':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'cy':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'cz':
            if len(parameters[i]) == 1:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        # Cones
        if c == 'k/x':
            if len(parameters[i]) == 4:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'k/y':
            if len(parameters[i]) == 4:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'k/z':
            if len(parameters[i]) == 4:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'kx':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'ky':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'kz':
            if len(parameters[i]) == 2:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        # Quadratics
        if c == 'sq':
            if 3 <= len(parameters[i]) <= 10:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'gq':
            if 1 <= len(parameters[i]) <= 10:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = count + 1
        # Tori
        if c == 'tx':
            if 3 <= len(parameters[i]) <= 6:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'ty':
            if 3 <= len(parameters[i]) <= 6:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        if c == 'tz':
            if 3 <= len(parameters[i]) <= 6:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
        # Points
        if c == 'xyzp':
            if len(parameters[i]) <= 3:
                continue
            else:
                entry = {i, c}
                incorrect_dict.update(entry)
                count = +1
    if count != 0:
        print(incorrect_dict)
        return False
    else:
        return True


def find_blank_lines(lines):
    """ find the location and count of balnk lines in the file """
    count = 0
    blank_dict = {}

    for i, line in enumerate(lines):
        if line == "":
            count = count + 1
            blank_dict[count] = i

    return count, blank_dict


def split_blocs(lines):
    """ split into the cell, surf and data blocks """
    blank_count, blank_loc = find_blank_lines(lines)
    cell_bloc = lines[:blank_loc[1]]
    surf_bloc = lines[blank_loc[1]:blank_loc[2]]
    data_bloc = lines[blank_loc[2]:]

    return cell_bloc, surf_bloc, data_bloc


def process_imp(part, cell):
    """ extracts importances for a cell """
    imp_val = part.split("=")[-1]
    imp_particle = part.split(":")[1][0]
    if imp_particle.lower() == "p":
        cell.imp_p = float(imp_val)
    elif imp_particle.lower() == "n":
        cell.imp_n = float(imp_val)

    return cell


def process_geom(geom, cell):
    """ processes geometry part of a cell """
    surfaces = []
    cell.geom = geom

    for part in geom:
        part = part.strip("()-")
        if "imp" in part.lower():
            cell = process_imp(part, cell)
        elif part[0].isdigit():
            part = part.split(":")
            for s in part:
                surfaces.append(float(s))
        else:
            print(" part not recogninsed")

    cell.surfaces = surfaces

    return cell


def process_cell_block(bloc):
    """ split cell block into cell objects """
    cell_list = []
    cell = None
    geom = []
    for line in bloc:
        if line[0].isdigit():
            if cell is not None:
                cell = process_geom(geom, cell)
                cell_list.append(cell)
                geom = []

            cell = mcnp_cell()
            line = ut.string_cleaner(line)
            line = line.split(" ")
            cell.number = int(line[0])
            cell.mat = int(line[1])
            geo_start_pos = 2
            if cell.mat != 0:
                cell.density = float(line[2])
                geo_start_pos = 3
            geom = line[geo_start_pos:]
        elif line[0:4] == "     ":
            geom.append(line)

    # add last cell
    cell = process_geom(geom, cell)
    cell_list.append(cell)

    return cell_list


def get_cell(cell_num, cell_list):
    """ get cell from cell list """
    for cell in cell_list:
        if cell_num == cell.number:
            return cell

    return None


def cells_with_mat(mat_num, cell_list):
    """ get all cells with mat """
    cells = []
    for cell in cell_list:
        if mat_num == cell.mat:
            cells.append(cell)
    return cells


def float_check(n):
    """ tries to take input as float, returns false if error """
    try:
        float(n)
        return True
    except Exception:
        return False


def surface_reader(fpath):
    """ reads from the mcnp file and outputs
    dataframe with the details of the surfaces """
    ifile = ut.get_lines(fpath)
    cell_bloc, surf_bloc, data_bloc = split_blocs(ifile)
    # takes the blank and c line out
    del surf_bloc[0:2]

    # Assumes that a surface description that goes over one line
    # will have a whitespace at the end of every continuing line.
    bloc = []
    comments_list = []
    for i, row in enumerate(surf_bloc):
        if row[-1] == ' ':
            surf_bloc[i] = surf_bloc[i] + surf_bloc[i+1]
            surf_bloc.pop(i+1)

    # finds the comments and pops them out and into another list
    for i, row in enumerate(surf_bloc):
        data, sep, comment = row.partition(' $')
        bloc.append(data)
        if comment == '':
            comments_list.append('--')
        else:
            comments_list.append(comment)

    # joins the row separated list
    # splits it on spaces, now there is a list
    bloc_str = ' \n '.join(bloc)
    bloc_sep = bloc_str.split(' ')

    # gets rid of empty entries ''
    surf = []
    [surf.append(c) for c in bloc_sep if c != '']

    # back into one string, but line separated with \n from earlier
    # so it can be split based on \n
    joined = ' '.join(surf)
    split_l = joined.splitlines()

    # now splits on whitespace and then appends to new list so every
    # interesting bit of data is an entry in a list of lists
    new_list = []
    for i in range(len(split_l)):
        new_list.append(split_l[i].split(' '))

    # list with no ''
    sdata = []
    for i, row in enumerate(new_list):
        row = list(filter(None, new_list[i]))
        sdata.append(row)

    # init lists for dict to go to dataframe
    s_num = []
    s_type = []
    s_transform = []
    s_params = []

    # adds data to columns, special case for transform
    for i, c in enumerate(sdata):
        s_num.append(c[0])
        if float_check(c[1]) is True:
            s_transform.append(c[1])
            s_type.append(c[2])
            s_params.append(c[3:])
        else:
            s_transform.append('--')
            s_type.append(c[1])
            s_params.append(c[2:])

    dict_df = {'Num': s_num, 'Transform': s_transform, 'Type': s_type,
               'Parameters': s_params, 'Comments': comments_list}
    df = pd.DataFrame(dict_df)

    return df


def read_mcnp_input(fpath):
    """ reads and returns: ifile, cells, mats, surf_df, tallies"""

    ifile = ut.get_lines(fpath)
    cell_bloc, surf_bloc, data_bloc = split_blocs(ifile)
    cell_list = process_cell_block(cell_bloc)
    # comments = get_full_line_comments(ifile)
    surf_df = surface_reader(surf_bloc)
    mat_nums = get_material_numbers(data_bloc)
    tally_nums = get_tally_numbers(data_bloc)

    return ifile, cell_list, mat_nums, surf_df, tally_nums


def unused_surfaces(fpath):
    """ checks input for surfaces not used in cells"""
    ifile = ut.get_lines(fpath)
    cell_bloc, surf_bloc, data_bloc = split_blocs(ifile)
    cell_data = []
    cell_used = []
    for row in cell_bloc:
        new_row = row.split(' ')
        if new_row[0] != 'c':
            cell_data.append(new_row)

    for row in cell_data:
        if row[1] == '0':
            cell_used.append(row[2])
            if float_check(row[3]) is True:
                cell_used.append(row[3])
            else:
                continue
        else:
            cell_used.append(row[3])
            if float_check(row[4]) is True:
                cell_used.append(row[4])
            else:
                continue

    df = surface_reader(fpath)
    used = df.loc[:, 'Num']
    used_list = used.values.tolist()

    check = all(i in cell_used for i in used_list)

    if check is False:
        print('Not all surfaces are used')
        return False
    if check is True:
        return True


def dup_surfaces(fpath):
    """ reads in dataframe of surface card and returns duplicate
    entries. True = duplicate. """
    df = surface_reader(fpath)
    # for False - not a duplicate. For True - is duplicate.
    duplicate_df = df.astype(str).duplicated(keep=False)
    print('Duplicated rows: \n', duplicate_df)

    return duplicate_df


def tab_finder(lines):
    """ takes a list of strings and finds tabs and returns the indexes
    of which element of the list has a tab in """
    count = []
    scan = []
    for i, line in enumerate(lines):
        scan.append(re.search('\t', line))
    for i, line in enumerate(lines):
        if scan[i] is not None:
            count.append(i)
    result = [i + 1 for i in count]

    return result


def tab_to_whitespace(lines):
    """ takes lines and converts all tabs
    to five whitespaces and returns the list"""
    # an unusual filler to join and separate. unusual so that it
    # does not appear anywhere else by coincidence
    line = 'filler£!"£$%^&*()[]£'.join(lines)
    new_line = line.replace('\t', '     ')
    new_lines = new_line.split(sep='filler£!"£$%^&*()[]£')

    if len(new_lines) != len(lines):
        raise Exception("""Does not match. Potentially list contains the
                        delimiter. Change the file or
                        change the delimiter.""")

    return new_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    read_mcnp_input(args.input)
