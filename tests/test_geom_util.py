import unittest
import geom_utils
import numpy as np

class geom_perim_test_case(unittest.TestCase):
    """ tests for perimeter functions"""

    def test_perim_is_zero(self):
        self.assertEqual(geom_utils.perim_circle(0.0),0.0)

    def test_perim_1_is_2pi(self):
        self.assertEqual(geom_utils.perim_circle(1.0),2*np.pi)


class geom_area_test_case(unittest.TestCase):
    """ test for area functions"""

    def test_area_is_zero(self):
        self.assertEqual(geom_utils.area_circle(0.0),0.0)
        self.assertEqual(geom_utils.area_cyl(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.area_cyl(1.0, 0.0),0.0)
        self.assertEqual(geom_utils.area_cyl(0.0, 1.0),0.0)
        self.assertEqual(geom_utils.area_sphere(0.0),0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 1.0),0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.area_cone_surf(1.0, 0.0),0.0)

    def test_area_is_pi(self):
        self.assertEqual(geom_utils.area_circle(1.0), np.pi)
        self.assertEqual(geom_utils.area_sphere(1.0), 4*np.pi)
        self.assertEqual(geom_utils.area_cyl(1.0, 1.0), 4*np.pi)


class geom_volume_test_case(unittest.TestCase):
    """ test for volume functions"""

    def test_vol_is_zero(self):
        self.assertEqual(geom_utils.volume_sphere(0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 1.0),0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(1.0, 1.0),0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(0.0, 0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(1.0, 1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 1.0),0.0)


class geom_planes_test_case(unittest.TestCase):
    """ tests for plane functions"""

    def test_dist_is_zero(self):
        self.assertEqual(geom_utils.dist_between_planes(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),0.0)


    def test_angle_is_zero(self):
        self.assertEqual(geom_utils.angle_between_planes(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),0.0)


class geom_points_test_case(unittest.TestCase):
    """ tests for points functions"""

    def test_dist_is_zero(self):
        self.assertEqual(geom_utils.dist_bet_points(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),0.0)
        self.assertEqual(geom_utils.dist_bet_points(1.0, 1.0, 1.0, 1.0, 1.0, 1.0),0.0)

    def test_1d_case(self):
       self.assertEqual(geom_utils.dist_bet_points(2.0, 0.0, 0.0, 1.0, 0.0, 0.0), 1.0)
       self.assertEqual(geom_utils.dist_bet_points(1.0, 0.0, 0.0, 2.0, 0.0, 0.0), 1.0)
       self.assertEqual(geom_utils.dist_bet_points(0.0, 1.0, 0.0, 0.0, 2.0, 0.0), 1.0)
       self.assertEqual(geom_utils.dist_bet_points(0.0, 0.0, 1.0, 0.0, 0.0, 2.0), 1.0)

    def test_negative(self):
        self.assertEqual(geom_utils.dist_bet_points(2.0, 0.0, 0.0, -1.0, 0.0, 0.0), 3.0)
        self.assertEqual(geom_utils.dist_bet_points(-1.0, 0.0, 0.0, 2.0, 0.0, 0.0), 3.0)


class geom_pythag_test_case(unittest.TestCase):
    """ tests for points functions"""

    def test_345(self):
        self.assertEqual(geom_utils.pythag_h(3,4), 5)
        self.assertEqual(geom_utils.pythag_h(4,3), 5)
        self.assertEqual(geom_utils.pythag_h(3.0,4.0), 5.0)
        self.assertEqual(geom_utils.pythag_h(4.0,3), 5.0)

    def test_zeros(self):
        self.assertEqual(geom_utils.pythag_h(0,4), 0)
        self.assertEqual(geom_utils.pythag_h(4,0), 0)


if __name__ == '__main__':
    unittest.main()