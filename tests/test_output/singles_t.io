          Code Name & Version = MCNP6, 1.0
  
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
  
1mcnp     version 6.mpi ld=04/01/16                     05/18/21 09:43:59 
 *************************************************************************                 probid =  05/18/21 09:43:59 
 n=singles_t.i XSDIR=/home/vol03/scarf473/my_mcnp/mcnpx_data/xsdir               

 
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
     XSDIR used: /home/vol03/scarf473/my_mcnp/mcnpx_data/xsdir

     table    length

                        tables from file mcplib05t                                                       

 
  comment.   13000.05p pips data for photon energy broadening converted to CDF form.
  13000.05p    5468  ENDF/B-VI Release 8 Photoatomic Data for 13-AL                               mat1300      12/14/09

  total        5468

 maximum photon energy set to    100.0 mev (maximum electron energy)

                        tables from file el03                                                            

  13000.03e    2337                                                                                          6/6/98    

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
1problem summary                                                                                                           

      run terminated when      200000  particle histories were done.
+                                                                                                    05/18/21 09:44:17 
      c test input to generate output for MCNP output reader                               probid =  05/18/21 09:43:59 

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
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total           245256    1.2263E+00    1.3393E+00              total           245256    1.2263E+00    1.3393E+00

   number of photons banked                    38942        average time of (shakes)              cutoffs
   photon tracks per source particle      1.2263E+00          escape            7.3426E-02          tco   1.0000E+33
   photon collisions per source particle  8.4714E+00          capture           3.8549E-02          eco   1.0000E-03
   total photon collisions                   1694280          capture or escape 4.5515E-02          wc1  -5.0000E-01
                                                              any termination   4.5487E-02          wc2  -2.5000E-01

 computer time so far in this run     0.28 minutes            maximum number ever in bank         3
 computer time in mcrun               0.27 minutes            bank overflows to backup file       0
 source particles per minute            7.4972E+05
 random numbers generated                 29160770            most random numbers used was         558 in history       86713

 range of sampled source weights = 1.0000E+00 to 1.0000E+00
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1      241777       200350            0    0.0000E+00   1.0816E+00   1.0816E+00   1.0000E+00   0.0000E+00
        2        2      241777       238942      1694280    8.4714E+00   5.8294E-01   5.8294E-01   1.0000E+00   9.8171E-01
        3        3       48931        48931            0    0.0000E+00   6.7301E-01   6.7301E-01   1.0000E+00   0.0000E+00

           total        532485       488223      1694280    8.4714E+00

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
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 2.4369E-01 to 2.4562E-01; 2.4272E-01 to 2.4659E-01; 2.4176E-01 to 2.4755E-01
 estimated  symmetric confidence interval(1,2,3 sigma): 2.4369E-01 to 2.4562E-01; 2.4272E-01 to 2.4659E-01; 2.4176E-01 to 2.4755E-01

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
      figure of merit                 2.40451E+05             2.40450E+05                    -0.000001

 the 100 largest  history tallies appear to have a  maximum value of about 2.00000E+00
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (7.497E+05)*( 5.663E-01)**2 = (7.497E+05)*(3.207E-01) = 2.405E+05

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
      figure of merit                 1.28494E+05             1.28156E+05                    -0.002631

 the estimated slope of the 200 largest  tallies starting at  7.40410E+00 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (7.497E+05)*( 4.140E-01)**2 = (7.497E+05)*(1.714E-01) = 1.285E+05

