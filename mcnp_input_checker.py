"""
MCNP input checker
"""

import argparse
import neut_utilities as ut
import mcnp_input_reader


def line_checker(fpath):
    """ takes a file and checks for lines over 80 chars and coverts tabs to
    whitespace. prints lines over 80 and those that had tabs."""
    lines = ut.get_lines(fpath)
    tab_list = mcnp_input_reader.tab_finder(lines)
    new_lines = mcnp_input_reader.tab_to_whitespace(lines)
    long_list = mcnp_input_reader.long_line_index(lines)
    for i in tab_list:
        print('\nLine', i, 'has a tab.')
    if long_list is not None:
        for i in long_list:
            print('\nLine', i, 'is over 79 characters.')
    else:
        pass

    return new_lines


def input_summary(fpath):
    """ returns an input class for printing a summary of the mcnp input file
    by calling str(). """
    # initialises input object in the function as it is only for printing
    # will always be empty beforehand
    input = mcnp_input_reader.mcnp_input()

    ifile = ut.get_lines(fpath)
    cell_bloc, surf_bloc, data_bloc = mcnp_input_reader.split_blocs(ifile)
    cell_list = mcnp_input_reader.process_cell_block(cell_bloc)
    surf_df = mcnp_input_reader.surface_reader(surf_bloc)
    mat_nums = mcnp_input_reader.get_material_numbers(data_bloc)
    tally_nums = mcnp_input_reader.get_tally_numbers(data_bloc)
    input.filename = fpath
    input.cell_list = len(cell_list)
    input.mat_list = len(mat_nums)
    input.tally_list = len(tally_nums)
    input.surface_list = len(surf_df)

    return input


def dup_data_checker(ifile):
    """ checks for duplicate card entries in data block. returns mode, nps,
    sdef, mphys, prdmp index and duplicate entry """
    bloc = []
    spaced = []
    text = []
    # finds the comments and pops them out and into another list
    for row in ifile:
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
    mphys = []
    prdmp = []
    for i, e in enumerate(card_data):
        if e[0] == 'mode':
            mode.append((i+1, e[1:]))
        if e[0] == 'nps':
            nps.append((i+1, e[1]))
        if e[0] == 'sdef':
            sdef.append((i+1, e[1:]))
        if e[0] == 'mphys':
            mphys.append((i+1, e[1]))
        if e[0] == 'prdmp':
            prdmp.append((i+1, e[1:]))
    if len(mode) >= 2:
        print('More than one mode card entry')
        print('mode (line, entry) --', mode)
    if len(nps) >= 2:
        print('More than one nps card entry')
        print('nps (line, entry) --', nps)
    if len(sdef) >= 2:
        print('More than one sdef card entry')
        print('sdef (line, entry) --', sdef)
    if len(mphys) >= 2:
        print('More than one sdef card entry')
        print('mphys (line, entry) --', mphys)
    if len(prdmp) >= 2:
        print('More than one sdef card entry')
        print('prdmp (line, entry) --', prdmp)

    return mode, nps, sdef, mphys, prdmp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""for checking validity
                                     of mcnp input and printing summary
                                     of input file.""")
    parser.add_argument("filepath", help="path to mcnp input file",
                        nargs="?", default='test_output/default.txt')
    args = parser.parse_args()

    lines = ut.get_lines(args.filepath)
    line_checker(args.filepath)
    print(str(input_summary(args.filepath)))
    dup_data_checker(lines)
