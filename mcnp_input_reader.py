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
        self.surfaces_dict = None
        self.surface_block = None
        self.cell_block = None
        self.data_block = None
        self.comments = None
        self.file_path = None
        self.mode = None
        self.is_sdef = True
        self.is_kcode = False
        self.is_void = False
        self.is_ptrac = False

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

class mcnp_surface():
    """ class representing a MCNP surface definition """
    def __init__(self):
        self.number = None
        self.surf_type = None
        self.params = []
        self.has_transform = False
        self.transform = None
        self.comment = None

    def __str__(self):
        print_list = []
        print_list.append("Surface number: ", self.number)
        print_list.append("Surface type: ", self.surf_type)
        print_list.append("Surface parameters: ", self.params)
        if self.has_transform:
            print_list.append("Surface transform: ", self.transform)
        if self.comment is not None:
            print_list.append("Surface comment: ", self.comment)

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
        if self.density is not None:
            print_list.append("Cell density: ", self.density)
        print_list.append("Cell geom: ", self.geom)
        print_list.append("Cell surfaces: ", self.surfaces)
        print_list.append("Cell importances: ", self.imp)
        print_list.append("Cell comments: ", self.cell_comment)
        print_list.append("Cell parameters: ", self.param_list)


        return "\n".join(print_list)


class mcnp_material():
    """ class representing a MCNP materials definition """
    def __init__(self):
        self.number = None
        self.is_by_weight = True
        self.num_nuclides = 0
        self.composition = None
        self.keywords = None
        self.thermal_scattering = None
        self.mx_lines = None

    def __str__(self):
        print_list = []
        print_list.append("Material number: ", self.number)
        print_list.append("Number of Nuclides: ", self.num_nuclides)
        print_list.append("Composition: ", self.composition)
        if self.keywords is not None:
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
    line = get_card_lines(lines, "mode")
    if len(line) == 0:
        return None # mode card not present
    line = " ".join(line)
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
        elif is_continue_line(line):
            geom.append(line)

    # add last cell
    cell = process_geom(geom, cell)
    cell_dict[cell.number] = cell

    return cell_dict


def get_cell(cell_num, cells):
    """ get cell from cell dict """
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
    """ checks cell number is a valid MCNP cell number """
    return is_valid_number(cell_num)


def is_valid_tally_num(tally_num):
    """ checks tally number is a valid MCNP tally number """
    return is_valid_number(tally_num)


def is_valid_universe_num(uni_num):
    """ checks universe number is a valid MCNP universe number """
    return is_valid_number(uni_num)


def is_number_of_tallies_valid(num_tallies):
    """ chekcks that the total number of tallies in file is valid """
    return is_valid_number(num_tallies, 9999)


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


def get_inline_comment(line):
    """ get the inline comment """
    if has_inline_comment(line):
        line = line.split("$")[1]
    return line


def has_inline_comment(line):
    """ check if there is an inline comment """
    return "$" in line


def read_material_lines(mat_num, lines):
    """ extracts the block of lines used for a given material """
    material_lines = []
    in_mat = False

    for line in lines:
        line = line.lower()

        # check if line is a continuation of material
        if in_mat:
            if is_continue_line(line):
                line = remove_inline_comment(line)
                material_lines.append(line)
            # check for full line comments
            elif line.startswith("c "):
                continue
            # find end of material
            elif line and not is_continue_line(line):
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
    
    # look for any thermal scattering input assocated with the material
    material.thermal_scattering = get_mt_lines(lines, mat_num)
    # look for any mx lines assocated with the material
    material.mx_lines = get_mx_lines(lines, mat_num)

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

        # validate any keywords found
        check_valid_mat_keyword(mat)
    # remove keyword entries from mat_line
    filtered_data = [entry for entry in mat_line if not (isinstance(entry, str) and "=" in entry)]
    # convert to a material dict with zaid - fraction pairs
    mat.composition = {filtered_data[i]: float(filtered_data[i + 1]) for i in range(0, len(filtered_data), 2)}
    mat.num_nuclides = len(mat.composition)

    return mat


def check_valid_mat_keyword(mat):
    """ checks that any keywords found for the material are valid inputs """
    valid_keywords = ("plib", "hlib", "gas", "estep", "hstep",
                      "nlib", "pnlib", "elib", "alib", "slib",
                      "tlib", "dlib", "cond", "refi", "refc", "refs")
    for key in mat.keywords.keys():
        if key not in valid_keywords:
            raise ValueError(f'{key} input not recognised as valid keyword for a material')


def get_mt_lines(lines, mnum):
    """ finds mt lines for a material"""
    return get_prefixed_lines(lines, "mt", mnum)


def get_mx_lines(lines, mnum):
    """ finds mx lines for a material"""
    return get_prefixed_lines(lines, "mx", mnum)


def is_card_present(lines, card):
    """ check if a particular card is present in the lines """
    for line in lines:
        line = line.lower()
        if line.startswith(card.lower()):
            return True
    return False


def get_card_lines(lines, card):
    """ get all lines associated with a particular card """
    card_lines = []
    in_block = False

    for line in lines:
        line = line.lower()

        if in_block:
            if is_continue_line(line):
                line = remove_inline_comment(line)
                card_lines.append(line)
            elif line.startswith("c "):
                continue
            elif line and not is_continue_line(line):
                break

        # find starting card line
        if line.startswith(card.lower()) and (line[len(card):len(card)+1] in (" ", ":")):
            in_block = True
            line = remove_inline_comment(line)
            card_lines.append(line)

    return card_lines


