import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import neut_utilities as ut


def plot_act(time_hrs, act, offset=0, fname=None, vlines=None, hlines=None, y_units="Bq/kg"):
    """ plots activity as function of time """
    # check and convert data
    act = np.asarray(act)
    act = act.astype('float')
    
    if y_units == "Bq/kg" or "Bq/g":
        act_lab = "Specific Activity " + y_units
    else:
        act_lab = "Activity Bq"
    
    # make sensible graphs for short half lives
    zero_pos = ut.find_first_zero(act)
    if zero_pos:
       act = act[:zero_pos]
       time_hrs = time_hrs[:zero_pos]
    
    # make plot
    plt.clf()
    plt.plot(time_hrs, act)
    plt.xlabel("Time (hrs)")
    plt.ylabel(act_lab)
    plt.yscale("log")
    
    # set to x axis to log if longer than 10 hours
    if max(time_hrs) > 10:
        plt.xscale("log")
    
    # add any vertical or horizontal lines i.e. highlight specific times or activities
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
    else:
        plt.show()

    
def plot_dose(time_hrs, dose_rate, offset=0, fname=None, vlines=None, hlines=None):
    """ plot dose as function of time """
    
    # check and convert data
    dose_rate = np.asarray(dose_rate)
    dose_rate = dose_rate.astype('float')
    dose_rate = dose_rate * 1e6
    # make sensible graphs for short half lives
    zero_pos = ut.find_first_zero(dose_rate)
    if zero_pos:
       dose_rate = dose_rate[:zero_pos]
       time_hrs = time_hrs[:zero_pos]
    
    # create plot
    plt.clf()
    plt.plot(time_hrs, dose_rate)
    plt.xlabel("Time (hrs)")
    plt.ylabel("Dose rate $\mu$Sv/h")
    plt.yscale("log")
    
    # set to x axis to log if longer than 10 hours
    if max(time_hrs) > 10:
        plt.xscale("log")
    
    # add any vertical or horizontal lines i.e. highlight specific times or activities    
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
    else:
        plt.show()  

        
def plot_spectra(timestep, fname=None):
    """ plots the group wise gamma emission spectra """
    plt.clf() 
    plt.xlabel("Energy (MeV)")
    plt.ylabel("gamma/s")
    plt.yscale("log")
    plt.xscale("log")
    y_upper_lim = max(timestep.gspec) + (max(timestep.gspec)*0.5)
    plt.ylim(ymin = 1e-4, ymax=y_upper_lim)
    
    # groups are fixed by fispact
    xbounds = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 
               1.0, 1.22, 1.44, 1.66, 2.0, 2.5, 3.0, 4.0, 5.0, 6.5, 
               8.0, 10.0, 12.0, 14.0, 20.0,)
    
    plt.step(xbounds, timestep.gspec)
    
    # plot to screen or file
    if fname:
        plt.savefig(fname)
    else:
        plt.show()  
    
    
def plot_pie(time_step, quantity, fname):
    """ """
    plt.clf()
    
    
    
    if fname:
        plt.savefig(fname)
    else:
        plt.show()  