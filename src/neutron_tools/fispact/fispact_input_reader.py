# -*- coding: utf-8 -*-
"""
Fispact input file reader
S Lilley
March 2019
"""
import argparse
import os
from typing import Sequence

from neutron_tools.utilities import neut_utilities as ut


Lines = Sequence[str]


def get_irrad_profile(lines: Lines) -> None:
    """ """
    return None


def get_cool_times(lines: Lines) -> None:
    """ """
    return None


def get_comments(lines: Lines) -> None:
    """ extract comment lines from the file """
    return None


def read_fispact_input(fpath: str) -> Lines:
    """  processes a fispact input file """
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"FISPACT input file not found: {fpath}")

    if not os.path.isfile(fpath):
        raise ValueError(f"Path is not a file: {fpath}")

    try:
        ifile = ut.get_lines(fpath)
    except Exception as e:
        raise IOError(f"Failed to read FISPACT input file {fpath}: {e}") from e

    return ifile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads Fispact input file")
    parser.add_argument("input", help="path to the fispact input file")
    args = parser.parse_args()

    read_fispact_input(args.input)
