# -*- coding: utf-8 -*-
"""
Fispact output file reader
S Lilley
March 2019
"""
import sys
import argparse
import neut_utilities as ut

def read_fispact_output(fpath):
    """ """
    ifile = ut.get_lines(fpath)
    return ifile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads fispact output file")
    parser.add_argument("input", help="path to the fispact output file")
    args = parser.parse_args()

    read_fispact_output(args.input)