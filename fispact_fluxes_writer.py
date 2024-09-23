# -*- coding: utf-8 -*-
"""
Created on Tue Jan 2020
Functions for writing fispact fluxes files
@author: S Lilley
"""
import argparse
import numpy as np
import logging as ntlogger
import neut_utilities as ut


def get_group_pos(groups, energy):
    """ finds the energy bin number for a given energy
        input is the group energy boundaries and the energy
        output is the position in the list of the bin in whihc that energy sits
    """
    energy = float(energy)
    i = 0
    n = len(groups)

    # check for energy above the highest group
    if energy > groups[0]:
        return 0
    # check for energy below the lowest energy
    if energy <= groups[-1]:
        return n - 2

    # find bin for energies in the group structure range
    while i < n - 1:
        if energy <= groups[i] and energy > groups[i+1]:
            return i
        i += 1

    # just in case it does not fit in the above categories
    return -1


def get_group_struct(gs):
    """ returns a named group structure bin boundaries """

    gs_162 = (1.0000E+9, 9.6000E+8, 9.2000E+8, 8.8000E+8, 8.4000E+8, 8.0000E+8,
              7.6000E+8, 7.2000E+8, 6.8000E+8, 6.4000E+8, 6.0000E+8, 5.6000E+8,
              5.2000E+8, 4.8000E+8, 4.4000E+8, 4.0000E+8, 3.6000E+8, 3.2000E+8,
              2.8000E+8, 2.4000E+8, 2.0000E+8, 1.8000E+8, 1.6000E+8, 1.4000E+8,
              1.2000E+8, 1.0000E+8, 9.0000E+7, 8.0000E+7, 7.0000E+7, 6.0000E+7,
              5.5000E+7, 5.4000E+7, 5.0000E+7, 4.5000E+7, 4.0000E+7, 3.5000E+7,
              3.0000E+7, 2.8000E+7, 2.6000E+7, 2.4000E+7, 2.2000E+7, 2.0000E+7,
              1.9000E+7, 1.8000E+7, 1.7000E+7, 1.6000E+7, 1.5000E+7, 1.4000E+7,
              1.3000E+7, 1.2000E+7, 1.1000E+7, 1.0000E+7, 9.8000E+6, 9.6000E+6,
              9.4000E+6, 9.2000E+6, 9.0000E+6, 8.8000E+6, 8.6000E+6, 8.4000E+6,
              8.2000E+6, 8.0000E+6, 7.8000E+6, 7.6000E+6, 7.4000E+6, 7.2000E+6,
              7.0000E+6, 6.8000E+6, 6.6000E+6, 6.4000E+6, 6.2000E+6, 6.0000E+6,
              5.8000E+6, 5.6000E+6, 5.4000E+6, 5.2000E+6, 5.0000E+6, 4.8000E+6,
              4.6000E+6, 4.4000E+6, 4.2000E+6, 4.0000E+6, 3.8750E+6, 3.7500E+6,
              3.6250E+6, 3.5000E+6, 3.3750E+6, 3.2500E+6, 3.1250E+6, 3.0000E+6,
              2.8750E+6, 2.7500E+6, 2.6250E+6, 2.5000E+6, 2.3750E+6, 2.2500E+6,
              2.1250E+6, 2.0000E+6, 1.8750E+6, 1.7500E+6, 1.6250E+6, 1.5000E+6,
              1.3750E+6, 1.2500E+6, 1.1250E+6, 1.0000E+6, 9.7500E+5, 9.5000E+5,
              9.2500E+5, 9.0000E+5, 8.7500E+5, 8.5000E+5, 8.2500E+5, 8.0000E+5,
              7.7500E+5, 7.5000E+5, 7.2500E+5, 7.0000E+5, 6.7500E+5, 6.5000E+5,
              6.2500E+5, 6.0000E+5, 5.7500E+5, 5.5000E+5, 5.2500E+5, 5.0000E+5,
              4.7500E+5, 4.5000E+5, 4.2500E+5, 4.0000E+5, 3.7500E+5, 3.5000E+5,
              3.2500E+5, 3.0000E+5, 2.8000E+5, 2.6000E+5, 2.4000E+5, 2.2000E+5,
              2.0000E+5, 1.8000E+5, 1.6000E+5, 1.4000E+5, 1.2000E+5, 1.0000E+5,
              9.5000E+4, 9.0000E+4, 8.5000E+4, 8.0000E+4, 7.5000E+4, 7.0000E+4,
              6.5000E+4, 6.0000E+4, 5.5000E+4, 5.0000E+4, 4.5000E+4, 4.0000E+4,
              3.5000E+4, 3.0000E+4, 2.5000E+4, 2.0000E+4, 1.5000E+4, 1.0000E+4)

    gs_709 = (1.00E+03, 9.60E+02, 9.20E+02, 8.80E+02, 8.40E+02, 8.00E+02,
              7.60E+02, 7.20E+02, 6.80E+02, 6.40E+02, 6.00E+02, 5.60E+02,
              5.20E+02, 4.80E+02, 4.40E+02, 4.00E+02, 3.60E+02, 3.20E+02,
              2.80E+02, 2.40E+02, 2.00E+02, 1.80E+02, 1.60E+02, 1.50E+02,
              1.40E+02, 1.30E+02, 1.20E+02, 1.10E+02, 1.00E+02, 9.00E+01,
              8.00E+01, 7.50E+01, 7.00E+01, 6.50E+01, 6.00E+01, 5.80E+01,
              5.60E+01, 5.40E+01, 5.20E+01, 5.00E+01, 4.80E+01, 4.60E+01,
              4.40E+01, 4.20E+01, 4.00E+01, 3.80E+01, 3.60E+01, 3.40E+01,
              3.20E+01, 3.00E+01, 2.90E+01, 2.80E+01, 2.70E+01, 2.60E+01,
              2.50E+01, 2.40E+01, 2.30E+01, 2.20E+01, 2.10E+01, 2.00E+01,
              1.98E+01, 1.96E+01, 1.94E+01, 1.92E+01, 1.90E+01, 1.88E+01,
              1.86E+01, 1.84E+01, 1.82E+01, 1.80E+01, 1.78E+01, 1.76E+01,
              1.74E+01, 1.72E+01, 1.70E+01, 1.68E+01, 1.66E+01, 1.64E+01,
              1.62E+01, 1.60E+01, 1.58E+01, 1.56E+01, 1.54E+01, 1.52E+01,
              1.50E+01, 1.48E+01, 1.46E+01, 1.44E+01, 1.42E+01, 1.40E+01,
              1.38E+01, 1.36E+01, 1.34E+01, 1.32E+01, 1.30E+01, 1.28E+01,
              1.26E+01, 1.24E+01, 1.22E+01, 1.20E+01, 1.18E+01, 1.16E+01,
              1.14E+01, 1.12E+01, 1.10E+01, 1.08E+01, 1.06E+01, 1.04E+01,
              1.02E+01, 1.00E+01, 9.55E+00, 9.12E+00, 8.71E+00, 8.32E+00,
              7.94E+00, 7.59E+00, 7.24E+00, 6.92E+00, 6.61E+00, 6.31E+00,
              6.03E+00, 5.75E+00, 5.50E+00, 5.25E+00, 5.01E+00, 4.79E+00,
              4.57E+00, 4.37E+00, 4.17E+00, 3.98E+00, 3.80E+00, 3.63E+00,
              3.47E+00, 3.31E+00, 3.16E+00, 3.02E+00, 2.88E+00, 2.75E+00,
              2.63E+00, 2.51E+00, 2.40E+00, 2.29E+00, 2.19E+00, 2.09E+00,
              2.00E+00, 1.91E+00, 1.82E+00, 1.74E+00, 1.66E+00, 1.58E+00,
              1.51E+00, 1.45E+00, 1.38E+00, 1.32E+00, 1.26E+00, 1.20E+00,
              1.15E+00, 1.10E+00, 1.05E+00, 1.00E+00, 9.55E-01, 9.12E-01,
              8.71E-01, 8.32E-01, 7.94E-01, 7.59E-01, 7.24E-01, 6.92E-01,
              6.61E-01, 6.31E-01, 6.03E-01, 5.75E-01, 5.50E-01, 5.25E-01,
              5.01E-01, 4.79E-01, 4.57E-01, 4.37E-01, 4.17E-01, 3.98E-01,
              3.80E-01, 3.63E-01, 3.47E-01, 3.31E-01, 3.16E-01, 3.02E-01,
              2.88E-01, 2.75E-01, 2.63E-01, 2.51E-01, 2.40E-01, 2.29E-01,
              2.19E-01, 2.09E-01, 2.00E-01, 1.91E-01, 1.82E-01, 1.74E-01,
              1.66E-01, 1.58E-01, 1.51E-01, 1.45E-01, 1.38E-01, 1.32E-01,
              1.26E-01, 1.20E-01, 1.15E-01, 1.10E-01, 1.05E-01, 1.00E-01,
              9.55E-02, 9.12E-02, 8.71E-02, 8.32E-02, 7.94E-02, 7.59E-02,
              7.24E-02, 6.92E-02, 6.61E-02, 6.31E-02, 6.03E-02, 5.75E-02,
              5.50E-02, 5.25E-02, 5.01E-02, 4.79E-02, 4.57E-02, 4.37E-02,
              4.17E-02, 3.98E-02, 3.80E-02, 3.63E-02, 3.47E-02, 3.31E-02,
              3.16E-02, 3.02E-02, 2.88E-02, 2.75E-02, 2.63E-02, 2.51E-02,
              2.40E-02, 2.29E-02, 2.19E-02, 2.09E-02, 2.00E-02, 1.91E-02,
              1.82E-02, 1.74E-02, 1.66E-02, 1.58E-02, 1.51E-02, 1.45E-02,
              1.38E-02, 1.32E-02, 1.26E-02, 1.20E-02, 1.15E-02, 1.10E-02,
              1.05E-02, 1.00E-02, 9.55E-03, 9.12E-03, 8.71E-03, 8.32E-03,
              7.94E-03, 7.59E-03, 7.24E-03, 6.92E-03, 6.61E-03, 6.31E-03,
              6.03E-03, 5.75E-03, 5.50E-03, 5.25E-03, 5.01E-03, 4.79E-03,
              4.57E-03, 4.37E-03, 4.17E-03, 3.98E-03, 3.80E-03, 3.63E-03,
              3.47E-03, 3.31E-03, 3.16E-03, 3.02E-03, 2.88E-03, 2.75E-03,
              2.63E-03, 2.51E-03, 2.40E-03, 2.29E-03, 2.19E-03, 2.09E-03,
              2.00E-03, 1.91E-03, 1.82E-03, 1.74E-03, 1.66E-03, 1.58E-03,
              1.51E-03, 1.45E-03, 1.38E-03, 1.32E-03, 1.26E-03, 1.20E-03,
              1.15E-03, 1.10E-03, 1.05E-03, 1.00E-03, 9.55E-04, 9.12E-04,
              8.71E-04, 8.32E-04, 7.94E-04, 7.59E-04, 7.24E-04, 6.92E-04,
              6.61E-04, 6.31E-04, 6.03E-04, 5.75E-04, 5.50E-04, 5.25E-04,
              5.01E-04, 4.79E-04, 4.57E-04, 4.37E-04, 4.17E-04, 3.98E-04,
              3.80E-04, 3.63E-04, 3.47E-04, 3.31E-04, 3.16E-04, 3.02E-04,
              2.88E-04, 2.75E-04, 2.63E-04, 2.51E-04, 2.40E-04, 2.29E-04,
              2.19E-04, 2.09E-04, 2.00E-04, 1.91E-04, 1.82E-04, 1.74E-04,
              1.66E-04, 1.58E-04, 1.51E-04, 1.45E-04, 1.38E-04, 1.32E-04,
              1.26E-04, 1.20E-04, 1.15E-04, 1.10E-04, 1.05E-04, 1.00E-04,
              9.55E-05, 9.12E-05, 8.71E-05, 8.32E-05, 7.94E-05, 7.59E-05,
              7.24E-05, 6.92E-05, 6.61E-05, 6.31E-05, 6.03E-05, 5.75E-05,
              5.50E-05, 5.25E-05, 5.01E-05, 4.79E-05, 4.57E-05, 4.37E-05,
              4.17E-05, 3.98E-05, 3.80E-05, 3.63E-05, 3.47E-05, 3.31E-05,
              3.16E-05, 3.02E-05, 2.88E-05, 2.75E-05, 2.63E-05, 2.51E-05,
              2.40E-05, 2.29E-05, 2.19E-05, 2.09E-05, 2.00E-05, 1.91E-05,
              1.82E-05, 1.74E-05, 1.66E-05, 1.58E-05, 1.51E-05, 1.45E-05,
              1.38E-05, 1.32E-05, 1.26E-05, 1.20E-05, 1.15E-05, 1.10E-05,
              1.05E-05, 1.00E-05, 9.55E-06, 9.12E-06, 8.71E-06, 8.32E-06,
              7.94E-06, 7.59E-06, 7.24E-06, 6.92E-06, 6.61E-06, 6.31E-06,
              6.03E-06, 5.75E-06, 5.50E-06, 5.25E-06, 5.01E-06, 4.79E-06,
              4.57E-06, 4.37E-06, 4.17E-06, 3.98E-06, 3.80E-06, 3.63E-06,
              3.47E-06, 3.31E-06, 3.16E-06, 3.02E-06, 2.88E-06, 2.75E-06,
              2.63E-06, 2.51E-06, 2.40E-06, 2.29E-06, 2.19E-06, 2.09E-06,
              2.00E-06, 1.91E-06, 1.82E-06, 1.74E-06, 1.66E-06, 1.58E-06,
              1.51E-06, 1.45E-06, 1.38E-06, 1.32E-06, 1.26E-06, 1.20E-06,
              1.15E-06, 1.10E-06, 1.05E-06, 1.00E-06, 9.55E-07, 9.12E-07,
              8.71E-07, 8.32E-07, 7.94E-07, 7.59E-07, 7.24E-07, 6.92E-07,
              6.61E-07, 6.31E-07, 6.03E-07, 5.75E-07, 5.50E-07, 5.25E-07,
              5.01E-07, 4.79E-07, 4.57E-07, 4.37E-07, 4.17E-07, 3.98E-07,
              3.80E-07, 3.63E-07, 3.47E-07, 3.31E-07, 3.16E-07, 3.02E-07,
              2.88E-07, 2.75E-07, 2.63E-07, 2.51E-07, 2.40E-07, 2.29E-07,
              2.19E-07, 2.09E-07, 2.00E-07, 1.91E-07, 1.82E-07, 1.74E-07,
              1.66E-07, 1.58E-07, 1.51E-07, 1.45E-07, 1.38E-07, 1.32E-07,
              1.26E-07, 1.20E-07, 1.15E-07, 1.10E-07, 1.05E-07, 1.00E-07,
              9.55E-08, 9.12E-08, 8.71E-08, 8.32E-08, 7.94E-08, 7.59E-08,
              7.24E-08, 6.92E-08, 6.61E-08, 6.31E-08, 6.03E-08, 5.75E-08,
              5.50E-08, 5.25E-08, 5.01E-08, 4.79E-08, 4.57E-08, 4.37E-08,
              4.17E-08, 3.98E-08, 3.80E-08, 3.63E-08, 3.47E-08, 3.31E-08,
              3.16E-08, 3.02E-08, 2.88E-08, 2.75E-08, 2.63E-08, 2.51E-08,
              2.40E-08, 2.29E-08, 2.19E-08, 2.09E-08, 2.00E-08, 1.91E-08,
              1.82E-08, 1.74E-08, 1.66E-08, 1.58E-08, 1.51E-08, 1.45E-08,
              1.38E-08, 1.32E-08, 1.26E-08, 1.20E-08, 1.15E-08, 1.10E-08,
              1.05E-08, 1.00E-08, 9.55E-09, 9.12E-09, 8.71E-09, 8.32E-09,
              7.94E-09, 7.59E-09, 7.24E-09, 6.92E-09, 6.61E-09, 6.31E-09,
              6.03E-09, 5.75E-09, 5.50E-09, 5.25E-09, 5.01E-09, 4.79E-09,
              4.57E-09, 4.37E-09, 4.17E-09, 3.98E-09, 3.80E-09, 3.63E-09,
              3.47E-09, 3.31E-09, 3.16E-09, 3.02E-09, 2.88E-09, 2.75E-09,
              2.63E-09, 2.51E-09, 2.40E-09, 2.29E-09, 2.19E-09, 2.09E-09,
              2.00E-09, 1.91E-09, 1.82E-09, 1.74E-09, 1.66E-09, 1.58E-09,
              1.51E-09, 1.45E-09, 1.38E-09, 1.32E-09, 1.26E-09, 1.20E-09,
              1.15E-09, 1.10E-09, 1.05E-09, 1.00E-09, 9.55E-10, 9.12E-10,
              8.71E-10, 8.32E-10, 7.94E-10, 7.59E-10, 7.24E-10, 6.92E-10,
              6.61E-10, 6.31E-10, 6.03E-10, 5.75E-10, 5.50E-10, 5.25E-10,
              5.01E-10, 4.79E-10, 4.57E-10, 4.37E-10, 4.17E-10, 3.98E-10,
              3.80E-10, 3.63E-10, 3.47E-10, 3.31E-10, 3.16E-10, 3.02E-10,
              2.88E-10, 2.75E-10, 2.63E-10, 2.51E-10, 2.40E-10, 2.29E-10,
              2.19E-10, 2.09E-10, 2.00E-10, 1.91E-10, 1.82E-10, 1.74E-10,
              1.66E-10, 1.58E-10, 1.51E-10, 1.45E-10, 1.38E-10, 1.32E-10,
              1.26E-10, 1.20E-10, 1.15E-10, 1.10E-10, 1.05E-10, 1.00E-10,
              9.55E-11, 9.12E-11, 8.71E-11, 8.32E-11, 7.94E-11, 7.59E-11,
              7.24E-11, 6.92E-11, 6.61E-11, 6.31E-11, 6.03E-11, 5.75E-11,
              5.50E-11, 5.25E-11, 5.01E-11, 4.79E-11, 4.57E-11, 4.37E-11,
              4.17E-11, 3.98E-11, 3.80E-11, 3.63E-11, 3.47E-11, 3.31E-11,
              3.16E-11, 3.02E-11, 2.88E-11, 2.75E-11, 2.63E-11, 2.51E-11,
              2.40E-11, 2.29E-11, 2.19E-11, 2.09E-11, 2.00E-11, 1.91E-11,
              1.82E-11, 1.74E-11, 1.66E-11, 1.58E-11, 1.51E-11, 1.45E-11,
              1.38E-11, 1.32E-11, 1.26E-11, 1.20E-11, 1.15E-11, 1.10E-11,
              1.05E-11)

    if gs == "709":
        return gs_709
    elif gs == "162":
        return gs_162
    else:
        ntlogger.debug("Error group structure not found")
        return False


