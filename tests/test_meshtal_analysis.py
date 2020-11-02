#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import meshtal_analysis
import neut_utilities as ut
import unittest

path = "test_output/cup_low_res.imsht"
    
class calc_mid_points_test(unittest.TestCase):
    
    def test_calc_mid_points(self):
        test_data_1 = [1.0, 9.0]
        test_data_2 = [0.0, 1.0]
        test_data_3 = [1.0, 1.5]
        test_data_4 = [-1.0, 1.0]
        test_data_5 = [-1.0, -1.5]
        test_data_6 = [1.0, 2.0, 3.0, 4.0]
    
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_1), [5.0])
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_2), [0.5]) 
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_3), [1.25])
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_4), [0.0])
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_5), [-1.25])
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_6), [1.5, 2.5, 3.5])
        
        
class count_zeros_test(unittest.TestCase):
   
    def test_count_zeros(self):
        meshtally_test = meshtal_analysis.meshtally()
        meshtally_test.ctype="6col"
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00', '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00', '9.00']]
        meshtally_test.data = meshtal_analysis.convert_to_df(meshtally_test)    
        self.assertEqual(meshtal_analysis.count_zeros(meshtally_test), 2)
        #looks for zeros in 5th column as thats the 'results' 


class read_mesh_file_tests(unittest.TestCase):  
    
    def test_read_mesh_file(self):
        mesh = meshtal_analysis.read_mesh_tally_file(path)
        length = len(mesh[0].data)
        
        self.assertEqual(mesh[0].x_bounds[1], '-8.00')
        self.assertEqual(mesh[0].x_mids[2], -5.0)
        self.assertEqual(mesh[0].e_bounds[1], '1.00E+36')
        self.assertEqual(mesh[0].y_bounds[2], '-6.00')
        self.assertEqual(mesh[0].y_mids[3], -3.00)
        self.assertEqual(mesh[0].z_bounds[2], '2.20')
        self.assertEqual(mesh[0].z_mids[1], 1.4)
        self.assertEqual(mesh[0].ptype, 'photon')
        self.assertEqual(mesh[0].idnum, 214)
        self.assertEqual(length, 1000)

        
        
    def test_read_mesh(self):
        data = ut.get_lines(path)
        read_mesh = meshtal_analysis.read_mesh(214, data, {214: 4})
        
        self.assertEqual(read_mesh.ptype, 'photon')
        self.assertEqual(read_mesh.idnum, 214)
        self.assertEqual(read_mesh.ctype, '6col')
        
        
class find_mesh_tally_num_test(unittest.TestCase):
    
    def test_find_mesh_tally_num(self):
        data = ut.get_lines(path)
        
        self.assertEqual(meshtal_analysis.find_mesh_tally_numbers(data), {214: 4})
            
class add_mesh_test(unittest.TestCase):
    
    def test_add_mesh(self):
        mesh1_test = meshtal_analysis.meshtally()
        mesh1_test.ctype="6col"
        mesh2_test = meshtal_analysis.meshtally()
        mesh2_test.ctype="6col"
        
        mesh1_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4', '7.329430e-07', '0.017765']]
        mesh2_test.data = [['1.000E+36', '9.0', '9.0', '7.8', '6.566330e-07', '0.018680']]
        mesh1_test.data = meshtal_analysis.convert_to_df(mesh1_test)
        mesh2_test.data = meshtal_analysis.convert_to_df(mesh2_test)
        
        self.assertEqual(meshtal_analysis.add_mesh(mesh1_test, mesh2_test), 'Bounds not equal')
        
         
if __name__ == '__main__':
    unittest.main()
 
    
    
    
                       
         
        


    