import matplotlib
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import neut_utilities as ut
import neut_constants
matplotlib.use('agg')
import logging

def reduce_to_non_zero(variable, time):
     # make sensible graphs for short half lives
    zero_pos = ut.find_first_zero(variable)
    if zero_pos:
        variable = variable[:zero_pos]
        time= time[:zero_pos]
    return variable, time


def plot_act(sum_dat, offset=0, fname=None,
             vlines=None, hlines=None, y_units="Bq/kg", x_units="time_hours"):
    """ plots activity as function of time """
    act = sum_dat["act"]
    

    # correct for sensible x unit requests, otherwise just use x_units
    # if it is not a valid column name that will be picked up by the dataframe
    if x_units == "s" or "seconds":
        x_units = "time_secs"
    elif x_units == "d" or "days":
        x_units = "time_days"
    elif x_units == "h" or "hours" or "hrs":
        x_units = "time_hours"
    

    time_vals = sum_dat[x_units]

    if y_units == "Bq/kg" or "Bq/g":
        act_lab = "Specific Activity " + y_units
    else:
        act_lab = "Activity Bq"

    act, time_vals = reduce_to_non_zero(act, time_vals)

    # make plot
    plt.clf()
    plot = plt.plot(time_vals, act)
    plt.xlabel(x_units)
    plt.ylabel(act_lab)
    plt.yscale("log")

    # set to x axis to log if longer than 10 hours
    if max(time_vals) > 10:
        plt.xscale("log")

    # add any vertical or horizontal lines
    # i.e. highlight specific times or activities
    if vlines:
        for xc in vlines:
            plt.vline(x=xc+offset)
    if hlines:
        for xc in hlines:
            plt.hline(x=xc)

    plt.legend()

    # plot to screen or file
    if fname:
        plt.savefig(fname)
        logging.info("plotted activity")
    else:
        plt.show()
    return plot


def plot_dose(sum_dat, offset=0, fname=None,
              vlines=None, hlines=None, x_units="time_hours"):
    """ plot dose as function of time """

    dose_rate = sum_dat["dose_rate"]
    dose_rate = dose_rate * 1e6

    # correct for sensible x unit requests, otherwise just use x_units
    # if it is not a valid column name that will be picked up by the dataframe
    if x_units == "s" or "seconds":
        x_units = "time_secs"
    elif x_units == "d" or "days":
        x_units = "time_days"
    elif x_units == "h" or "hours" or "hrs":
        x_units = "time_hours"
    

    time_vals = sum_dat[x_units]

    dose_rate, time_vals = reduce_to_non_zero(dose_rate, time_vals)

    # create plot
    plt.clf()
    plot, = plt.plot(time_vals, dose_rate)
    plt.xlabel(x_units)
    plt.ylabel(r"Dose rate $\mu$Sv/h")
    plt.yscale("log")

    # set to x axis to log if longer than 10 hours
    if max(time_vals) > 10:
        plt.xscale("log")

    # add any vertical or horizontal lines
    # i.e. highlight specific times or activities
    if vlines:
        for xc in vlines:
            plt.vline(x=xc+offset)
    if hlines:
        for xc in hlines:
            plt.hline(x=xc)

    plt.legend()

    # plot to screen or file
    if fname:
        plt.savefig(fname)
    elif matplotlib.rcParams['backend'] == "agg":
        print("using agg - no plot - give a file name")
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
    y_upper_lim = max(timestep.gspec) + (max(timestep.gspec)*0.5)
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


def plot_pie(dom_data, title, fname=None, thres=1.0):
    """ """
    dom_data=dom_data[dom_data["act_percent"]>thres]   

    # cmap = plt.cm.prism
    colors = plt.cm.Set1(np.arange(len(dom_data["act_nuc"]))/len(dom_data["act_nuc"]))
    plt.clf()
    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)

    pie_wedge_collection = ax.pie(dom_data["act"], labels=dom_data["act_nuc"],
                                  colors=colors, labeldistance=1.1,
                                  startangle=90)

    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    ax.set_title(title)

    if fname:
        plt.savefig(fname)
    else:
        plt.show()


def plot_nuc_chart(inv_dat, prop="act", fname=None, arange=None, zrange=None):
    """ plots a table of nuclides style plot of the given parameter """
  
    z_min = 0
    z_max = 118
    a_min = 0
    a_max = 294
    
    data = np.zeros((a_max, z_max))
    
    if arange:
        a_min = arange[0]
        a_max = arange[1]
    
    if zrange:
        z_min = zrange[0]
        z_max = zrange[1]
     
    min_val = inv_dat[prop].min()+1e-8
    max_val = inv_dat[prop].max()
      
    zdict = neut_constants.Z_dict()
    inv_dat["Z"] = inv_dat["element"].map(zdict)
    
    for a in np.arange(a_min,a_max):
        for z in np.arange(z_min,z_max):
                 
            df = inv_dat[(inv_dat["A"]==str(a)) & (inv_dat["Z"]==z)]
                    
            if df.empty:
                value = 0.0
            else:
                value = df[prop].item()
       
            data[a][z] = value
    
    fig, ax = plt.subplots(figsize=(14, 8))
    im = plt.imshow(data, cmap='gnuplot', norm=LogNorm(vmin=min_val, vmax=max_val))
    ax.invert_yaxis()
    plt.xlabel("Z", fontsize=16)
    plt.ylabel("A", fontsize=16)
    plt.xlim(z_min, z_max)
    plt.ylim(a_min, a_max)
    plt.title(prop)
    fig.colorbar(im, cax = fig.add_axes([0.91, 0.2, 0.03, 0.6]))

    if fname:
        plt.savefig(fname)
    else:
        plt.show()
    