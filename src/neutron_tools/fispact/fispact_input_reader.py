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


ntlogger = ut.get_ntlogger()

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
    ntlogger.info("reading FISPACT input file %s", fpath)
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"FISPACT input file not found: {fpath}")

    if not os.path.isfile(fpath):
        raise ValueError(f"Path is not a file: {fpath}")

    try:
        ifile = ut.get_lines(fpath)
    except Exception as e:
        raise IOError(f"Failed to read FISPACT input file {fpath}: {e}") from e

    ntlogger.info("loaded %d lines from FISPACT input file %s", len(ifile), fpath)
    return ifile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads Fispact input file")
    parser.add_argument("input", help="path to the fispact input file")
    args = parser.parse_args()

    ut.setup_ntlogger(console_level="INFO")
    read_fispact_input(args.input)
