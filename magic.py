# -*- coding: utf-8 -*-
"""
Magic GVR tool
S Lilley
Sept 2020
"""
import argparse
import neut_utilities as ut
import meshtal_analysis as ma
import numpy as np


def generate_header(output_data):
    return output_data


def generate_mesh_header(mesh, output_data):
    return output_data


def normalise_to_half(mesh):
    """ normalise so highest point is a half """
    result = mesh.data["value"]
    result = result.astype(np.float)
    norm_const = 0.5/max(result)
    norm_data = result * norm_const

    return norm_data


def do_magic(infile, ofile='wwinp'):
    """ generates a weight window file based on magic GVR method """
    ut.setup_ntlogger()

    # read meshtal file
    meshes = ma.read_mesh_tally_file(infile)

    # set up output
    output_data = []
    output_data = generate_header(output_data)

    # generate ww meshes for each meshtal
    for mesh in meshes:
        output_data = generate_mesh_header(mesh, output_data)
        # normed = normalise_mesh(mesh)

    # write output
    ut.write_lines(ofile, output_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform magic GVR")
    parser.add_argument("input", help="path to the mcnp meshtal file")
    parser.add_argument("output", help="path to the output ww file")
    args = parser.parse_args()

    do_magic(args.input, args.output)
