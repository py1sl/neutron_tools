import unittest
import geom_utils
import numpy as np


class geom_evaluate_test_case(unittest.TestCase):
    """ Tests evaluate functions """

    def test_check_evaluate_plane_eq(self):
        self.assertEqual(geom_utils.evaluate_plane_eq(np.array([1.0, 1.0, 1.0]),
                                                      3.0, np.array([1.0, 1.0, 1.0])), 0.0)
        self.assertEqual(geom_utils.evaluate_plane_eq(np.array([1.0, 1.0, 1.0]),
                                                      2.0, np.array([1.0, 1.0, 1.0])), 1.0)
        self.assertEqual(geom_utils.evaluate_plane_eq(np.array([1.0, 1.0, 1.0]),
                                                      4.0, np.array([1.0, 1.0, 1.0])), -1.0)

    def test_check_evaluate_sphere_eq(self):
        self.assertEqual(geom_utils.evaluate_sphere_eq(np.array([1.0, 0.0, 0.0]),
                                                       np.array([0.0, 0.0, 0.0]), 1.0), 0.0)
        self.assertEqual(geom_utils.evaluate_sphere_eq(np.array([2.0, 0.0, 0.0]),
                                                       np.array([0.0, 0.0, 0.0]), 1.0), 3.0)
        self.assertEqual(geom_utils.evaluate_sphere_eq(np.array([0.5, 0.0, 0.0]),
                                                       np.array([0.0, 0.0, 0.0]), 1.0), -0.75)

    def test_check_evaluate_gq_eq(self):
        self.assertEqual(geom_utils.evaluate_gq_eq(np.array([0.0, 0.0, 0.0]),
                         np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]), 0.0), 0.0)
        self.assertEqual(geom_utils.evaluate_gq_eq(np.array([1.0, 1.0, 1.0]),
                         np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 8.0), 1.0)
        self.assertEqual(geom_utils.evaluate_gq_eq(np.array([1.0, 1.0, 1.0]),
                         np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 10.0), -1.0)


class geom_positive_quantity_test_case(unittest.TestCase):
    """ Tests check positive function"""

    def test_check_positive(self):
        self.assertRaises(ValueError, geom_utils.check_positive, -1.0)


class geom_perim_test_case(unittest.TestCase):
    """ tests for perimeter functions"""

    def test_perim_circle(self):
        self.assertEqual(geom_utils.perim_circle(0.0), 0.0)
        self.assertEqual(geom_utils.perim_circle(1.0), 2*np.pi)
        self.assertRaises(ValueError, geom_utils.perim_circle, -1.0)


