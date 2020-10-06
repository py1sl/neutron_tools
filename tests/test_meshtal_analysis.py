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
    
        self.assertEqual(meshtal_analysis.calc_mid_points(1.0, 9.0), 5.0)
        self.assertEqual(meshtal_analysis.calc_mid_points(0.0, 1.0), 0.5) 
        self.assertEqual(meshtal_analysis.calc_mid_points(1.0, 1.5), 1.25)          
        

class count_zeros_test(unittest.TestCase):
    
    meshtally_test = meshtal_analysis.meshtally()
    meshtally_test.data = ['0.00', '5.00', '3.00', '6.00', '-1.00', '0.00', '8.00']
   
    def test_count_zeros(self):
            
         self.assertEqual(meshtal_analysis.count_zeros(meshtally_test.data, 2)
  

if __name__ == '__main__':
    unittest.main()
    
    



                        
   
#to do       
#class find_mesh_tally_no_test(unittest.TestCase):
    
    #def test_find_mest_tally_no(self):

#class read_mesh_test(unittest.TestCase):     
    #def test_read_mest(self):
#think this is the one to do next - apparently just give path to the function' 
#(still not too sure how to do that)'
#should then give list of mesh objects so can compare and see if data matches'
#in theory anyway'
        
#class read_mesh_file_test(unittest.TestCase):
    #def test_read_mesh_file(self):   
        


    