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
        self.assertEqual(geom_utils.area_sphere(0.0),0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 1.0),0.0)
        self.assertEqual(geom_utils.area_cone_surf(0.0, 0.0),0.0)

        
class geom_volume_test_case(unittest.TestCase):
    """ test for volume functions"""
    
    def test_vol_is_zero(self):
        self.assertEqual(geom_utils.volume_sphere(0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl(0.0, 1.0),0.0)
        self.assertEqual(geom_utils.volume_spherical_shell(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(0.0, 0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cyl_shell(1.0, 1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(1.0, 0.0),0.0)
        self.assertEqual(geom_utils.volume_cone(0.0, 1.0),0.0)
        
        
class geom_planes_test_case(unittest.TestCase):
    """ tests for plane functions"""
    
    def test_dist_is_zero(self):
        self.assertEqual(geom_utils.dist_between_planes(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),0.0)
       
        
class geom_points_test_case(unittest.TestCase):
    """ tests for points functions"""
    
    def test_dist_is_zero(self):
        self.assertEqual(geom_utils.dist_bet_points(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),0.0)      
        
        
if __name__ == '__main__':
    unittest.main()