class geom_area_test_case(unittest.TestCase):
    """ tests for area functions"""

    def test_area_circle(self):
        self.assertEqual(geom_utils.area_circle(0.0), 0.0)
        self.assertEqual(geom_utils.area_circle(1.0), np.pi)
        self.assertRaises(ValueError, geom_utils.area_circle, -1.0)

    def test_area_cyl(self):
        self.assertEqual(geom_utils.area_cyl(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cyl(1.0, 1.0), 4*np.pi)
        self.assertRaises(ValueError, geom_utils.area_cyl, -1.0, 0.0)
        self.assertRaises(ValueError, geom_utils.area_cyl, 0.0, -1.0)

    def test_area_cyl_shell(self):
        self.assertEqual(geom_utils.area_cyl_shell(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cyl_shell(1.0, 1.0), 0.0)
        self.assertEqual(geom_utils.area_cyl_shell(1.0, 2.0), 3*np.pi)
        self.assertEqual(geom_utils.area_cyl_shell(2.0, 1.0), 3*np.pi)
        self.assertRaises(ValueError, geom_utils.area_cyl_shell, -1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.area_cyl_shell, 1.0, -1.0)

    def test_area_sphere(self):
        self.assertEqual(geom_utils.area_sphere(0.0), 0.0)
        self.assertEqual(geom_utils.area_sphere(1.0), 4*np.pi)
        self.assertRaises(ValueError, geom_utils.area_sphere, -1.0)

    def test_area_cone_surf(self):
        self.assertEqual(geom_utils.area_cone_surf(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cone_surf(3.0, 4.0), 15*np.pi)
        self.assertRaises(ValueError, geom_utils.area_cone_surf, -1.0, 0.0)
        self.assertRaises(ValueError, geom_utils.area_cone_surf, 0.0, -1.0)


class geom_volume_test_case(unittest.TestCase):
    """ tests for volume functions"""

    def test_vol_sphere(self):
        self.assertEqual(geom_utils.volume_sphere(0.0), 0.0)
        self.assertEqual(geom_utils.volume_sphere(1.0), (4/3)*np.pi)
        self.assertRaises(ValueError, geom_utils.volume_sphere, -1.0)

    def test_vol_spherical_shell(self):
        self.assertEqual(geom_utils.volume_spherical_shell(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(1.0, 1.0), 0.0)
        self.assertAlmostEqual(geom_utils.volume_spherical_shell(1.0, 2.0), (28/3)*np.pi)
        self.assertAlmostEqual(geom_utils.volume_spherical_shell(2.0, 1.0), (28/3)*np.pi)
        self.assertRaises(ValueError, geom_utils.volume_spherical_shell, -1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.volume_spherical_shell, 1.0, -1.0)

    def test_vol_cyl(self):
        self.assertEqual(geom_utils.volume_cyl(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl(1.0, 1.0), np.pi)
        self.assertRaises(ValueError, geom_utils.volume_cyl, -1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.volume_cyl, 1.0, -1.0)

    def test_vol_cyl_shell(self):
        self.assertEqual(geom_utils.volume_cyl_shell(0.0, 0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(1.0, 1.0, 1.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(1.0, 2.0, 1.0), 3*np.pi)
        self.assertEqual(geom_utils.volume_cyl_shell(2.0, 1.0, 1.0), 3*np.pi)
        self.assertRaises(ValueError, geom_utils.volume_cyl_shell, -1.0, 1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.volume_cyl_shell, 1.0, -1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.volume_cyl_shell, 1.0, 1.0, -1.0)

    def test_vol_cone(self):
        self.assertEqual(geom_utils.volume_cone(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cone(1.0, 1.0), np.pi/3)
        self.assertRaises(ValueError, geom_utils.volume_cone, -1.0, 1.0)
        self.assertRaises(ValueError, geom_utils.volume_cone, 1.0, -1.0)


class geom_conversions_test_case(unittest.TestCase):
    """Tests for coodinate conversion functions"""

    def test_cartesian_to_cylindrical(self):
        rho, phi, z = geom_utils.cartesian_to_cylindrical(1, 1, 1)
        self.assertAlmostEqual(rho, np.sqrt(2))
        self.assertAlmostEqual(phi, np.pi/4)
        self.assertAlmostEqual(z, 1)
        rho, theta, z = geom_utils.cartesian_to_cylindrical(-1, 1, 1)
        self.assertAlmostEqual(theta, 3*np.pi/4)

    def test_cartesian_to_spherical(self):
        r, theta, phi = geom_utils.cartesian_to_spherical(1, 1, 1)
        self.assertAlmostEqual(r, np.sqrt(3))
        self.assertAlmostEqual(theta, np.arccos(1/np.sqrt(3)))
        self.assertAlmostEqual(phi, np.pi/4)
        r, theta, phi = geom_utils.cartesian_to_spherical(-1, 1, 1)
        self.assertAlmostEqual(phi, 3*np.pi/4)

    def test_cylindrical_to_cartesian(self):
        x, y, z = geom_utils.cylindrical_to_cartesian(np.sqrt(2), np.pi/4, 1)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)
        self.assertAlmostEqual(z, 1)
        self.assertRaises(ValueError, geom_utils.cylindrical_to_cartesian, -1, np.pi/4, 1)

    def test_cylindrical_to_spherical(self):
        r, theta, phi = geom_utils.cylindrical_to_spherical(np.sqrt(2), np.pi/4, 1)
        self.assertAlmostEqual(r, np.sqrt(3))
        self.assertAlmostEqual(theta, np.arccos(1/np.sqrt(3)))
        self.assertAlmostEqual(phi, np.pi/4)
        self.assertRaises(ValueError, geom_utils.cylindrical_to_spherical, -1, np.pi/4, 1)

    def test_spherical_to_cartesian(self):
        x, y, z = geom_utils.spherical_to_cartesian(np.sqrt(3), np.arccos(1/np.sqrt(3)), np.pi/4)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)
        self.assertAlmostEqual(z, 1)
        self.assertRaises(ValueError, geom_utils.spherical_to_cartesian, -1, np.pi/4, np.pi/4)

    def test_spherical_to_cylindrical(self):
        rho, phi, z = geom_utils.spherical_to_cylindrical(np.sqrt(3), np.arccos(1/np.sqrt(3)), np.pi/4)
        self.assertAlmostEqual(rho, np.sqrt(2))
        self.assertAlmostEqual(phi, np.pi/4)
        self.assertEqual(z, 1)
        self.assertRaises(ValueError, geom_utils.spherical_to_cylindrical, -1, np.pi/4, np.pi/4)


class geom_planes_test_case(unittest.TestCase):
    """ tests for plane functions"""

    def test_check_plane_exists(self):
        self.assertRaises(ValueError, geom_utils.check_plane_exists, np.array([0.0, 0.0, 0.0]))

    def test_check_parallel_planes(self):
        self.assertTrue(geom_utils.check_parallel_planes(np.array([1.0, 1.0, 1.0]),
                        np.array([2.0, 2.0, 2.0])))
        self.assertFalse(geom_utils.check_parallel_planes(np.array([1.0, 1.0, 1.0]),
                                                          np.array([1.0, 2.0, 3.0])))

    def test_angle_between_planes(self):
        self.assertEqual(geom_utils.angle_between_planes(np.array([1.0, 0.0, 0.0]), 0.0,
                         np.array([0.0, 1.0, 0.0]), 0.0), np.pi/2)
        self.assertRaises(ValueError, geom_utils.angle_between_planes, np.array([0.0, 0.0, 0.0]), 0.0,
                          np.array([0.0, 0.0, 0.0]), 0.0)
        self.assertRaises(ValueError, geom_utils.angle_between_planes, np.array([1.0, 1.0, 1.0]), 1.0,
                          np.array([1.0, 1.0, 1.0]), 1.0)
        self.assertRaises(ValueError, geom_utils.angle_between_planes, np.array([1.0, 1.0, 1.0]), 1.0,
                          np.array([2.0, 2.0, 2.0]), 1.0)

    def test_dist_between_planes(self):
        self.assertEqual(geom_utils.dist_between_planes(np.array([1.0, 1.0, 1.0]), 1.0,
                         np.array([1.0, 1.0, 1.0]), 1.0), 0.0)
        self.assertEqual(geom_utils.dist_between_planes(np.array([1.0, 2.0, 3.0]), 4.0,
                         np.array([5.0, 6.0, 7.0]), 8.0), 0.0)
        self.assertEqual(geom_utils.dist_between_planes(np.array([1.0, 0.0, 0.0]), 1.0,
                         np.array([1.0, 0.0, 0.0]), 2.0), 1.0)
        self.assertEqual(geom_utils.dist_between_planes(np.array([1.0, 0.0, 0.0]), 2.0,
                         np.array([1.0, 0.0, 0.0]), 1.0), -1.0)
        self.assertEqual(geom_utils.dist_between_planes(np.array([2.0, 4.0, -4.0]), 6.0,
                         np.array([1.0, 2.0, -2.0]), -9.0), -4.0)
        self.assertRaises(ValueError, geom_utils.dist_between_planes, np.array([0.0, 0.0, 0.0]), 0.0,
                          np.array([0.0, 0.0, 0.0]), 0.0)

    def test_dist_between_point_plane(self):
        self.assertEqual(geom_utils.dist_between_point_plane(np.array([1.0, 2.0, 3.0]),
                                                             6.0, np.array([1.0, 1.0, 1.0])), 0.0)
        self.assertEqual(geom_utils.dist_between_point_plane(np.array([1.0, 0.0, 0.0]),
                                                             5.0, np.array([0.0, 0.0, 0.0])), 5.0)
        self.assertEqual(geom_utils.dist_between_point_plane(np.array([1.0, 0.0, 0.0]),
                                                             0.0, np.array([5.0, 0.0, 0.0])), -5.0)
        self.assertRaises(ValueError, geom_utils.dist_between_point_plane, np.array([0.0, 0.0, 0.0]),
                          1.0, np.array([0.0, 0.0, 0.0]))

    def test_line_segment_plane_intersection(self):
        np.testing.assert_array_almost_equal(geom_utils.line_segment_plane_intersection(np.array([0.0, 0.0, 0.0]),
                                             np.array([0.0, 0.0, 1.0]), np.array([0.0, 0.0, 1.0]), 0.5), np.array([0, 0, 0.5]))
        self.assertRaises(ValueError, geom_utils.line_segment_plane_intersection, np.array([0.0, 0.0, 0.0]),
                          np.array([0.0, 0.0, 1.0]), np.array([0.0, 0.0, 0.0]), 2.0)
        self.assertRaises(ValueError, geom_utils.line_segment_plane_intersection, np.array([0.0, 0.0, 0.0]),
                          np.array([0.0, 0.0, 1.0]), np.array([0.0, 0.0, 1.0]), 2.0)
        self.assertRaises(ValueError, geom_utils.line_segment_plane_intersection, np.array([0.0, 0.0, 0.0]),
                          np.array([0.0, 1.0, 0.0]), np.array([1.0, 0.0, 0.0]), 0.0)

    def test_sphere_plane_intersect(self):
        r, centre_coords = geom_utils.plane_sphere_intersect(np.array([1.0, 0.0, 0.0]), 1.0,
                                                             np.array([0.0, 0.0, 0.0]), 1.0)
        self.assertEqual(r, 0.0)
        np.testing.assert_array_equal(centre_coords, np.array([1.0, 0.0, 0.0]))
        r, centre_coords = geom_utils.plane_sphere_intersect(np.array([1.0, 0.0, 0.0]), 0.5,
                                                             np.array([0.0, 0.0, 0.0]), 1.0)
        self.assertEqual(r, np.sqrt(3)/2)
        np.testing.assert_array_equal(centre_coords, np.array([0.5, 0.0, 0.0]))
        self.assertRaises(ValueError, geom_utils.plane_sphere_intersect, np.array([0.0, 0.0, 0.0]),
                          1.0, np.array([1.0, 1.0, 1.0]), 1.0)
        self.assertRaises(ValueError, geom_utils.plane_sphere_intersect, np.array([1.0, 1.0, 1.0]),
                          1.0, np.array([1.0, 1.0, 1.0]), -1.0)
        self.assertRaises(ValueError, geom_utils.plane_sphere_intersect, np.array([1.0, 0.0, 0.0]),
                          2.0, np.array([0.0, 0.0, 0.0]), 1.0)

    def test_plane_plane_intersect(self):
        p, q = geom_utils.plane_plane_intersect(np.array([1.0, 0.0, 0.0]), 0.0,
                                                np.array([0.0, 1.0, 0.0]), 0.0, 0.0)
        np.testing.assert_array_equal(p, np.array([0.0, 0.0, 0.0]))
        np.testing.assert_array_equal(q, np.array([0.0, 0.0, 1.0]))
        self.assertRaises(ValueError, geom_utils.plane_plane_intersect, np.array([0.0, 0.0, 0.0]),
                          1.0, np.array([1.0, 1.0, 1.0]), 1.0, 0.0)
        self.assertRaises(ValueError, geom_utils.plane_plane_intersect, np.array([1.0, 1.0, 1.0]),
                          1.0, np.array([0.0, 0.0, 0.0]), 1.0, 0.0)
        self.assertRaises(ValueError, geom_utils.plane_plane_intersect, np.array([1.0, 1.0, 1.0]),
                          1.0, np.array([1.0, 1.0, 1.0]), -1.0, 0.0)
        self.assertRaises(ValueError, geom_utils.plane_plane_intersect, np.array([1.0, 1.0, 1.0]),
                          1.0, np.array([2.0, 2.0, 2.0]), 1.0, 0.0)


class geom_points_test_case(unittest.TestCase):
    """ tests for points functions"""

    def test_dist_bet_points(self):
        self.assertEqual(geom_utils.dist_bet_points(np.array([0.0, 0.0, 0.0]),
                         np.array([0.0, 0.0, 0.0])), 0.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([1.0, 1.0, 1.0]),
                         np.array([1.0, 1.0, 1.0])), 0.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([2.0, 0.0, 0.0]),
                         np.array([1.0, 0.0, 0.0])), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([1.0, 0.0, 0.0]),
                         np.array([2.0, 0.0, 0.0])), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([0.0, 1.0, 0.0]),
                         np.array([0.0, 2.0, 0.0])), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([0.0, 0.0, 1.0]),
                         np.array([0.0, 0.0, 2.0])), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([2.0, 0.0, 0.0]),
                         np.array([-1.0, 0.0, 0.0])), 3.0)
        self.assertEqual(geom_utils.dist_bet_points(np.array([-1.0, 0.0, 0.0]),
                         np.array([2.0, 0.0, 0.0])), 3.0)

    def test_mid_point(self):
        np.testing.assert_array_equal(geom_utils.midpoint_bet_points(np.array([1.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0])),
                                      np.array([1.0, 0.0, 0.0]))
        np.testing.assert_array_equal(geom_utils.midpoint_bet_points(np.array([2.0, 0.0, 0.0]), np.array([4.0, 0.0, 0.0])),
                                      np.array([3.0, 0.0, 0.0]))
        np.testing.assert_array_equal(geom_utils.midpoint_bet_points(np.array([4.0, 0.0, 0.0]), np.array([2.0, 0.0, 0.0])),
                                      np.array([3.0, 0.0, 0.0]))
        np.testing.assert_array_equal(geom_utils.midpoint_bet_points(np.array([0.0, 2.0, 0.0]), np.array([0.0, 4.0, 0.0])),
                                      np.array([0.0, 3.0, 0.0]))
        np.testing.assert_array_equal(geom_utils.midpoint_bet_points(np.array([0.0, 0.0, 2.0]), np.array([0.0, 0.0, 4.0])),
                                      np.array([0.0, 0.0, 3.0]))

    def test_rotate(self):
        np.testing.assert_array_almost_equal(geom_utils.rotate_x(np.array([[1, 1, 1]]),
                                                                 np.array([0, 0, 0]), np.pi/2), np.array([[1, -1, 1]]))
        np.testing.assert_array_almost_equal(geom_utils.rotate_y(np.array([[1, 1, 1]]),
                                                                 np.array([0, 0, 0]), np.pi/2), np.array([[1, 1, -1]]))
        np.testing.assert_array_almost_equal(geom_utils.rotate_z(np.array([[1, 1, 1]]),
                                                                 np.array([0, 0, 0]), np.pi/2), np.array([[-1, 1, 1]]))

    def test_translate(self):
        np.testing.assert_array_almost_equal(geom_utils.translate(np.array([[0, 0, 0]]),
                                             np.array([10, 10, 10])), np.array([[10, 10, 10]]))


