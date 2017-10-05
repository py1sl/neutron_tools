"""
Reads MCNP output file
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import sys
import argparse


def get_version(data):
    """ """
    return 1


def get_table_fifty(data):
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
