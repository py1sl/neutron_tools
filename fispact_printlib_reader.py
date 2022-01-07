# -*- coding: utf-8 -*-
"""
Fispact printlib file reader
S Lilley
october 2021
"""
import argparse
import neut_utilities as ut
import pandas as pd


def energy_filter(data, energy):
    """ filter emission lines based on energy """
    data = data[data["energy_ev"] > energy]
    return data


def particle_filter(data, particle):
    """ filter emission lines based on emission particle """
    data = data[data["particle"] == particle]
    return data


def read_fispact_printlib(fpath):
    """  processes a fispact printlib file """
    averages = []
    nucs = []
    particle = []
    energy = []
    intensity = []
    in_discrete = False
    in_average = False

    with open(fpath, 'r') as plf:
        for line in plf:
            if "fispact run time" in line:
                discrete_lines_df = pd.DataFrame()
                discrete_lines_df["nuclide"] = nucs
                discrete_lines_df["particle"] = particle
                discrete_lines_df["energy_ev"] = energy
                discrete_lines_df["intensity"] = intensity
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

    return discrete_lines_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads Fispact printlib file")
    parser.add_argument("input", help="path to the fispact printlib file")
    args = parser.parse_args()

    read_fispact_printlib(args.input)
