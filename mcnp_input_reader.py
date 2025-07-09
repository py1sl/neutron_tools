"""
MCNP input file reader
"""
import argparse
import neut_utilities as ut
import pandas as pd


class mcnp_input():
    """ """

    def __init__(self):
        self.cell_list = None
        self.mat_num_list = None
        self.mat_list = []
        self.tal_num_list = None
        self.surface_list = None
        self.surface_block = None
        self.cell_block = None
        self.data_block = None
        self.comments = None
        self.file_path = None
        self.mode = None
        self.is_sdef = True
        self.is_kcode = False


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
        self.cell_comment = []

    def __str__(self):
        print_list = []
        print_list.append("Cell number: ", self.number)
        print_list.append("Cell material: ", self.mat)
        print_list.append("Cell density: ", self.density)
        print_list.append("Cell geom: ", self.geom)
        print_list.append("Cell surfaces: ", self.surfaces)
        print_list.append("Cell imp p:", self.imp_p)
        print_list.append("Cell imp n:", self.imp_n)

        return "\n".join(print_list)


class mcnp_material():
    """ class representing a MCNP materials definition """
    def __init__(self):
        self.number = None
        self.is_by_weight = True
        self.num_nuclides = 0
        self.composition = None
        self.keywords = None


class mcnp_tally():
    """MCNP tally input """
    def __init__(self):
        self.number = None
        self.tal_type = None
        self.data = None
        self.has_ebins = False
        self.has_tbins = False
        self.has_fm = False
        self.has_sd_card = False
        self.has_fc_comment = False

    def __str__(self):
        print_list = []
        print_list.append("Tally number: ", self.number)
        print_list.append("Tally card:", self.data)

        if self.has_ebins:
            print_list.append("Has energy bins")
        if self.has_tbins:
            print_list.append("Has time bins")
        if self.has_fm:
            print_list.append("Is modified by a flux modifed card")

        return "\n".join(print_list)


def long_line_index(lines):
    """ find index of lines longer than 80 characters"""
    long_lines = []
    for i, line in enumerate(lines):
        if len(line) > 79:
            if line.lower().startswith("c "):
                continue
            elif " $ " in line:
                continue
            else:
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
    particle_list = ["n", "p", "h", "e", "|", "q", "u", "v", "!"]
    for particle in mode:
        if particle.lower() not in particle_list:
            return False
    return True


def get_full_line_comments(lines):
    """  extracts all full line comments """
    comments = {}
    for i, line in enumerate(lines):
        if len(line) > 1 and line[0].lower() == "c" and line[1] == " ":
            comments[i] = line
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
    surface_types = ("p", "px", "py", "pz", "cx", "cy", "cz",
                     "s", "so", "c/x", "c/y", "c/z", "gq", "sq",
                     "sx", "sy", "sz", "kx", "ky", "kz", "k/x",
                     "k/y", "k/z", "tx", "ty", "tz")
    macro_types = ("rpp", "rcc", "box", "sph", "wed", "rec", "ell",
                   "hex", "arb", "trc", "rhp")
    if surface in surface_types:
        return True
    elif surface in macro_types:
        return True

    return False


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
    """ find the location and count of blank lines in the file """
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
        if "$" in part:
            part = part.split("$")
            cell.cell_comment.append(part[-1])
            part = part[0]
        if len(part) == 0:
            continue
        part = part.strip("()-")
        if "imp" in part.lower():
            cell = process_imp(part, cell)
        elif part[0].isdigit():
            part = part.split(":")
            for s in part:
                surfaces.append(float(s))
        else:
            print(f"{part} part not recogninsed")

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
        elif line.startswith("     "):
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


def cells_with_surface(surf_num, cell_list):
    """ get all cells that contain surface """
    cells = []
    for cell in cell_list:
        if surf_num in cell.surfaces:
            cells.append(cell)
    return cells


def get_mat(mat_num, mat_list):
    """ retrieve a particular material number  """
    for mat in mat_list:
        if mat.number == mat_num:
            return mat

    return None


def check_valid_mat_num(mat_num):
    """ checks a material number is valid in MCNP"""
    if mat_num > 99999999:
        return False
    else:
        return True


def check_valid_surf_num(surf_num):
    """ checks surface number is a valid MCNP surface number """
    if surf_num > 99999999:
        return False
    else:
        return True


