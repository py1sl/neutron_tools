#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import meshtal_analysis
import unittest

path = "/tests/test_output/cup_low_res.imsht"
    
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
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00', '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00', '9.00']]
            
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
        self.assertEqual(mesh[0].data[0],['1.000E+36', '-9.000', '-9.000', '-0.200', '6.38182E-07', '1.89545E-02'])
        self.assertEqual(mesh[0].data[-1], ['1.000E+36', '9.000', '9.000', '14.200', '3.03275E-07', '2.57182E-02'])
        
        
    def test_read_mesh(self):
        data = meshtal_analysis.get_lines(path)
        read_mesh = meshtal_analysis.read_mesh(214, data, {214: 4})
        
        self.assertEqual(read_mesh.ptype, 'photon')
        self.assertEqual(read_mesh.idnum, 214)
        self.assertEqual(read_mesh.ctype, '6col')
        
        
class find_mesh_tally_num_test(unittest.TestCase):
    
    def test_find_mesh_tally_num(self):
        data = meshtal_analysis.get_lines(path)
        
        self.assertEqual(meshtal_analysis.find_mesh_tally_numbers(data), {214: 4})
            

if __name__ == '__main__':
    unittest.main()
 
    
    
    
                       
         
        


    