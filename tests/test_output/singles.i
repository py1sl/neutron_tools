c test input to generate output for MCNP output reader
1 0 -1 imp:p=1 
2 1 -2.7 1 -2 imp:p=1
3 0 -3 2 imp:p=1 
99 0 3 imp:p=0

c 
1 so 5
2 so 10
3 so 20

c
mode p
nps 1e6 
m1 13027.24c 1  $ Al27
sdef erg=1.332 par=p 
f1:p 1 
f2:p 1 
f4:p 2 
f5:p 15 0 0 1 
f6:p 2 
f8:p 2 
print