def create_fluxes_data(groups, epos):
    """ produces a list representing a fluxes file
        with a single 1 in the correct energy bin
        all other bins are set to zero
        a power line is also added to ensure it is the correct size
    """

    # Check if epos is within bounds
    if not 0 <= epos < len(groups):
        raise ValueError(f" The energy bin position ({epos}) is out of bounds for the given groups array.")

    flux_data = np.zeros(len(groups) + 1)
    flux_data[epos] = 1
    flux_data[-1] = 1  # deals with 'power line'

    return flux_data


def convert_mcnp_spect_to_fispact_fluxes_format(mcnp_spect):
    """ takes a list asumed to be ordered low to high energy
        inverts to fispact fluxes format high to low energy
        adds a power line
    """
    mcnp_spect = np.asarray(mcnp_spect)

    # Check if the input is sorted in ascending order
    if not np.all(mcnp_spect[:-1] <= mcnp_spect[1:]):
        raise ValueError("MCNP spectrum is not sorted in ascending order (low to high energy).")

    # reverse to be high to low energy
    fispact_spect = mcnp_spect[::-1]
    # add power line
    fispact_spect = np.append(fispact_spect, 1.0)

    return fispact_spect


def check_upper_bound(groups, energy):
    """ checks energy is not beyond the upper energy of the group structure """
    if energy > groups[0]:
        ntlogger.debug("Energy above max group structure energy")
        return False
    else:
        return True


def write_fluxes_file(opath, data):
    """ writes the data to a file """
    data = data.astype(str)
    data = data.tolist()
    ut.write_lines(opath, data)


def check_group_struct(gs):
    """ checks if the requested group structure is a valid fispact group structure
    """
    structures = ("709", "162")
    if gs not in structures:
        ntlogger.debug(f"{gs} group structure is not recognised.")
        return False
    ntlogger.debug(f"{gs} group structure recognised.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="write a new fispact spectra")
    parser.add_argument("-o", "--output", action="store", dest="output",
                        default="fluxes", help="path to the output file")
    parser.add_argument("-g", "--group", action="store", dest="group_struct",
                        help="group structure to use",
                        choices=["709", "162"])
    parser.add_argument("-e", "--energy", action="store", dest="energy",
                        help="the energy in MeV to return a spectra for")

    args = parser.parse_args()
    check_group_struct(args.group_struct)
    gs = get_group_struct(args.group_struct)
    epos = get_group_pos(gs, args.energy)
    fdata = create_fluxes_data(gs, epos)
    write_fluxes_file(args.output, fdata)
