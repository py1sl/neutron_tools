# -*- coding: utf-8 -*-
"""
Fispact printlib file reader
S Lilley
october 2021
"""
import argparse
import os

import pandas as pd

from neutron_tools.utilities import neut_utilities as ut


def energy_filter(data: pd.DataFrame, energy: float) -> pd.DataFrame:
    """ filter emission lines based on energy """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a pandas DataFrame")
    if "energy_ev" not in data.columns:
        raise ValueError("data DataFrame must contain an 'energy_ev' column")
    return data[data["energy_ev"] > energy]


def particle_filter(data: pd.DataFrame, particle: str) -> pd.DataFrame:
    """ filter emission lines based on emission particle """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a pandas DataFrame")
    if "particle" not in data.columns:
        raise ValueError("data DataFrame must contain a 'particle' column")
    return data[data["particle"] == particle]


def read_fispact_printlib(fpath: str) -> pd.DataFrame:
    """  processes a fispact printlib file """
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"FISPACT printlib file not found: {fpath}")

    if not os.path.isfile(fpath):
        raise ValueError(f"Path is not a file: {fpath}")

    averages = []
    nucs = []
    particle = []
    energy = []
    intensity = []
    in_discrete = False
    in_average = False

    try:
        with open(fpath, "r") as plf:
            for line in plf:
                if "fispact run time" in line:
                    discrete_lines_df = pd.DataFrame(
                        {
                            "nuclide": nucs,
                            "particle": particle,
                            "energy_ev": energy,
                            "intensity": intensity,
                        }
                    )
                    break
                elif in_discrete:
                    if ("Type" not in line) and ("no spectral data" not in line):
                        if line[2] != " ":
                            cur_nuc = line[2:8]
                            cur_nuc = cur_nuc.replace(" ", "")
                        nucs.append(cur_nuc)
                        part = line[25:34]
                        part = ut.string_cleaner(part)
                        particle.append(part)
                        energy.append(float(line[43:54]))
                        intensity.append(float(line[71:82]))

                elif " FD " in line:
                    in_average = False
                    in_discrete = True
                elif in_average:
                    averages.append(line)

                elif "A V E R A G E S" in line:
                    in_average = True
    except Exception as e:
        raise IOError(f"Failed to read FISPACT printlib file {fpath}: {e}") from e

    return discrete_lines_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads Fispact printlib file")
    parser.add_argument("input", help="path to the fispact printlib file")
    args = parser.parse_args()

    read_fispact_printlib(args.input)
