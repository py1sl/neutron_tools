# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


def dist_between_planes(x1, y1, z1, d1, x2, y2, z2, d2):
    """ calculate distance between two planes"""

    if y1 != 0.0:
        x = 0.0
        y = d1 / y1
        z = 0.0
    elif z1 != 0.0:
        x = 0.0
        y = 0.0
        z = d1 / z1
    elif x1 != 0.0:
        x = d1 / x1
        y = 0.0
        z = 0.0

    check = evaluate_plane_eq(x, y, z, x1, y1, z1, d1)
    if check != 0.0:
        print("warning check not equal to 0.0")
        print(check)

    top = (x2 * x)+(y2 * y)+(z2 * z) - d2
    bottom = (x2 * x2) + (y2 * y2) + (z2 * z2)
    bottom = np.sqrt(bottom)

    D = top / bottom

    return D


def evaluate_plane_eq(x, y, z, coeff_X, coeff_Y, coeff_Z, d):
    """ """
    val = (coeff_X * x) + (coeff_Y * y) + (coeff_Z * z) - d
    return val


def find_sense_plane(x, y, z, coeff_X, coeff_Y, coeff_Z, d):
    """ """
    val = evaluate_plane_eq(x, y, z, coeff_X, coeff_Y, coeff_Z, d)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        print("on the plane")
