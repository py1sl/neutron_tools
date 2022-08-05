# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:01:04 2022

Tests for extract_line and pick_point functions 
"""
import meshtal_analysis as ma
import unittest


class find_line_test(unittest.TestCase):
    
    def test_extract_line(self):
        
        mesh_test = ma.meshtally()
        mesh_test.ctype = "6col_e"
        mesh_test.x_mids = [1.0]
        mesh_test.y_mids = [5.0]
        mesh_test.z_mids = [5.0]
        mesh_test.data = [[5.0,5.0,3.0e6, -5e-1, 50, 0.41]]
        mesh_test.data = ma.convert_to_df(mesh_test)
        result = ma.extract_line(mesh_test, ((1,5,5)),(2,5,5))
        self.assertAlmostEqual(result[0], )