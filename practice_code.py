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
#print(df)      #this is a dataframe


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
'''
mids = [4, 5]
value = 4.6
def find_nearest_mid(mids, value): 
      
    return mids[min(range(len(mids)), key = lambda i: abs(mids[i]-value))]
    #applys a key that finds absolout distance and returns element with min distance

print(find_nearest_mid(mids, value))

#Task 1 - done bar test ( i think )

#Task 2
#Ignore for now - dont really get the code

#Task 3 - ( i thinkn this is okay now but its saying df is undefined) 

#Task 4 
# - make new branch for geom utils
#add a couple extras to it to start



  



