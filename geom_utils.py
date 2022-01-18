# -*- coding: utf-8 -*-
"""
Geometry utility functions
Part of neutron tools

"""
import numpy as np
import logging


def check_plane_exists(n):
    if np.all(n == 0):
        raise ValueError('At least one plane has all zero coefficients and so does not exist.')


def check_parallel_planes(n1, n2):
    n1_unit = n1 / np.linalg.norm(n1)
    n2_unit = n2 / np.linalg.norm(n2)
    if np.array_equal(n1_unit, n2_unit):
        return True
    else:
        return False


def angle_between_planes(n1, d1, n2, d2):
    """
    Calculate angle between planes cartesian form
    Planes should be inputted in the form n.p = d with n = [a, b, c]
    """
    # Check planes exist and are not identical or parallel
    check_plane_exists(n1)
    check_plane_exists(n2)
    if check_parallel_planes(n1, n2):
        raise ValueError('Planes are either identical or parallel. They do not intersect.')

    numerator = np.sqrt(np.dot(n1, n2)**2)

    denom1 = np.linalg.norm(n1)
    denom2 = np.linalg.norm(n2)

    denom = denom1 * denom2

    cos_theta = numerator / denom
    theta = np.arccos(cos_theta)

    return theta


def dist_between_planes(n1, d1, n2, d2):
    """
    Calculate absolute distance between two planes
    Planes should be inputted in the form n.p = d with n = [a, b, c]
    """

    # Check if planes exist and are parallel. If not parallel return 0 as they will intersect
    check_plane_exists(n1)
    check_plane_exists(n2)
    if not check_parallel_planes(n1, n2):
        logging.debug('Planes are not parallel and thus intersect.')
        return 0.0

    # Ensure planes have form ax + by + cz = d1 and ax + by + cz = d2
    ratio = n1[0] / n2[0]
    n2 *= ratio
    d2 *= ratio

    # Shortest distance FROM PLANE 1 TO PLANE 2 is:
    D = (d2-d1) / np.linalg.norm(n2)

    # Function designed to return signed distance as opposed to magnitude
    # as allows more flexibility in interactions with other functions

    return D


def dist_between_point_plane(n, d, p):
    """
    Calculate minimum distance between a point and a plane
    Planes should be inputted in the form n.p = d with n = [a, b, c]
    Point p should be inputted in the form [x, y, z]
    """

    check_plane_exists(n)

    # Check point does not lie in plane
    if np.dot(n, p) == d:
        return 0.0

    x = 0.0
    y = 0.0
    z = 0.0

    # Creates a point p_0 that lies in the plane
    if n[0] != 0.0:
        x = d / n[0]
    elif n[1] != 0.0:
        y = d / n[1]
    elif n[2] != 0.0:
        z = d / n[2]

    p_0 = np.array([x, y, z])

    check = evaluate_plane_eq(n, d, p_0)
    if check != 0.0:
        logging.debug("Warning check not equal to 0.0 in function dist_between_point_plane.")
        logging.debug(check)

    # Shortest distance FROM POINT TO PLANE is (p_0-p).n_hat
    dist = np.dot(p_0-p, n) / np.linalg.norm(n)

    # Function designed to return signed distance as opposed to magnitude
    # as allows more flexibility in interactions with other functions

    return dist


def line_segment_plane_intersection(p0, p1, n, d):
    """
    Determines the coordinates of the intersection point between a line segment and a plane
    Point on a plane p satisfies n.p = d
    Point on a line s satisfies s = p0 + t*(p1-p0)
    Need to find s = p
    So n.s = n.(p0+t*(p1-p0)) = d
    Rearranging gives t = (d-(n.p0)) / n.(p1-p0)
    """
    check_plane_exists(n)

    # Necessary to avoid division by zero
    if np.dot(p1-p0, n) == 0:
        raise ValueError('Line segment parallel to plane so does not intersect')

    # If val < 0, the two points must lie either side of the plane and so the line
    # segment must intersect the plane
    val = (np.dot(p0, n) - d) * (np.dot(p1, n) - d)

    if val < 0:
        t = d - np.dot(p0, n) / np.dot(p1-p0, n)

        return p0 + t*(p1-p0)

    else:
        raise ValueError('Line segment does not intersect plane')


