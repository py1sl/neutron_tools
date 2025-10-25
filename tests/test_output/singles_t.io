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
  
1mcnp     version 6.mpi ld=01/13/25                     07/24/25 09:39:23 
 *************************************************************************                 probid =  07/24/25 09:39:23 
 n=singles_t.i XSDIR=/home/vol03/scarf473/neutronic_data1/mcnpx_data/xsdir       

 
  warning.  Physics models disabled.
         1-       c test input to generate output for MCNP output reader                          
         2-       1 0 -1 imp:p=1                                                                  
         3-       2 1 -11.7 1 -2 imp:p=1                                                          
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
        14-       nps 2e5                                                                         
        15-       m1 13027.24c 1  $ Al27                                                          
  warning.  neutron table inconsistent with mode will be ignored.
        16-       sdef erg=1.332 par=p                                                            
        17-       f1:p 2                                                                          
        18-       t1 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        19-       f2:p 2                                                                          
        20-       t2 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        21-       f4:p 2                                                                          
        22-       t4 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        23-       f5:p 15 0 0 1                                                                   
        24-       t5 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        25-       f6:p 2                                                                          
        26-       t6 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        27-                                                                                       
 
  warning.  last time bin of tally        1 is less than time cutoff.
 
  warning.  last time bin of tally        2 is less than time cutoff.
 
  warning.  last time bin of tally        4 is less than time cutoff.
 
  warning.  last time bin of tally        5 is less than time cutoff.
 
  warning.  last time bin of tally        6 is less than time cutoff.
1cells                                                                                                  print table 60

                               atom        gram                                            photon                                      
              cell      mat   density     density     volume       mass            pieces importance                                   

        1        1        0  0.00000E+00 0.00000E+00 5.23599E+02 0.00000E+00           1  1.0000E+00                                   
        2        2        1  2.61134E-01 1.17000E+01 3.66519E+03 4.28827E+04           1  1.0000E+00                                   
        3        3        0  0.00000E+00 0.00000E+00 2.93215E+04 0.00000E+00           1  1.0000E+00                                   
        4       99        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00                                   

 total                                               3.35103E+04 4.28827E+04

    minimum source weight = 1.0000E+00    maximum source weight = 1.0000E+00

 ***************************************************
 * Random Number Generator  =                    1 *
 * Random Number Seed       =       19073486328125 *
 * Random Number Multiplier =       19073486328125 *
 * Random Number Adder      =                    0 *
 * Random Number Bits Used  =                   48 *
 * Random Number Stride     =               152917 *
 ***************************************************


         7 warning messages so far.
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

 dump no.    1 on file singles_t.ir     nps =           0     coll =              0     ctm =        0.00   nrn =       
          0

         8 warning messages so far.
 master starting      11 MPI slave tasks with       1 threads each  07/24/25 09:39:23 
 master set rendezvous nps =        1000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        2000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        3000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        4000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        5000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        6000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        7000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        8000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =        9000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       10000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       11000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       12000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       13000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       14000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       15000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       16000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       17000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       18000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       19000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       20000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       22000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       24000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       26000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       28000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       30000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       32000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       34000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       36000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       38000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       40000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       44000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       48000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       52000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       56000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       60000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       64000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       68000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       72000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       76000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       80000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       88000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =       96000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      104000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      112000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      120000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      128000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      136000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      144000,  work chunks =    11    07/24/25 09:39:23 
 master set rendezvous nps =      152000,  work chunks =    11    07/24/25 09:39:24 
 master set rendezvous nps =      160000,  work chunks =    11    07/24/25 09:39:24 
 master set rendezvous nps =      176000,  work chunks =    11    07/24/25 09:39:24 
 master set rendezvous nps =      192000,  work chunks =    11    07/24/25 09:39:24 
 master set rendezvous nps =      200000,  work chunks =    11    07/24/25 09:39:24 
1problem summary                                                                                                           

      run terminated when      200000  particle histories were done.
