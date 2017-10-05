"""
Reads MCNP output file
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import sys
import argparse


class MCNPOutput():
    """ MCNP output data"""
    def __init__(self):
        """ define data"""
        self.file_name = ""
        self.version = ""
        self.date = ""
        self.start_time = ""
        self.cell_mass_volume = []
        self.surface.area = []
        self.num_tallies = 1
        self.num_rendevous = 1
        self.tally_data = []
        self.summary_data = []
        self.tfc_data = []
        

class MCNP_tally_data():
    """ data for an individual tally """
    def __init__(self):
        self.number = 1
        self.type = 1


class MCNP_summary_data():
    """ data for an individual tally """
    def __init__(self):
        self.number = 1
        self.type = 1


def get_version(data):
    """ """
    return 1


def get_cell_mass(data):
    """ """
    return 1


def get_surface_area(data):
    """ """
    return 1


def get_num_tallies(data):
    """ """
    return 1


def get_num_rendevous(data):
    """ """
    return 1


def get_summary(data, ptype, rnum):
    """ """
    return 1


def get_tally(data, tnum, rnum):
    """ """
    return 1


def read_output_file(path):
    """ """
    return 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()

    read_output_file(args.input)
