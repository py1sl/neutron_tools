# -*- coding: utf-8 -*-
"""
Geometry utility functions
Part of neutron tools

"""
import numpy as np
import logging


def evaluate_plane_eq(x, y, z, coeff_X, coeff_Y, coeff_Z, d):
    """ calculate plane equation """
    val = (coeff_X * x) + (coeff_Y * y) + (coeff_Z * z) - d
    return val


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

    # Check if planes are parallel; if not then return 0 as they will intersect
    if x1/x2 != y1/y2 != z1/z2:
        return 0.0

    # Check planes are not identical
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
        raise ValueError('Plane equation does not evaluate, check input.')

    top = (x2 * x)+(y2 * y)+(z2 * z) - d2
    bottom = (x2 * x2) + (y2 * y2) + (z2 * z2)
    bottom = np.sqrt(bottom)

    D = top / bottom

    return D


def dist_between_point_plane(x1, y1, z1, d, x2, y2, z2):
    """Calculate minimum distance between a point and a plane
       x1*x + y1*y + z1*z = d defines the plane; (x, y, z) is the point q lying in the plane
       (x2, y2, z2) is the point p
    """

    # Check point does not lie in plane
    if (x1*x2)+(y1*y2)+(z1*z2) == d:
        return 0.0

    x = 0.0
    y = 0.0
    z = 0.0

    # Creates a point p that lies in the plane
    if y1 != 0.0:
        y = d / y1
    elif z1 != 0.0:
        z = d / z1
    elif x1 != 0.0:
        x = d / x1

    check = evaluate_plane_eq(x, y, z, x1, y1, z1, d)
    if check != 0.0:
        logging.debug("warning check not equal to 0.0")
        logging.debug(check)

    xd = x - x2
    yd = y - y2
    zd = z - z2

    # Let q be the point (x2, y2, z2). Shortest distance FROM POINT TO PLANE is (q-p).n_hat
    dist = ((xd*x1)+(yd*y1)+(zd*z1))/np.sqrt(x1**2+y1**2+z1**2)

    # Function designed to return signed distance as opposed to magnitude
    # as allows more flexibility in interactions with other functions

    return dist


def line_segment_plane_intersection(p0, p1, x, y, z, d):
    """
    Determines the coordinates of the intersection point between a line segment and a plane
    Point on a plane p satisfies n.p = d
    Point on a line s satisfies s = p0 + t*(p1-p0)
    Need to find s = p
    So n.s = n.(p0+t*(p1-p0)) = d
    Rearranging gives t = (d-(n.p0)) / n.(p1-p0)
    """
    plane = np.array([x, y, z, d])

    # If val < 0, the two points must lie either side of the plane and so the line
    # segment must intersect the plane
    val = (np.dot(p0, plane[:3])-d)*(np.dot(p1, plane[:3])-d)

    if val < 0:
        if np.dot(p1-p0, plane[:3]) == 0:
            return None  # Since line segment parallel to plane
        t = plane[3] - np.dot(p0, plane[:3]) / np.dot(p1-p0, plane[:3])

        return p0 + t*(p1-p0)

    else:
        raise ValueError('Line segment does not intersect plane')


def plane_sphere_intersect(x1, y1, z1, d, a, b, c, R):
    """Calculate the centre and radius of the circle produced at the intersection of a plane and sphere
       x1*x + y1*y + z1*z = d defines the plane
       (x-a)**2 + (y-b)**2 + (z-c)**2 = R**2 is the general equation of a sphere
    """

    if R <= 0:
        raise ValueError('Sphere does not exist')

    # First find the distance between the centre of the sphere and the centre of the circle
    # This is the shortest distance between the centre of the sphere and the plane
    centre_dist = dist_between_point_plane(x1, y1, z1, d, a, b, c)

    # Check to see if the plane and sphere intersect
    if centre_dist > R:
        raise ValueError('Plane and sphere do not intersect')

    # Pythagoras then gives the radius of the circle
    r = np.sqrt(R**2 - centre_dist**2)

    centre_x = a + (centre_dist*x1)/np.sqrt(x1**2+y1**2+z1**2)
    centre_y = b + (centre_dist*y1)/np.sqrt(x1**2+y1**2+z1**2)
    centre_z = c + (centre_dist*z1)/np.sqrt(x1**2+y1**2+z1**2)

    centre = np.array([centre_x, centre_y, centre_z])

    return r, centre


def plane_plane_intersect(x1, y1, z1, d1, x2, y2, z2, d2, z_ini):
    """
    Take equation of plane as x1*x + y1*y + z1*z = d1
    Planes intersect at line p + qt, where t is a parameter.
    Use normals to calculate cross product. This is the direction vector of the line, q.
    Determine a point on the line by setting one coordinate to zero and solving the system of equations
    """

    if x1/x2 == y1/y2 == z1/z2:
        raise ValueError('Planes are parallel and thus do not intersect.')

    n1 = np.array([x1, y1, z1])
    n2 = np.array([x2, y2, z2])

    # Direction vector of line
    n = np.cross(n1, n2)
    n = n / np.sqrt(n[0]**2 + n[1]**2 + n[2]**2)

    # To generate a point on the line, let z=z_ini - more flexible than just setting z=0

    a = np.array([[x1, y1], [x2, y2]])
    b = np.array([d1-(z1*z_ini), d2-(z2*z_ini)])
    x = np.linalg.solve(a, b)

    p = np.array([x[0], x[1], z_ini])

    # Returns parameterised equation of the line of intersection, where t is a parameter
    return p, n


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


