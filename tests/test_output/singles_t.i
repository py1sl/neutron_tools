c test input to generate output for MCNP output reader
1 0 -1 imp:p=1 
2 1 -11.7 1 -2 imp:p=1
3 0 -3 2 imp:p=1 
99 0 3 imp:p=0

c 
1 so 5
2 so 10
3 so 20

c
mode p
nps 2e5 
m1 13027.24c 1  $ Al27
sdef erg=1.332 par=p 
f1:p 2
t1 0 1 2 3 4 5 6 7 8 9 10 50 100  
f2:p 2 
t2 0 1 2 3 4 5 6 7 8 9 10 50 100 
f4:p 2
t4 0 1 2 3 4 5 6 7 8 9 10 50 100  
f5:p 15 0 0 1
t5 0 1 2 3 4 5 6 7 8 9 10 50 100  
f6:p 2 
t6 0 1 2 3 4 5 6 7 8 9 10 50 100 

