          Code Name & Version = MCNP, 6.1.1b
  
     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/
    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       
   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    
  _/      _/      _/             _/    _/_/       _/           _/    _/   
 _/      _/        _/_/_/       _/      _/       _/             _/_/      
  
  +---------------------------------------------------------------------+
  | Copyright 2008. Los Alamos National Security, LLC.  All rights      |
  | reserved.                                                           |
  |   This material was produced under U.S. Government contract         |
  | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      |
  | operated by Los Alamos National Security, LLC, for the U.S.         |
  | Department of Energy. The Government is granted for itself and      |
  | others acting on its behalf a paid-up, nonexclusive, irrevocable    |
  | worldwide license in this material to reproduce, prepare derivative |
  | works, and perform publicly and display publicly. Beginning five    |
  | (5) years after 2008, subject to additional five-year worldwide     |
  | renewals, the Government is granted for itself and others acting on |
  | its behalf a paid-up, nonexclusive, irrevocable worldwide license   |
  | in this material to reproduce, prepare derivative works, distribute |
  | copies to the public, perform publicly and display publicly, and to |
  | permit others to do so. NEITHER THE UNITED STATES NOR THE UNITED    |
  | STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, |
  | NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, |
  | OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  |
  | COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, |
  | OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE |
  | PRIVATELY OWNED RIGHTS.                                             |
  +---------------------------------------------------------------------+
  
1mcnp     version 6.mpi ld=01/13/25                     07/24/25 09:38:50 
 *************************************************************************                 probid =  07/24/25 09:38:50 
 n=singles_et.i XSDIR=/home/vol03/scarf473/neutronic_data1/mcnpx_data/xsdir      

 
  warning.  Physics models disabled.
         1-       c test input to generate output for MCNP output reader                          
         2-       1 0 -1 imp:p=1                                                                  
         3-       2 1 -2.7 1 -2 imp:p=1                                                           
         4-       3 0 -3 2 imp:p=1                                                                
         5-       99 0 3 imp:p=0                                                                  
         6-                                                                                       
         7-       c                                                                               
         8-       1 so 5                                                                          
         9-       2 so 10                                                                         
        10-       3 so 20                                                                         
        11-                                                                                       
        12-       c                                                                               
        13-       mode p                                                                          
        14-       nps 1e6                                                                         
        15-       m1 13027.24c 1  $ Al27                                                          
  warning.  neutron table inconsistent with mode will be ignored.
        16-       sdef erg=1.332 par=p tme=d1                                                     
        17-       sp1 -41 12.5 25                                                                 
        18-       f1:p 1                                                                          
        19-       e1  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        20-       t1     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        21-       f2:p 1                                                                          
        22-       e2  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        23-       t2     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        24-       f4:p 2                                                                          
        25-       e4  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        26-       t4     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        27-       f5:p 15 0 0 1                                                                   
        28-       e5  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        29-       t5     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        30-       f6:p 2                                                                          
        31-       e6  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        32-       t6     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        33-       f8:p 2                                                                          
        34-       e8  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
 
  warning.  last time bin of tally        1 is less than time cutoff.
 
  warning.  last time bin of tally        2 is less than time cutoff.
 
  warning.  last time bin of tally        4 is less than time cutoff.
 
  warning.  last time bin of tally        5 is less than time cutoff.
 
  warning.  last time bin of tally        6 is less than time cutoff.
 
  warning.  tally        8 needs zero energy bin for negative f8 scores.
1cells                                                                                                  print table 60

                               atom        gram                                            photon                                      
              cell      mat   density     density     volume       mass            pieces importance                                   

        1        1        0  0.00000E+00 0.00000E+00 5.23599E+02 0.00000E+00           1  1.0000E+00                                   
        2        2        1  6.02616E-02 2.70000E+00 3.66519E+03 9.89602E+03           1  1.0000E+00                                   
        3        3        0  0.00000E+00 0.00000E+00 2.93215E+04 0.00000E+00           1  1.0000E+00                                   
        4       99        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00                                   

 total                                               3.35103E+04 9.89602E+03

    minimum source weight = 1.0000E+00    maximum source weight = 1.0000E+00

 ***************************************************
 * Random Number Generator  =                    1 *
 * Random Number Seed       =       19073486328125 *
 * Random Number Multiplier =       19073486328125 *
 * Random Number Adder      =                    0 *
 * Random Number Bits Used  =                   48 *
 * Random Number Stride     =               152917 *
 ***************************************************

 
  warning.  Force analog capture for pulse height tallies

         9 warning messages so far.
1cross-section tables                                                                                   print table 100
     XSDIR used: /home/vol03/scarf473/neutronic_data1/mcnpx_data/xsdir

     table    length

                        tables from file mcplib05t                                                       

 
  comment.   13000.05p pips data for photon energy broadening converted to CDF form.
  13000.05p    5468  ENDF/B-VI Release 8 Photoatomic Data for 13-AL                               mat1300      12/14/09
                     Energy range:   1.00000E-03  to  1.00000E+05 MeV.

  total        5468

 maximum photon energy set to    100.0 mev (maximum electron energy)

                        tables from file el03                                                            

  13000.03e    2337                                                                                          6/6/98    
                     Energy range:   1.00000E-03  to  1.00000E+03 MeV.

1particles and energy limits                                                                            print table 101

                         particle      maximum       smallest      largest       always        always
                         cutoff        particle      table         table         use table     use model
   particle type         energy        energy        maximum       maximum       below         above

    2  p    photon      1.0000E-03    1.0000E+02    1.0000E+05    1.0000E+05    1.0000E+36    1.0000E+36
    3  e    electron    1.0000E-03    1.0000E+02    1.0000E+02    1.0000E+02    1.0000E+36    1.0000E+36
 
 
  warning.  material        1 has been set to a conductor.

 ***********************************************************************************************************************

 dump no.    1 on file singles_et.ir     nps =           0     coll =              0     ctm =        0.00   nrn =      
           0

        10 warning messages so far.
 master starting      11 MPI slave tasks with       1 threads each  07/24/25 09:38:51 
 master set rendezvous nps =        1000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        2000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        3000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        4000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        5000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        6000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        7000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        8000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =        9000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       10000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       11000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       12000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       13000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       14000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       15000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       16000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       17000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       18000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       19000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       20000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       22000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       24000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       26000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       28000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       30000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       32000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       34000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       36000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       38000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       40000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       44000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       48000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       52000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       56000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       60000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       64000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       68000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       72000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       76000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       80000,  work chunks =    11    07/24/25 09:38:51 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.6889E-01 1.0000E+00 5.0064E+02 5.6665E-01 8.9149E+00 1.0000E+00 6.0729E-01     2       79378    3                  44         6   
 master set rendezvous nps =       88000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =       96000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      104000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      112000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      120000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      128000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      136000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      144000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      152000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      160000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      176000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      192000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      208000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      224000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      240000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      256000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      272000,  work chunks =    11    07/24/25 09:38:51 
 master set rendezvous nps =      288000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      304000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      320000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      352000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      384000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      416000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      448000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      480000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      512000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      544000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      576000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      608000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      640000,  work chunks =    11    07/24/25 09:38:52 
 master set rendezvous nps =      704000,  work chunks =    11    07/24/25 09:38:53 
 master set rendezvous nps =      768000,  work chunks =    11    07/24/25 09:38:53 
 master set rendezvous nps =      832000,  work chunks =    11    07/24/25 09:38:53 
 master set rendezvous nps =      896000,  work chunks =    11    07/24/25 09:38:53 
 master set rendezvous nps =      960000,  work chunks =    11    07/24/25 09:38:53 
 master set rendezvous nps =     1000000,  work chunks =    11    07/24/25 09:38:53 
1problem summary                                                                                                           

      run terminated when     1000000  particle histories were done.