def check_valid_cell_num(cell_num):
    """ checks surface number is a valid MCNP surface number """
    if cell_num > 99999999:
        return False
    else:
        return True


def check_cell_mat_exists(cell, mat_list):
    """ checks the material listed in a cell has a material """
    if get_mat(cell.mat, mat_list) is None:
        return False
    else:
        return True


def check_cell_exists(cell_num, cell_list):
    """ checks a cell object exists for that cell number"""
    if get_cell(cell_num, cell_list) is None:
        return False
    else:
        return True


def remove_inline_comment(line):
    """ in line comments are  every thing after a $ """
    line = line.split("$")[0]
    return line


def read_material_lines(mat_num, lines):
    """ extracts the block of lines used for a given material """
    material_lines = []
    in_mat = False

    for line in lines:
        line = line.lower()

        # check if line is a continuation of material
        if in_mat:
            if line.startswith("    "):
                line = remove_inline_comment(line)
                material_lines.append(line)
            # check for full line comments
            elif line.startswith("c "):
                continue
            # find end of material
            elif line and not line.startswith("    "):
                break
        # find material lines
        if len(line) > 1 and line[0] == "m" and line[1].isdigit():
            mnum = line.split(" ")[0][1:]
            if mnum == str(mat_num):
                in_mat = True
                line = remove_inline_comment(line)
                material_lines.append(line)

    material = " ".join(material_lines)
    material = ut.string_cleaner(material)
    material = process_material_line(material, mat_num)

    return material


def process_material_keyword(entry, mat):
    """ process a material keyword """
    entry = entry.split("=")
    key = entry[0]

    # deal with multiple value keywords - the reflectivity ones
    if len(entry) == 2:
        value = entry[-1]
    else:
        value = entry[1:]

    if mat.keywords:
        mat.keywords[key] = value
    else:
        mat.keywords = {key: value}

    return mat


def process_material_line(mat_line, mat_num):
    """ """
    mat = mcnp_material()
    mat.number = mat_num

    # split and ignore the mat number part
    mat_line = mat_line.split(" ")[1:]

    # search for key words
    keyword_entries = [entry for entry in mat_line if isinstance(entry, str) and "=" in entry]
    if len(keyword_entries) > 0:
        for entry in keyword_entries:
            mat = process_material_keyword(entry, mat)

    # remove keyword entries from mat_line
    filtered_data = [entry for entry in mat_line if not (isinstance(entry, str) and "=" in entry)]
    # convert to a material dict with zaid - fraction pairs
    material_dict = {filtered_data[i]: float(filtered_data[i + 1]) for i in range(0, len(filtered_data), 2)}

    mat.composition = material_dict

    return mat


def check_valid_mat_keyword(mat):
    """ checks that any keywords found for the material are valid inputs """
    valid_keywords = ("plib", "hlib", "gas", "estep", "hstep",
                      "nlib", "pnlib", "elib", "alib", "slib",
                      "tlib", "dlib", "cond", "refi", "refc", "refs")
    for key in mat.keywords.keys():
        if key not in valid_keywords:
            raise ValueError(f'{key} input not recognised as valid keyword for a material')


def read_mcnp_input(fpath):
    """ reads the mcnp input file,
        main entry point for this module
    """

    ifile = ut.get_lines(fpath)

    mc_in = mcnp_input()
    mc_in.file_path = fpath
    mc_in.cell_block, mc_in.surface_block, mc_in.data_block = split_blocs(ifile)
    mc_in.cell_list = process_cell_block(mc_in.cell_block)

    mc_comments = get_full_line_comments(ifile)

    mc_in.mode = read_mode_card(mc_in.data_block)
    mc_in.tal_num_list = get_tally_numbers(mc_in.data_block)
    mc_in.mat_num_list = get_material_numbers(mc_in.data_block)

    for mat_num in mc_in.mat_num_list:
        mat = read_material_lines(mat_num, mc_in.data_block)
        mc_in.mat_list.append(mat)

    return mc_in


def vised_compatible(fname):
    """ makes a modern mcnp file work with vised mcnpx version """
    ut.text_replace(fname, "mphys", "c mphys")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    mc_in = read_mcnp_input(args.input)
