import logging
import matplotlib
import os
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import neut_utilities as ut
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
    if not isinstance(inv, pd.DataFrame):
        raise ValueError("inv must be a pandas DataFrame")
    if "nuclide" not in inv.columns:
        raise ValueError("inv DataFrame must contain a 'nuclide' column")
    return nuc in inv["nuclide"].unique()


def remove_stable(inv):
    """ removes stable isotopes from inventory listing"""
    if not isinstance(inv, pd.DataFrame):
        raise ValueError("inv must be a pandas DataFrame")
    if "act" not in inv.columns:
        raise ValueError("inv DataFrame must contain an 'act' column")
    return inv[inv["act"] > 0.0]


def filter_emits_gamma(inv):
    """ remove stable or pure alpha or pure beta emitters  """
    if not isinstance(inv, pd.DataFrame):
        raise ValueError("inv must be a pandas DataFrame")
    if "g_energy" not in inv.columns:
        raise ValueError("inv DataFrame must contain a 'g_energy' column")
    return inv[inv["g_energy"] > 0.0]


def filter_emits_beta(inv):
    """ remove stable or pure alpha or pure gamma emitters  """
    if not isinstance(inv, pd.DataFrame):
        raise ValueError("inv must be a pandas DataFrame")
    if "b_energy" not in inv.columns:
        raise ValueError("inv DataFrame must contain a 'b_energy' column")
    return inv[inv["b_energy"] > 0.0]


def filter_emits_alpha(inv):
    """ remove stable or pure beta or pure gamma emitters  """
    if not isinstance(inv, pd.DataFrame):
        raise ValueError("inv must be a pandas DataFrame")
    if "a_energy" not in inv.columns:
        raise ValueError("inv DataFrame must contain an 'a_energy' column")
    return inv[inv["a_energy"] > 0.0]


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


def read_OOS(oos_path="data/t1.txt"):
    """ read the external data file with a tab seperated list of nuclides and the
        out of scope value for that nuclide
        returns a pandas dataframe with the data
    """
    base = os.path.dirname(__file__)  # path to core.py
    path = os.path.join(base, oos_path)
    OOS_df = pd.read_csv(path, sep='\t')

    return OOS_df


def check_nuclide_oos(nuclide, nuc_act, oos_data, mass=1000):
    """ checks if a nuclide is in the OOS data and compares if the activity is above that value
        returns true if activity is lower than the OOS value
        returns false if above the OOS value
    """
    oos_values = oos_data[oos_data["Nuclide"] == nuclide]["OOS Level"].values
    if oos_values.size > 0:
        oos_value = oos_values[0]

    else:
        oos_values = oos_data[oos_data["Nuclide"] == 'Other']["OOS Level"].values
        oos_value = oos_values[0]

    # now do the comparison
    if nuc_act /mass > oos_value:
        return False
    else:
        return True


def check_inventory_oos(inv, oos_path="data/t1.txt"):
    """ checks all nuclides in an inventory
        returns true if all nuclides are below the OOS value
        returns false if any nuclide is above the OOS value
    """
    oos_data = read_OOS(oos_path)
    inv = remove_stable(inv)

    oos_result = inv.apply(lambda row: check_nuclide_oos(row['nuclide'], row['act'], oos_data), axis=1)

    # Check if any of the result values are False
    if not oos_result.all():

        # Get the index of the first False value - for future output options
        first_false_index = oos_result.idxmin()

        return False
    else:
        return True


def get_not_oos_nuclides(inv, oos_path="data/t1.txt"):
    """ """
    oos_data = read_OOS(oos_path)
    inv = remove_stable(inv)

    inv["oos_result"] = inv.apply(lambda row: check_nuclide_oos(row['nuclide'], row['act'], oos_data), axis=1)
    inv = inv[~inv["oos_result"]]
    return inv


def find_when_oos(ts_data, oos_path="data/t1.txt"):
    """ checks all times steps to find first one which is OOS
        returns the time step number
    """
    for ts in ts_data:

        oos_result = check_inventory_oos(ts.inventory)
        if oos_result:
            return ts.step_num


def cooling_ts_data(fout):
    """ """
    ts_data = fout.timestep_data[fout.cooling_step_index:]
    return ts_data


def plot_summary(sum_dat, column="act", offset=0, fname=None,
                 vlines=None, hlines=None, x_units="time_hours", y_units=None, cooling=False):
    """ plots any of the columns from the data frame as a function of time
    (included: activity, dose rate, heat output, ingestion dose, inhalation dose,
    tritium activity)"""

    if not isinstance(sum_dat, pd.DataFrame):
        raise ValueError("sum_dat must be a pandas DataFrame")
    if column not in sum_dat.columns:
        raise ValueError(f"column '{column}' not found in sum_dat DataFrame")

    if cooling:
        sum_dat = sum_dat[sum_dat["is_cooling"]]

    data = sum_dat[column]
    x_units = check_time_units(x_units)

    if x_units not in sum_dat.columns:
        raise ValueError(f"time units '{x_units}' not found in sum_dat DataFrame")

    time_vals = sum_dat[x_units]
    data, time_vals = reduce_to_non_zero(data, time_vals)

    if column == "dose_rate":
        data = data * 1e6
        y_label = r"Dose rate $\mu$Sv/h"

    elif column == "act":
        if y_units in ["Bq/kg", "Bq/g"]:
            y_label = f"Specific Activity {y_units}"
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

    # set to x axis to log if longer than 10 time val units
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
        logging.info(f"plotted {column}")
    else:
        plt.show()

    return plot


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
    xbounds = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8,
               1.0, 1.22, 1.44, 1.66, 2.0, 2.5, 3.0, 4.0, 5.0, 6.5,
               8.0, 10.0, 12.0, 14.0, 20.0)

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
    if not hasattr(fout, 'timestep_data') or not hasattr(fout, 'sumdat'):
        raise ValueError("fout must be a FispactOutput object with timestep_data and sumdat attributes")
    if not isinstance(nuc_list, (list, tuple)) or len(nuc_list) == 0:
        raise ValueError("nuc_list must be a non-empty list or tuple of nuclide names")

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
    if not isinstance(inv_dat, pd.DataFrame):
        raise ValueError("inv_dat must be a pandas DataFrame")
    if prop not in inv_dat.columns:
        raise ValueError(f"Property '{prop}' not found in inv_dat DataFrame")
    if "element" not in inv_dat.columns or "A" not in inv_dat.columns:
        raise ValueError("inv_dat DataFrame must contain 'element' and 'A' columns")

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

    # map Z values to data frame and convert A to integer in single operation
    zdict = neut_constants.Z_dict()
    inv_dat = inv_dat.copy()
    inv_dat["Z"] = inv_dat["element"].map(zdict)
    inv_dat["A_int"] = pd.to_numeric(inv_dat["A"], errors='coerce').fillna(0).astype(int)

    # Vectorized approach: filter and group data
    mask = (
        (inv_dat["A_int"] >= a_min) & (inv_dat["A_int"] < a_max)
        & (inv_dat["Z"] >= z_min) & (inv_dat["Z"] < z_max)
    )
    filtered_data = inv_dat[mask]

    # Populate data array - indices already validated by mask
    for _, row in filtered_data.iterrows():
        a_idx = int(row["A_int"])
        z_idx = int(row["Z"])
        data[a_idx][z_idx] = row[prop]

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