+                                                                                                    07/24/25 09:38:53 
      c test input to generate output for MCNP output reader                               probid =  07/24/25 09:38:50 

 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source             1000000    1.0000E+00    1.3320E+00          escape              930154    9.3015E-01    9.0695E-01
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            1.8191E-05
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 from neutrons            0    0.            0.                  compton scatter          0    0.            4.1926E-01
 bremsstrahlung       73630    7.3630E-02    2.5016E-03          capture             148849    1.4885E-01    8.0813E-03
 p-annihilation        1286    1.2860E-03    6.5716E-04          pair production        643    6.4300E-04    8.5551E-04
 photonuclear             0    0.            0.                  photonuclear abs         0    0.            0.        
 electron x-rays          0    0.            0.                  loss to photofis         0    0.            0.        
 compton fluores          0    0.            0.                                                                        
 muon capt fluores        0    0.            0.                                                                        
 1st fluorescence      4730    4.7300E-03    6.9506E-06                                                                
 2nd fluorescence         0    0.            0.                                                                        
 cerenkov                 0    0.            0.                                                                        
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total          1079646    1.0796E+00    1.3352E+00              total          1079646    1.0796E+00    1.3352E+00

   number of photons banked                    74916        average time of (shakes)              cutoffs
   photon tracks per source particle      1.0796E+00          escape            2.5070E+01          tco   1.0000E+33
   photon collisions per source particle  1.6901E+00          capture           2.4244E+01          eco   1.0000E-03
   total photon collisions                   1690149          capture or escape 2.4956E+01          wc1   0.0000E+00
                                                              any termination   2.4956E+01          wc2   0.0000E+00

 computer time so far in this run     0.56 minutes            maximum number ever in bank         4
 computer time in mcrun               0.40 minutes            bank overflows to backup file       0
 source particles per minute            2.5153E+06
 random numbers generated                 35178899            most random numbers used was         491 in history      921363

 range of sampled source weights = 1.0000E+00 to 1.0000E+00

 estimated system efficiency for MPI usage =  9%

 number of histories processed by each MPI task
           0       90866       90916       90897       90926       90906       90902       90906       90926       90897
       90916       90942
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1     1081665      1000797            0    0.0000E+00   1.2224E+00   1.2224E+00   1.0000E+00   0.0000E+00
        2        2     1081665      1074916      1690149    1.6901E+00   8.6475E-01   8.6475E-01   1.0000E+00   5.3222E+00
        3        3      930154       930154            0    0.0000E+00   9.4412E-01   9.4412E-01   1.0000E+00   0.0000E+00

           total       3093484      3005867      1690149    1.6901E+00

1tally        1        nps =     1000000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  1                                                                                                                            
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.00000E-06 1.0000   4.40000E-05 0.2490   8.39000E-04 0.0564   4.20100E-03 0.0250
    2.0000E-01   0.00000E+00 0.0000   1.00000E-05 0.4472   1.43000E-04 0.1291   1.57300E-03 0.0385   8.22900E-03 0.0167
    3.0000E-01   0.00000E+00 0.0000   1.00000E-05 0.4472   1.61000E-04 0.1113   2.00700E-03 0.0316   1.02920E-02 0.0140
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   4.00000E-06 0.7071   8.20000E-05 0.1562   4.40000E-04 0.0674
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.00000E-06 0.5000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.00000E-06 0.5000   5.80000E-05 0.1857
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   5.00000E-06 0.4472   8.50000E-05 0.1085   2.29700E-03 0.0208   2.73230E-02 0.0060   1.43205E-01 0.0024
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      5.00000E-06 0.4472   1.07000E-04 0.1364   2.64900E-03 0.0237   3.18320E-02 0.0069   1.66433E-01 0.0029
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   9.38700E-03 0.0168   9.47900E-03 0.0167   4.23300E-03 0.0255   8.37000E-04 0.0556   5.20000E-05 0.2433
    2.0000E-01   1.89640E-02 0.0110   1.89240E-02 0.0109   8.60000E-03 0.0163   1.75000E-03 0.0362   1.05000E-04 0.1503
    3.0000E-01   2.38530E-02 0.0091   2.37690E-02 0.0092   1.05040E-02 0.0138   1.98800E-03 0.0318   1.78000E-04 0.1057
    4.0000E-01   9.42000E-04 0.0460   9.67000E-04 0.0455   3.59000E-04 0.0746   4.60000E-05 0.2085   1.00000E-05 0.4472
    5.0000E-01   2.20000E-05 0.3015   1.60000E-05 0.3536   2.00000E-06 1.0000   2.00000E-06 1.0000   0.00000E+00 0.0000
    6.0000E-01   8.50000E-05 0.1529   8.50000E-05 0.1529   3.20000E-05 0.2500   1.00000E-05 0.4472   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   3.26405E-01 0.0014   3.26822E-01 0.0014   1.43876E-01 0.0024   2.75880E-02 0.0059   2.29500E-03 0.0209
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      3.79658E-01 0.0018   3.80062E-01 0.0017   1.67606E-01 0.0029   3.22210E-02 0.0069   2.64000E-03 0.0237
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   8.00000E-06 0.6124   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.90820E-02 0.0095
    2.0000E-01   6.00000E-06 0.5773   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.83040E-02 0.0062
    3.0000E-01   4.00000E-06 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.27660E-02 0.0052
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.85000E-03 0.0265
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.00000E-05 0.2000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.78000E-04 0.0848
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   9.70000E-05 0.1015   2.00000E-06 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.15000E-04 0.1304   2.00000E-06 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.16333E+00 0.0006


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.1627E+00 to 1.1640E+00; 1.1620E+00 to 1.1647E+00; 1.1613E+00 to 1.1653E+00
 estimated  symmetric confidence interval(1,2,3 sigma): 1.1627E+00 to 1.1640E+00; 1.1620E+00 to 1.1647E+00; 1.1613E+00 to 1.1653E+00

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        1 with nps =     1000000  print table 160


 normed average tally per history  = 1.16333E+00          unnormed average tally per history  = 1.16333E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       96197          largest  unnormalized history tally = 1.30000E+01
 (largest  tally)/(average tally)  = 1.11748E+01          (largest  tally)/(avg nonzero tally)= 1.11748E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.16333E+00


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.16333E+00             1.16334E+00                     0.000010
      relative error                  5.76504E-04             5.76588E-04                     0.000145
      variance of the variance        3.26788E-05             3.27544E-05                     0.002315
      shifted center                  1.16333E+00             1.16333E+00                     0.000000
      figure of merit                 7.56806E+06             7.56588E+06                    -0.000289

 the estimated slope of the  49 largest  tallies starting at  1.00000E+01 appears to be decreasing at least exponentially.
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.515E+06)*( 1.735E+00)**2 = (2.515E+06)*(3.009E+00) = 7.568E+06