class geom_pythag_test_case(unittest.TestCase):
    """ tests for pythag functions"""

    def test_pythag(self):
        self.assertEqual(geom_utils.pythag_h(0, 0), 0)
        self.assertEqual(geom_utils.pythag_h(0, 4), 0)
        self.assertEqual(geom_utils.pythag_h(4, 0), 0)
        self.assertEqual(geom_utils.pythag_h(3, 4), 5)
        self.assertEqual(geom_utils.pythag_h(4, 3), 5)
        self.assertEqual(geom_utils.pythag_h(3.0, 4.0), 5.0)
        self.assertEqual(geom_utils.pythag_h(4.0, 3), 5.0)
        self.assertEqual(geom_utils.pythag_h(0, 4), 0)
        self.assertEqual(geom_utils.pythag_h(4, 0), 0)


class line_eq_test_case(unittest.TestCase):
    """ tests for line equation functions"""

    def test_line(self):
        m, c = geom_utils.coefficients_of_line_from_points((-1, 3),  (3, 11))
        self.assertAlmostEqual(m, 2.0, 7)
        self.assertAlmostEqual(c, 5.0, 7)


class ray_test_case(unittest.TestCase):
    """ tests for ray functions"""

    def test_ray_project(self):
        np.testing.assert_array_equal(geom_utils.project_ray(np.array([10.0, 0.0, 0.0]),
                                      np.array([1.0, 0.0, 0.0]), 5), np.array([15.0, 0.0, 0.0]))


