"""
Reads the output file and gets a list of the co-ordinates of the lost particles
"""

import sys
import argparse


def output_lost_points(path, outpath="lost"):
    """ """
    with open(path) as f:
        lines = f.read().splitlines()
    f.close()

    x = []
    y = []
    z = []
    out_list = []
    out_list.append("x y z temp")

    for l in lines:
        if l[0:19] == " x,y,z coordinates:":
            x.append(float(l[28:40]))
            y.append(float(l[43:55]))
            z.append(float(l[58:70]))

    i = 0
    while i < len(x):
        out_list.append(str(x[i])+ " " + str(y[i])+ " " + str(z[i]) + " 1")
        i = i + 1

    ofile = open(outpath+".3d", 'w')
    for l in out_list:
        ofile.write("%s\n" % l)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract location of lost particles from MCNP output  file and output to a .3d file compatible with VisIt")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file")
    args = parser.parse_args()  

    if args.output:
        output_lost_points(args.input, args.output)
    else:
        output_lost_points(args.input)


