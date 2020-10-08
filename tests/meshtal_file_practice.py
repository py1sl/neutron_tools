#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:27:17 2020

@author: oliviatindle
"""

import meshtal_analysis

Meshes = meshtal_analysis.read_mesh_tally_file("/Users/oliviatindle/Desktop/Placement /neutron_tools/tests/test_output/cup_low_res.imsht")
print ('meshes=', Meshes)

Count0 = meshtal_analysis.count_zeros(Meshes[0])

#meshtal = meshtal_analysis.find_mesh_tally_numbers(Meshes[0])
#print(meshtal)


print ('count=', Count0)

print(Meshes[0].x_bounds)
print(Meshes[0].ptype)
print(Meshes[0].x_mids)

print('x=', Meshes[0].x_mids[2])

data = meshtal_analysis.get_lines("/Users/oliviatindle/Desktop/Placement /neutron_tools/tests/test_output/cup_low_res.imsht")

tally = meshtal_analysis.find_mesh_tally_numbers(data)
print (tally)


read_mesh = meshtal_analysis.read_mesh(214, data, {214: 4})
print (read_mesh)
print(read_mesh.ctype)

