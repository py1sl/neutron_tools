#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice so i can see things clearer

"""
#To Do:
#Rough idea
#pray
#dont forget print statements 

import meshtal_analysis
import pandas as pd
import numpy as np

meshes = meshtal_analysis.read_mesh_tally_file("/Users/oliviatindle/Desktop/Placement /neutron_tools/tests/test_output/cup_low_res.imsht")

df = meshes[0].data
print(df)      #this is a dataframe

mesh3_test = meshtal_analysis.meshtally()
mesh3_test.ctype="6col"
mesh4_test = meshtal_analysis.meshtally()
mesh4_test.ctype="6col"
        
mesh3_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4', '7.329430e-07', '0.017765']]
mesh4_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4', '6.566330e-07', '0.018680']]
mesh3_test.data = meshtal_analysis.convert_to_df(mesh3_test)
mesh4_test.data = meshtal_analysis.convert_to_df(mesh4_test)

mesh3_test.x_bounds = (-9, -9.1)
mesh3_test.y_bounds = (-9, -9.1)
mesh3_test.z_bounds = (1.4, 1.5)
mesh4_test.x_bounds = (-9, -9.1)
mesh4_test.y_bounds = (-9, -9.1)
mesh4_test.z_bounds = (1.4, 1.5)
        
mesh3_test.data['value'] = 7.329430e-07
mesh3_test.data['rel_err'] = 0.017765
mesh4_test.data['value'] = 6.566330e-07
mesh4_test.data['rel_err'] = 0.018680

x = meshtal_analysis.add_mesh(mesh3_test, mesh4_test)
print(x.data)
print(x.x_bounds)
print(x.data['value'])
print(x.data['rel_err'])

'''
for i, v in enumerate(mids):
    print('i=',i)
    print('v=' ,v)
    if value > float(v):
        print(float(v))
        pos = i
        mid = v
print('pos=', pos)
print('mid =', mid)

mids = [4, 5]
value = 4.6
def find_nearest_mid(value, mids): 
      
    return mids[min(range(len(mids)), key = lambda i: abs(mids[i]-value))]
    #applys a key that finds absolout distance and returns element with min distance

print(find_nearest_mid(value, mids))
'''
#Task 1 - done bar test ( i think )

#Task 2
#Ignore for now - dont really get the code

#Task 3 - ( i thinkn this is okay now but its saying df is undefined) 

#Task 4 
# - make new branch for geom utils
#add a couple extras to it to start
