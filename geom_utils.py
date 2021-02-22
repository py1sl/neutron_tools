# -*- coding: utf-8 -*-
"""
Geometry utility functions
Part of neutron tools

"""
import numpy as np


def angle_between_planes(x1, y1, z1, d1, x2, y2, z2, d2):
    """ calculate angle between planes cartesian form """
    # check planes are not identical or parrellel
    if x1 == x2 and y1 == y2 and z1 == z2:
        return 0.0

    numerator = (x1 * x2) + (y1 * y2) + (z1 * z2)
    numerator = np.sqrt(numerator * numerator)

    denom1 = np.sqrt((x1 * x1) + (y1 * y1) + (z1 * z1))
    denom2 = np.sqrt((x2 * x2) + (y2 * y2) + (z2 * z2))

    denom = denom1 * denom2

    cos_theta = numerator / denom
    theta = np.arccos(cos_theta)

    return theta


def dist_between_planes(x1, y1, z1, d1, x2, y2, z2, d2):
    """ calculate distance between two planes"""

    # check planes are not identical
    if x1 == x2 and y1 == y2 and z1 == z2 and d1 == d2:
        return 0.0

    x = 0.0
    y = 0.0
    z = 0.0
    if y1 != 0.0:
        y = d1 / y1
    elif z1 != 0.0:
        z = d1 / z1
    elif x1 != 0.0:
        x = d1 / x1

    check = evaluate_plane_eq(x, y, z, x1, y1, z1, d1)
    if check != 0.0:
        print("warning check not equal to 0.0")
        print(check)

    top = (x2 * x)+(y2 * y)+(z2 * z) - d2
    bottom = (x2 * x2) + (y2 * y2) + (z2 * z2)
    bottom = np.sqrt(bottom)

    D = top / bottom

    return D


def dist_between_point_plane():
    """ """
    dist = 0
    return dist


def dist_bet_points(x1, y1, z1, x2, y2, z2):
    """ calculate distance between two points """
    if (x1 == x2) and (y1 == y2) and (z1 == z2):
        return 0.0
    else:
        xd = x1 - x2
        yd = y1 - y2
        zd = z1 - z2

        dist = np.sqrt((xd*xd)+(yd*yd)+(zd*zd))
        return dist


def midpoint_bet_points(x1, y1, z1, x2, y2, z2):
    """ calculate the mid point between 2 points
        returns a tuple of the x, y, z co-ords of the mid point
    """
    if (x1 == x2) and (y1 == y2) and (z1 == z2):
        return 0.0
    else:
        x = (x1 + x2)/2.0
        y = (y1 + y2)/2.0
        z = (z1 + z2)/2.0
        return (x, y, z)


def pythag_h(l1, l2):
    """ calculate length of hypotenuse """
    if l1 == 0.0 or l2 == 0.0:
        return 0.0

    hyp = np.sqrt((l1*l1)+(l2*l2))
    return hyp


def perim_circle(r):
    """ calculate perimeter of circle """
    perim = 2 * np.pi * r
    return perim


def area_circle(r):
    """calculate area of a circle"""
    area = np.pi*r*r
    return area


def area_cyl(r, h):
    """ calculate surface area of closed cylinder """
    if r == 0.0 or h == 0.0:
        return 0.0

    end_area = area_circle(r)
    side_area = perim_circle(r) * h
    area = (2 * end_area) + side_area
    return area


def area_cyl_shell(r1, r2):
    """calculate area of cylindrical shell cross section like a pipe"""
    area1 = area_circle(r1)
    area2 = area_circle(r2)
    area = area1 - area2
    return area


def area_sphere(r):
    """calculate surface area of sphere """
    area = 4 * np.pi * r * r
    return area


def area_cone_surf(r, h):
    """calculate surface area of conical surface"""
    if r == 0.0 or h == 0.0:
        return 0.0

    t1 = np.sqrt((r*r)+(h*h))
    area = np.pi * r * t1
    return area


def volume_sphere(r):
    """ calculate volume of sphere """
    volume = (4.0/3.0)*np.pi*r*r*r
    return volume


def volume_spherical_shell(r1, r2):
    """ calculate volume of spherical shell"""
    vol1 = volume_sphere(r1)
    vol2 = volume_sphere(r2)
    volume = vol1 - vol2
    return volume


def volume_cyl(r, h):
    """ calculate volume of cylinder """
    if r == 0.0 or h == 0.0:
        return 0.0

    area = area_circle(r)
    volume = area * h
    return volume


def volume_cyl_shell(r1, r2, h):
    """ calculate volume of cylindrical shell - pipe"""
    area = area_cyl_shell(r1, r2)
    volume = area * h
    return volume


def volume_cone(r, h):
    """ calculate volume cone """
    if r == 0.0 or h == 0.0:
        return 0.0

    volume = volume_cyl(r, h) * (1.0/3.0)
    return volume


def evaluate_plane_eq(x, y, z, coeff_X, coeff_Y, coeff_Z, d):
    """ calculate plane equation """
    val = (coeff_X * x) + (coeff_Y * y) + (coeff_Z * z) - d
    return val


def evaluate_sphere_eq(x1, y1, z1, x2, y2, z2, r):
    """ calc sphere equation
       x1, y1, z1 are the co-ords of the point being evaluated
       x2, y2, z2 are the centre point of the sphere surface
       r is the radius
    """
    x = x1 - x2
    y = y1 - y2
    z = z1 - z2
    val = (x*x) + (y*y) + (z*z) - (r*r)
    return val


def evaluate_gq_eq(x, y, z, coeffs):
    """ calculate gq equation
        x, y, z are the co-ords of the point of interest
        coeff is a dict of co-effieicents A-H
    """
    val = 0
    return val


def find_sense_plane(x, y, z, coeff_X, coeff_Y, coeff_Z, d):
    """ determine which side of a plane a point is on i.e the sense """
    val = evaluate_plane_eq(x, y, z, coeff_X, coeff_Y, coeff_Z, d)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        print("on the plane")
        return 0


def find_sense_sphere(x1, y1, z1, x2, y2, z2, r):
    """ determine if a point is inside or outside the sphere"""
    val = evaluate_sphere_eq(x1, y1, z1, x2, y2, z2, r)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        print("on the sphere")
        return 0


def project_ray(x ,y, z, ux, uy, uz, mu):
    """ calculate the new co-ordinates for moving mu along the unit vector direct """
    x1 = x + (ux*mu)
    y1 = y + (uy*mu)
    z1 = z + (uz*mu)

    return (x1,y1,z1)


def sphere_ray_intesect(x,y,z, ux, uv, uz, spherex, spherey,
                        spherez, sphere_rad):
    """ calculate mu for a ray intersecting a sphere """
    dpx = x - spherex
    dpy = y - spherey
    dpz = z - spherez
    dp2 = (dpx * dpx) + (dpy * dpy) + (dpz * dpz)
    ddot = np.dot([dpx, dpy, dpz], [ux, uy, uz])
    mu1 = -1 * ddot + np.sqrt((ddot*ddot) - (dp2) + (sphere_rad*sphere_rad))
    mu2 = -1 * ddot - np.sqrt((ddot*ddot) - (dp2) + (sphere_rad*sphere_rad))

    return (mu1, mu2)