"""
MCNP input checker
"""

import argparse
import neut_utilities as ut
import mcnp_input_reader


def line_checker(fpath):
    """ takes a file and checks for lines over 80 chars and tabs"""
    lines = ut.get_lines(fpath)
    tab_list = mcnp_input_reader.tab_finder(lines)
    new_lines = mcnp_input_reader.tab_to_whitespace(lines)
    long_list = mcnp_input_reader.long_line_index(lines)
    for i in tab_list:
        print('\nLine', i, 'has a tab.')
    for i in long_list:
        print('\nLine', i, 'is over 79 characters')

    return new_lines


def input_summary(ifile):
    """ prints a summary of the mcnp input file """
    cell_bloc, surf_bloc, data_bloc = mcnp_input_reader.split_blocs(ifile)
    cell_list = mcnp_input_reader.process_cell_block(cell_bloc)
    surf_df = mcnp_input_reader.surface_reader(surf_bloc)
    mat_nums = mcnp_input_reader.get_material_numbers(data_bloc)
    tally_nums = mcnp_input_reader.get_tally_numbers(data_bloc)
    n_cells = len(cell_list)
    n_mats = len(mat_nums)
    n_surf = len(surf_df)
    n_tallies = len(tally_nums)
    print('No. of cells =', n_cells)
    print('No. of materials =', n_mats)
    print('No. of surfaces =', n_surf)
    print('No. of tallies =', n_tallies)

    return n_cells, n_mats, n_surf, n_tallies


def dup_data_checker(ifile):
    """ checks for duplicate card entries in data block. returns mode, nps,
    sdef index and duplicate entry """
    cell_data, surf_data, data_bloc = mcnp_input_reader.split_blocs(ifile)
    data = cell_data + surf_data + data_bloc
    bloc = []
    spaced = []
    text = []
    # finds the comments and pops them out and into another list
    for row in data:
        text, _, _ = row.partition(' $')
        bloc.append(text)
    for row in bloc:
        new_row = row.split(' ')
        spaced.append(new_row)
    card_data = []
    [card_data.append(c) for c in spaced if c != '']
    # finds the mode, nps and sdef data (only if the first element of the row)
    mode = []
    nps = []
    sdef = []
    for i, e in enumerate(card_data):
        if e[0] == 'mode':
            mode.append((i+1, e[1]))
        if e[0] == 'nps':
            nps.append((i+1, e[1]))
        if e[0] == 'sdef':
            sdef.append((i+1, e[1:]))
    for i, s in enumerate(mode):
        if i >= 1:
            print('More than one mode card entry')
            print('mode (line, entry) --', mode)
    for i, s in enumerate(nps):
        if i >= 1:
            print('More than one nps card entry')
            print('nps (line, entry) --', nps)
    for i, s in enumerate(sdef):
        if i >= 1:
            print('More than one sdef card entry')
            print('sdef (line, entry) --', sdef)

    return mode, nps, sdef


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""takes file name and will
                                     print the line numbers of lines more
                                     than 80 characters long,
                                     and lines with tabs""")
    parser.add_argument("input", help="path to input file", type=str)
    args = parser.parse_args()

    line_checker(args.input)
