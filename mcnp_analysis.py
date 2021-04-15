""" """
import matplotlib
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import logging

import neut_utilities as ut
matplotlib.use('agg')


def normalise(data, norm_val):
    """convert raw data to normalised data"""
    norm = []
    for i in data:
        norm.append(float(i) * float(norm_val))
    return norm


def calc_err_abs(res, err):
    """ calculates absolute errors"""
    i = 0
    abs_err = []
    while i < len(res):
        abs_err.append(res[i]*float(err[i]))
        i = i + 1
    return abs_err


def calc_bin_width(bins):
    """ calculate energy bin widths """
    bw = []
    # 1st bin is its own width
    bw.append(bins[0])
    i = 1
    while i < len(bins):
        width = float(bins[i]) - float(bins[i-1])
        bw.append(width)
        i = i + 1
    bw = np.asarray(bw)
    return bw


def calc_mid_points(bounds):
    """ calculate the mid points of a list"""
    mids = []
    bounds = np.array(bounds).astype(float)
    i = 0
    while i < len(bounds) - 1:
        val = (bounds[i] + bounds[i+1]) / 2.0
        mids.append(val)
        i = i + 1
    return mids


def plot_raw_spectra(data, fname, title, sp="proton"):
    """ plots spectra from MCNP tally data object per bin no normalisation """
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/"+sp+"/bin")
    plt.xscale('log')
    plt.yscale('log')
    if type(data) is not list:
        data = [data]

    for d in data:
        plt.step(np.asarray(d.eng), np.asarray(d.result))
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_spectra(data, fname, title, sp="proton", err=False,
                 xlow=None, legend=None):
    """ plots spectr afrom MCNP tally data object, dividing by bin width """
    if type(data) is not list:
        data = [data]

    plt.clf()
    plt.title(" " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/MeV/" + sp)
    plt.xscale('log')
    plt.yscale('log')

    for d in data:
        bw = calc_bin_width(d.eng)
        if d.type == '2':
            y_vals = np.asarray(d.result[0])/bw
        else:
            y_vals = np.asarray(d.result)/bw

        splot = plt.step(np.asarray(d.eng),  y_vals)
        if err is True:
            abs_err = calc_err_abs(y_vals, d.err)
            mids = calc_mid_points(d.eng)
            ecol = splot[0].get_color()
            plt.errorbar(mids, y_vals[1:], yerr=abs_err[:-1], fmt="none",
                         ecolor=ecol, markeredgewidth=1, capsize=2)

    if xlow is None:
        non_zero_loc = ut.find_first_non_zero(y_vals)
        plt.xlim(xmin=d.eng[non_zero_loc])
    else:
        plt.xlim(xmin=xlow)

    if legend is not None:
        plt.legend(legend)

    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_spectra_ratio(data1, data2, fname, title):
    """  plots the ratio of two energy spectra """
    plt.clf()
    plt.title("Comparison of " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("ratio")
    plt.xscale('log')
    if data1.type == '2':
        ratio = np.asarray(data1.result[0])/np.asarray(data2.result[0])
    else:
        ratio = np.asarray(data1.result)/np.asarray(data2.result)

    plt.plot(data1.eng, ratio)
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_run_comp(data, err, fname, title, xlab="Run #",
                  ylab="Dose Rate microSv/h"):
    """ plot single value tally results with error """
    plt.clf()

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    x = np.arange(1, len(data) + 1)
    plt.xlim(xmin=0, xmax=len(x)+1)
    plt.errorbar(x, data, yerr=err, fmt='o')
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_en_time(data, fname):
    """ plotting energy time data"""
    plt.clf()
    if data.times is None:
        logging.info("Error - no time bins")
    if data.eng is None:
        logging.info("Error - no energy bins")
    plt.xlabel("time")
    plt.ylabel("energy")

    masked_vals = np.asarray(data.result)
    masked_vals = masked_vals[:-1, :-1]
    # np.ma.masked_where(data.result[1] < 1e-50, data.result[1])

    plt.pcolormesh(masked_vals.T,
                   norm=colors.LogNorm(vmin=1e-50, vmax=masked_vals.max()),
                   cmap="PuBu_r")
    """
    plt.pcolormesh(data.times[:-3], data.eng, masked_vals.T,
                   norm=colors.LogNorm(vmin=1e-50, vmax=masked_vals.max()),
                   cmap="PuBu_r")
    """
    plt.colorbar()
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def html_tab_out(data, fname):
    """ produces f4 tally data as html table output """
    if type(data) is not list:
        data = [data]

    strTable = "<html><table><tr><th>Tally Number</th><th>CellNumber"
    strTable = strTable + "</th><th>Result</th><th>Relative error</th></tr>"
    for tall in data:
        for i, cell in enumerate(tall.cells):
            strTable = strTable + "<tr><td>" + str(tall.number) + "</td>"
            strTable = strTable + "<td>" + str(tall.cells[i]) + "</td>"
            strTable = strTable + "<td>" + str(tall.result[i]) + "</td>"
            strTable = strTable + "<td>" + str(tall.err[i]) + "</td>"
            strTable = strTable + "</tr>"

    strTable = strTable+"</table></html>"

    hs = open(fname, 'w')
    hs.write(strTable)
    logging.info("produced html file: %s", fname)


def csv_out(data, fname):
    """ produces  tally data as csv output   """
    if type(data) is not list:
        data = [data]

    lines = []
    for tall in data:
        for i, cell in enumerate(tall.cells):
            ltext = str(tall.number) + ", "
            ltext = ltext + str(tall.cells[i]) + ", "
            ltext = ltext + str(tall.result[i]) + ", "
            ltext = ltext + str(tall.err[i])
            lines.append(ltext)

    ut.write_lines(fname, lines)
    logging.info("produced csv file: %s", fname)