1tally        2        nps =     1000000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): photons  

           areas   
                surface:       1                                                                                   
                         3.14159E+02
 
 surface  1                                                                                                                            
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.37387E-08 1.0000   2.17720E-07 0.2621   5.88333E-06 0.0876   2.84893E-05 0.0360
    2.0000E-01   0.00000E+00 0.0000   4.71277E-08 0.4615   9.99105E-07 0.1863   1.08815E-05 0.0579   5.34837E-05 0.0239
    3.0000E-01   0.00000E+00 0.0000   4.55833E-08 0.4618   9.68333E-07 0.1306   1.24740E-05 0.0416   6.87552E-05 0.0203
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   1.61361E-07 0.8168   1.59425E-06 0.2087   9.97318E-06 0.0886
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.88202E-08 0.5150
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.85761E-08 0.5497   3.02016E-07 0.1955
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   1.59155E-08 0.4472   2.70563E-07 0.1085   7.31158E-06 0.0208   8.69718E-05 0.0060   4.55836E-04 0.0024
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.59155E-08 0.4472   3.87013E-07 0.1693   9.65810E-06 0.0354   1.17853E-04 0.0109   6.16918E-04 0.0047
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   6.13038E-05 0.0236   6.37242E-05 0.0239   2.73258E-05 0.0349   5.22961E-06 0.0769   4.29488E-07 0.3480
    2.0000E-01   1.29121E-04 0.0160   1.26230E-04 0.0159   5.64359E-05 0.0231   1.12341E-05 0.0483   7.76158E-07 0.2364
    3.0000E-01   1.57923E-04 0.0133   1.54066E-04 0.0130   6.98328E-05 0.0206   1.25413E-05 0.0431   1.43748E-06 0.1627
    4.0000E-01   2.13922E-05 0.0599   2.21811E-05 0.0584   8.02010E-06 0.0952   1.20861E-06 0.2524   4.24004E-07 0.5253
    5.0000E-01   2.90274E-07 0.4884   2.21893E-07 0.6036   1.27324E-07 1.0000   9.90303E-09 1.0000   0.00000E+00 0.0000
    6.0000E-01   4.97575E-07 0.1768   6.23065E-07 0.2473   1.83827E-07 0.2809   5.80091E-08 0.5011   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   1.03898E-03 0.0014   1.04031E-03 0.0014   4.57972E-04 0.0024   8.78153E-05 0.0059   7.30521E-06 0.0209
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.40951E-03 0.0030   1.40735E-03 0.0030   6.19897E-04 0.0046   1.18097E-04 0.0103   1.03723E-05 0.0449
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   2.89493E-08 0.6208   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.92656E-04 0.0135
    2.0000E-01   3.04260E-08 0.5800   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.89240E-04 0.0090
    3.0000E-01   1.52621E-08 0.7117   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.78059E-04 0.0075
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.49548E-05 0.0343
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.28214E-07 0.3249
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.71307E-06 0.1156
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   3.08761E-07 0.1015   6.36620E-09 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   3.18310E-03 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      3.83398E-07 0.1427   6.36620E-09 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   4.31045E-03 0.0015


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       4.49
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.3040E-03 to 4.3170E-03; 4.2975E-03 to 4.3235E-03; 4.2910E-03 to 4.3300E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 4.3039E-03 to 4.3170E-03; 4.2974E-03 to 4.3235E-03; 4.2909E-03 to 4.3300E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        2 with nps =     1000000  print table 160


 normed average tally per history  = 4.31045E-03          unnormed average tally per history  = 1.35417E+00
 estimated tally relative error    = 0.0015               estimated variance of the variance  = 0.0002
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0015

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      951196          largest  unnormalized history tally = 9.21616E+01
 (largest  tally)/(average tally)  = 6.80578E+01          (largest  tally)/(avg nonzero tally)= 6.80578E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.31049E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.31045E-03             4.31074E-03                     0.000067
      relative error                  1.50949E-03             1.51088E-03                     0.000918
      variance of the variance        2.46272E-04             2.49176E-04                     0.011792
      shifted center                  4.31049E-03             4.31049E-03                     0.000000
      figure of merit                 1.10390E+06             1.10188E+06                    -0.001834

 the estimated inverse power slope of the 198 largest  tallies starting at 4.62355E+01 is 4.4927
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.515E+06)*( 6.625E-01)**2 = (2.515E+06)*(4.389E-01) = 1.104E+06

1tally        4        nps =     1000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2                                                                                   
                         3.66519E+03
 
 cell  2                                                                                                                               
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.87254E-08 0.4273   2.23560E-07 0.0903   3.30022E-06 0.0246   1.72371E-05 0.0107
    2.0000E-01   5.91582E-10 1.0000   2.12499E-08 0.2844   5.59364E-07 0.0610   6.49221E-06 0.0176   3.41451E-05 0.0076
    3.0000E-01   0.00000E+00 0.0000   1.91276E-08 0.3046   4.43260E-07 0.0626   5.21368E-06 0.0185   2.65332E-05 0.0081
    4.0000E-01   0.00000E+00 0.0000   7.07232E-09 0.3627   1.94150E-07 0.0873   2.59437E-06 0.0238   1.37192E-05 0.0103
    5.0000E-01   0.00000E+00 0.0000   5.22536E-09 0.5282   1.18999E-07 0.0986   1.51817E-06 0.0279   7.80504E-06 0.0123
    6.0000E-01   0.00000E+00 0.0000   2.98080E-09 0.5379   1.10309E-07 0.1001   1.11838E-06 0.0312   5.94885E-06 0.0135
    8.0000E-01   2.70642E-10 0.7129   8.51352E-09 0.3547   1.56233E-07 0.0810   1.74078E-06 0.0238   8.82878E-06 0.0105
    9.0000E-01   1.15325E-09 1.0000   3.06520E-09 0.5818   5.88631E-08 0.1269   7.02701E-07 0.0359   3.83812E-06 0.0155
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   5.42173E-08 0.1344   7.09346E-07 0.0355   3.61782E-06 0.0156
    1.1000E+00   0.00000E+00 0.0000   2.16768E-09 0.6699   5.22657E-08 0.1314   6.46721E-07 0.0371   3.50925E-06 0.0158
    1.2000E+00   9.04963E-10 1.0000   1.62413E-09 0.6497   5.97005E-08 0.1230   6.76041E-07 0.0360   3.42718E-06 0.0160
    1.3000E+00   0.00000E+00 0.0000   5.29181E-10 0.9137   5.54952E-08 0.1233   6.14122E-07 0.0368   3.35143E-06 0.0159
    1.4000E+00   3.78860E-09 0.5457   8.06590E-08 0.1220   2.21077E-06 0.0233   2.66334E-05 0.0066   1.40287E-04 0.0028
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      6.70903E-09 0.4633   1.70940E-07 0.1293   4.29719E-06 0.0238   5.19602E-05 0.0069   2.72248E-04 0.0029
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   3.90628E-05 0.0071   3.96481E-05 0.0070   1.71961E-05 0.0107   3.46225E-06 0.0238   2.39282E-07 0.0904
    2.0000E-01   7.84537E-05 0.0050   7.95581E-05 0.0050   3.47895E-05 0.0076   6.80691E-06 0.0172   5.07267E-07 0.0607
    3.0000E-01   6.14024E-05 0.0053   6.16823E-05 0.0053   2.69138E-05 0.0081   5.41993E-06 0.0182   4.37806E-07 0.0637
    4.0000E-01   3.10481E-05 0.0068   3.12349E-05 0.0068   1.34125E-05 0.0104   2.62082E-06 0.0235   1.91051E-07 0.0876
    5.0000E-01   1.84222E-05 0.0080   1.82050E-05 0.0080   8.00620E-06 0.0121   1.53630E-06 0.0278   1.28119E-07 0.0972
    6.0000E-01   1.33376E-05 0.0090   1.35814E-05 0.0089   5.98310E-06 0.0135   1.16307E-06 0.0310   1.00778E-07 0.1013
    8.0000E-01   2.00414E-05 0.0070   1.99738E-05 0.0070   8.89704E-06 0.0105   1.67655E-06 0.0242   1.41775E-07 0.0818
    9.0000E-01   8.73429E-06 0.0102   8.72952E-06 0.0102   3.83051E-06 0.0155   7.49089E-07 0.0350   4.93373E-08 0.1313
    1.0000E+00   8.19827E-06 0.0104   8.27088E-06 0.0103   3.56021E-06 0.0159   7.08846E-07 0.0354   5.48165E-08 0.1299
    1.1000E+00   8.04720E-06 0.0104   8.06650E-06 0.0104   3.50148E-06 0.0159   6.86015E-07 0.0356   5.94807E-08 0.1254
    1.2000E+00   7.81972E-06 0.0105   7.74975E-06 0.0106   3.41438E-06 0.0159   6.76933E-07 0.0359   4.61782E-08 0.1352
    1.3000E+00   7.89526E-06 0.0104   7.87064E-06 0.0104   3.36662E-06 0.0159   6.75117E-07 0.0357   5.82860E-08 0.1239
    1.4000E+00   3.20107E-04 0.0017   3.21154E-04 0.0017   1.42085E-04 0.0027   2.70752E-05 0.0066   2.29382E-06 0.0230
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      6.22570E-04 0.0018   6.25725E-04 0.0018   2.74956E-04 0.0029   5.32571E-05 0.0069   4.30800E-06 0.0237
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   1.18218E-08 0.4161   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.20400E-04 0.0039
    2.0000E-01   1.61576E-08 0.3217   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.41350E-04 0.0027
    3.0000E-01   1.55968E-08 0.3001   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.88081E-04 0.0029
    4.0000E-01   7.72703E-09 0.4478   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.50299E-05 0.0038
    5.0000E-01   1.33308E-09 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.57466E-05 0.0045
    6.0000E-01   4.60593E-09 0.4755   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.13511E-05 0.0050
    8.0000E-01   7.74130E-09 0.3716   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.14729E-05 0.0039
    9.0000E-01   4.60303E-09 0.4680   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.67013E-05 0.0058
    1.0000E+00   2.31297E-09 0.6127   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.51767E-05 0.0059
    1.1000E+00   1.16830E-09 0.7480   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.45722E-05 0.0059
    1.2000E+00   2.96566E-09 0.6037   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.38754E-05 0.0060
    1.3000E+00   2.85882E-09 0.6136   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.38904E-05 0.0059
    1.4000E+00   9.42152E-08 0.1123   2.72837E-09 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   9.82028E-04 0.0005
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.73108E-07 0.1119   2.72837E-09 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.90968E-03 0.0006


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        4

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed    increase       0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?         no          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =     1000000  print table 160


 normed average tally per history  = 1.90968E-03          unnormed average tally per history  = 6.99933E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      773258          largest  unnormalized history tally = 5.24409E+01
 (largest  tally)/(average tally)  = 7.49227E+00          (largest  tally)/(avg nonzero tally)= 7.49227E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.90968E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.90968E-03             1.90969E-03                     0.000006
      relative error                  5.80379E-04             5.80411E-04                     0.000055
      variance of the variance        1.01496E-05             1.01623E-05                     0.001256
      shifted center                  1.90968E-03             1.90968E-03                     0.000000
      figure of merit                 7.46734E+06             7.46652E+06                    -0.000110

 the estimated slope of the 200 largest  tallies starting at  3.62629E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.515E+06)*( 1.723E+00)**2 = (2.515E+06)*(2.969E+00) = 7.467E+06