+                                                                                                    07/24/25 09:39:24 
      c test input to generate output for MCNP output reader                               probid =  07/24/25 09:39:23 

 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source              200000    1.0000E+00    1.3320E+00          escape               48931    2.4466E-01    1.7208E-01
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            4.9909E-05
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 from neutrons            0    0.            0.                  compton scatter          0    0.            1.1011E+00
 bremsstrahlung       38392    1.9196E-01    5.8819E-03          capture             196050    9.8025E-01    6.4303E-02
 p-annihilation         550    2.7500E-03    1.4053E-03          pair production        275    1.3750E-03    1.8293E-03
 photonuclear             0    0.            0.                  photonuclear abs         0    0.            0.        
 electron x-rays          0    0.            0.                  loss to photofis         0    0.            0.        
 compton fluores          0    0.            0.                                                                        
 muon capt fluores        0    0.            0.                                                                        
 1st fluorescence      6314    3.1570E-02    4.6391E-05                                                                
 2nd fluorescence         0    0.            0.                                                                        
 cerenkov                 0    0.            0.                                                                        
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total           245256    1.2263E+00    1.3393E+00              total           245256    1.2263E+00    1.3393E+00

   number of photons banked                    38942        average time of (shakes)              cutoffs
   photon tracks per source particle      1.2263E+00          escape            7.3426E-02          tco   1.0000E+33
   photon collisions per source particle  8.4714E+00          capture           3.8548E-02          eco   1.0000E-03
   total photon collisions                   1694278          capture or escape 4.5515E-02          wc1  -5.0000E-01
                                                              any termination   4.5487E-02          wc2  -2.5000E-01

 computer time so far in this run     0.21 minutes            maximum number ever in bank         3
 computer time in mcrun               0.13 minutes            bank overflows to backup file       0
 source particles per minute            1.4883E+06
 random numbers generated                 29160728            most random numbers used was         558 in history       86713

 range of sampled source weights = 1.0000E+00 to 1.0000E+00

 estimated system efficiency for MPI usage = 10%

 number of histories processed by each MPI task
           0       18145       18187       18175       18198       18185       18167       18185       18198       18175
       18187       18198
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1      241777       200350            0    0.0000E+00   1.0816E+00   1.0816E+00   1.0000E+00   0.0000E+00
        2        2      241777       238942      1694278    8.4714E+00   5.8294E-01   5.8294E-01   1.0000E+00   9.8172E-01
        3        3       48931        48931            0    0.0000E+00   6.7301E-01   6.7301E-01   1.0000E+00   0.0000E+00

           total        532485       488223      1694278    8.4714E+00

1tally        1        nps =      200000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  2                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   2.44655E-01 0.0039   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.44655E-01 0.0039


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            decrease    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes                no        yes         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        1 with nps =      200000  print table 160


 normed average tally per history  = 2.44655E-01          unnormed average tally per history  = 2.44655E-01
 estimated tally relative error    = 0.0039               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0039               relative error from nonzero scores  = 0.0003

 number of nonzero history tallies =       48748          efficiency for the nonzero tallies  = 0.2437
 history number of largest  tally  =        2655          largest  unnormalized history tally = 2.00000E+00
 (largest  tally)/(average tally)  = 8.17478E+00          (largest  tally)/(avg nonzero tally)= 1.99252E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.44656E-01


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            2.44655E-01             2.44664E-01                     0.000036
      relative error                  3.94839E-03             3.94839E-03                     0.000000
      variance of the variance        7.98316E-06             7.98735E-06                     0.000526
      shifted center                  2.44656E-01             2.44656E-01                     0.000000
      figure of merit                 4.77345E+05             4.77345E+05                    -0.000001

 the 100 largest  history tallies appear to have a  maximum value of about 2.00000E+00
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.488E+06)*( 5.663E-01)**2 = (1.488E+06)*(3.207E-01) = 4.773E+05

1unnormed tally density for tally        1          nonzero tally mean(m) = 1.004E+00   nps =      200000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope=10.0)
  tally  number num den log den:d----------------------------------d------------------------------------d---------------------------
 1.26+00  48565 9.38-01  -0.028 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmmmmmmmmmmm
 1.58+00      0 0.00+00   0.000                                    |                                    |                           
 2.00+00      0 0.00+00   0.000                                    |                                    |                           
 2.51+00    183 1.77-03  -2.752 *                                  |                                    |                           
  total   48748 2.44-01         d----------------------------------d------------------------------------d---------------------------

