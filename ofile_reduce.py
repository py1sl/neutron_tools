# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse


def get_lines(path):
    with open(path) as f:
        lines = f.read().splitlines()
    f.close()
    return lines


def find_line(text, lines, num):
    """finds a index of the line in lines where the text is present in
       the first num characters
    """
    i = 0
    imax = len(lines) -1
    for l in lines:
        if i == imax:
            raise EOFError(text + " not found in file")
        i = i + 1
        if l[0:num] == text:
            print("found " + text + " at line :" + str(i))
            return i - 1

def write_lines(path, lines):
    f = open(path, 'w')
    for l in lines:
        f.write(l)
        f.write("\n")
    f.close()


def reduce_ofile(infile, ofile):
    """ reduces mcnp output file to just the data from last rendevous"""

    lines=get_lines(infile)
    
    # reduce to only the final result set
    try:
        term_line = find_line("      run terminated when", lines, 25)
    except EOFError as e:
        print(repr(e))
        sys.exit()

    lines = lines[term_line:]
    write_lines(ofile, lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduces MCNP output file to just last rendvous data")
    parser.add_argument("input", help="path to the mcnp output file")
    parser.add_argument("output", help="path to the reduced output file")
    args = parser.parse_args()

    reduce_ofile(args.input, args.output)
