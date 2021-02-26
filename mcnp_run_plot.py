"""
Reads to output dumped to screen and plots rendevous frequency etc
works on the output to std out from MCNP6
does not work on the MCNP output file
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import argparse

import neut_utilities as ut


def plot_nps_stats(path):
    """ reads std out file of mcnp run and produces graphs vs nps
        these are useful for identifing any long history issues
        process - read file, extract data, plot graphs
    """
    lines = ut.get_lines(path)

    ctm = []    # computer time
    nrn = []    # number random numbers
    nps = []    # number source particles
    coll = []   # number of collisions
    time = []   # wall clock time

    for line in lines:
        if "ctm" in line:
            ctm.append(float(line[6:18]))
            nrn.append(int(line[26:44]))
        if "dump" in line:
            coll.append(int(line[61:78]))
        if "master set rendezvous" in line:
            nps.append(int(line[28:40]))
            t1 = datetime.datetime.strptime(line[66:83], '%m/%d/%y %H:%M:%S')
            time.append(t1)

    time = matplotlib.dates.date2num(time)
    fmt = matplotlib.dates.DateFormatter('%d/%m  %H:%M')

    fig = plt.figure()
    ax = fig.add_subplot(221)
    ax.xaxis.set_major_formatter(fmt)
    ax.set_xlabel("time")
    ax.set_ylabel("nps")
    ax.plot(time, nps)

    ax1 = fig.add_subplot(222)
    ax1.set_xlabel("nps")
    ax1.set_ylabel("ctm")
    ax1.plot(nps, ctm[1:])

    ax2 = fig.add_subplot(223)
    ax2.set_xlabel("nps")
    ax2.set_ylabel("nrn")
    ax2.plot(nps, nrn[1:])

    ax3 = fig.add_subplot(224)
    ax3.set_xlabel("nps")
    ax3.set_ylabel("coll")
    ax3.plot(nps, coll[1:])

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    desc = "data about run time and rendevous frequency"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("input", help="path to the input file")
    args = parser.parse_args()

    plot_nps_stats(args.input)