def plane_sphere_intersect(n, d, p, R):
    """
    Calculate the centre and radius of the circle produced at the intersection of a plane and sphere
    Planes should be inputted in the form n.p = d with n = [a, b, c]
    (x-a)**2 + (y-b)**2 + (z-c)**2 = R**2 is the general equation of a sphere
    p = [u, v, w] is the centre of the sphere
    """

    check_plane_exists(n)
    check_positive(R)

    # First find the distance between the centre of the sphere and the centre of the circle
    # This is the shortest distance between the centre of the sphere and the plane
    centre_dist = dist_between_point_plane(n, d, p)

    # Check to see if the plane and sphere intersect
    if centre_dist > R:
        raise ValueError('Plane and sphere do not intersect')

    # Pythagoras then gives the radius of the circle
    r = np.sqrt(R**2 - centre_dist**2)

    centre_coords = p + (centre_dist*n)/np.linalg.norm(n)

    return r, centre_coords


def plane_plane_intersect(n1, d1, n2, d2, z_ini):
    """
    Planes should be inputted in the form n.p = d with n = [a, b, c]
    Planes intersect at line p + qt, where t is a parameter.
    Use normals to calculate cross product. This is the direction vector of the line, q.
    Determine a point on the line by setting one coordinate to an initial value and
    solving the system of equations
    """

    check_plane_exists(n1)
    check_plane_exists(n2)

    if check_parallel_planes(n1, n2):
        raise ValueError('Planes are either identical or parallel. They do not intersect.')

    # Direction vector of line
    q = np.cross(n1, n2)
    q = q / np.linalg.norm(q)

    # To generate a point on the line, let z=z_ini - more flexible than just setting z=0
    # Necessary to be able to solve fort the x, y coordinates of the point on the line

    a = np.array([[n1[0], n1[1]], [n2[0], n2[1]]])
    b = np.array([d1-(n1[2]*z_ini), d2-(n2[2]*z_ini)])
    x = np.linalg.solve(a, b)

    p = np.array([x[0], x[1], z_ini])

    # Returns the point on the line and the direction of the line of intersection
    return p, q


def dist_bet_points(p1, p2):
    """ calculate distance between two points """

    dist_vec = p2 - p1
    dist = np.linalg.norm(dist_vec)

    return dist


def midpoint_bet_points(p1, p2):
    """ calculate the mid point between 2 points
        returns a tuple of the x, y, z co-ords of the mid point
    """
    p = (p1+p2)/2

    return p


def coefficients_of_line_from_points(p1, p2):
    """
    Computes the m and c coefficients of the equation (y=mx+c) for
    a straight line from two points on a plane.
    p1 and p2 are two co-ordinate points. i.e. p1=(ax, ay)
    """

    points = [p1, p2]
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
        logging.debug('One of the side lengths of the triangle is zero.')
        return 0.0

    hyp = np.sqrt((l1**2)+(l2**2))
    return hyp


def check_positive(x):
    if x < 0:
        raise ValueError('Invalid input. Ensure input is positive.')


def perim_circle(r):
    """ calculate perimeter of circle """
    check_positive(r)
    perim = 2 * np.pi * r
    return perim


def area_circle(r):
    """calculate area of a circle"""
    check_positive(r)
    area = np.pi*r*r
    return area


def area_cyl(r, h):
    """ calculate surface area of closed cylinder """
    check_positive(r)
    check_positive(h)
    end_area = area_circle(r)
    side_area = perim_circle(r) * h
    area = (2 * end_area) + side_area
    return area


def area_cyl_shell(r1, r2):
    """calculate area of cylindrical shell cross section like a pipe"""
    area1 = area_circle(r1)
    area2 = area_circle(r2)
    area = np.abs(area1 - area2)
    return area


def area_sphere(r):
    """calculate surface area of sphere """
    check_positive(r)
    area = 4 * np.pi * r**2
    return area


def area_cone_surf(r, h):
    """calculate surface area of conical surface (not including area of circular base)"""
    check_positive(r)
    check_positive(h)
    t1 = np.sqrt((r*r)+(h*h))
    area = np.pi * r * t1
    return area