1unnormed tally density for tally        4          nonzero tally mean(m) = 6.999E+00   nps =     1000000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope=10.0)
  tally  number num den log den:d--------------d---------------d----------------d---------------d---------------d---------------d---
 2.51-02      2 3.87-04  -3.412 ***************|***************|****************|*              |               |               |   
 3.16-02      0 0.00+00   0.000                |               |                |               |               |               |   
 3.98-02      1 1.22-04  -3.913 ***************|***************|**********      |               |               |               |   
 5.01-02      1 9.70-05  -4.013 ***************|***************|********        |               |               |               |   
 6.31-02      0 0.00+00   0.000                |               |                |               |               |               |   
 7.94-02      0 0.00+00   0.000                |               |                |               |               |               |   
 1.00-01      0 0.00+00   0.000                |               |                |               |               |               |   
 1.26-01      5 1.93-04  -3.714 ***************|***************|*************   |               |               |               |   
 1.58-01      0 0.00+00   0.000                |               |                |               |               |               |   
 2.00-01      3 7.31-05  -4.136 ***************|***************|******          |               |               |               |   
 2.51-01      4 7.74-05  -4.111 ***************|***************|******          |               |               |               |   
 3.16-01      4 6.15-05  -4.211 ***************|***************|*****           |               |               |               |   
 3.98-01      5 6.11-05  -4.214 ***************|***************|*****           |               |               |               |   
 5.01-01     13 1.26-04  -3.899 ***************|***************|**********      |               |               |               |   
 6.31-01     14 1.08-04  -3.967 ***************|***************|*********       |               |               |               |   
 7.94-01     27 1.65-04  -3.782 ***************|***************|************    |               |               |               |   
 1.00+00     36 1.75-04  -3.757 ***************|***************|************    |               |               |               |   
 1.26+00     46 1.78-04  -3.750 ***************|***************|************    |               |               |               |   
 1.58+00     76 2.33-04  -3.632 ***************|***************|**************  |               |               |               |   
 2.00+00    139 3.39-04  -3.470 ***************|***************|****************|               |               |               |   
 2.51+00    214 4.14-04  -3.383 ***************|***************|****************|*              |               |               |   
 3.16+00    419 6.44-04  -3.191 ***************|***************|****************|****           |               |               |   
 3.98+00    829 1.01-03  -2.995 ***************|***************|****************|*******        |               |               |   
 5.01+00 502564 4.88-01  -0.312 ***************|***************|****************|***************|***************|***************|***
 6.31+00 220349 1.70-01  -0.770 ***************|***************|****************|***************|***************|************   |   
 7.94+00  70708 4.33-02  -1.364 mmmmmmmmmmmmmmm|mmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmm|mmmmmmmmmmmmmmm|mm             |   
 1.00+01  55174 2.68-02  -1.571 ***************|***************|****************|***************|***************|               |   
 1.26+01  50291 1.94-02  -1.712 ***************|***************|****************|***************|************   |               |   
 1.58+01  43779 1.34-02  -1.872 ***************|***************|****************|***************|**********     |               |   
 2.00+01  32222 7.85-03  -2.105 ***************|***************|****************|***************|******         |               |   
 2.51+01  17032 3.30-03  -2.482 ***************|***************|****************|***************|               |               |   
 3.16+01   5180 7.96-04  -3.099 ***************|***************|****************|******         |               |               |   
 3.98+01    796 9.72-05  -4.012 ***************|***************|********        |               |               |               |   
 5.01+01     62 6.01-06  -5.221 ***************|****           |                |               |               |               |   
 6.31+01      5 3.85-07  -6.414 *              |               |                |               |               |               |   
  total 1000000 1.00+00         d--------------d---------------d----------------d---------------d---------------d---------------d---

