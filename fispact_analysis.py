import matplotlib.pyplot as plt
import numpy as np


def plot_act(time_hrs, act, offset=0, fname=None, vlines=None, hlines=None):
    """ """
    plt.clf()
    plt.plot(time_hrs, act)
    plt.xlabel("Time (hrs)")
    plt.ylabel("Activity Bq")
    plt.yscale("log")
    plt.xscale("log")
    
    if vlines:
        for xc in vlines:
            plt.vline(x=xc+offset)
            
    if hlines:
        for xc in hlines:
            plt.hline(x=xc)
    
    plt.legend()
    
    if fname:
        plt.savefig(fname)
    else:
        plt.show()

    
def plot_dose(time_hrs, dose_rate, offset=0, fname=None, vlines=None, hlines=None):
    """ """

    plt.clf()
    plt.plot(time_hrs, dose_rate)
    plt.xlabel("Time (hrs)")
    plt.ylabel("Dose rate microSv/h")
    plt.yscale("log")
    plt.xscale("log")
        
    if vlines:
        for xc in vlines:
            plt.vline(x=xc+offset)
            
    if hlines:
        for xc in hlines:
            plt.hline(x=xc)
    
    plt.legend()
    
    if fname:
        plt.savefig(fname)
    else:
        plt.show()  

        
def plot_spectra(timestep, fname=None):
    """ """
    plt.clf() 
    plt.xlabel("Energy (MeV)")
    plt.ylabel("gamma/s")
    plt.yscale("log")
    plt.xscale("log")
    y_upper_lim = max(timestep.gspec) + (max(timestep.gspec)*0.5)
    plt.ylim(ymin = 1e-4, ymax=y_upper_lim)
    
    xbounds = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 
               1.0, 1.22, 1.44, 1.66, 2.0, 2.5, 3.0, 4.0, 5.0, 6.5, 
               8.0, 10.0, 12.0, 14.0, 20.0,)
    
    plt.step(xbounds, timestep.gspec)
    
        
    
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