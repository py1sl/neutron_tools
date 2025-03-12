""" """
import matplotlib
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import logging as ntlogger

import neut_utilities as ut
matplotlib.use('agg')


def normalise(data, norm_val):
    """convert raw data to normalised data"""
    norm = [float(i)*float(norm_val) for i in data]
    return norm


def calc_err_abs(results, errors):
    """ calculates absolute errors"""
    # check same length
    if len(results) != len(errors):
        raise ValueError(f"The length of results and errors must be the same")

    # calculate absolute error for all results
    abs_err = [res*float(err) for res, err in zip(results, errors)]

    return abs_err


def calc_bin_width(bins):
    """ calculate energy bin widths """
    # calculate bin widths and add 1st bin
    if len(bins) < 2:
        raise ValueError("At least two bin edges are required to calculate bin widths.")

    bw = np.diff(bins, prepend=0)
    return bw


def calc_mid_points(bounds):
    """ calculate the mid points of a list"""
    mids = []
    bounds = np.array(bounds).astype(float)
    i = 0
    while i < len(bounds) - 1:
        val = (bounds[i] + bounds[i + 1]) / 2.0
        mids.append(val)
        i = i + 1
    return mids


def plot_raw_spectra(data, fname, title, sp="proton"):
    """ plots spectra from MCNP tally data object per bin no normalisation """
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/" + sp + "/bin")
    plt.xscale('log')
    plt.yscale('log')
    if not isinstance(data, list):
        data = [data]

    for d in data:
        if not hasattr(d, 'eng'):
            raise ValueError("Invalid MCNP tally does not have energy bins.")

        plt.step(np.asarray(d.eng), np.asarray(d.result[0]))
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_spectra(data, fname, title, sp="proton", err=False,
                 xlow=None, legend=None):
    """ plots spectr afrom MCNP tally data object, dividing by bin width """
    if not isinstance(data, list):
        data = [data]

    plt.clf()
    plt.title(" " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/MeV/" + sp)
    plt.xscale('log')
    plt.yscale('log')

    for d in data:
        bw = calc_bin_width(d.eng)
        if d.tally_type == '1':
            plt.ylabel("current n/MeV/" + sp)
            if len(d.surfaces) > 1:
                for surf in d.result:
                    if len(d.ang_bins) > 1:
                        print("not implemented yet - plotting spectra, angle and multiple surfaces")
                        raise NotImplementedError

                    else:
                        y_vals = np.asarray(surf)/bw
                        splot = plt.step(np.asarray(d.eng),  y_vals)
                        legend = d.surfaces
            else:
                if len(d.ang_bins) > 1:
                    for ang in d.result:
                        y_vals = np.asarray(ang)/bw
                        splot = plt.step(np.asarray(d.eng),  y_vals)
                        legend = d.ang_bins
                else:
                    y_vals = np.asarray(d.result)/bw
                    splot = plt.step(np.asarray(d.eng),  y_vals)
        elif d.tally_type == '2':
            
            if len(d.surfaces)>1:
                for surf in d.result:
                    y_vals = np.asarray(surf)/bw
                    splot = plt.step(np.asarray(d.eng),  y_vals)
            else:
                y_vals = np.asarray(d.result)/bw
                splot = plt.step(np.asarray(d.eng),  y_vals)
        elif d.tally_type == '4' and len(d.cells) > 1:

            for cell in d.result:
                y_vals = np.asarray(cell) / bw
                splot = plt.step(np.asarray(d.eng), y_vals)
            legend = d.cells
        elif d.tally_type == '4' and len(d.cells) == 1:
            for cell in d.result:
                y_vals = np.asarray(cell) / bw
                splot = plt.step(np.asarray(d.eng), y_vals)

        else:
            y_vals = np.asarray(d.result) / bw
            splot = plt.step(np.asarray(d.eng), y_vals)

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
    ntlogger.info("produced figure: %s", fname)


def plot_spectra_ratio(data1, data2, fname, title):
    """  plots the ratio of two energy spectra """
    plt.clf()
    plt.title("Comparison of " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("ratio")
    plt.xscale('log')

    ratio = np.asarray(data1.result[0]) / np.asarray(data2.result[0])

    plt.plot(data1.eng, ratio)
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_run_comp(data, err, fname, title, xlab="Run #",
                  ylab="Dose Rate microSv/h"):
    """ plot single value tally results with error """
    plt.clf()

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    x = np.arange(1, len(data) + 1)
    plt.xlim(xmin=0, xmax=len(x) + 1)
    plt.errorbar(x, data, yerr=err, fmt='o')
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_en_time(data, fname):
    """ plotting energy time data"""
    plt.clf()
    if data.times is None:
        ntlogger.info("Error - no time bins")
    if data.eng is None:
        ntlogger.info("Error - no energy bins")
    plt.xlabel("time")
    plt.ylabel("energy")

    masked_vals = np.asarray(data.result)
    masked_vals = masked_vals[:-1, :-1]
    # np.ma.masked_where(data.result[1] < 1e-50, data.result[1])

    """
    plt.pcolormesh(masked_vals.T,
                   norm=colors.LogNorm(vmin=1e-50, vmax=masked_vals.max()),
                   cmap="PuBu_r")
    """
    plt.pcolormesh(data.times, data.eng, masked_vals.T,
                   norm=colors.LogNorm(vmin=1e-50, vmax=masked_vals.max()),
                   cmap="PuBu_r")
    
    plt.colorbar()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def html_output(mc_object, fname):
    """produces html output of file """
    # TODO refactor this to work with a template system

    hlines = []
    hlines.append("<!DOCTYPE html><HTML><HEAD>")
    hlines.append("<meta charset=\"utf-8\">")
    hlines.append("<meta name=\"viewport\" content=\"width=device-width\">")
    hlines.append("</HEAD>")

    hlines.append("<title>" + mc_object.file_name + "</title>")

    hlines.append("<body>")
    hlines.append("<H1>" + mc_object.file_name + "</H1>")
    hlines.append("Date run: " + mc_object.date)
    hlines.append("Time run: " + mc_object.start_time)
    hlines.append("Rendevous: " + str(mc_object.num_rendevous))
    hlines.append("Number of warnings: " + str(len(mc_object.warnings)))

    # add tally specific data
    for tdat in mc_object.tally_data:
        hlines.append("<p><H2> Tally Number: " + str(tdat.number) + "</H2>")
        hlines.append("Particle: " + tdat.particle)

        if tdat.eng:
            hlines.append("Number Energy Bins: " + str(len(tdat.eng)))
        if tdat.times:
            hlines.append("Number Time Bins: " + str(len(tdat.times)))

        if tdat.stat_tests:
            hlines.append("Statistical test results")

            stat_string = "<table><tr><th>Test</th><th>Result</th></tr>"
            stat_string += "<tr><td>" + "Mean behaviour" + \
                "</td> <td>" + tdat.stat_tests[0] + "</td></tr>"
            stat_string += "<tr><td>" + "Rel err value" + \
                "</td> <td>" + tdat.stat_tests[1] + "</td></tr>"
            stat_string += "<tr><td>" + "rel err behavior" + \
                "</td> <td>" + tdat.stat_tests[2] + "</td></tr>"
            stat_string += "<tr><td>" + "rel err rate" + \
                "</td> <td>" + tdat.stat_tests[3] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance value" + \
                "</td> <td>" + tdat.stat_tests[4] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance behavior" + \
                "</td> <td>" + tdat.stat_tests[5] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance rate" + \
                "</td> <td>" + tdat.stat_tests[6] + "</td></tr>"
            stat_string += "<tr><td>" + "FOM value constant" + \
                "</td> <td>" + tdat.stat_tests[7] + "</td></tr>"
            stat_string += "<tr><td>" + "FOM behavior random" + \
                "</td> <td>" + tdat.stat_tests[8] + "</td></tr>"
            stat_string += "<tr><td>" + "PDF slope" + \
                "</td> <td>" + tdat.stat_tests[9] + "</td></tr>"
            stat_string += "</table>"
            hlines.append(stat_string)

        else:
            hlines.append("Warning Statistical test data not found")

        # add tally type specific data
        if tdat.tally_type == "4":
            hlines.append("Number Cells: " + str(len(tdat.cells)))
            cell_string = "".join(tdat.cells)
            hlines.append("Cells: " + cell_string)
            hlines.append("Volumes: " + "".join(tdat.vols))
            # add result plots
            if tdat.eng and len(tdat.cells) == 1:
                pname = "tally_" + str(tdat.number) + \
                    "_" + str(tdat.cells[0]) + ".png"
                title = tdat.particle + \
                    " Spectra for cell " + str(tdat.cells[0])
                plot_spectra(tdat, pname, title, sp="neutron")

                hlines.append(
                    "<img src=" +
                    pname +
                    " alt=\"simulated spectrum\">")
            else:
                print("no energy bins or more than one cell")

        hlines.append("</p>")

    hlines.append("</body>")
    hlines.append("</HTML>")

    # output the file
    ut.write_html(fname, hlines)
    ntlogger.info("produced html file: %s", fname)


def html_f4_tab_out(data, fname):
    """ produces f4 tally data as html table output """
    if not isinstance(data, list):
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

    strTable = strTable + "</table></html>"

    hs = open(fname, 'w')
    hs.write(strTable)
    ntlogger.info("produced html file: %s", fname)


def csv_out(data, fname):
    """ produces  tally data as csv output   """
    if not isinstance(data, list):
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
    ntlogger.info("produced csv file: %s", fname)