1tally        5        nps =     1000000
           tally type 5    particle flux at a point detector.           units   1/cm**2        
           particle(s): photons  
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.18549E-10 0.4110   1.87985E-08 0.2473   3.29569E-07 0.1060   1.63779E-06 0.0621
    2.0000E-01   3.60401E-10 1.0000   5.09698E-10 0.3324   6.22632E-08 0.1422   8.34570E-07 0.0781   4.02908E-06 0.0358
    3.0000E-01   1.41827E-10 0.7948   4.36169E-10 0.3971   4.17687E-08 0.1896   4.81960E-07 0.0519   2.57042E-06 0.0230
    4.0000E-01   0.00000E+00 0.0000   2.55910E-10 0.3813   5.71614E-08 0.3155   3.37465E-07 0.0500   1.93219E-06 0.0224
    5.0000E-01   2.65897E-10 1.0000   1.00064E-09 0.5564   2.89991E-08 0.1964   3.45020E-07 0.0513   1.84321E-06 0.0229
    6.0000E-01   0.00000E+00 0.0000   1.38050E-10 1.0000   3.18776E-08 0.1725   3.33497E-07 0.0607   1.67213E-06 0.0258
    8.0000E-01   0.00000E+00 0.0000   2.07191E-09 0.6514   5.30661E-08 0.1547   5.75874E-07 0.0550   3.47794E-06 0.1658
    9.0000E-01   0.00000E+00 0.0000   6.77119E-10 1.0000   3.19195E-08 0.2904   3.00677E-07 0.0927   1.35381E-06 0.0407
    1.0000E+00   0.00000E+00 0.0000   8.02530E-10 1.0000   2.50138E-08 0.3261   2.41677E-07 0.1153   1.41005E-06 0.0454
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   1.32682E-08 0.3727   2.56164E-07 0.1150   1.45936E-06 0.0547
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   1.70387E-08 0.4494   2.06490E-07 0.1372   1.42355E-06 0.0555
    1.3000E+00   0.00000E+00 0.0000   1.37511E-08 0.8695   2.88193E-08 0.6019   1.65507E-07 0.1671   1.42411E-06 0.0648
    1.4000E+00   6.90691E-10 0.5000   1.46772E-08 0.1085   4.06872E-07 0.0345   4.70197E-06 0.0068   2.49721E-05 0.0033
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.45882E-09 0.6589   3.45388E-08 0.3616   8.16866E-07 0.0600   9.11044E-06 0.0157   4.92057E-05 0.0136
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   3.96700E-06 0.0571   3.91139E-06 0.0345   1.60877E-06 0.0374   3.59425E-07 0.1028   3.71779E-08 0.2458
    2.0000E-01   9.32487E-06 0.0158   9.46158E-06 0.0153   4.19352E-06 0.0278   7.98370E-07 0.0609   8.75624E-08 0.1672
    3.0000E-01   5.89526E-06 0.0384   5.84251E-06 0.0144   2.97556E-06 0.1056   4.94757E-07 0.0510   3.52388E-08 0.1683
    4.0000E-01   4.56710E-06 0.0159   4.43190E-06 0.0152   1.99146E-06 0.0228   3.98375E-07 0.0540   4.07710E-08 0.1768
    5.0000E-01   4.23059E-06 0.0172   4.37032E-06 0.0157   1.99811E-06 0.0256   3.64206E-07 0.0538   4.81161E-08 0.1796
    6.0000E-01   3.96988E-06 0.0172   3.87255E-06 0.0185   1.76531E-06 0.0276   3.52082E-07 0.0607   3.24683E-08 0.1886
    8.0000E-01   6.82372E-06 0.0160   6.95938E-06 0.0161   3.03075E-06 0.0240   6.29449E-07 0.0534   6.63434E-08 0.2152
    9.0000E-01   3.19469E-06 0.0269   3.24112E-06 0.0265   1.42613E-06 0.0411   2.95588E-07 0.0890   2.83420E-08 0.2422
    1.0000E+00   3.16920E-06 0.0301   3.14138E-06 0.0307   1.50836E-06 0.0441   2.56611E-07 0.1045   1.80018E-08 0.3339
    1.1000E+00   3.12195E-06 0.0349   3.16668E-06 0.0348   1.49354E-06 0.0534   2.82633E-07 0.1154   2.72930E-08 0.3641
    1.2000E+00   3.02732E-06 0.0394   3.30798E-06 0.0378   1.34892E-06 0.0590   2.41872E-07 0.1440   1.54345E-08 0.4316
    1.3000E+00   3.16466E-06 0.0425   3.23405E-06 0.0433   1.50765E-06 0.0633   2.61818E-07 0.1376   1.79655E-08 0.4271
    1.4000E+00   5.69293E-05 0.0019   5.76490E-05 0.0020   2.54766E-05 0.0031   4.92490E-06 0.0075   4.12057E-07 0.0249
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.11386E-04 0.0050   1.12590E-04 0.0043   5.03246E-05 0.0090   9.66008E-06 0.0153   8.66771E-07 0.0524
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   8.62943E-10 0.6857   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.18710E-05 0.0247
    2.0000E-01   6.11407E-10 0.3859   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.87933E-05 0.0100
    3.0000E-01   6.36403E-10 0.4311   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.83387E-05 0.0219
    4.0000E-01   6.44411E-10 0.4758   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.37573E-05 0.0088
    5.0000E-01   3.45521E-09 0.6654   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.32333E-05 0.0093
    6.0000E-01   1.73479E-10 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.20301E-05 0.0101
    8.0000E-01   1.65654E-09 0.5927   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.16202E-05 0.0279
    9.0000E-01   2.13393E-09 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.87509E-06 0.0153
    1.0000E+00   1.42811E-09 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.77253E-06 0.0173
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.82089E-06 0.0200
    1.2000E+00   2.24034E-09 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.59086E-06 0.0220
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.81833E-06 0.0245
    1.4000E+00   1.72673E-08 0.1000   3.45345E-10 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.75506E-04 0.0008
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      3.11100E-08 0.1784   3.45345E-10 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   3.44027E-04 0.0031
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   1.01651E-09 0.7236   3.45028E-08 0.5907   1.41437E-07 0.5107
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   6.97067E-11 0.7071   2.08868E-09 0.4400   6.43181E-08 0.3349
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.09928E-10 0.4284   3.17299E-08 0.4436
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   1.19645E-08 1.0000   3.14828E-09 0.9289   8.25051E-09 0.4905
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.73424E-10 1.0000   3.26619E-09 0.7427
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.48742E-09 0.3215   1.63114E-08 0.1600
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.03874E-09 0.5528
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.47636E-11 1.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   6.90691E-10 0.5000   1.46772E-08 0.1085   3.87650E-07 0.0211   4.65025E-06 0.0060   2.45271E-05 0.0025
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      6.90691E-10 0.5000   1.46772E-08 0.1085   4.00701E-07 0.0366   4.69356E-06 0.0074   2.47935E-05 0.0040
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   2.43575E-07 0.2008   3.41666E-07 0.2543   9.24444E-08 0.1879   5.35079E-08 0.4808   1.82773E-09 0.5454
    2.0000E-01   1.90518E-07 0.2450   1.79367E-07 0.1902   1.03420E-07 0.4363   1.81229E-08 0.4313   2.43452E-09 0.9618
    3.0000E-01   8.35786E-08 0.3221   6.48166E-08 0.4775   2.63924E-08 0.4290   1.70951E-08 0.7705   0.00000E+00 0.0000
    4.0000E-01   5.87054E-08 0.3781   2.75447E-08 0.3524   6.41613E-09 0.4133   5.65082E-10 0.6807   0.00000E+00 0.0000
    5.0000E-01   1.33510E-08 0.7435   4.12339E-09 0.4417   2.53833E-08 0.8783   4.96170E-10 0.6563   0.00000E+00 0.0000
    6.0000E-01   5.42919E-08 0.1581   5.72082E-08 0.2151   1.62632E-08 0.2083   7.04078E-09 0.2709   1.29683E-09 0.9040
    8.0000E-01   2.69742E-09 0.4690   1.79647E-08 0.8681   1.35590E-09 0.6941   7.08064E-10 0.7993   0.00000E+00 0.0000
    9.0000E-01   2.60168E-10 1.0000   3.73906E-10 0.9127   5.05640E-11 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   3.44549E-11 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   7.43651E-11 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   5.62089E-05 0.0014   5.65771E-05 0.0014   2.50574E-05 0.0024   4.82862E-06 0.0059   4.02673E-07 0.0207
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      5.68560E-05 0.0020   5.72702E-05 0.0023   2.53291E-05 0.0032   4.92615E-06 0.0085   4.08232E-07 0.0218
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.09977E-07 0.1413
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.60339E-07 0.1372
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.24422E-07 0.2082
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.16595E-07 0.2368
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.68935E-08 0.5245
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.54900E-07 0.1019
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.37648E-08 0.6604
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.84638E-10 0.6311
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.92184E-11 0.7071
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.43651E-11 1.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   1.72673E-08 0.1000   3.45345E-10 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.72673E-04 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.72673E-08 0.1000   3.45345E-10 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   1.74710E-04 0.0009
 
 detector score diagnostics                  cumulative          tally         cumulative
                                             fraction of         per           fraction of
   times average score     transmissions     transmissions       history       total tally
        1.00000E-01             246896         0.15024        8.50887E-06        0.02473
        1.00000E+00            1288390         0.93425        2.06831E-04        0.62594
        2.00000E+00              48690         0.96388        2.37142E-05        0.69487
        5.00000E+00              37956         0.98698        4.05143E-05        0.81264
        1.00000E+01              13323         0.99509        3.15097E-05        0.90423
        1.00000E+02               5520         0.99845        3.05387E-05        0.99299
        1.00000E+03                 20         0.99846        1.51610E-06        0.99740
        1.00000E+38                  1         0.99846        5.68887E-07        0.99905
 before dd roulette               2533         1.00000        3.25266E-07        1.00000

 average tally per history = 3.44027E-04            largest score = 5.68887E-01
 (largest score)/(average tally) = 1.65361E+03      nps of largest score =       79378

 score contributions by cell
        cell      misses        hits    tally per history    weight per hit
     1     1           0     1000000       1.72673E-04         1.72673E-04
     2     2      976331      643329       1.71355E-04         2.66356E-04
       total      976331     1643329       3.44027E-04         2.09348E-04

 score misses
   russian roulette on pd                        0
   psc=0.                                        0
   russian roulette in transmission         936874
   underflow in transmission                 39457
   hit a zero-importance cell                    0
   energy cutoff                                 0


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        5

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.09      yes         yes            constant    random       2.18
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes          no

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        5 with nps =     1000000  print table 160


 normed average tally per history  = 3.44027E-04          unnormed average tally per history  = 3.44027E-04
 estimated tally relative error    = 0.0031               estimated variance of the variance  = 0.0912
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0031

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       79378          largest  unnormalized history tally = 5.73849E-01
 (largest  tally)/(average tally)  = 1.66803E+03          (largest  tally)/(avg nonzero tally)= 1.66803E+03

 (confidence interval shift)/mean  = 0.0003               shifted confidence interval center  = 3.44133E-04


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            3.44027E-04             3.44601E-04                     0.001667
      relative error                  3.11921E-03             3.53084E-03                     0.131966
      variance of the variance        9.11655E-02             1.04515E-01                     0.146435
      shifted center                  3.44133E-04             3.44173E-04                     0.000117
      figure of merit                 2.58523E+05             2.01759E+05                    -0.219572

 the estimated inverse power slope of the 200 largest  tallies starting at 1.49554E-02 is 2.1802
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.515E+06)*( 3.206E-01)**2 = (2.515E+06)*(1.028E-01) = 2.585E+05

