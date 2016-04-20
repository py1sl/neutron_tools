"""
Reads to output file and gets a list of the co-ordinates of the lost particles
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import sys


def output_lost_points(path):
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

    ofile = open(path+".3d", 'w')
    for l in out_list:
        ofile.write("%s\n" % l)


if __name__ == "__main__":
    output_lost_points(sys.argv[1])
