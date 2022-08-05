# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:47:49 2022

@author: Elmos PC
"""
import numpy as np
from time import perf_counter

def calc_mid_points(bounds):
    """ finds the mid points given a set of bounds """
    mids = []
    bounds = np.array(bounds).astype(float)
    i = 0
    while i < len(bounds) - 1:
        val = (bounds[i] + bounds[i+1]) / 2.0
        val = round(val, 5)
        mids.append(val)
        i += 1
        
    return mids

def fast_midpoints(bounds, axis=0):
    bounds = np.array(bounds).astype(float)
    mid = (bounds[1:] + bounds[:-1]) * 0.5
    return mid


st = perf_counter()
a = calc_mid_points([5,8,9])
et = perf_counter()
print(et-st)

e = [-10.00  , -8.00,  -6.00, -4.00, -2.00]
c = ['5','6','0']
#c = np.array(c).astype(float)
start_time = perf_counter()
b = fast_midpoints(c)
time_end = perf_counter()

#d = fast_midpoints([5,8,9])

time = time_end - start_time
print(time)

for i in c:
    da = i
    
