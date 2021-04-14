# -*- coding: utf-8 -*-
"""
Output file reduce utility
reduces MCNP output to just the last rendevous
S Lilley
March 2019
"""
import sys
import argparse
import neut_utilities as ut
import logging


def reduce_ofile(infile, ofile):
    """ reduces mcnp output file to just the data from last rendevous"""

    lines = ut.get_lines(infile)

    # reduce to only the final result set
    try:
        term_line = ut.find_line("      run terminated when", lines, 25)
    except EOFError as e:
        logging.debug(repr(e))
        sys.exit()

    lines = lines[term_line:]
    ut.write_lines(ofile, lines)


if __name__ == "__main__":
    desc = "Reduces MCNP output file to just last rendvous data"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("input", help="path to the mcnp output file")
    parser.add_argument("output", help="path to the reduced output file")
    args = parser.parse_args()

    reduce_ofile(args.input, args.output)