1tally        4        nps =      200000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2                                                                                   
                         3.66519E+03
 
 cell  2                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
                 0.00000E+00 0.0000   1.70644E-03 0.0008   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
                 0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.70644E-03 0.0008


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
 estimated  symmetric confidence interval(1,2,3 sigma): 1.7051E-03 to 1.7078E-03; 1.7037E-03 to 1.7092E-03; 1.7023E-03 to 1.7106E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =      200000  print table 160


 normed average tally per history  = 1.70644E-03          unnormed average tally per history  = 6.25442E+00
 estimated tally relative error    = 0.0008               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0008

 number of nonzero history tallies =      200000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       84052          largest  unnormalized history tally = 2.25250E+01
 (largest  tally)/(average tally)  = 3.60145E+00          (largest  tally)/(avg nonzero tally)= 3.60145E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.70644E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.70644E-03             1.70646E-03                     0.000013
      relative error                  8.09670E-04             8.09760E-04                     0.000111
      variance of the variance        1.56662E-05             1.57217E-05                     0.003538
      shifted center                  1.70644E-03             1.70644E-03                     0.000000
      figure of merit                 5.71808E+06             5.71681E+06                    -0.000222

 the estimated slope of the 198 largest  tallies starting at  1.59993E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (7.497E+05)*( 2.762E+00)**2 = (7.497E+05)*(7.627E+00) = 5.718E+06

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
     2     2     1439079      103857       7.84241E-05         1.51023E-04
       total     1439079      303857       9.42466E-05         6.20335E-05

 score misses
   russian roulette on pd                        0
   psc=0.                                        0
   russian roulette in transmission        1402487
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
      figure of merit                 1.68633E+04             1.58180E+04                    -0.061987

 the estimated inverse power slope of the 200 largest  tallies starting at 8.49254E-03 is 3.4764
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (7.497E+05)*( 1.500E-01)**2 = (7.497E+05)*(2.249E-02) = 1.686E+04

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
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 2.6993E-05 to 2.7050E-05; 2.6964E-05 to 2.7078E-05; 2.6936E-05 to 2.7107E-05
 estimated  symmetric confidence interval(1,2,3 sigma): 2.6993E-05 to 2.7050E-05; 2.6964E-05 to 2.7078E-05; 2.6936E-05 to 2.7107E-05

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
      variance of the variance        4.24818E-06             4.25275E-06                     0.001076
      shifted center                  2.70212E-05             2.70212E-05                     0.000000
      figure of merit                 3.35627E+06             3.35610E+06                    -0.000049

 the estimated slope of the 196 largest  tallies starting at  2.42045E+00 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (7.497E+05)*( 2.116E+00)**2 = (7.497E+05)*(4.477E+00) = 3.356E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10

        5   missed  1 of 10 tfc bin checks: the variance of the variance appears not to decrease as 1/nps for the last half of problem
         passed all bin error check:    28 tally bins had    24 bins with zeros and     0 bins with relative errors exceeding 0.05

        6   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    14 tally bins had    12 bins with zeros and     0 bins with relative errors exceeding 0.10


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       1 of the     5 tally fluctuation chart bins did not pass all 10 statistical checks.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        16000   2.4388E-01 0.0140 0.0001  4.6  237718   2.7436E-04 0.0204 0.0128  2.4  112271   1.7076E-03 0.0029 0.0002 10.0 5599669
        32000   2.4359E-01 0.0099 0.0001  9.7  238401   2.7215E-04 0.0142 0.0064  2.5  115980   1.7054E-03 0.0020 0.0001 10.0 5591003
        48000   2.4431E-01 0.0081 0.0000 10.0  239298   2.7228E-04 0.0114 0.0042  2.8  119285   1.7065E-03 0.0017 0.0001 10.0 5663976
        64000   2.4528E-01 0.0070 0.0000 10.0  240937   2.7338E-04 0.0098 0.0031  2.5  121324   1.7056E-03 0.0014 0.0001 10.0 5681888
        80000   2.4555E-01 0.0062 0.0000 10.0  241322   2.7260E-04 0.0087 0.0025  2.6  122687   1.7065E-03 0.0013 0.0000 10.0 5686730
        96000   2.4434E-01 0.0057 0.0000 10.0  239722   2.7116E-04 0.0080 0.0020  2.8  123323   1.7060E-03 0.0012 0.0000 10.0 5681432
       112000   2.4442E-01 0.0053 0.0000 10.0  239745   2.7136E-04 0.0074 0.0017  2.7  123672   1.7060E-03 0.0011 0.0000 10.0 5688365
       128000   2.4495E-01 0.0049 0.0000 10.0  240620   2.7208E-04 0.0069 0.0015 10.0  123553   1.7061E-03 0.0010 0.0000 10.0 5691788
       144000   2.4465E-01 0.0047 0.0000 10.0  240266   2.7121E-04 0.0065 0.0014 10.0  124514   1.7060E-03 0.0010 0.0000 10.0 5683404
       160000   2.4489E-01 0.0044 0.0000 10.0  240721   2.7112E-04 0.0061 0.0012 10.0  126429   1.7065E-03 0.0009 0.0000 10.0 5697778
       176000   2.4467E-01 0.0042 0.0000 10.0  240333   2.6985E-04 0.0057 0.0011 10.0  129075   1.7066E-03 0.0009 0.0000 10.0 5704834
       192000   2.4456E-01 0.0040 0.0000 10.0  240290   2.6983E-04 0.0055 0.0010 10.0  128490   1.7067E-03 0.0008 0.0000 10.0 5713275
       200000   2.4466E-01 0.0039 0.0000 10.0  240451   2.6984E-04 0.0054 0.0010 10.0  128494   1.7064E-03 0.0008 0.0000 10.0 5718080
 

                            tally        5                          tally        6
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        16000   8.2913E-05 0.0425 0.0135  9.5   25765   2.7044E-05 0.0037 0.0001 10.0 3350135
        32000   8.8616E-05 0.0337 0.0149  6.3   20520   2.7036E-05 0.0026 0.0000 10.0 3342554
        48000   8.9761E-05 0.0271 0.0085 10.0   21301   2.7060E-05 0.0022 0.0000 10.0 3365447
        64000   8.9371E-05 0.0238 0.0068 10.0   20603   2.7031E-05 0.0019 0.0000 10.0 3362455
        80000   8.9568E-05 0.0213 0.0058  9.5   20675   2.7037E-05 0.0017 0.0000 10.0 3360342
        96000   9.0683E-05 0.0204 0.0132  5.4   18683   2.7015E-05 0.0015 0.0000 10.0 3356722
       112000   9.1879E-05 0.0192 0.0107  4.7   18220   2.7001E-05 0.0014 0.0000 10.0 3346022
       128000   9.2193E-05 0.0183 0.0089  4.0   17527   2.7012E-05 0.0013 0.0000 10.0 3348957
       144000   9.3068E-05 0.0170 0.0073  4.0   17953   2.7009E-05 0.0012 0.0000 10.0 3346092
       160000   9.2888E-05 0.0161 0.0062  4.1   18024   2.7022E-05 0.0012 0.0000 10.0 3352654
       176000   9.3254E-05 0.0152 0.0053  4.1   18313   2.7026E-05 0.0011 0.0000 10.0 3353439
       192000   9.3743E-05 0.0147 0.0049  3.8   18129   2.7030E-05 0.0011 0.0000 10.0 3358386
       200000   9.4247E-05 0.0149 0.0095  3.5   16863   2.7021E-05 0.0011 0.0000 10.0 3356268

 ***********************************************************************************************************************

 dump no.    2 on file singles_t.ir     nps =      200000     coll =        1694280     ctm =        0.27   nrn =       
   29160770

        10 warning messages so far.


 run terminated when      200000  particle histories were done.

 computer time =    0.28 minutes

 mcnp     version 6.mpi 04/01/16                     05/18/21 09:44:17                     probid =  05/18/21 09:43:59 