class sphere_intersect_test_case(unittest.TestCase):
    """ tests for ray functions"""

    def test_sphere_ray_intersect(self):
        mu1, mu2 = geom_utils.sphere_ray_intersect(np.array([1.0, 0.0, 0.0]),
                                                   np.array([2.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), 1.0)
        self.assertEqual(mu1, 0.0)
        self.assertEqual(mu2, -4.0)
        self.assertRaises(ValueError, geom_utils.sphere_ray_intersect, np.array([1.0, 0.0, 0.0]),
                          np.array([2.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), -1.0)


class surface_sense_test_case(unittest.TestCase):
    """ tests for surface sense functions"""

    def test_sense_plane(self):
        sense = geom_utils.find_sense_plane(np.array([1.0, 0.0, 0.0]), 0.0, np.array([-1.0, 0.0, 0.0]))
        self.assertEqual(sense, 1)
        sense = geom_utils.find_sense_plane(np.array([1.0, 0.0, 0.0]), 0.0, np.array([0.0, 0.0, 0.0]))
        self.assertEqual(sense, 0)
        sense = geom_utils.find_sense_plane(np.array([1.0, 0.0, 0.0]), 0.0, np.array([1.0, 0.0, 0.0]))
        self.assertEqual(sense, -1)
        self.assertRaises(ValueError, geom_utils.find_sense_plane, np.array([0.0, 0.0, 0.0]), 0.0, np.array([0.0, 0.0, 0.0]))

    def test_sense_sphere(self):
        sense = geom_utils.find_sense_sphere(np.array([0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), 10)
        self.assertEqual(sense, 1)
        sense = geom_utils.find_sense_sphere(np.array([0.0, 0.0, 0.0]), np.array([10.0, 0.0, 0.0]), 10)
        self.assertEqual(sense, 0)
        sense = geom_utils.find_sense_sphere(np.array([0.0, 0.0, 0.0]), np.array([20.0, 0.0, 0.0]), 10)
        self.assertEqual(sense, -1)
        self.assertRaises(ValueError, geom_utils.find_sense_sphere, np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), -1.0)

    def test_sense_gq(self):
        sense = geom_utils.find_sense_gq(np.array([1.0, 1.0, 1.0]),
                                         np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 8.0)
        self.assertEqual(sense, -1)
        sense = geom_utils.find_sense_gq(np.array([0.0, 0.0, 0.0]),
                                         np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]), 0.0)
        self.assertEqual(sense, 0)
        sense = geom_utils.find_sense_gq(np.array([1.0, 1.0, 1.0]),
                                         np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 10.0)
        self.assertEqual(sense, 1)


if __name__ == '__main__':
    unittest.main()
