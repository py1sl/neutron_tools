# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import neut_utilities as ut


def reduce_ofile(infile, ofile):
    """ reduces mcnp output file to just the data from last rendevous"""

    lines=ut.get_lines(infile)
    
    # reduce to only the final result set
    try:
        term_line = ut.find_line("      run terminated when", lines, 25)
    except EOFError as e:
        print(repr(e))
        sys.exit()

    lines = lines[term_line:]
    ut.write_lines(ofile, lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduces MCNP output file to just last rendvous data")
    parser.add_argument("input", help="path to the mcnp output file")
    parser.add_argument("output", help="path to the reduced output file")
    args = parser.parse_args()

    reduce_ofile(args.input, args.output)