1tally        2        nps =      200000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): photons  

           areas   
                surface:       2                                                                                   
                         1.25664E+03
 
 surface  2                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   2.69842E-04 0.0054   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.69842E-04 0.0054


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.01      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 2.6840E-04 to 2.7131E-04; 2.6694E-04 to 2.7277E-04; 2.6548E-04 to 2.7423E-04
 estimated  symmetric confidence interval(1,2,3 sigma): 2.6838E-04 to 2.7130E-04; 2.6693E-04 to 2.7276E-04; 2.6547E-04 to 2.7421E-04

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        2 with nps =      200000  print table 160


 normed average tally per history  = 2.69842E-04          unnormed average tally per history  = 3.39094E-01
 estimated tally relative error    = 0.0054               estimated variance of the variance  = 0.0010
 relative error from zero tallies  = 0.0039               relative error from nonzero scores  = 0.0037

 number of nonzero history tallies =       48748          efficiency for the nonzero tallies  = 0.2437
 history number of largest  tally  =      107876          largest  unnormalized history tally = 2.12773E+01
 (largest  tally)/(average tally)  = 6.27477E+01          (largest  tally)/(avg nonzero tally)= 1.52941E+01

 (confidence interval shift)/mean  = 0.0001               shifted confidence interval center  = 2.69857E-04


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            2.69842E-04             2.69925E-04                     0.000309
      relative error                  5.40121E-03             5.40833E-03                     0.001318
      variance of the variance        9.56311E-04             9.60642E-04                     0.004529
      shifted center                  2.69857E-04             2.69857E-04                     0.000000
      figure of merit                 2.55089E+05             2.54418E+05                    -0.002631

 the estimated slope of the 200 largest  tallies starting at  7.40410E+00 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.488E+06)*( 4.140E-01)**2 = (1.488E+06)*(1.714E-01) = 2.551E+05

1tally        4        nps =      200000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2                                                                                   
                         3.66519E+03
 
 cell  2                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   1.70643E-03 0.0008   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.70643E-03 0.0008


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        4

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.7051E-03 to 1.7078E-03; 1.7037E-03 to 1.7092E-03; 1.7023E-03 to 1.7106E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 1.7050E-03 to 1.7078E-03; 1.7037E-03 to 1.7092E-03; 1.7023E-03 to 1.7106E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =      200000  print table 160


 normed average tally per history  = 1.70643E-03          unnormed average tally per history  = 6.25440E+00
 estimated tally relative error    = 0.0008               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0008

 number of nonzero history tallies =      200000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       84052          largest  unnormalized history tally = 2.25250E+01
 (largest  tally)/(average tally)  = 3.60146E+00          (largest  tally)/(avg nonzero tally)= 3.60146E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.70643E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.70643E-03             1.70645E-03                     0.000013
      relative error                  8.09672E-04             8.09762E-04                     0.000111
      variance of the variance        1.56663E-05             1.57218E-05                     0.003538
      shifted center                  1.70643E-03             1.70643E-03                     0.000000
      figure of merit                 1.13516E+07             1.13490E+07                    -0.000222

 the estimated slope of the 198 largest  tallies starting at  1.59993E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.488E+06)*( 2.762E+00)**2 = (1.488E+06)*(7.627E+00) = 1.135E+07

