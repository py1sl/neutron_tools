#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:58:31 2020

@author: oliviatindle
"""
import meshtal_analysis
import unittest

    
class calc_mid_points_test(unittest.TestCase):
    
    def test_calc_mid_points(self):
        test_data_1 = [1.0, 9.0]
        test_data_2 = [0.0, 1.0]
        test_data_3 = [1.0, 1.5]
    
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_1), [5.0])
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_2), [0.5]) 
        self.assertEqual(meshtal_analysis.calc_mid_points(test_data_3), [1.25])          
        

class count_zeros_test(unittest.TestCase):
   
    def test_count_zeros(self):
        meshtally_test = meshtal_analysis.meshtally()
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00', '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00', '9.00']]
            
        self.assertEqual(meshtal_analysis.count_zeros(meshtally_test), 2)
        #looks for zeros in 5th column as thats the 'results' 

class read_mesh_file_test(unittest.TestCase):  
    
    def test_read_mesh_file(self):
        Mesh = meshtal_analysis.read_mesh_tally_file("/Users/oliviatindle/Desktop/Placement /neutron_tools/tests/test_output/cup_low_res.imsht")
        
        self.assertEqual(Mesh[0].x_bounds[1], '-8.00')
        self.assertEqual(Mesh[0].x_bounds[4], '-2.00')
        self.assertEqual(Mesh[0].ptype, 'photon')
        self.assertEqual(Mesh[0].x_mids[2], -5.0)
        
        
class find_mesh_tally_no_test(unittest.TestCase):
    
    def test_find_mesh_tally_no(self):
        data = meshtal_analysis.get_lines("/Users/oliviatindle/Desktop/Placement /neutron_tools/tests/test_output/cup_low_res.imsht")
        
        self.assertEqual(meshtal_analysis.find_mesh_tally_numbers(data), {214: 4})
        
    

if __name__ == '__main__':
    unittest.main()
    
    
                       
   
#to do       
#class find_mesh_tally_no_test(unittest.TestCase):
    
    #def test_find_mest_tally_no(self):

#class read_mesh_test(unittest.TestCase):     
    #def test_read_mest(self):
         
        


    