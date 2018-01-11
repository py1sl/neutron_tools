# neutron_tools
non pyne based neutron tools
might become pyne tools in future

lost_points :-	simple script to read MCNP output file and create a list of x,y,z co-ordinates where particles were lost 
		which can be plotted in visit

mcnp_run_plot :- read the dump to std out from MCNP6 and plots graphs of nps vs time, coll, nrn, ctm

ofile_reduce :-  reduces mcnp output file to just the last rendevous data, can be useful if the file size exceeds that of most text editors