1tally        5        nps =      200000
           tally type 5    particle flux at a point detector.           units   1/cm**2        
           particle(s): photons  
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   9.42466E-05 0.0149   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.42466E-05 0.0149
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   1.60865E-05 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.60865E-05 0.0050
 
 detector score diagnostics                  cumulative          tally         cumulative
                                             fraction of         per           fraction of
   times average score     transmissions     transmissions       history       total tally
        1.00000E-01              27948         0.09198        1.26067E-06        0.01338
        1.00000E+00             241588         0.88705        2.26327E-05        0.25352
        2.00000E+00               9064         0.91688        5.83520E-06        0.31543
        5.00000E+00               8861         0.94604        1.26423E-05        0.44957
        1.00000E+01               4161         0.95973        1.32605E-05        0.59027
        1.00000E+02               3646         0.97173        3.49893E-05        0.96153
        1.00000E+03                 40         0.97187        3.20459E-06        0.99553
        1.00000E+38                  0         0.97187        0.00000E+00        0.99553
 before dd roulette               8549         1.00000        4.21372E-07        1.00000

 average tally per history = 9.42466E-05            largest score = 7.52380E-02
 (largest score)/(average tally) = 7.98310E+02      nps of largest score =      192165

 score contributions by cell
        cell      misses        hits    tally per history    weight per hit
     1     1           0      200000       1.58226E-05         1.58226E-05
     2     2     1439077      103857       7.84241E-05         1.51023E-04
       total     1439077      303857       9.42466E-05         6.20335E-05

 score misses
   russian roulette on pd                        0
   psc=0.                                        0
   russian roulette in transmission        1402485
   underflow in transmission                 36592
   hit a zero-importance cell                    0
   energy cutoff                                 0


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        5

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.01      yes          yes            0.01      yes          no            constant    random       3.48
 passed?        yes          yes      yes          yes             yes      yes          no               yes        yes         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        5 with nps =      200000  print table 160


 normed average tally per history  = 9.42466E-05          unnormed average tally per history  = 9.42466E-05
 estimated tally relative error    = 0.0149               estimated variance of the variance  = 0.0095
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0149

 number of nonzero history tallies =      200000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      192165          largest  unnormalized history tally = 7.69594E-02
 (largest  tally)/(average tally)  = 8.16574E+02          (largest  tally)/(avg nonzero tally)= 8.16574E+02

 (confidence interval shift)/mean  = 0.0005               shifted confidence interval center  = 9.42913E-05


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            9.42466E-05             9.46310E-05                     0.004078
      relative error                  1.49095E-02             1.53942E-02                     0.032513
      variance of the variance        9.52792E-03             1.30910E-02                     0.373957
      shifted center                  9.42913E-05             9.43015E-05                     0.000109
      figure of merit                 3.34773E+04             3.14021E+04                    -0.061987

 the estimated inverse power slope of the 200 largest  tallies starting at 8.49254E-03 is 3.4764
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.488E+06)*( 1.500E-01)**2 = (1.488E+06)*(2.249E-02) = 3.348E+04

