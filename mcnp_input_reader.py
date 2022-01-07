# -*- coding: utf-8 -*-
"""
MCNP input file reader
S Lilley
March 2019
"""
import argparse
import neut_utilities as ut


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
    comments = []
    for line in lines:
        if len(line) > 1 and line[0].lower() == "c" and line[1] == " ":
            comments.append(line)
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


def check_surface_type_validity(surface):
    """ check surface is a valid mcnp type"""
    return True


def check_plane(surface):
    """ check entries on plane surface are valid """
    return True


def check_sphere(surface):
    """ check entries on sphere surface are valid"""
    return True


def check_cylinder(surface):
    """ check entries on cylinder surface are valid"""
    return True


def check_cone(surface):
    """ check entries on conical surface are valid """
    return True


def check_GQ(surface):
    """ check entries on GQ surface are valid """
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


def print_cell(cell):
    """ pretty printing of cell object """
    print("Cell number: ", cell.number)
    print("Cell material: ", cell.mat)
    print("Cell density: ", cell.density)
    print("Cell geom: ", cell.geom)
    print("Cell surfaces: ", cell.surfaces)
    print("Cell imp p:", cell.imp_p)
    print("Cell imp n:", cell.imp_n)


def read_mcnp_input(fpath):
    """ """

    ifile = ut.get_lines(fpath)
    cell_bloc, surf_bloc, data_bloc = split_blocs(ifile)
    cell_list = process_cell_block(cell_bloc)

    comments = get_full_line_comments(ifile)

    mat_nums = get_material_numbers(data_bloc)

    return ifile, comments, mat_nums, cell_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    read_mcnp_input(args.input)
