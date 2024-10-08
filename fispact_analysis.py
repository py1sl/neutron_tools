import logging
import matplotlib
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import neut_utilities as ut
import output_utilities as o_ut
import neut_constants
matplotlib.use('agg')


def reduce_to_non_zero(values, time_values):
    """ reduce to only positive no zero values for parameter and time
        this is useful to then make sensible graphs for short half lives
    """
    if len(values) != len(time_values):
        raise ValueError("Lengths of values and time_points must be equal.")

    zero_pos = ut.find_first_zero(values)
    if zero_pos is not None:
        values = values[:zero_pos]
        time_values = time_values[:zero_pos]
    return values, time_values


def is_nuc_present(inv, nuc):
    """ checks if a nuclide is in an inventory"""
    if nuc in inv["nuclide"].unique():
        return True
    else:
        return False


def remove_stable(inv):
    """ removes stable isotopes from inventory listing"""
    inv = inv[inv["act"] > 0.0]
    return inv


def filter_emits_gamma(inv):
    """ remove stable or pure alpha or pure beta emitters  """
    inv = inv[inv["g_energy"] > 0.0]
    return inv


def filter_emits_beta(inv):
    """ remove stable or pure alpha or pure gamma emitters  """
    inv = inv[inv["b_energy"] > 0.0]
    return inv


def filter_emits_alpha(inv):
    """ remove stable or pure beta or pure gamma emitters  """
    inv = inv[inv["a_energy"] > 0.0]
    return inv


def output_mcnp_mat(inv, lib=".70c"):
    """ convert the fispact inventory into an MCNP material
        note: metastables are converted to ground state
    """
    zdict = neut_constants.Z_dict()  # Load Z to element dictionary
    inv["Z"] = inv["element"].map(zdict)  # Map elements to Z
    inv["ZAID"] = inv["Z"] * 1000 + inv["A"]  # Calculate ZAID

    # Normalize atom counts
    inv["atoms_norm"] = inv["atoms"] / inv["atoms"].sum()

    # Select necessary columns
    matdf = inv[["ZAID", "atoms_norm"]].copy()  # Create a copy to avoid SettingWithCopyWarning

    # Format the output string using f-strings and apply
    matdf["output"] = matdf.apply(lambda row: f"     {row['ZAID']}  {row['atoms_norm']:.5e}", axis=1)

    return matdf


def check_time_units(t_units):
    """ convert time units to column heading, allowing sensible input """
    # correct for sensible time unit requests, otherwise just use t_units
    # if it is not a valid column name that will be picked up by the dataframe
    if (t_units.lower() == "s") or (t_units.lower() == "seconds"):
        t_units = "time_secs"
    elif (t_units.lower() == "d") or (t_units.lower() == "days"):
        t_units = "time_days"
    elif (t_units.lower() == "h") or (t_units.lower() == "hours") or (
            t_units.lower() == "hrs"):
        t_units = "time_hours"
    elif (t_units.lower() == "y") or (t_units.lower() == "yrs") or (
            t_units.lower() == "years"):
        t_units = "time_years"

    return t_units


def plot_summary(sum_dat, column="act", offset=0, fname=None,
                 vlines=None, hlines=None, x_units="time_hours", y_units=None):
    """ plots any of the columns from the data frame as a function of time
    (included: activity, dose rate, heat output, ingestion dose, inhalation dose,
    tritium activity)"""

    data = sum_dat[column]
    x_units = check_time_units(x_units)
    time_vals = sum_dat[x_units]
    data, time_vals = reduce_to_non_zero(data, time_vals)

    if column == "dose_rate":
        data = data * 1e6
        y_label = r"Dose rate $\mu$Sv/h"

    elif column == "act":
        if y_units in ["Bq/kg", "Bq/g"]:
            y_label = "Specific Activity " + y_units
        else:
            y_label = "Activity Bq"

    elif column == "heat_output":
        y_label = "Heat output (kW)"

    elif column == "ingestion_dose":
        y_label = "Ingestion dose (Sv)"

    elif column == "inhalation_dose":
        y_label = "Inhalation dose (Sv)"

    elif column == "tritium_activity":
        y_label = "Tritium activity (Bq)"
    else:
        y_label = column

    # make plot
    plt.clf()
    plot = plt.plot(time_vals, data)
    plt.xlabel(x_units)
    plt.ylabel(y_label)
    plt.yscale("log")

    # set to x axis to log if longer than 10 hours
    if max(time_vals) > 10:
        plt.xscale("log")

    # add any vertical or horizontal lines
    # i.e. highlight specific times or activities
    if vlines:
        for xc in vlines:
            plt.vline(x=xc + offset)
    if hlines:
        for xc in hlines:
            plt.hline(x=xc)

    # plot to screen or file
    if fname:
        plt.savefig(fname)
        logging.info("plotted " + column)
    else:
        plt.show()

    return plot


def get_fispact_gamma_bounds():
    """ returns the 24 gamma spectra energy bounds used by fispact """
    bounds = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8,
              1.0, 1.22, 1.44, 1.66, 2.0, 2.5, 3.0, 4.0, 5.0, 6.5,
              8.0, 10.0, 12.0, 14.0, 20.0)
    return bounds


def plot_spectra(timestep, fname=None):
    """ plots the group wise gamma emission spectra """
    plt.clf()
    plt.xlabel("Energy (MeV)")
    plt.ylabel("gamma/s")
    plt.yscale("log")
    plt.xscale("log")
    y_upper_lim = max(timestep.gspec) + (max(timestep.gspec) * 0.5)
    plt.ylim(ymin=1e-4, ymax=y_upper_lim)

    # groups are fixed by fispact
    xbounds = get_fispact_gamma_bounds()

    plt.step(xbounds, timestep.gspec)

    # plot to screen or file
    if fname:
        plt.savefig(fname)
    else:
        plt.show()


