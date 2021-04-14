# Neutron Tools

All to be considered work in progress

1. MCNP related
lost_points :-	simple script to read MCNP output file and create a list of x,y,z co-ordinates where particles were lost 
		which can be plotted in visit

mcnp_run_plot :- read the dump to std out from MCNP6 and plots graphs of nps vs time, coll, nrn, ctm
ofile_reduce :-  reduces mcnp output file to just the last rendevous data, can be useful if the file size exceeds that of most text editors

mcnp_input_reader :- work in progress, soem basic ability to read and extract data from MCNP input file
mcnp_output_reader :- work in progress, can read some f2, f4 and f5 tally results
mcnp_analysis :- work in progress tools to analyse and plot MCNP output when read by mcnp_output_reader
meshtal_analysis :- reads MCNP meshtal file, can plot a slice, do some statistics, plot histogram of the rel err, count zeros etc
ptrac_reader :- reads MCNP ptrac files
magic:- mesh based magic variance reduction method

2. Fispact related
fispact_input_reader :- currently just template stuff - do not use
fispact_output_reader :- currently just template stuff - do not use
fispact_analysis :-  a few plotting routines for fispact data
fispact_fluxes_writer:- useful functions for generating fluxes files
It should be noted that these are now mostly for historic useage as UKAEA have released an python fispact API which is superior for most cases.


3. General
neut_utilities :- simple functions used by multiple modules
neut_constants :- set of useful constants and unit conversions
geom_utils :- set of geometry functions, distance between planes, area, volumes, intersections etc

[![Build Status](https://travis-ci.org/py1sl/neutron_tools.svg?branch=master)](https://travis-ci.org/py1sl/neutron_tools)