def volume_sphere(r):
    """ calculate volume of sphere """
    check_positive(r)
    volume = (4/3) * np.pi * r**3
    return volume


def volume_spherical_shell(r1, r2):
    """ calculate volume of spherical shell"""
    vol1 = volume_sphere(r1)
    vol2 = volume_sphere(r2)
    volume = np.abs(vol1 - vol2)
    return volume


def volume_cyl(r, h):
    """ calculate volume of cylinder """
    check_positive(h)

    area = area_circle(r)
    volume = area * h
    return volume


def volume_cyl_shell(r1, r2, h):
    """ calculate volume of cylindrical shell - pipe"""
    check_positive(h)
    area = area_cyl_shell(r1, r2)
    volume = area * h
    return volume


def volume_cone(r, h):
    """ calculate volume cone """
    volume = volume_cyl(r, h) * (1/3)
    return volume


def evaluate_plane_eq(n, d, p):
    """ calculate plane equation """
    val = np.dot(n, p) - d

    return val


def evaluate_sphere_eq(p, c, r):
    """
    Calc sphere equation
    p is the point being evaluated
    c is the centre point of the sphere surface
    r is the radius of the sphere
    """
    diff = p - c
    val = np.linalg.norm(diff)**2 - r**2

    return val


def evaluate_gq_eq(p, coeffs, k):
    """
    Calculate gq equation
    p = [x, y,z] are the co-ords of the point of interest
    coeffs is a numpy array of coefficients A-J
    """
    val = coeffs[0]*p[0]**2 + coeffs[1]*p[1]**2 + coeffs[2]*p[2]**2 + \
          coeffs[3]*p[0]*p[1] + coeffs[4]*p[1]*p[2] + coeffs[5]*p[0]*p[2] + \
          coeffs[6]*p[0] + coeffs[7]*p[1] + coeffs[8]*p[2] - k
    return val


def find_sense_plane(n, d, p):
    """ determine which side of a plane a point is on i.e the sense """
    check_plane_exists(n)
    val = evaluate_plane_eq(n, d, p)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        logging.debug("on the plane")
        return 0


def find_sense_sphere(p, c, r):
    """ determine if a point is inside or outside the sphere"""
    check_positive(r)
    val = evaluate_sphere_eq(p, c, r)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        logging.debug("on the sphere")
        return 0
    
    
def find_sense_gq(p, coeffs, k):
    """ determine if a point is inside or outside a general quadratic"""
    val = evaluate_gq_eq(p, coeffs, k)
    if val > 0.0:
        return -1
    elif val < 0.0:
        return 1
    elif val == 0.0:
        logging.debug("on the sphere")
        return 0


def project_ray(p0, u, mu):
    """
    Calculate the new co-ordinates
    for moving mu along the unit vector direct
    """
    p1 = p0 + (u*mu)

    return p1


def sphere_ray_intersect(p, u, sphere_centre, sphere_rad):
    """ calculate mu for a ray intersecting a sphere """
    check_positive(sphere_rad)
    dp = p - sphere_centre
    dp2 = np.linalg.norm(dp)**2
    ddot = np.dot(dp, u)
    mu1 = (-1*ddot) + np.sqrt(ddot**2 - dp2 + sphere_rad**2)
    mu2 = (-1*ddot) - np.sqrt(ddot**2 - dp2 + sphere_rad**2)

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

    check_positive(rho)

    x = rho * np.cos(phi)
    y = rho * np.sin(phi)

    return (x, y, z)


def cylindrical_to_spherical(rho, theta_cyl, z):
    """Converts cylindrical polar coordinates to spherical polar coordinates"""

    check_positive(rho)

    r = np.sqrt(rho**2 + z**2)
    theta = np.arccos(z/r)
    phi = theta_cyl

    return (r, theta, phi)


def spherical_to_cartesian(r, theta, phi):
    """Converts spherical polar coordinates to Cartesian coordinates"""

    check_positive(r)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    return (x, y, z)


def spherical_to_cylindrical(r, theta, phi):
    """Converts spherical polar coordinates to cylindrical polar coordinates"""

    check_positive(r)

    rho = r * np.sin(theta)
    theta_cyl = phi
    z = r * np.cos(theta)

    return (rho, theta_cyl, z)
