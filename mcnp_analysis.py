""" """
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import logging

import neut_utilities as ut


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


def plot_raw_spectra(data, fname, title):
    """ plots spectra from MCNP tally data object per bin no normalisation """
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/proton/bin")
    plt.xscale('log')
    plt.yscale('log')
    plt.step(data.eng, data.result)
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_spectra(data, fname, title, sp="proton"):
    """ plots spectr afrom MCNP tally data object, dividing by bin width """
    if type(data) is not list: data = [data]

    plt.clf()
    plt.title(" " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/MeV/" + sp)
    plt.xscale('log')
    plt.yscale('log')

    for d in data:
        #if isinstance(d, pd.Series):
            #bw = calc_bin_width(d.index.values)
            #plt.step(d.index.values, np.asarray(d)/bw)
        #else:
        bw = calc_bin_width(d.eng)
        plt.step(d.eng, np.asarray(d.result)/bw)
    
    plt.savefig(fname)
    logging.info("produced figure: %s", fname)


def plot_spectra_ratio(data1, data2, fname, title):
    """  plots the ratio of two energy spectra """
    plt.clf()
    plt.title("Comparison of " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("ratio")
    plt.xscale('log')
    plt.plot(data1.eng, np.asarray(data1.result)/np.asarray(data2.result))
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
    if data.times == None:
        logging.info("Error - no time bins")
    if data.eng == None:
        logging.info("Error - no energy bins")
    plt.xlabel("time")
    plt.ylabel("energy")
    
    
    masked_vals = np.ma.masked_where(data.result[1] < 1e-50, data.result[1])
    
    plt.pcolormesh(masked_vals.T, norm=colors.LogNorm(vmin=1e-50, vmax=masked_vals.max()), cmap="PuBu_r")
    plt.colorbar()
    logging.info(data.result[1].shape)
    logging.info(len(data.user_bins))
    plt.savefig(fname)

def html_tab_out(data, fname):
    """ produces f4 tally data as html table output """
    if type(data) is not list: data = [data]

    strTable = "<html><table><tr><th>Tally Number</th><th>Cell Number</th><th>Result</th><th>Relative error</th></tr>"
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
    if type(data) is not list: data = [data]

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



