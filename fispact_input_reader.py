# -*- coding: utf-8 -*-
"""
Fispact input file reader
S Lilley
March 2019
"""
import sys
import argparse
import neut_utilities as ut


def get_irrad_profile(lines):
    """ """
    return None
    
    
def get_cool_times(lines):
    """ """
    return None

    
def get_comments(lines):
    """ extract comment lines from the file """
    return None

    
def read_fispact_input(fpath):
    """  processes a fispact input file """
    ifile = ut.get_lines(fpath)
    return ifile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads Fispact input file")
    parser.add_argument("input", help="path to the fispact input file")
    args = parser.parse_args()

    read_fispact_input(args.input)