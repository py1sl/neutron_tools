"""
MCNP input checker
"""

import argparse
import re
import neut_utilities as ut
import mcnp_input_reader


def line_checker(fpath):
    """ takes a file and checks for lines over 80 chars and tabs"""
    clist = []
    tlist = []
    f = open(fpath)
    if f is None:
        raise Exception("File not opened.")
    f.seek(0)
    for i, line in enumerate(f):
        if len(line) > 79:
            clist.append(i+1)
            print('line', i+1, 'is overfull')
    f.seek(0)
    for i, line in enumerate(f):
        if (re.search('\t', line)) is not None:
            print('line', i+1, 'has a tab')
            tlist.append(i+1)
        #     line.replace('\t', '     ')
    f.seek(0)
    f.close()

    return clist, tlist


def dup_data_checker(fpath):
    """ checks for duplicate card entries in data block. returns mode, nps,
    sdef index and duplicate entry """
    ifile = ut.get_lines(fpath)
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