def get_prefixed_lines(lines, prefix, mnum):
    """Generic finder for continuation blocks that start with a prefixed card.
    """
    card = f"{prefix}{mnum}"
    pref_lines = get_card_lines(lines, card)

    return pref_lines


def is_continue_line(line):
    """checks if line has 5 spaces at start """
    return line.startswith(" " * 5)


def process_tally_line(tal_line, tal_num):
    """ process a tally line into a tally object """
    tally = mcnp_tally()
    tally.number = tal_num
    tally.data = tal_line

    # get tally type
    tal_type = tal_line.split(" ")[0]
    tal_type = tal_type.split(":")[0][1:]
    tally.tal_type = tal_type

    return tally


def read_tally_lines(tal_num, lines):
    """ extracts the block of lines used for a given tally """
    tally_lines = []
    in_tal = False

    for line in lines:
        line = line.lower()

        # check if line is a continuation of tally
        if in_tal:
            if is_continue_line(line):
                line = remove_inline_comment(line)
                tally_lines.append(line)
            # check for full line comments
            elif line.startswith("c "):
                continue
            # find end of tally
            elif line and not is_continue_line(line):
                break
        # find tally lines
        if len(line) > 1 and line[0] == "f" and line[1].isdigit():
            tnum = line.split(" ")[0][1:]
            tnum = tnum.split(":")[0]
            if tnum == str(tal_num):
                in_tal = True
                line = remove_inline_comment(line)
                tally_lines.append(line)

    tally = " ".join(tally_lines)
    tally = ut.string_cleaner(tally)
    # process tally line into object
    tally = process_tally_line(tally, tal_num)

    # look for any ebins, tbins, fm, sd, fc associated with tally
    tally.has_ebins = is_card_present(lines, f"e{tal_num} ")
    tally.has_tbins = is_card_present(lines, f"t{tal_num} ")
    tally.has_fm = is_card_present(lines, f"fm{tal_num} ")
    tally.has_sd = is_card_present(lines, f"sd{tal_num} ")
    tally.has_fc = is_card_present(lines, f"fc{tal_num} ")

    return tally


def process_data_block(mc_in):
    """ """
    mc_in.mode = read_mode_card(mc_in.data_block)
    mc_in.tal_num_list = get_tally_numbers(mc_in.data_block)
    mc_in.mat_num_list = get_material_numbers(mc_in.data_block)
    mc_in.materials = {}
    
    mc_in.is_void = is_card_present(mc_in.data_block, "void")
    mc_in.is_kcode = is_card_present(mc_in.data_block, "kcode")
    mc_in.is_sdef = is_card_present(mc_in.data_block, "sdef")
    mc_in.is_ptrac = is_card_present(mc_in.data_block, "ptrac")


    for mat_num in mc_in.mat_num_list:
        mat = read_material_lines(mat_num, mc_in.data_block)
        mc_in.materials[mat.number] = mat

    for tal_num in mc_in.tal_num_list:
        tally = read_tally_lines(tal_num, mc_in.data_block)
        if mc_in.tallies is None:
            mc_in.tallies = {}
        mc_in.tallies[tally.number] = tally

    return mc_in


def process_surface_block(surf_bloc):
    """ process surface block into a surface list """
    surface_dict = {}
    surf_line = ""
    for line in surf_bloc:
        if is_continue_line(line):
            surf_line = surf_line + " " + ut.string_cleaner(line)
        elif line.strip() == "":
            continue
        elif line.lower().startswith("c "):
            continue
        elif len(surf_line) > 0:
            surf = process_surface_line(surf_line)
            surface_dict[surf.number] = surf
            surf_line = ut.string_cleaner(line)
        else:
            surf_line = ut.string_cleaner(line)
    
    # add last surface line if present
    if len(surf_line) > 0:
        surf = process_surface_line(surf_line)
        surface_dict[surf.number] = surf

    return surface_dict


def process_surface_line(surf_line):
    """ process a surface line into a surface object """
    surf_line = surf_line.lower()
    surf_line = surf_line.split(" ")

    surf = mcnp_surface()
    surf.number = int(surf_line[0]) # surface number
    surf.has_transform = check_surf_transform(surf_line)
    if surf.has_transform:
        surf.surf_type = surf_line[2]
        surf.params = surf_line[3:]
        surf.transform = surf_line[1]
    else:
        surf.surf_type = surf_line[1]
        surf.params = surf_line[2:]
    
    if not is_surface_type_valid(surf.surf_type):
        raise ValueError(f"Surface type {surf.surf_type} not valid MCNP surface type")

    return surf


def check_surf_transform(surf_line):
    """ check if surface has a transform """

    if surf_line[1].isdigit():
        return True
    return False


def read_mcnp_input(fpath):
    """ reads the mcnp input file,
        main entry point for this module
    """

    ifile = ut.get_lines(fpath)

    mc_in = mcnp_input()
    mc_in.file_path = fpath
    mc_in.cell_block, mc_in.surface_block, mc_in.data_block = split_blocs(ifile)
    mc_in.cells = process_cell_block(mc_in.cell_block)

    mc_in.surfaces_dict = process_surface_block(mc_in.surface_block)
    mc_in.comments = get_full_line_comments(ifile)
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