1unnormed tally density for tally        5          nonzero tally mean(m) = 9.425E-05   nps =      200000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 3.5)
  tally  number num den log den:d---------d----------d----------d----------d-----------d----------d----------d----------d----------d
 1.58-05 164849 2.53+05   5.403 **********|**********|**********|**********|***********|**********|**********|**********|**********|
 2.00-05    331 4.03+02   2.606 **********|**********|**********|**********|***********|**********|**        |          |          |
 2.51-05   6146 5.95+03   3.774 **********|**********|**********|**********|***********|**********|**********|****      |          |
 3.16-05   3319 2.55+03   3.407 **********|**********|**********|**********|***********|**********|**********|          |          |
 3.98-05   3291 2.01+03   3.303 **********|**********|**********|**********|***********|**********|**********|          |          |
 5.01-05   2235 1.08+03   3.035 **********|**********|**********|**********|***********|**********|*******   |          |          |
 6.31-05   1911 7.36+02   2.867 **********|**********|**********|**********|***********|**********|*****     |          |          |
 7.94-05   1728 5.29+02   2.723 **********|**********|**********|**********|***********|**********|***       |          |          |
 1.00-04   1588 3.86+02   2.587 mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmmm|mmmmmmmmmm|mm        |          |          |
 1.26-04   1448 2.80+02   2.447 **********|**********|**********|**********|***********|**********|          |          |          |
 1.58-04   1389 2.13+02   2.328 **********|**********|**********|**********|***********|**********|          |          |          |
 2.00-04   1347 1.64+02   2.215 **********|**********|**********|**********|***********|********* |          |          |          |
 2.51-04   1322 1.28+02   2.107 **********|**********|**********|**********|***********|*******   |          |          |          |
 3.16-04   1145 8.80+01   1.945 **********|**********|**********|**********|***********|******    |          |          |          |
 3.98-04   1045 6.38+01   1.805 **********|**********|**********|**********|***********|****      |          |          |          |
 5.01-04    890 4.32+01   1.635 **********|**********|**********|**********|***********|**        |          |          |          |
 6.31-04    906 3.49+01   1.543 **********|**********|**********|**********|***********|*         |          |          |          |
 7.94-04    765 2.34+01   1.369 **********|**********|**********|**********|***********|          |          |          |          |
 1.00-03    683 1.66+01   1.220 **********|**********|**********|**********|********** |          |          |          |          |
 1.26-03    635 1.23+01   1.089 **********|**********|**********|**********|********   |          |          |          |          |
 1.58-03    597 9.16+00   0.962 **********|**********|**********|**********|*******    |          |          |          |          |
 2.00-03    488 5.95+00   0.774 **********|**********|**********|**********|*****      |          |          |          |          |
 2.51-03    411 3.98+00   0.600 **********|**********|**********|**********|***        |          |          |          |          |
 3.16-03    361 2.78+00   0.443 **********|**********|**********|**********|*          |          |          |          |          |
 3.98-03    310 1.89+00   0.277 **********|**********|**********|**********|           |          |          |          |          |
 5.01-03    262 1.27+00   0.104 **********|**********|**********|********  |           |          |          |          |          |
 6.31-03    203 7.82-01  -0.107 **********|**********|**********|******    |           |          |          |          |          |
 7.94-03    163 4.99-01  -0.302 **********|**********|**********|****      |           |          |          |          |          |
 1.00-02    112 2.72-01  -0.565 **********|**********|**********|*        s|           |          |          |          |          |
 1.26-02     56 1.08-01  -0.966 **********|**********|*******   |       s  |           |          |          |          |          |
 1.58-02     38 5.83-02  -1.234 **********|**********|****      |    s     |           |          |          |          |          |
 2.00-02      9 1.10-02  -1.960 **********|*******   |          |  s       |           |          |          |          |          |
 2.51-02      8 7.74-03  -2.111 **********|******    |          s          |           |          |          |          |          |
 3.16-02      3 2.31-03  -2.637 **********|          |       s  |          |           |          |          |          |          |
 3.98-02      3 1.83-03  -2.737 **********|          |   s      |          |           |          |          |          |          |
 5.01-02      1 4.85-04  -3.314 ***       |          |s         |          |           |          |          |          |          |
 6.31-02      1 3.85-04  -3.414 **        |        s |          |          |           |          |          |          |          |
 7.94-02      1 3.06-04  -3.514 *         |    s     |          |          |           |          |          |          |          |
  total  200000 1.00+00         d---------d----------d----------d----------d-----------d----------d----------d----------d----------d

1tally        6        nps =      200000
           tally type 6    track length estimate of heating.            units   mev/gram       
           particle(s): photons  

           masses  
                   cell:       2                                                                                   
                         4.28827E+04
 
 cell  2                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   2.70212E-05 0.0011   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.70212E-05 0.0011


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        6

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            decrease    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes                no        yes         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        6 with nps =      200000  print table 160


 normed average tally per history  = 2.70212E-05          unnormed average tally per history  = 1.15874E+00
 estimated tally relative error    = 0.0011               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0011

 number of nonzero history tallies =      200000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       71788          largest  unnormalized history tally = 3.31577E+00
 (largest  tally)/(average tally)  = 2.86152E+00          (largest  tally)/(avg nonzero tally)= 2.86152E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.70212E-05


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            2.70212E-05             2.70215E-05                     0.000009
      relative error                  1.05683E-03             1.05686E-03                     0.000024
      variance of the variance        4.24819E-06             4.25276E-06                     0.001076
      shifted center                  2.70212E-05             2.70212E-05                     0.000000
      figure of merit                 6.66289E+06             6.66257E+06                    -0.000049

 the estimated slope of the 196 largest  tallies starting at  2.42045E+00 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.488E+06)*( 2.116E+00)**2 = (1.488E+06)*(4.477E+00) = 6.663E+06

