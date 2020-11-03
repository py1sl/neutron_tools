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
'''
data = df.rel_err.to_string(index = False) 
df.hist(data, bins = 15)


data = [df.rel_err]
print (data)
rel_errs = []
for r in data:
    if r !=0:
        rel_errs.append(r)

df.hist(data, bins = 15)
'''

"""    
def add_mesh_(mesha, meshb):
    if mesha.x != meshb.x and mesha.y != meshb.y and mesha.z != meshb.z:
        print ('Bounds not equal')
    
    else:
        new_val = mesha.value + meshb.value
        print ('new value =', new_val)
        new_err = np.sqrt((mesha.rel_err)**2+(meshb.rel_err)**2)
        print ('error in quadrature =', new_err)
       
"""


#Task 1
#def add_mesh(mesha, meshb):       you dumb bitch 
    #for row in df.itertuples():
        #if df.xa =! df.xb and df.ya =! df.yb and df.za =! df.zb:
            #print no can do 
        
        #else:
            #value a + value b
            #np.sqrt((error a)^2 + (error b)^2
            #print both lines and new vals 
        #idk how to specify the two different meshes
    
#think it could be something along the lines of 
#diff = df.diff(periods = -1)
#print (diff) - if difference is 0 then do the calcs if not ignore 
#but i get TypeError: unsupported operand type(s) for -: 'str' and 'str' idk why

#dont need to iterate 

#Task 2
#Ignore for now - dont really get the code

#Task 3
#do basic plot first then go from there 

#def plot_rel_err_hist(data):
    #data = [x for x in df[5]]
    #print (data)                    this probably needs simplifying further 
    #rel_err = []
    #for r in df:
        #if r[5] != 0:
            #rel_errs.append(r[5])
    #df.plothist(bins = 15)

#def plot_rel_err_hist(data):
#data = [x for x in df.rel_err]
                             #this probably needs simplifying further once it actually works
#rel_errs = []
#for row in data:
#    if df.rel_err != 0:
 #       rel_errs.append(rel_err)
#df.plothist(rel_err, bins = 15)  
    #why wont this show?

#pd.df.plothist(column = 'rel_err', bins = 15)

#Task 4 
# - make new branch for geom utils
#add a couple extras to it to start



 



