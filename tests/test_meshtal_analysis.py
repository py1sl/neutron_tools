#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:58:31 2020

@author: oliviatindle
"""

import unittest
import numpy as np

class count_zeros_test(unittest.TestCase):
    
    def test_count_zeros(self):
        test_zeros_data =[0, 1, 5, 8, 0, 3]
        
        self.assertEqual(count_zeros(test_zeros_data), 2)
        
class calc_mid_points_test(unittest.TestCase):
    
    def test_calc_mid_points(self):
        test_midpoint_data = np.array[1, 9]
        
        self.assertEqual(calc_mid_points(test_midpoint_data), 5)
        

if __name__ == '__main__':
    unittest.main()
    