1unnormed tally density for tally        6          nonzero tally mean(m) = 1.159E+00   nps =      200000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope=10.0)
  tally  number num den log den:d------------------d-------------------d------------------d-------------------d-------------------d-
 2.51-03      1 9.68-03  -2.014 *******************|*******************|******************|*****              |                   | 
 3.16-03      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 3.98-03      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 5.01-03      1 4.85-03  -2.314 *******************|*******************|******************|                   |                   | 
 6.31-03      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 7.94-03      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 1.00-02      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 1.26-02      0 0.00+00   0.000                    |                   |                  |                   |                   | 
 1.58-02      2 3.07-03  -2.513 *******************|*******************|**************    |                   |                   | 
 2.00-02      3 3.66-03  -2.437 *******************|*******************|****************  |                   |                   | 
 2.51-02      7 6.77-03  -2.169 *******************|*******************|******************|**                 |                   | 
 3.16-02      2 1.54-03  -2.813 *******************|*******************|********          |                   |                   | 
 3.98-02      7 4.27-03  -2.369 *******************|*******************|***************** |                   |                   | 
 5.01-02     16 7.76-03  -2.110 *******************|*******************|******************|***                |                   | 
 6.31-02     30 1.16-02  -1.937 *******************|*******************|******************|*******            |                   | 
 7.94-02     78 2.39-02  -1.622 *******************|*******************|******************|*************      |                   | 
 1.00-01    129 3.14-02  -1.504 *******************|*******************|******************|***************    |                   | 
 1.26-01    279 5.39-02  -1.269 *******************|*******************|******************|*******************|                   | 
 1.58-01    568 8.71-02  -1.060 *******************|*******************|******************|*******************|****               | 
 2.00-01   1218 1.48-01  -0.829 *******************|*******************|******************|*******************|*********          | 
 2.51-01   2326 2.25-01  -0.648 *******************|*******************|******************|*******************|************       | 
 3.16-01   4120 3.17-01  -0.499 *******************|*******************|******************|*******************|***************    | 
 3.98-01   6969 4.26-01  -0.371 *******************|*******************|******************|*******************|****************** | 
 5.01-01  10767 5.22-01  -0.282 *******************|*******************|******************|*******************|*******************| 
 6.31-01  15380 5.93-01  -0.227 *******************|*******************|******************|*******************|*******************|*
 7.94-01  20240 6.19-01  -0.208 *******************|*******************|******************|*******************|*******************|*
 1.00+00  24695 6.00-01  -0.222 *******************|*******************|******************|*******************|*******************|*
 1.26+00  27761 5.36-01  -0.271 mmmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmmm|mmmmmmmmmmmmmmmmmmm| 
 1.58+00  30179 4.63-01  -0.334 *******************|*******************|******************|*******************|****************** | 
 2.00+00  50416 6.14-01  -0.212 *******************|*******************|******************|*******************|*******************|*
 2.51+00   4714 4.56-02  -1.341 *******************|*******************|******************|*******************|                   | 
 3.16+00     91 7.00-04  -3.155 *******************|*******************|**                |                   |                   | 
 3.98+00      1 6.11-06  -5.214 *                  |                   |                  |                   |                   | 
  total  200000 1.00+00         d------------------d-------------------d------------------d-------------------d-------------------d-

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   missed  1 of 10 tfc bin checks: the figure of merit does not appear to be a constant for the last half of the problem     
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        5   missed  1 of 10 tfc bin checks: the variance of the variance appears not to decrease as 1/nps for the last half of problem
         passed all bin error check:    28 tally bins had    24 bins with zeros and     0 bins with relative errors exceeding 0.05

        6   missed  1 of 10 tfc bin checks: the figure of merit does not appear to be a constant for the last half of the problem     
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       3 of the     5 tally fluctuation chart bins did not pass all 10 statistical checks.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        16000   2.4388E-01 0.0140 0.0001  4.6  486082   2.7436E-04 0.0204 0.0128  2.4  229571   1.7076E-03 0.0029 0.0002 10.0 1.1E+07
        32000   2.4359E-01 0.0099 0.0001  9.7  491736   2.7215E-04 0.0142 0.0064  2.5  239224   1.7054E-03 0.0020 0.0001 10.0 1.2E+07
        48000   2.4431E-01 0.0081 0.0000 10.0  473081   2.7228E-04 0.0114 0.0042  2.8  235820   1.7065E-03 0.0017 0.0001 10.0 1.1E+07
        64000   2.4528E-01 0.0070 0.0000 10.0  477527   2.7338E-04 0.0098 0.0031  2.5  240459   1.7056E-03 0.0014 0.0001 10.0 1.1E+07
        80000   2.4555E-01 0.0062 0.0000 10.0  485261   2.7260E-04 0.0087 0.0025  2.6  246705   1.7065E-03 0.0013 0.0000 10.0 1.1E+07
        96000   2.4434E-01 0.0057 0.0000 10.0  485851   2.7116E-04 0.0080 0.0020  2.8  249942   1.7060E-03 0.0012 0.0000 10.0 1.2E+07
       112000   2.4442E-01 0.0053 0.0000 10.0  489195   2.7136E-04 0.0074 0.0017  2.7  252352   1.7060E-03 0.0011 0.0000 10.0 1.2E+07
       128000   2.4495E-01 0.0049 0.0000 10.0  481548   2.7208E-04 0.0069 0.0015 10.0  247263   1.7061E-03 0.0010 0.0000 10.0 1.1E+07
       144000   2.4465E-01 0.0047 0.0000 10.0  485217   2.7121E-04 0.0065 0.0014 10.0  251457   1.7060E-03 0.0010 0.0000 10.0 1.1E+07
       160000   2.4489E-01 0.0044 0.0000 10.0  484052   2.7112E-04 0.0061 0.0012 10.0  254228   1.7065E-03 0.0009 0.0000 10.0 1.1E+07
       176000   2.4467E-01 0.0042 0.0000 10.0  485762   2.6985E-04 0.0057 0.0011 10.0  260886   1.7066E-03 0.0009 0.0000 10.0 1.2E+07
       192000   2.4456E-01 0.0040 0.0000 10.0  477395   2.6983E-04 0.0055 0.0010 10.0  255276   1.7067E-03 0.0008 0.0000 10.0 1.1E+07
       200000   2.4466E-01 0.0039 0.0000 10.0  477345   2.6984E-04 0.0054 0.0010 10.0  255089   1.7064E-03 0.0008 0.0000 10.0 1.1E+07
 

                            tally        5                          tally        6
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        16000   8.2913E-05 0.0425 0.0135  9.5   52683   2.7044E-05 0.0037 0.0001 10.0 6850297
        32000   8.8616E-05 0.0337 0.0149  6.3   42325   2.7036E-05 0.0026 0.0000 10.0 6894482
        48000   8.9761E-05 0.0271 0.0085 10.0   42112   2.7060E-05 0.0022 0.0000 10.0 6653325
        64000   8.9371E-05 0.0238 0.0068 10.0   40835   2.7031E-05 0.0019 0.0000 10.0 6664235
        80000   8.9568E-05 0.0213 0.0058  9.5   41574   2.7037E-05 0.0017 0.0000 10.0 6757113
        96000   9.0683E-05 0.0204 0.0132  5.4   37865   2.7015E-05 0.0015 0.0000 10.0 6803163
       112000   9.1879E-05 0.0192 0.0107  4.7   37178   2.7001E-05 0.0014 0.0000 10.0 6827507
       128000   9.2193E-05 0.0183 0.0089  4.0   35077   2.7012E-05 0.0013 0.0000 10.0 6702184
       144000   9.3068E-05 0.0170 0.0073  4.0   36257   2.7009E-05 0.0012 0.0000 10.0 6757438
       160000   9.2888E-05 0.0161 0.0062  4.1   36243   2.7022E-05 0.0012 0.0000 10.0 6741642
       176000   9.3254E-05 0.0152 0.0053  4.1   37015   2.7026E-05 0.0011 0.0000 10.0 6777962
       192000   9.3743E-05 0.0147 0.0049  3.8   36019   2.7030E-05 0.0011 0.0000 10.0 6672245
       200000   9.4247E-05 0.0149 0.0095  3.5   33477   2.7021E-05 0.0011 0.0000 10.0 6662893

 ***********************************************************************************************************************

 dump no.    2 on file singles_t.ir     nps =      200000     coll =        1694278     ctm =        0.13   nrn =       
   29160728

        12 warning messages so far.


 run terminated when      200000  particle histories were done.

 computer time =    0.21 minutes

 mcnp     version 6.mpi 01/13/25                     07/24/25 09:39:24                     probid =  07/24/25 09:39:23 
