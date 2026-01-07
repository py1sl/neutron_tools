""" """
import matplotlib
# import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import logging as ntlogger

import neut_utilities as ut
import neut_constants
matplotlib.use('agg')


def normalise(data, norm_val):
    """convert raw data to normalised data"""
    data = np.asarray(data, dtype=float)
    norm_val = float(norm_val)
    norm = data * norm_val
    return norm


def calc_err_abs(results, errors):
    """ calculates absolute errors"""
    # check same length
    if len(results) != len(errors):
        raise ValueError(f"The length of results ({len(results)}) and errors ({len(errors)}) must be the same")

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

        for obj_id, results in d.result.items():
            splot = plt.step(np.asarray(d.eng),  results["result"], label=obj_id)
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_spectra(data, fname, title, sp="proton", err=False,
                 xlow=None, legend=None):
    """ plots spectra from MCNP tally data object, dividing by bin width """
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
                if len(d.ang_bins) > 1:
                    print("not implemented yet - plotting spectra, angle and multiple surfaces")
                    raise NotImplementedError
                for surf, data in d.result.items():
                    y_vals = data["result"]/bw
                    splot = plt.step(np.asarray(d.eng),  y_vals, label=surf)

            else:
                if len(d.ang_bins) > 1:
                    for ang in d.result:
                        y_vals = np.asarray(ang)/bw
                        splot = plt.step(np.asarray(d.eng),  y_vals)
                        legend = d.ang_bins
                else:
                    for surf, data in d.result.items():
                        y_vals = data["result"]/bw
                        splot = plt.step(np.asarray(d.eng),  y_vals, label=surf)
                    plt.legend()

        elif d.tally_type == '2':
            for surf, data in d.result.items():
                y_vals = data["result"]/bw
                splot = plt.step(np.asarray(d.eng),  y_vals, label=surf)
            plt.legend()

        elif d.tally_type == '4':
            for cell, data in d.result.items():
                y_vals = data["result"]/bw
                splot = plt.step(np.asarray(d.eng),  y_vals, label=cell)
            plt.legend()

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
        if non_zero_loc:
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


