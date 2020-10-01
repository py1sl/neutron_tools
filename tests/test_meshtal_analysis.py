#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:58:31 2020

@author: oliviatindle
"""
import meshtal_analysis
import unittest

    
class calc_mid_points_test(unittest.TestCase):  'i think this is fine now'
    
    def test_calc_mid_points(self):
        test_midpoint_data = [1.0, 9.0]
        
        self.assertEqual(meshtal_analysis.calc_mid_points(test_midpoint_data), [5.0])           
        

class count_zeros_test(unittest.TestCase):
    
    meshtally_test = meshtal_analysis.meshtally()
    meshtally_test.data = [0, 1, 5, 3, 6, 7, 2, 0, 1, 8, 9]   'data is in the wrong format'
    
    def test_count_zeros(self):
            
         self.assertEqual(meshtal_analysis.count_zeros(meshtally_test.data, 2)
  
                          
   
#to do       
#class find_mesh_tally_no_test(unittest.TestCase):
    
    #def test_find_mest_tally_no(self):

#class read_mesh_test(unittest.TestCase):
    #def test_read_mest(self):
        
#class read_mesh_file_test(unittest.TestCase):
    #def test_read_mesh_file(self):   
        
if __name__ == '__main__':      'god knows whats going on here'
    unittest.main()

    