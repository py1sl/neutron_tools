import unittest
import geom_utils
import numpy as np


class geom_perim_test_case(unittest.TestCase):
    """ tests for perimeter functions"""

    def test_perim_is_zero(self):
        self.assertEqual(geom_utils.perim_circle(0.0), 0.0)

    def test_perim_1_is_2pi(self):
        self.assertEqual(geom_utils.perim_circle(1.0), 2*np.pi)


class geom_area_test_case(unittest.TestCase):
    """ test for area functions"""

    def test_area_is_zero(self):
        self.assertEqual(geom_utils.area_circle(0.0), 0.0)
        self.assertEqual(geom_utils.area_cyl(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cyl(1.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cyl(0.0, 1.0), 0.0)
        self.assertEqual(geom_utils.area_sphere(0.0), 0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 1.0), 0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.area_cone_surf(1.0, 0.0), 0.0)

    def test_area_is_pi(self):
        self.assertEqual(geom_utils.area_circle(1.0), np.pi)
        self.assertEqual(geom_utils.area_sphere(1.0), 4*np.pi)
        self.assertEqual(geom_utils.area_cyl(1.0, 1.0), 4*np.pi)


class geom_volume_test_case(unittest.TestCase):
    """ test for volume functions"""

    def test_vol_is_zero(self):
        self.assertEqual(geom_utils.volume_sphere(0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl(1.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 1.0), 0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(1.0, 1.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(0.0, 0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(1.0, 1.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cone(1.0, 0.0), 0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 1.0), 0.0)


class geom_conversions_test_case(unittest.TestCase):
    """Tests for coodinate conversion functions"""

    def test_cartesian_to_cylindrical(self):
        rho, theta, z = geom_utils.cartesian_to_cylindrical(1, 1, 1)
        self.assertAlmostEqual(rho, np.sqrt(2))
        self.assertAlmostEqual(theta, np.pi/4)
        self.assertAlmostEqual(z, 1)

    def test_cartesian_to_spherical(self):
        r, theta, phi = geom_utils.cartesian_to_spherical(1, 1, 1)
        self.assertAlmostEqual(r, np.sqrt(3))
        self.assertAlmostEqual(theta, np.arccos(1/np.sqrt(3)))
        self.assertAlmostEqual(phi, np.pi/4)

    def test_cylindrical_to_cartesian(self):
        x, y, z = geom_utils.cylindrical_to_cartesian(np.sqrt(2), np.pi/4, 1)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)
        self.assertAlmostEqual(z, 1)

    def test_cylindrical_to_spherical(self):
        r, theta, phi = geom_utils.cylindrical_to_spherical(np.sqrt(2), np.pi/4, 1)
        self.assertAlmostEqual(r, np.sqrt(3))
        self.assertAlmostEqual(theta, np.arccos(1/np.sqrt(3)))
        self.assertAlmostEqual(phi, np.pi/4)

    def test_spherical_to_cartesian(self):
        x, y, z = geom_utils.spherical_to_cartesian(np.sqrt(3), np.arccos(1/np.sqrt(3)), np.pi/4)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)
        self.assertAlmostEqual(z, 1)

    def test_spherical_to_cylindrical(self):
        rho, theta, z = geom_utils.spherical_to_cylindrical(np.sqrt(3), np.arccos(1/np.sqrt(3)), np.pi/4)
        self.assertAlmostEqual(rho, np.sqrt(2))
        self.assertAlmostEqual(theta, np.pi/4)
        self.assertEqual(z, 1)


class geom_planes_test_case(unittest.TestCase):
    """ tests for plane functions"""

    def test_dist_is_zero_same_plane(self):
        self.assertEqual(geom_utils.dist_between_planes(1.0, 1.0, 1.0, 1.0,
                         1.0, 1.0, 1.0, 1.0), 0.0)

    def test_dist_is_zero_not_parallel(self):
        self.assertEqual(geom_utils.dist_between_planes(1.0, 2.0, 3.0, 4.0,
                         5.0, 6.0, 7.0, 8.0), 0.0)

    def test_angle_is_zero(self):
        self.assertEqual(geom_utils.angle_between_planes(0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0), 0.0)

    def test_dist_is_zero_point_plane(self):
        self.assertEqual(geom_utils.dist_between_point_plane(0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0), 0.0)

    def test_sphere_plane_intersect(self):
        self.assertRaises(ValueError, geom_utils.plane_sphere_intersect, 1.0, 1.0,
                          1.0, 1.0, 1.0, 1.0, 1.0, -1.0)
        self.assertRaises(ValueError, geom_utils.plane_sphere_intersect, 1.0, 0.0,
                          0.0, 2.0, 0.0, 0.0, 0.0, 1.0)

    def test_plane_plane_intersect(self):
        self.assertRaises(ValueError, geom_utils.plane_plane_intersect, 1.0, 1.0,
                          1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 0.0)

    def test_line_segment_plane_intersection(self):
        np.testing.assert_array_almost_equal(geom_utils.line_segment_plane_intersection(np.array([0, 0, 0]),
                         np.array([0, 0, 1]), 0, 0, 1, 0.5), np.array([0, 0, 0.5]))


class geom_points_test_case(unittest.TestCase):
    """ tests for points functions"""

    def test_dist_is_zero(self):
        self.assertEqual(geom_utils.dist_bet_points(0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0), 0.0)
        self.assertEqual(geom_utils.dist_bet_points(1.0, 1.0, 1.0,
                         1.0, 1.0, 1.0), 0.0)

    def test_1d_case(self):
        self.assertEqual(geom_utils.dist_bet_points(2.0, 0.0, 0.0, 1.0,
                         0.0, 0.0), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(1.0, 0.0, 0.0, 2.0,
                         0.0, 0.0), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(0.0, 1.0, 0.0, 0.0,
                         2.0, 0.0), 1.0)
        self.assertEqual(geom_utils.dist_bet_points(0.0, 0.0, 1.0, 0.0,
                         0.0, 2.0), 1.0)

    def test_negative(self):
        self.assertEqual(geom_utils.dist_bet_points(2.0, 0.0, 0.0, -1.0,
                         0.0, 0.0), 3.0)
        self.assertEqual(geom_utils.dist_bet_points(-1.0, 0.0, 0.0, 2.0,
                         0.0, 0.0), 3.0)

    def test_mid_point(self):
        self.assertEqual(geom_utils.midpoint_bet_points(0.0, 2.0, 0.0, 0.0,
                         4.0, 0.0), (0.0, 3.0, 0.0))
        self.assertEqual(geom_utils.midpoint_bet_points(0.0, 0.0, 2.0, 0.0,
                         0.0, 4.0), (.0, 0.0, 3.0))
        self.assertEqual(geom_utils.midpoint_bet_points(2.0, 0.0, 0.0, 4.0,
                         0.0, 0.0), (3.0, 0.0, 0.0))

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


    """def test_rotate_point(self):
        x, y = geom_utils.rotate_point(0, 0, 10, 0, np.pi/2.0)
        self.assertEqual(y, 10)   # simple 90 degree rotate
        x, y = geom_utils.rotate_point(0, 0, 10, 0, np.pi)
        self.assertEqual(x, -10)   # simple 180 degree rotate
        x, y = geom_utils.rotate_point(0, 0, 10, 0, np.pi*2.0)
        self.assertEqual(x, 10)   # 360 degree rotate
        x, y = geom_utils.rotate_point(0, 0, 10, 0, -np.pi*2.0)
        self.assertEqual(x, 10)   # -360 degree rotate"""


class geom_pythag_test_case(unittest.TestCase):
    """ tests for pythag functions"""

    def test_345(self):
        self.assertEqual(geom_utils.pythag_h(3, 4), 5)
        self.assertEqual(geom_utils.pythag_h(4, 3), 5)
        self.assertEqual(geom_utils.pythag_h(3.0, 4.0), 5.0)
        self.assertEqual(geom_utils.pythag_h(4.0, 3), 5.0)

    def test_zeros(self):
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
        x, y, z = geom_utils.project_ray(10, 0, 0, 1, 0, 0, 5)
        self.assertEqual(x, 15)
        self.assertEqual(y, 0)
        self.assertEqual(z, 0)


class sphere_intersect_test_case(unittest.TestCase):
    """ tests for ray functions"""

    def test_sphere(self):
        self.assertEqual(1, 1)


class surface_sense_test_case(unittest.TestCase):
    """ tests for surface sense functions"""

    def test_sphere(self):
        sense = geom_utils.find_sense_sphere(0, 0, 0, 1, 0, 0, 10)
        self.assertEqual(sense, 1)
        sense = geom_utils.find_sense_sphere(0, 0, 0, 10, 0, 0, 10)
        self.assertEqual(sense, 0)
        sense = geom_utils.find_sense_sphere(0, 0, 0, 20, 0, 0, 10)
        self.assertEqual(sense, -1)


if __name__ == '__main__':
    unittest.main()
