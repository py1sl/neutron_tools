c test input to generate output for MCNP output reader
1 0 -1 imp:p=1 
2 1 -2.7 1 -2 imp:p=1
3 0 -3 2 imp:p=1 
99 0 3 imp:p=0

c 
1 -4 so 5
2 2 so 10 4 $ spheres
3 so 20
3 so 20
55 -55.5 gq 3 4 5 6 7  
      8 9 10 11 12 $ general quadratic

c
mode p
nps 1e6 
m1 13027.24c 1  $ Al27
sdef erg=1.332 par=p 
f1:p 1
e1  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
f2:p 1 
e2  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5
f4:p 2 
e4  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
f5:p 15 0 0 1 
e5  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5
f6:p 2 
e6  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5
f8:p 2 
e8  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5
mode n
