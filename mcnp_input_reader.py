"""
MCNP input file reader
"""
import argparse
import neut_utilities as ut
import pandas as pd


class mcnp_input():
    """ """

    def __init__(self):
        self.cells = None
        self.mat_num_list = None
        self.materials = None
        self.tal_num_list = None
        self.tallies = None
        self.surface_list = None
        self.surface_block = None
        self.cell_block = None
        self.data_block = None
        self.comments = None
        self.file_path = None
        self.mode = None
        self.is_sdef = True
        self.is_kcode = False

    def __str__(self):
        print_list = []
        print_list.append("File: ", self.file_path)
        print_list.append("Mode: ", self.mode)

        if self.is_sdef:
            print_list.append("Fixed source calculation")
        elif self.is_kcode:
            print_list.append("Kcode calculation")
        else:
            print_list.append("Unknown calculation type")


        return "\n".join(print_list)


class mcnp_cell():
    """ """

    def __init__(self):
        self.number = ""
        self.mat = ""
        self.density = None
        self.imp = {}
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

        return "\n".join(print_list)


class mcnp_material():
    """ class representing a MCNP materials definition """
    def __init__(self):
        self.number = None
        self.is_by_weight = True
        self.num_nuclides = 0
        self.composition = None
        self.keywords = None

    def __str__(self):
        print_list = []
        print_list.append("Material number: ", self.number)
        print_list.append("Number of Nuclides: ", self.num_nuclides)
        print_list.append("Composition: ", self.composition)
        print_list.append("Keywords: ", self.keywords)

        return "\n".join(print_list)


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
    """ find index of lines longer than 80 characters
        ignores full comment lines and inline comment lines
    """
    long_lines = []
    for i, line in enumerate(lines):
        if len(line) > 79:
            if line.lower().startswith("c "):
                continue
            elif " $" in line:
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
        if line.lower().startswith("mode "):
            line = ut.string_cleaner(line)
            mode = line.split(" ")[1:]
    return mode


def is_mode_valid(mode):
    """ checks the particles on a mode card are valid particles identifiers
    """
    # todo : particle list should live somewhere else
    particle_list = ["n", "p", "h", "e", "|", "q", "u", "v", "!"]
    for particle in mode:
        if particle.lower() not in particle_list:
            return False
    return True


def get_full_line_comments(lines):
    """  extracts all full line comments """
    comments = {}
    for i, line in enumerate(lines):
        if line.lower().startswith("c "):
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


def is_surface_type_valid(surface):
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
        if line.strip() == "":
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
    # todo add check valid particle type
    cell.imp[imp_particle] = float(imp_val)

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
    cell_dict = {}
    cell = None
    geom = []
    for line in bloc:
        if line[0].isdigit():
            if cell is not None:
                cell = process_geom(geom, cell)
                cell_dict[cell.number] = cell
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
    cell_dict[cell.number] = cell

    return cell_dict


def get_cell(cell_num, cells):
    """ get cell from cell list """
    return cells.get(cell_num)


def cells_with_mat(mat_num, cells):
    """ get all cells with mat """
    return [cell for cell in cells.values() if cell.mat == mat_num]


def cells_with_surface(surf_num, cells):
    """ get all cells that contain surface with id surf_num """
    return [cell for cell in cells.values() if surf_num in cell.surfaces]


def get_mat(mat_num, mats):
    """ retrieve a particular material number  """
    return mats.get(mat_num)


def is_valid_number(num, max_num=99999999):
    """  check if a number is less than the max_number """
    return num <= max_num


def is_valid_mat_num(mat_num):
    """ checks a material number is valid in MCNP"""
    return is_valid_number(mat_num)


def is_valid_surf_num(surf_num):
    """ checks surface number is a valid MCNP surface number """
    return is_valid_number(surf_num)


def is_valid_cell_num(cell_num):
    """ checks surface number is a valid MCNP surface number """
    return is_valid_number(cell_num)


def check_cell_mat_exists(cell, mats):
    """ checks the material listed in a cell has a material """
    if get_mat(cell.mat, mats) is None:
        return False
    else:
        return True


def check_cell_exists(cell_num, cells):
    """ checks a cell object exists for that cell number"""
    if get_cell(cell_num, cells) is None:
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
    mat.composition = {filtered_data[i]: float(filtered_data[i + 1]) for i in range(0, len(filtered_data), 2)}

    return mat


def check_valid_mat_keyword(mat):
    """ checks that any keywords found for the material are valid inputs """
    valid_keywords = ("plib", "hlib", "gas", "estep", "hstep",
                      "nlib", "pnlib", "elib", "alib", "slib",
                      "tlib", "dlib", "cond", "refi", "refc", "refs")
    for key in mat.keywords.keys():
        if key not in valid_keywords:
            raise ValueError(f'{key} input not recognised as valid keyword for a material')


def process_data_block(mc_in):
    """ """
    mc_in.mode = read_mode_card(mc_in.data_block)
    mc_in.tal_num_list = get_tally_numbers(mc_in.data_block)
    mc_in.mat_num_list = get_material_numbers(mc_in.data_block)
    mc_in.materials = {}

    for mat_num in mc_in.mat_num_list:
        mat = read_material_lines(mat_num, mc_in.data_block)
        mc_in.materials[mat.number] = mat

    return mc_in
    
    
def read_mcnp_input(fpath):
    """ reads the mcnp input file,
        main entry point for this module
    """

    ifile = ut.get_lines(fpath)

    mc_in = mcnp_input()
    mc_in.file_path = fpath
    mc_in.cell_block, mc_in.surface_block, mc_in.data_block = split_blocs(ifile)
    mc_in.cells = process_cell_block(mc_in.cell_block)

    mc_comments = get_full_line_comments(ifile)
    mc_in = process_data_block(mc_in)
    
    return mc_in


def vised_compatible(fname):
    """ makes a modern mcnp file work with vised mcnpx version """
    ut.text_replace(fname, "mphys", "c mphys")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    mc_in = read_mcnp_input(args.input)