def plot_ET_heatmap(energy_arr, time_arr, ET_results, fname):
    """ plot an energy time heat map from a tally with energy and time bins """

    # set up to do log ignoring o bins
    ET_results_safe = np.where(ET_results > 0, ET_results, np.nan)
    log_values = np.log10(ET_results_safe)

    # convert shakes to microS
    time_arr = neut_constants.shake_to_ms(time_arr)

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    pcm = plt.pcolormesh(time_arr, energy_arr, log_values[:-1, :-2], shading='auto', cmap='viridis')
    plt.colorbar(pcm, label='log10(flux)')
    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel(r'Time ($\mu$S)')
    plt.ylabel('Energy (MeV)')
    plt.title('Energy Over Time')
    plt.tight_layout()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def time_slice(target_time, energy_arr, time_arr, ET_results, fname):
    """ Extract and plot an energy spectrum at a given time from a
        tally with energy and time bins
    """
    # Find index of closest time
    time_index = np.argmin(np.abs(time_arr - target_time))
    flux_slice = ET_results[:, time_index]

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(energy_arr, flux_slice, marker='o')
    plt.xscale('log')
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Flux ')
    plt.title(f'Flux vs Energy at time = {time_arr[time_index]:.2e}')
    plt.tight_layout()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def energy_slice(target_energy, energy_arr, time_arr, ET_results, fname, min_time=None, max_time=None, wl=True, window=50):
    """ Extract and plot a time distributions for a given energy from a
        tally with energy and time bins
    """
    # Find index of closest energy and get that slice
    erg_index = np.argmin(np.abs(energy_arr - target_energy))
    flux_slice = ET_results[erg_index, :]

    # convert shakes to microS
    time_arr = neut_constants.shake_to_ms(time_arr)

    # focus on the peak
    # if no other instructions given
    peak_index = np.argmax(flux_slice)

    if not min_time:
        min_time = max(0, peak_index - window)
    if not max_time:
        max_time = min(len(flux_slice), peak_index + window)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(time_arr, flux_slice[:-1], marker='o')
    plt.xscale('log')
    plt.xlabel(r'Time ($\mu$S)')
    plt.ylabel('Flux ')

    plt.xlim(min_time, max_time)
    if wl:
        wave_length = np.sqrt(81.81 / (energy_arr[erg_index])/1e9)
        plt.title(f'Flux vs time at wavelength = {round(wave_length)} A')
    else:
        plt.title(f'Flux vs time at energy = {energy_arr[erg_index]:.2e} MeV')
    plt.tight_layout()
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

    hlines.append(f"<title>{mc_object.file_name}</title>")

    hlines.append("<body>")
    hlines.append(f"<H1>{mc_object.file_name}</H1>")
    hlines.append(f"Date run: {mc_object.date}")
    hlines.append(f"Time run: {mc_object.start_time}")
    hlines.append(f"Rendevous: {mc_object.num_rendevous}")
    hlines.append(f"Number of warnings: {len(mc_object.warnings)}")

    # add tally specific data
    for tdat in mc_object.tally_data:
        hlines.append(f"<p><H2> Tally Number: {tdat.number}</H2>")
        hlines.append(f"Particle: {tdat.particle}")

        if tdat.eng:
            hlines.append(f"Number Energy Bins: {len(tdat.eng)}")
        if tdat.times:
            hlines.append(f"Number Time Bins: {len(tdat.times)}")

        if tdat.stat_tests:
            hlines.append("Statistical test results")
            stat_rows = [
                ("Mean behaviour", tdat.stat_tests[0]),
                ("Rel err value", tdat.stat_tests[1]),
                ("rel err behavior", tdat.stat_tests[2]),
                ("rel err rate", tdat.stat_tests[3]),
                ("Variance value", tdat.stat_tests[4]),
                ("Variance behavior", tdat.stat_tests[5]),
                ("Variance rate", tdat.stat_tests[6]),
                ("FOM value constant", tdat.stat_tests[7]),
                ("FOM behavior random", tdat.stat_tests[8]),
                ("PDF slope", tdat.stat_tests[9]),
            ]
            stat_lines = ["<table><tr><th>Test</th><th>Result</th></tr>"]
            for name, val in stat_rows:
                stat_lines.append(f"<tr><td>{name}</td><td>{val}</td></tr>")
            stat_lines.append("</table>")
            hlines.append("\n".join(stat_lines))
        else:
            hlines.append("Warning Statistical test data not found")

        # add tally type specific data
            if tdat.tally_type == "4":
                hlines.append(f"Number Cells: {len(tdat.cells)}")
                cell_string = "".join(tdat.cells)
                hlines.append(f"Cells: {cell_string}")
                hlines.append(f"Volumes: {''.join(tdat.vols)}")
            # add result plots
                if tdat.eng and len(tdat.cells) == 1:
                    pname = f"tally_{tdat.number}_{tdat.cells[0]}.png"
                    title = f"{tdat.particle} Spectra for cell {tdat.cells[0]}"
                    plot_spectra(tdat, pname, title, sp="neutron")

                    hlines.append(f"<img src={pname} alt=\"simulated spectrum\">")
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
    header = "<html><table><tr><th>Tally Number</th><th>CellNumber</th><th>Result</th><th>Relative error</th></tr>"
    rows = []
    for tall in data:
        for i, cell in enumerate(tall.cells):
            row_parts = [
                f"<tr><td>{tall.number}</td>",
                f"<td>{tall.cells[i]}</td>",
                f"<td>{tall.result[i]}</td>",
                f"<td>{tall.err[i]}</td></tr>",
            ]
            rows.append("".join(row_parts))

    strTable = header + "\n" + "\n".join(rows) + "\n</table></html>"

    with open(fname, 'w') as hs:
        hs.write(strTable)
    ntlogger.info("produced html file: %s", fname)


def csv_out(data, fname):
    """ produces  tally data as csv output   """
    if not isinstance(data, list):
        data = [data]

    lines = []
    for tall in data:
        for i, cell in enumerate(tall.cells):
            lines.append(f"{tall.number}, {tall.cells[i]}, {tall.result[i]}, {tall.err[i]}")

    ut.write_lines(fname, lines)
    ntlogger.info("produced csv file: %s", fname)
