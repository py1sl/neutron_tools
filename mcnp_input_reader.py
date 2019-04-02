# -*- coding: utf-8 -*-
"""
MCNP input file reader
S Lilley
March 2019
"""
import sys
import argparse
import neut_utilities as ut

class mcnp_cell():
    """ """
    def __init__(self):
        self.number = ""
        self.mat = ""
        self.density = 0.0
        self.imp_p = 1.0
        self.imp_n = 1.0
        self.geom = ""
        self.surfaces = []
        
        
def get_full_line_comments(lines):
    """ """
    comments = []
    for l in lines:
        if len(l) > 1 and l[0].lower() == "c" and l[1] == " ":
            comments.append(l)
    return comments
    
    
def get_material_numbers(lines):
    """ """
    mat_nums = []
    for l in lines:
        if len(l) > 1 and l[0].lower() == "m" and l[1].isdigit():
             l = ut.string_cleaner(l)
             l = l.split(" ")[0]
             mnum = l[1:] 
             mat_nums.append(int(mnum))
    return mat_nums
   
   
def get_tally_numbers(lines):
    """ """
    tal_nums = []
    for l in lines:
        if len(l) > 1 and l[0].lower() == "f" and l[1].isdigit():
             l = ut.string_cleaner(l)
             l = l.split(" ")[0]
             l = l.split(":")[0]
             tnum = l[1:] 
             tal_nums.append(int(tnum))
    return tal_nums

    
def read_mcnp_input(fpath):
    """ """

    ifile = ut.get_lines(fpath)
    
    comments = get_full_line_comments(ifile) 
    mat_nums = get_material_numbers(ifile)
 
    return ifile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads MCNP input file")
    parser.add_argument("input", help="path to the mcnp input file")
    args = parser.parse_args()

    read_mcnp_input(args.input)