1unnormed tally density for tally        5          nonzero tally mean(m) = 3.440E-04   nps =     1000000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 2.2)
  tally  number num den log den:d---------d---------d----------d---------d----------d----------d---------d----------d---------d-----
 2.00-04 681617 1.66+04   4.220 **********|*********|**********|*********|**********|**********|*********|**********|*********|*****
 2.51-04 146465 2.84+03   3.453 **********|*********|**********|*********|**********|**********|*********|**********|*******  |     
 3.16-04  39674 6.10+02   2.785 **********|*********|**********|*********|**********|**********|*********|**********|         |     
 3.98-04  24765 3.02+02   2.481 mmmmmmmmmm|mmmmmmmmm|mmmmmmmmmm|mmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmm|mmmmmmmm  |         |     
 5.01-04  18799 1.82+02   2.261 **********|*********|**********|*********|**********|**********|*********|*****     |         |     
 6.31-04  15345 1.18+02   2.073 **********|*********|**********|*********|**********|**********|*********|***       |         |     
 7.94-04  12857 7.87+01   1.896 **********|*********|**********|*********|**********|**********|*********|*         |         |     
 1.00-03  11079 5.39+01   1.731 **********|*********|**********|*********|**********|**********|*********|          |         |     
 1.26-03   9510 3.67+01   1.565 **********|*********|**********|*********|**********|**********|******** |          |         |     
 1.58-03   8411 2.58+01   1.412 **********|*********|**********|*********|**********|**********|******   |          |         |     
 2.00-03   7094 1.73+01   1.238 **********|*********|**********|*********|**********|**********|****     |          |         |     
 2.51-03   6242 1.21+01   1.082 **********|*********|**********|*********|**********|**********|***      |          |         |     
 3.16-03   5039 7.75+00   0.889 **********|*********|**********|*********|**********|**********|*        |          |         |     
 3.98-03   4141 5.06+00   0.704 **********|*********|**********|*********|**********|**********|         |          |         |     
 5.01-03   3208 3.11+00   0.493 **********|*********|**********|*********|**********|*******   |         |          |         |     
 6.31-03   2367 1.82+00   0.261 **********|*********|**********|*********|**********|*****     |         |          |         |     
 7.94-03   1547 9.47-01  -0.024 **********|*********|**********|*********|**********|**        |         |          |         |     
 1.00-02    941 4.58-01  -0.340 **********|*********|**********|*********|**********|          |         |          |         |     
 1.26-02    501 1.93-01  -0.713 **********|*********|**********|*********|******    |          |         |          |         |     
 1.58-02    238 7.30-02  -1.137 **********|*********|**********|*********|*        s|          |         |          |         |     
 2.00-02     82 2.00-02  -1.699 **********|*********|**********|*****    |       s  |          |         |          |         |     
 2.51-02     25 4.84-03  -2.315 **********|*********|**********|         |     s    |          |         |          |         |     
 3.16-02     19 2.92-03  -2.534 **********|*********|*******   |         |   s      |          |         |          |         |     
 3.98-02     13 1.59-03  -2.799 **********|*********|*****     |         | s        |          |         |          |         |     
 5.01-02      8 7.76-04  -3.110 **********|*********|*         |         s          |          |         |          |         |     
 6.31-02      4 3.08-04  -3.511 **********|*******  |          |       s |          |          |         |          |         |     
 7.94-02      3 1.84-04  -3.736 **********|*****    |          |     s   |          |          |         |          |         |     
 1.00-01      1 4.86-05  -4.313 ********* |         |          |   s     |          |          |         |          |         |     
 1.26-01      1 3.86-05  -4.413 ********  |         |          | s       |          |          |         |          |         |     
 1.58-01      0 0.00+00   0.000           |         |         s|         |          |          |         |          |         |     
 2.00-01      1 2.44-05  -4.613 ******    |         |       s  |         |          |          |         |          |         |     
 2.51-01      1 1.94-05  -4.713 *****     |         |     s    |         |          |          |         |          |         |     
 3.16-01      1 1.54-05  -4.813 ****      |         |   s      |         |          |          |         |          |         |     
 3.98-01      0 0.00+00   0.000           |         |s         |         |          |          |         |          |         |     
 5.01-01      0 0.00+00   0.000           |        s|          |         |          |          |         |          |         |     
 6.31-01      1 7.71-06  -5.113 *         |      s  |          |         |          |          |         |          |         |     
  total 1000000 1.00+00         d---------d---------d----------d---------d----------d----------d---------d----------d---------d-----