def coefficients_of_line_from_points(point_a, point_b):
    """Computes the m and c coefficients of the equation (y=mx+c) for
    a straight line from two points on a plane.
    point_a and point_b are two co-ordinate points. i.e. point_a=(ax, ay)
    """

    points = [point_a, point_b]
    x_coords, y_coords = zip(*points)
    coord_array = np.vstack([x_coords, np.ones(len(x_coords))]).T
    m, c = np.linalg.lstsq(coord_array, y_coords, rcond=None)[0]
    return m, c


def rotate_x(point_list, o, theta):
    """
    Rotates a point p anticlockwise about the x axis by an angle theta around a given origin o
    Theta should be given in radians and o and p should be given in the form of numpy arrays
    Returns array of rotated points
    """

    R = np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])

    new_point_list = np.zeros(shape=(len(point_list), 3))

    for i, point in enumerate(point_list):
        new_point_list[i] = np.dot(R, (point.T - o.T))

    return new_point_list


def rotate_y(point_list, o, theta):
    """
    Rotates a point p anticlockwise about the y axis by an angle theta around a given origin o
    Theta should be given in radians and o and p should be given in the form of numpy arrays
    Returns array of rotated points
    """

    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])

    new_point_list = np.zeros(shape=(len(point_list), 3))

    for i, point in enumerate(point_list):
        new_point_list[i] = np.dot(R, (point.T - o.T))

    return new_point_list


def rotate_z(point_list, o, theta):
    """
    Rotates a point p anticlockwise about the z axis by an angle theta around a given origin o
    Theta should be given in radians and o and p should be given in the form of numpy arrays
    Returns array of rotated points
    """

    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])

    new_point_list = np.zeros(shape=(len(point_list), 3))

    for i, point in enumerate(point_list):
        new_point_list[i] = np.dot(R, (point.T - o.T))

    return new_point_list


def translate(point_list, translation):
    """
    Translates a point p by a translation vector
    Points and translation vector should be given in the form of numpy arrays
    """

    new_point_list = np.zeros(shape=(len(point_list), 3))

    for i, point in enumerate(point_list):
        new_point_list[i] = point + translation

    return new_point_list


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
        logging.debug("on the plane")
        return 0


def find_sense_sphere(x1, y1, z1, x2, y2, z2, r):
    """ determine if a point is inside or outside the sphere"""
    val = evaluate_sphere_eq(x1, y1, z1, x2, y2, z2, r)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        logging.debug("on the sphere")
        return 0


def project_ray(x, y, z, ux, uy, uz, mu):
    """ calculate the new co-ordinates
         for moving mu along the unit vector direct
    """
    x1 = x + (ux*mu)
    y1 = y + (uy*mu)
    z1 = z + (uz*mu)

    return (x1, y1, z1)


def sphere_ray_intesect(x, y, z, ux, uy, uz, spherex, spherey,
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


def cartesian_to_cylindrical(x, y, z):
    """Converts Cartesian coordinates to cylindrical polar coordinates"""

    rho = np.sqrt(x**2 + y**2)
    if x >= 0:
        phi = np.arctan(y/x)
    else:
        phi = np.arctan(y/x) + np.pi

    return (rho, phi, z)


def cartesian_to_spherical(x, y, z):
    """Converts Cartesian coordinates to spherical polar coordinates"""

    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)
    if x >= 0:
        phi = np.arctan(y/x)
    else:
        phi = np.arctan(y/x) + np.pi

    return (r, theta, phi)


def cylindrical_to_cartesian(rho, phi, z):
    """Converts cylindrical polar coordinates to Cartesian coordinates"""

    if rho < 0:
        raise ValueError('Invalid input')

    x = rho * np.cos(phi)
    y = rho * np.sin(phi)

    return (x, y, z)


def spherical_to_cartesian(r, theta, phi):
    """Converts spherical polar coordinates to Cartesian coordinates"""

    if r < 0:
        raise ValueError('Invalid input')

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    return (x, y, z)


def spherical_to_cylindrical(r, theta, phi):
    """Converts spherical polar coordinates to cylindrical polar coordinates"""

    if r < 0:
        raise ValueError('Invalid input')

    rho = r * np.sin(theta)
    theta_cyl = phi
    z = r * np.cos(theta)

    return (rho, theta_cyl, z)


def cylindrical_to_spherical(rho, theta_cyl, z):
    """Converts cylindrical polar coordinates to spherical polar coordinates"""

    if rho < 0:
        raise ValueError('Invalid input')

    r = np.sqrt(rho**2 + z**2)
    theta = np.arccos(z/r)
    phi = theta_cyl

    return (r, theta, phi)