def plot_pie(dom_data, title, param="act", fname=None, thres=1.0):
    """ """

    # check valid param
    if param not in dom_data.columns:
        raise ValueError("Plot pie - parameter not recognised")

    dom_data = dom_data[dom_data[param + "_percent"] > thres]
    param_nuc = param + "_nuc"

    # cmap = plt.cm.prism
    colors = plt.cm.Set1(np.arange(len(dom_data[param_nuc])) / len(
                         dom_data[param_nuc]))
    plt.clf()
    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)

    pie_wedge_collection = ax.pie(dom_data[param], labels=dom_data[param_nuc],
                                  colors=colors, labeldistance=1.1,
                                  startangle=90)

    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    ax.set_title(title)

    if fname:
        plt.savefig(fname)
    else:
        plt.show()


def plot_nuc_cont(fout, nuc_list, param="act", fname=None, total=False):
    """  plots all nuclides in nuclist over all times steps"""
    # clear old plots
    plt.clf()

    # get data
    time_vals = fout.sumdat["time_hours"]

    for nuc in nuc_list:
        vals = []

        for ts in fout.timestep_data:
            inv = ts.inventory
            if is_nuc_present(inv, nuc):

                val = inv.loc[inv["nuclide"] == nuc, param].iloc[0]
                vals.append(val)
            else:
                vals.append(0)

        plot = plt.plot(time_vals, vals, label=nuc)

    if total:
        vals = fout.sumdat[param]
        plot = plt.plot(time_vals, vals, label="Total")

    # make plot pretty
    # set to x axis to log if longer than 10 hours
    if max(time_vals) > 10:
        plt.xscale("log")
    plt.xlabel("Time hours")
    plt.ylabel("bq/kg")
    plt.yscale("log")
    plt.legend()

    # plot to screen or file
    if fname:
        plt.savefig(fname)
        logging.info("plotted activity")
    else:
        plt.show()
    return plot


def plot_nuc_chart(inv_dat, prop="act", fname=None, arange=None, zrange=None):
    """ plots a table of nuclides style plot of the given parameter """
    # set up the array
    z_min = 0
    z_max = 118  # max possible Z value element Og
    a_min = 0
    a_max = 294  # max possible A value for Og

    data = np.zeros((a_max, z_max))

    # reduce view to focus on an area
    if arange:
        a_min = arange[0]
        a_max = arange[1]

    if zrange:
        z_min = zrange[0]
        z_max = zrange[1]

    min_val = inv_dat[prop].min() + 1e-8
    max_val = inv_dat[prop].max()

    # map Z values to data frame
    zdict = neut_constants.Z_dict()
    inv_dat["Z"] = inv_dat["element"].map(zdict)

    # map the values to the array positions
    for a in np.arange(a_min, a_max):
        for z in np.arange(z_min, z_max):
            df = inv_dat[(inv_dat["A"] == str(a)) & (inv_dat["Z"] == z)]

            if df.empty:
                value = 0.0
            else:
                value = df[prop].iloc[0]

            data[a][z] = value

    # create the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    im = plt.imshow(data, cmap='gnuplot', norm=LogNorm(vmin=min_val,
                                                       vmax=max_val))
    ax.invert_yaxis()
    plt.xlabel("Z", fontsize=16)
    plt.ylabel("A", fontsize=16)
    plt.xlim(z_min, z_max)
    plt.ylim(a_min, a_max)
    plt.title(prop)
    fig.colorbar(im, cax=fig.add_axes([0.91, 0.2, 0.03, 0.6]))

    if fname:
        plt.savefig(fname)
    else:
        plt.show()


def summary_to_html(fout, fname=None):
    """ converts fispact summary data table to html table"""
    data = fout.sumdat
    sumdata_html = o_ut.dataframe_to_html_table(data)

    if fname:
        o_ut.output_html(sumdata_html, title="Fispact Summary Results", fname=fname)

    return sumdata_html


def gamma_spec_to_html_table(timestep):
    """ converts time step gamma spectrum to HTML table string """
    bounds = get_fispact_gamma_bounds()
    values = timestep.gspec
    data = [bounds, values]
    html_spectra = o_ut.list_to_html_table(data)

    return html_spectra


def inv_to_html(timestep):
    """ convert the nuclide inventory to html """
    html = ""
    return html


def dominant_to_html(timestep):
    """ convert dominant nuclides part of a time step to html """
    html = ""
    return html


def timestep_to_html(timestep):
    """ converts time step to html """

    html = ""
    html += inv_to_html(timestep)
    html += dominant_to_html(timestep)
    html += gamma_spec_to_html(timestep)

    return html


def fispact_output_to_html(fout, fname="fispact_results.html"):
    """ converts a fispact output to an html output
        acts as a quick summary of the output

    """
    html = []

    # loop over time steps
    for ts in fout.timestep_data:
        html.append(timestep_to_html(ts))

    # add summary
    html.append(summary_to_html(fout))

    # write file
    o_ut.output_html(html, title="Fispact Results", fname=fname)


def spectra_to_mcnp_source(timestep, dist_num="1", fname="source_spect.txt"):
    """ converts a fispact gamma spec to a  mcnp source energy distribution"""
    si_line = "SI" + dist_num + " "
    bounds = get_fispact_gamma_bounds()
    for bound in bounds:
        si_line += str(bound) + "\n       "


    sp_line = "SP"  + dist_num + " "
    for value in timestep.gspec:
        sp_line += str(value) + "\n       "


    data = [si_line, sp_line]
    ut.write_lines(fname, data)