1tally        6        nps =     1000000
           tally type 6    track length estimate of heating.            units   mev/gram       
           particle(s): photons  

           masses  
                   cell:       2                                                                                   
                         9.89602E+03
 
 cell  2                                                                                                                               
         time:       1.0000E+00           5.0000E+00           1.0000E+01           1.5000E+01           2.0000E+01
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.01440E-10 0.4137   1.02678E-09 0.0965   1.54123E-08 0.0266   7.98293E-08 0.0116
    2.0000E-01   2.49434E-12 1.0000   8.90075E-11 0.2821   2.37397E-09 0.0617   2.73686E-08 0.0177   1.43941E-07 0.0077
    3.0000E-01   0.00000E+00 0.0000   1.35948E-10 0.3148   3.02924E-09 0.0631   3.54620E-08 0.0187   1.80876E-07 0.0081
    4.0000E-01   0.00000E+00 0.0000   7.33944E-11 0.3625   1.89874E-09 0.0877   2.52762E-08 0.0238   1.33940E-07 0.0103
    5.0000E-01   0.00000E+00 0.0000   6.74604E-11 0.5304   1.52528E-09 0.0984   1.94843E-08 0.0279   9.99952E-08 0.0123
    6.0000E-01   0.00000E+00 0.0000   4.50613E-11 0.5269   1.73089E-09 0.1002   1.75175E-08 0.0312   9.31793E-08 0.0135
    8.0000E-01   4.80251E-12 0.7128   1.68160E-10 0.3532   3.08618E-09 0.0814   3.41610E-08 0.0239   1.73424E-07 0.0105
    9.0000E-01   2.62604E-11 1.0000   7.15431E-11 0.5808   1.38095E-09 0.1269   1.65283E-08 0.0359   9.01381E-08 0.0155
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   1.40311E-09 0.1344   1.83240E-08 0.0355   9.35380E-08 0.0156
    1.1000E+00   0.00000E+00 0.0000   6.10533E-11 0.6661   1.46580E-09 0.1314   1.81404E-08 0.0371   9.85155E-08 0.0158
    1.2000E+00   2.76532E-11 1.0000   4.91419E-11 0.6488   1.79972E-09 0.1227   2.04077E-08 0.0360   1.03443E-07 0.0160
    1.3000E+00   0.00000E+00 0.0000   1.66002E-11 0.9130   1.78740E-09 0.1233   1.97873E-08 0.0368   1.08062E-07 0.0159
    1.4000E+00   1.28227E-10 0.5457   2.72969E-09 0.1220   7.48200E-08 0.0233   9.01351E-07 0.0066   4.74777E-06 0.0028
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.89438E-10 0.4588   3.60850E-09 0.1103   9.73281E-08 0.0213   1.16922E-06 0.0061   6.14665E-06 0.0025
 
         time:       2.5000E+01           3.0000E+01           3.5000E+01           4.0000E+01           4.5000E+01
      energy   
    1.0000E-01   1.81941E-07 0.0077   1.84377E-07 0.0076   8.00843E-08 0.0115   1.61755E-08 0.0258   1.10074E-09 0.0995
    2.0000E-01   3.30598E-07 0.0050   3.35806E-07 0.0050   1.46854E-07 0.0077   2.86479E-08 0.0173   2.15739E-09 0.0611
    3.0000E-01   4.18122E-07 0.0053   4.20053E-07 0.0053   1.83316E-07 0.0081   3.69973E-08 0.0184   3.00035E-09 0.0643
    4.0000E-01   3.03186E-07 0.0068   3.04824E-07 0.0068   1.31003E-07 0.0104   2.55795E-08 0.0235   1.89096E-09 0.0877
    5.0000E-01   2.35923E-07 0.0080   2.33361E-07 0.0080   1.02285E-07 0.0121   1.96074E-08 0.0278   1.63693E-09 0.0965
    6.0000E-01   2.08781E-07 0.0090   2.12639E-07 0.0089   9.37505E-08 0.0135   1.82311E-08 0.0309   1.58923E-09 0.1014
    8.0000E-01   3.93727E-07 0.0070   3.92198E-07 0.0070   1.74700E-07 0.0105   3.29201E-08 0.0242   2.81643E-09 0.0824
    9.0000E-01   2.05132E-07 0.0102   2.05126E-07 0.0102   9.00578E-08 0.0155   1.76014E-08 0.0350   1.15686E-09 0.1312
    1.0000E+00   2.11793E-07 0.0104   2.13689E-07 0.0103   9.19436E-08 0.0159   1.83096E-08 0.0354   1.40779E-09 0.1297
    1.1000E+00   2.25825E-07 0.0104   2.26436E-07 0.0104   9.82826E-08 0.0159   1.92285E-08 0.0356   1.66959E-09 0.1253
    1.2000E+00   2.36091E-07 0.0105   2.33903E-07 0.0106   1.03123E-07 0.0159   2.04402E-08 0.0360   1.40083E-09 0.1353
    1.3000E+00   2.54527E-07 0.0104   2.53708E-07 0.0104   1.08509E-07 0.0159   2.17517E-08 0.0357   1.88626E-09 0.1240
    1.4000E+00   1.08334E-05 0.0017   1.08688E-05 0.0017   4.80860E-06 0.0027   9.16312E-07 0.0066   7.76309E-08 0.0230
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      1.40391E-05 0.0015   1.40850E-05 0.0015   6.21251E-06 0.0025   1.19180E-06 0.0060   9.93443E-08 0.0211
 
         time:       5.0000E+01           6.0000E+01           1.0000E+02           1.0000E+03             total   
      energy   
    1.0000E-01   6.34113E-11 0.4402   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.60112E-07 0.0043
    2.0000E-01   7.10534E-11 0.3253   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.01791E-06 0.0028
    3.0000E-01   1.08352E-10 0.2995   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.28110E-06 0.0029
    4.0000E-01   7.76238E-11 0.4492   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.27749E-07 0.0038
    5.0000E-01   1.78720E-11 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.13903E-07 0.0045
    6.0000E-01   7.50974E-11 0.4714   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.47539E-07 0.0050
    8.0000E-01   1.54706E-10 0.3719   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.20736E-06 0.0039
    9.0000E-01   1.09138E-10 0.4711   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.27328E-07 0.0058
    1.0000E+00   6.15350E-11 0.6139   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.50469E-07 0.0059
    1.1000E+00   3.35789E-11 0.7487   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.89658E-07 0.0059
    1.2000E+00   8.85122E-11 0.6015   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.20776E-07 0.0060
    1.3000E+00   9.13922E-11 0.6120   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.70126E-07 0.0059
    1.4000E+00   3.18823E-09 0.1123   9.23432E-11 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   3.32349E-05 0.0005
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      4.14050E-09 0.1026   9.23432E-11 0.7071   0.00000E+00 0.0000   0.00000E+00 0.0000   4.30489E-05 0.0002


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        6

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.3041E-05 to 4.3057E-05; 4.3033E-05 to 4.3065E-05; 4.3025E-05 to 4.3073E-05
 estimated  symmetric confidence interval(1,2,3 sigma): 4.3041E-05 to 4.3057E-05; 4.3033E-05 to 4.3065E-05; 4.3025E-05 to 4.3073E-05

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        6 with nps =     1000000  print table 160


 normed average tally per history  = 4.30489E-05          unnormed average tally per history  = 4.26013E-01
 estimated tally relative error    = 0.0002               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0002

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      618168          largest  unnormalized history tally = 1.31214E+00
 (largest  tally)/(average tally)  = 3.08006E+00          (largest  tally)/(avg nonzero tally)= 3.08006E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.30489E-05


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.30489E-05             4.30490E-05                     0.000002
      relative error                  1.82817E-04             1.82829E-04                     0.000062
      variance of the variance        6.65852E-06             6.67335E-06                     0.002227
      shifted center                  4.30489E-05             4.30489E-05                     0.000000
      figure of merit                 7.52584E+07             7.52491E+07                    -0.000123

 the estimated slope of the 200 largest  tallies starting at  8.49792E-01 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.515E+06)*( 5.470E+00)**2 = (2.515E+06)*(2.992E+01) = 7.526E+07

