# -*- coding: utf-8 -*-
"""
MCNP input file reader
S Lilley
March 2019
"""
import sys
import argparse
import neut_utilities as ut

def read_mcnp_input(fpath):
    """ """
    ifile = ut.get_lines(fpath)
    return ifile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    read_mcnp_input(args.input)