1tally        8        nps =     1000000
           tally type 8    pulse height distribution.                   units   number         
           particle(s): photons  
 
 cell  2                                                                                                                               
      energy   
    1.0000E-01   5.16116E-01 0.0010
    2.0000E-01   2.64600E-02 0.0061
    3.0000E-01   2.62280E-02 0.0061
    4.0000E-01   2.64080E-02 0.0061
    5.0000E-01   2.64270E-02 0.0061
    6.0000E-01   2.66330E-02 0.0060
    8.0000E-01   5.73380E-02 0.0041
    9.0000E-01   3.17670E-02 0.0055
    1.0000E+00   3.34870E-02 0.0054
    1.1000E+00   3.81850E-02 0.0050
    1.2000E+00   6.26270E-02 0.0039
    1.3000E+00   5.16650E-02 0.0043
    1.4000E+00   7.66590E-02 0.0035
    1.5000E+00   0.00000E+00 0.0000
      total      1.00000E+00 0.0000


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        8

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed    constant       0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.0000E+00 to 1.0000E+00; 1.0000E+00 to 1.0000E+00; 1.0000E+00 to 1.0000E+00
 estimated  symmetric confidence interval(1,2,3 sigma): 1.0000E+00 to 1.0000E+00; 1.0000E+00 to 1.0000E+00; 1.0000E+00 to 1.0000E+00

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        8 with nps =     1000000  print table 160


 normed average tally per history  = 1.00000E+00          unnormed average tally per history  = 1.00000E+00
 estimated tally relative error    = 0.0000               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0000

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =           1          largest  unnormalized history tally = 1.00000E+00
 (largest  tally)/(average tally)  = 1.00000E+00          (largest  tally)/(avg nonzero tally)= 1.00000E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.00000E+00


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.00000E+00             1.00000E+00                     0.000000
      relative error                  0.00000E+00             0.00000E+00                     0.000000
      variance of the variance        0.00000E+00             0.00000E+00                     0.000000
      shifted center                  1.00000E+00             1.00000E+00                     0.000000
      figure of merit                 1.00000E+30             1.00000E+30                     0.000000

 the 100 largest  history tallies appear to have a  maximum value of about 1.00000E+00
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 2.515E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   225 tally bins had   144 bins with zeros and    36 bins with relative errors exceeding 0.10

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   225 tally bins had   144 bins with zeros and    37 bins with relative errors exceeding 0.10

        4   missed  1 of 10 tfc bin checks: the estimated mean has a trend during the last half of the problem                        
         missed all bin error check:   225 tally bins had    64 bins with zeros and    47 bins with relative errors exceeding 0.10

        5   missed  1 of 10 tfc bin checks: the slope of decrease of largest tallies is less than the minimum acceptable value of 3.0 
         missed all bin error check:   450 tally bins had   204 bins with zeros and   162 bins with relative errors exceeding 0.05

        6   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   225 tally bins had    64 bins with zeros and    47 bins with relative errors exceeding 0.10

        8   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    15 tally bins had     1 bins with zeros and     0 bins with relative errors exceeding 0.10


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       2 of the     6 tally fluctuation chart bins did not pass all 10 statistical checks.
 warning.       5 of the     6 tallies had bins with relative errors greater than recommended.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   1.1618E+00 0.0023 0.0005  4.2 7205741   4.2833E-03 0.0057 0.0036  3.2 1129057   1.9070E-03 0.0023 0.0002 10.0 7028397
       128000   1.1603E+00 0.0016 0.0003  4.1 7619342   4.2761E-03 0.0041 0.0018 10.0 1161395   1.9040E-03 0.0016 0.0001 10.0 7387600
       192000   1.1616E+00 0.0013 0.0002  4.9 7541666   4.2962E-03 0.0034 0.0013 10.0 1100056   1.9048E-03 0.0013 0.0001 10.0 7415345
       256000   1.1618E+00 0.0011 0.0001  5.1 7599351   4.2916E-03 0.0029 0.0010 10.0 1132124   1.9059E-03 0.0011 0.0000 10.0 7471458
       320000   1.1637E+00 0.0010 0.0001  4.1 7544842   4.3090E-03 0.0027 0.0008 10.0 1114306   1.9081E-03 0.0010 0.0000 10.0 7467755
       384000   1.1638E+00 0.0009 0.0001  4.7 7360665   4.3131E-03 0.0024 0.0007 10.0 1071536   1.9080E-03 0.0009 0.0000  9.5 7270090
       448000   1.1638E+00 0.0009 0.0001  4.2 7407757   4.3155E-03 0.0023 0.0006  4.1 1077341   1.9082E-03 0.0009 0.0000 10.0 7360686
       512000   1.1636E+00 0.0008 0.0001 10.0 7401227   4.3131E-03 0.0021 0.0005  5.3 1084373   1.9086E-03 0.0008 0.0000 10.0 7346246
       576000   1.1633E+00 0.0008 0.0001 10.0 7428312   4.3124E-03 0.0020 0.0004  5.6 1084290   1.9081E-03 0.0008 0.0000 10.0 7364107
       640000   1.1631E+00 0.0007 0.0001 10.0 7467512   4.3132E-03 0.0019 0.0004  5.7 1086949   1.9084E-03 0.0007 0.0000 10.0 7395115
       704000   1.1634E+00 0.0007 0.0000 10.0 7519860   4.3118E-03 0.0018 0.0003  6.0 1101874   1.9086E-03 0.0007 0.0000 10.0 7451788
       768000   1.1633E+00 0.0007 0.0000 10.0 7571403   4.3109E-03 0.0017 0.0003  7.3 1108556   1.9087E-03 0.0007 0.0000 10.0 7485233
       832000   1.1634E+00 0.0006 0.0000 10.0 7554062   4.3117E-03 0.0017 0.0003  6.9 1106053   1.9092E-03 0.0006 0.0000 10.0 7462814
       896000   1.1633E+00 0.0006 0.0000 10.0 7549360   4.3100E-03 0.0016 0.0003  5.6 1106244   1.9092E-03 0.0006 0.0000 10.0 7462805
       960000   1.1633E+00 0.0006 0.0000 10.0 7550618   4.3104E-03 0.0015 0.0003  4.9 1101912   1.9094E-03 0.0006 0.0000 10.0 7451978
      1000000   1.1633E+00 0.0006 0.0000 10.0 7568064   4.3104E-03 0.0015 0.0002  4.5 1103900   1.9097E-03 0.0006 0.0000 10.0 7467343
 

                            tally        5                          tally        6                          tally        8
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   3.3967E-04 0.0091 0.0076  4.7  444036   4.3069E-05 0.0007 0.0001 10.0 7.1E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       128000   3.4847E-04 0.0151 0.5389  2.6   85715   4.3076E-05 0.0005 0.0001 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       192000   3.4647E-04 0.0106 0.4472  2.6  115867   4.3055E-05 0.0004 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       256000   3.4604E-04 0.0083 0.3737  2.6  141346   4.3042E-05 0.0004 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       320000   3.4612E-04 0.0069 0.3225  2.4  164516   4.3036E-05 0.0003 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       384000   3.4555E-04 0.0060 0.2722  2.5  175886   4.3040E-05 0.0003 0.0000 10.0 7.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       448000   3.4517E-04 0.0053 0.2393  2.5  194220   4.3040E-05 0.0003 0.0000 10.0 7.4E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       512000   3.4463E-04 0.0048 0.2159  2.4  209757   4.3045E-05 0.0003 0.0000 10.0 7.4E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       576000   3.4427E-04 0.0044 0.1942  2.3  223915   4.3051E-05 0.0002 0.0000 10.0 7.4E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       640000   3.4401E-04 0.0040 0.1776  2.3  238837   4.3056E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       704000   3.4461E-04 0.0040 0.1296  2.1  217342   4.3054E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       768000   3.4409E-04 0.0038 0.1207  2.0  228971   4.3051E-05 0.0002 0.0000 10.0 7.6E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       832000   3.4381E-04 0.0036 0.1126  2.1  238577   4.3053E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       896000   3.4397E-04 0.0034 0.1042  2.2  247296   4.3053E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       960000   3.4409E-04 0.0032 0.0954  2.2  253360   4.3050E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
      1000000   3.4403E-04 0.0031 0.0912  2.2  258523   4.3049E-05 0.0002 0.0000 10.0 7.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30

 ***********************************************************************************************************************

 dump no.    2 on file singles_et.ir     nps =     1000000     coll =        1690149     ctm =        0.40   nrn =      
    35178899

        14 warning messages so far.


 run terminated when     1000000  particle histories were done.

 computer time =    0.56 minutes

 mcnp     version 6.mpi 01/13/25                     07/24/25 09:38:54                     probid =  07/24/25 09:38:50 
