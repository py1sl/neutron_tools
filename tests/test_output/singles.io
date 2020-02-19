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
  
1mcnp     version 6.mpi ld=04/01/16                     02/04/20 11:52:08 
 *************************************************************************                 probid =  02/04/20 11:52:08 
 n=singles.i XSDIR=/home/vol03/scarf473/my_mcnp/mcnpx_data/xsdir                 

 
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
        16-       sdef erg=1.332 par=p                                                            
        17-       f1:p 1                                                                          
        18-       f2:p 1                                                                          
        19-       f4:p 2                                                                          
        20-       f5:p 15 0 0 1                                                                   
        21-       f6:p 2                                                                          
        22-       f8:p 2                                                                          
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

         3 warning messages so far.
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

 dump no.    1 on file singles.ir     nps =           0     coll =              0     ctm =        0.00   nrn =         
        0

         4 warning messages so far.
1problem summary                                                                                                           

      run terminated when     1000000  particle histories were done.
+                                                                                                    02/04/20 11:52:42 
      c test input to generate output for MCNP output reader                               probid =  02/04/20 11:52:08 

 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source             1000000    1.0000E+00    1.3320E+00          escape              930025    9.3002E-01    9.0710E-01
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            1.8077E-05
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 from neutrons            0    0.            0.                  compton scatter          0    0.            4.1908E-01
 bremsstrahlung       73750    7.3750E-02    2.5227E-03          capture             149084    1.4908E-01    8.1051E-03
 p-annihilation        1464    1.4640E-03    7.4812E-04          pair production        732    7.3200E-04    9.7392E-04
 photonuclear             0    0.            0.                  photonuclear abs         0    0.            0.        
 electron x-rays          0    0.            0.                  loss to photofis         0    0.            0.        
 compton fluores          0    0.            0.                                                                        
 muon capt fluores        0    0.            0.                                                                        
 1st fluorescence      4627    4.6270E-03    6.7993E-06                                                                
 2nd fluorescence         0    0.            0.                                                                        
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total          1079841    1.0798E+00    1.3353E+00              total          1079841    1.0798E+00    1.3353E+00

   number of photons banked                    75214        average time of (shakes)              cutoffs
   photon tracks per source particle      1.0798E+00          escape            7.3983E-02          tco   1.0000E+33
   photon collisions per source particle  1.6908E+00          capture           5.1571E-02          eco   1.0000E-03
   total photon collisions                   1690804          capture or escape 7.0887E-02          wc1   0.0000E+00
                                                              any termination   7.0855E-02          wc2   0.0000E+00

 computer time so far in this run     0.56 minutes            maximum number ever in bank         3
 computer time in mcrun               0.55 minutes            bank overflows to backup file       0
 source particles per minute            1.8345E+06
 random numbers generated                 32635054            most random numbers used was         444 in history      582379

 range of sampled source weights = 1.0000E+00 to 1.0000E+00
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1     1082430      1000835            0    0.0000E+00   1.2214E+00   1.2214E+00   1.0000E+00   0.0000E+00
        2        2     1082430      1075214      1690804    1.6908E+00   8.6439E-01   8.6439E-01   1.0000E+00   5.3208E+00
        3        3      930025       930025            0    0.0000E+00   9.4442E-01   9.4442E-01   1.0000E+00   0.0000E+00

           total       3094885      3006074      1690804    1.6908E+00

1tally        1        nps =     1000000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  1                                                                                                                            
                 1.16486E+00 0.0006


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       3.55
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.1642E+00 to 1.1655E+00; 1.1635E+00 to 1.1662E+00; 1.1628E+00 to 1.1669E+00
 estimated  symmetric confidence interval(1,2,3 sigma): 1.1642E+00 to 1.1655E+00; 1.1635E+00 to 1.1662E+00; 1.1628E+00 to 1.1669E+00

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        1 with nps =     1000000  print table 160


 normed average tally per history  = 1.16486E+00          unnormed average tally per history  = 1.16486E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       14112          largest  unnormalized history tally = 1.50000E+01
 (largest  tally)/(average tally)  = 1.28771E+01          (largest  tally)/(avg nonzero tally)= 1.28771E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.16486E+00


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.16486E+00             1.16487E+00                     0.000012
      relative error                  5.79258E-04             5.79372E-04                     0.000197
      variance of the variance        3.25935E-05             3.27415E-05                     0.004540
      shifted center                  1.16486E+00             1.16486E+00                     0.000000
      figure of merit                 5.46733E+06             5.46517E+06                    -0.000394

 the estimated inverse power slope of the  48 largest  tallies starting at 1.07561E+01 is 3.5468
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.835E+06)*( 1.726E+00)**2 = (1.835E+06)*(2.980E+00) = 5.467E+06

1tally        2        nps =     1000000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): photons  

           areas   
                surface:       1                                                                                   
                         3.14159E+02
 
 surface  1                                                                                                                            
                 4.31795E-03 0.0015


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       4.61
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.3115E-03 to 4.3245E-03; 4.3050E-03 to 4.3310E-03; 4.2984E-03 to 4.3375E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 4.3114E-03 to 4.3245E-03; 4.3049E-03 to 4.3310E-03; 4.2984E-03 to 4.3375E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        2 with nps =     1000000  print table 160


 normed average tally per history  = 4.31795E-03          unnormed average tally per history  = 1.35652E+00
 estimated tally relative error    = 0.0015               estimated variance of the variance  = 0.0002
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0015

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      703519          largest  unnormalized history tally = 8.39274E+01
 (largest  tally)/(average tally)  = 6.18695E+01          (largest  tally)/(avg nonzero tally)= 6.18695E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.31799E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.31795E-03             4.31821E-03                     0.000061
      relative error                  1.50974E-03             1.51088E-03                     0.000751
      variance of the variance        2.48237E-04             2.50061E-04                     0.007345
      shifted center                  4.31799E-03             4.31799E-03                     0.000000
      figure of merit                 8.04846E+05             8.03639E+05                    -0.001499

 the estimated inverse power slope of the 200 largest  tallies starting at 4.60254E+01 is 4.6137
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.835E+06)*( 6.624E-01)**2 = (1.835E+06)*(4.387E-01) = 8.048E+05

1tally        4        nps =     1000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2                                                                                   
                         3.66519E+03
 
 cell  2                                                                                                                               
                 1.91076E-03 0.0006


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

 estimated asymmetric confidence interval(1,2,3 sigma): 1.9097E-03 to 1.9119E-03; 1.9085E-03 to 1.9130E-03; 1.9074E-03 to 1.9141E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 1.9097E-03 to 1.9119E-03; 1.9085E-03 to 1.9130E-03; 1.9074E-03 to 1.9141E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =     1000000  print table 160


 normed average tally per history  = 1.91076E-03          unnormed average tally per history  = 7.00330E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      381161          largest  unnormalized history tally = 5.32047E+01
 (largest  tally)/(average tally)  = 7.59709E+00          (largest  tally)/(avg nonzero tally)= 7.59709E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.91076E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.91076E-03             1.91077E-03                     0.000007
      relative error                  5.80540E-04             5.80573E-04                     0.000057
      variance of the variance        1.00262E-05             1.00399E-05                     0.001367
      shifted center                  1.91076E-03             1.91076E-03                     0.000000
      figure of merit                 5.44320E+06             5.44258E+06                    -0.000114

 the estimated slope of the 198 largest  tallies starting at  3.60772E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.835E+06)*( 1.723E+00)**2 = (1.835E+06)*(2.967E+00) = 5.443E+06

1tally        5        nps =     1000000
           tally type 5    particle flux at a point detector.           units   1/cm**2        
           particle(s): photons  
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
                 3.42950E-04 0.0025
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
                 1.74366E-04 0.0008
 
 detector score diagnostics                  cumulative          tally         cumulative
                                             fraction of         per           fraction of
   times average score     transmissions     transmissions       history       total tally
        1.00000E-01             246684         0.14992        8.46227E-06        0.02467
        1.00000E+00            1290278         0.93409        2.06874E-04        0.62789
        2.00000E+00              49069         0.96392        2.37791E-05        0.69723
        5.00000E+00              37964         0.98699        4.04178E-05        0.81508
        1.00000E+01              13584         0.99524        3.18957E-05        0.90809
        1.00000E+02               5396         0.99852        2.97172E-05        0.99474
        1.00000E+03                 18         0.99853        1.45651E-06        0.99899
        1.00000E+38                  0         0.99853        0.00000E+00        0.99899
 before dd roulette               2411         1.00000        3.47496E-07        1.00000

 average tally per history = 3.42950E-04            largest score = 2.32897E-01
 (largest score)/(average tally) = 6.79099E+02      nps of largest score =      492485

 score contributions by cell
        cell      misses        hits    tally per history    weight per hit
     1     1           0     1000000       1.72673E-04         1.72673E-04
     2     2      974693      645404       1.70277E-04         2.63830E-04
       total      974693     1645404       3.42950E-04         2.08429E-04

 score misses
   russian roulette on pd                        0
   psc=0.                                        0
   russian roulette in transmission         935317
   underflow in transmission                 39376
   hit a zero-importance cell                    0
   energy cutoff                                 0


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        5

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.01      yes         yes            constant    random       2.14
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes          no

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        5 with nps =     1000000  print table 160


 normed average tally per history  = 3.42950E-04          unnormed average tally per history  = 3.42950E-04
 estimated tally relative error    = 0.0025               estimated variance of the variance  = 0.0087
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0025

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      492485          largest  unnormalized history tally = 2.33619E-01
 (largest  tally)/(average tally)  = 6.81206E+02          (largest  tally)/(avg nonzero tally)= 6.81206E+02

 (confidence interval shift)/mean  = 0.0001               shifted confidence interval center  = 3.42971E-04


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            3.42950E-04             3.43183E-04                     0.000680
      relative error                  2.52536E-03             2.61358E-03                     0.034935
      variance of the variance        8.68971E-03             1.21291E-02                     0.395806
      shifted center                  3.42971E-04             3.42977E-04                     0.000019
      figure of merit                 2.87655E+05             2.68563E+05                    -0.066371

 the estimated inverse power slope of the 200 largest  tallies starting at 1.44973E-02 is 2.1397
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.835E+06)*( 3.960E-01)**2 = (1.835E+06)*(1.568E-01) = 2.877E+05

1unnormed tally density for tally        5          nonzero tally mean(m) = 3.429E-04   nps =     1000000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 2.1)
  tally  number num den log den:d---------d----------d----------d----------d----------d----------d-----------d----------d----------d
 2.00-04 681313 1.66+04   4.220 **********|**********|**********|**********|**********|**********|***********|**********|**********|
 2.51-04 146549 2.84+03   3.453 **********|**********|**********|**********|**********|**********|***********|**********|**        |
 3.16-04  39693 6.10+02   2.786 **********|**********|**********|**********|**********|**********|***********|******    |          |
 3.98-04  24837 3.03+02   2.482 mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmm|mmmmmmmmmmm|mmm       |          |
 5.01-04  18559 1.80+02   2.255 **********|**********|**********|**********|**********|**********|***********|          |          |
 6.31-04  15402 1.19+02   2.074 **********|**********|**********|**********|**********|**********|********** |          |          |
 7.94-04  12831 7.85+01   1.895 **********|**********|**********|**********|**********|**********|********   |          |          |
 1.00-03  11039 5.37+01   1.730 **********|**********|**********|**********|**********|**********|******     |          |          |
 1.26-03   9429 3.64+01   1.561 **********|**********|**********|**********|**********|**********|*****      |          |          |
 1.58-03   8446 2.59+01   1.413 **********|**********|**********|**********|**********|**********|***        |          |          |
 2.00-03   7393 1.80+01   1.256 **********|**********|**********|**********|**********|**********|*          |          |          |
 2.51-03   6313 1.22+01   1.087 **********|**********|**********|**********|**********|**********|           |          |          |
 3.16-03   5232 8.04+00   0.905 **********|**********|**********|**********|**********|********  |           |          |          |
 3.98-03   4202 5.13+00   0.710 **********|**********|**********|**********|**********|******    |           |          |          |
 5.01-03   3238 3.14+00   0.497 **********|**********|**********|**********|**********|****      |           |          |          |
 6.31-03   2187 1.69+00   0.227 **********|**********|**********|**********|**********|*         |           |          |          |
 7.94-03   1585 9.70-01  -0.013 **********|**********|**********|**********|********* |          |           |          |          |
 1.00-02    911 4.43-01  -0.354 **********|**********|**********|**********|*****     |          |           |          |          |
 1.26-02    482 1.86-01  -0.730 **********|**********|**********|**********|*         |          |           |          |          |
 1.58-02    221 6.78-02  -1.169 **********|**********|**********|*******   |     s    |          |           |          |          |
 2.00-02     67 1.63-02  -1.787 **********|**********|**********|          |   s      |          |           |          |          |
 2.51-02     25 4.84-03  -2.315 **********|**********|******    |          | s        |          |           |          |          |
 3.16-02     15 2.31-03  -2.637 **********|**********|**        |          s          |          |           |          |          |
 3.98-02     13 1.59-03  -2.799 **********|**********|          |        s |          |          |           |          |          |
 5.01-02      5 4.85-04  -3.314 **********|*****     |          |      s   |          |          |           |          |          |
 6.31-02      2 1.54-04  -3.812 **********|          |          |    s     |          |          |           |          |          |
 7.94-02      3 1.84-04  -3.736 **********|*         |          | s        |          |          |           |          |          |
 1.00-01      2 9.72-05  -4.012 ********* |          |          s          |          |          |           |          |          |
 1.26-01      3 1.16-04  -3.936 **********|          |        s |          |          |          |           |          |          |
 1.58-01      1 3.07-05  -4.513 ***       |          |     s    |          |          |          |           |          |          |
 2.00-01      1 2.44-05  -4.613 **        |          |   s      |          |          |          |           |          |          |
 2.51-01      1 1.94-05  -4.713 *         |          | s        |          |          |          |           |          |          |
  total 1000000 1.00+00         d---------d----------d----------d----------d----------d----------d-----------d----------d----------d

1tally        6        nps =     1000000
           tally type 6    track length estimate of heating.            units   mev/gram       
           particle(s): photons  

           masses  
                   cell:       2                                                                                   
                         9.89602E+03
 
 cell  2                                                                                                                               
                 4.30567E-05 0.0002


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

 estimated asymmetric confidence interval(1,2,3 sigma): 4.3049E-05 to 4.3065E-05; 4.3041E-05 to 4.3072E-05; 4.3033E-05 to 4.3080E-05
 estimated  symmetric confidence interval(1,2,3 sigma): 4.3049E-05 to 4.3065E-05; 4.3041E-05 to 4.3072E-05; 4.3033E-05 to 4.3080E-05

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        6 with nps =     1000000  print table 160


 normed average tally per history  = 4.30567E-05          unnormed average tally per history  = 4.26089E-01
 estimated tally relative error    = 0.0002               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0002

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      618168          largest  unnormalized history tally = 1.31214E+00
 (largest  tally)/(average tally)  = 3.07950E+00          (largest  tally)/(avg nonzero tally)= 3.07950E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.30567E-05


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.30567E-05             4.30567E-05                     0.000002
      relative error                  1.82801E-04             1.82813E-04                     0.000062
      variance of the variance        6.67501E-06             6.68982E-06                     0.002219
      shifted center                  4.30567E-05             4.30567E-05                     0.000000
      figure of merit                 5.48983E+07             5.48916E+07                    -0.000123

 the estimated slope of the 200 largest  tallies starting at  8.54882E-01 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.835E+06)*( 5.470E+00)**2 = (1.835E+06)*(2.993E+01) = 5.490E+07

1tally        8        nps =     1000000
           tally type 8    pulse height distribution.                   units   number         
           particle(s): photons  
 
 cell  2                                                                                                                               
                 1.00000E+00 0.0000


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

 relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 1.835E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     1 tally bins all have relative errors less than 0.10 with no zero bins

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     1 tally bins all have relative errors less than 0.10 with no zero bins

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     1 tally bins all have relative errors less than 0.10 with no zero bins

        5   missed  1 of 10 tfc bin checks: the slope of decrease of largest tallies is less than the minimum acceptable value of 3.0 
         passed all bin error check:     2 tally bins all have relative errors less than 0.05 with no zero bins

        6   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     1 tally bins all have relative errors less than 0.10 with no zero bins

        8   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     1 tally bins all have relative errors less than 0.10 with no zero bins


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 warning.       1 of the     6 tally fluctuation chart bins did not pass all 10 statistical checks.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   1.1666E+00 0.0023 0.0005 10.0 5383874   4.3110E-03 0.0059 0.0035 10.0  830652   1.9098E-03 0.0023 0.0002 10.0 5460112
       128000   1.1668E+00 0.0016 0.0003  2.6 5389230   4.3154E-03 0.0042 0.0017 10.0  828930   1.9098E-03 0.0016 0.0001 10.0 5459612
       192000   1.1662E+00 0.0013 0.0002  2.7 5400528   4.3119E-03 0.0034 0.0012 10.0  827465   1.9103E-03 0.0013 0.0001 10.0 5452060
       256000   1.1654E+00 0.0011 0.0001  3.4 5423277   4.3118E-03 0.0030 0.0010  8.3  813941   1.9091E-03 0.0011 0.0000  9.8 5459619
       320000   1.1655E+00 0.0010 0.0001  3.8 5425454   4.3178E-03 0.0027 0.0008  5.9  803406   1.9100E-03 0.0010 0.0000 10.0 5455973
       384000   1.1650E+00 0.0009 0.0001  3.8 5441742   4.3133E-03 0.0024 0.0007  5.9  806133   1.9104E-03 0.0009 0.0000 10.0 5458856
       448000   1.1650E+00 0.0009 0.0001  4.0 5457029   4.3124E-03 0.0022 0.0006  3.5  812299   1.9100E-03 0.0009 0.0000 10.0 5461889
       512000   1.1644E+00 0.0008 0.0001 10.0 5474243   4.3099E-03 0.0021 0.0005  4.2  813194   1.9101E-03 0.0008 0.0000 10.0 5458901
       576000   1.1646E+00 0.0008 0.0001  3.1 5465687   4.3124E-03 0.0020 0.0004  4.4  812638   1.9101E-03 0.0008 0.0000 10.0 5454052
       640000   1.1649E+00 0.0007 0.0001  3.0 5462461   4.3192E-03 0.0019 0.0004  4.8  801948   1.9104E-03 0.0007 0.0000 10.0 5446704
       704000   1.1650E+00 0.0007 0.0000  3.0 5456193   4.3183E-03 0.0018 0.0004  4.0  801073   1.9102E-03 0.0007 0.0000 10.0 5453610
       768000   1.1650E+00 0.0007 0.0000  3.3 5452192   4.3162E-03 0.0017 0.0003  3.6  806830   1.9106E-03 0.0007 0.0000 10.0 5449538
       832000   1.1651E+00 0.0006 0.0000  3.3 5447004   4.3164E-03 0.0017 0.0003  3.8  807498   1.9107E-03 0.0006 0.0000 10.0 5447619
       896000   1.1650E+00 0.0006 0.0000  3.6 5459213   4.3162E-03 0.0016 0.0003  4.2  807349   1.9107E-03 0.0006 0.0000 10.0 5447181
       960000   1.1649E+00 0.0006 0.0000  3.6 5464813   4.3171E-03 0.0015 0.0003  4.7  805475   1.9107E-03 0.0006 0.0000 10.0 5445097
      1000000   1.1649E+00 0.0006 0.0000  3.5 5467327   4.3179E-03 0.0015 0.0002  4.6  804846   1.9108E-03 0.0006 0.0000 10.0 5443199
 

                            tally        5                          tally        6                          tally        8
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   3.4556E-04 0.0109 0.0622  3.4  240169   4.3057E-05 0.0007 0.0001 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       128000   3.4293E-04 0.0070 0.0243  3.6  292606   4.3006E-05 0.0005 0.0001 10.0 5.4E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       192000   3.4266E-04 0.0055 0.0130  3.7  319528   4.3037E-05 0.0004 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       256000   3.4218E-04 0.0047 0.0087  3.2  322229   4.3038E-05 0.0004 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       320000   3.4293E-04 0.0042 0.0059  2.8  324682   4.3048E-05 0.0003 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       384000   3.4349E-04 0.0039 0.0054  2.8  313464   4.3049E-05 0.0003 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       448000   3.4298E-04 0.0036 0.0043  2.8  322954   4.3053E-05 0.0003 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       512000   3.4306E-04 0.0036 0.0221  2.5  283928   4.3055E-05 0.0003 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       576000   3.4274E-04 0.0033 0.0185  2.3  291293   4.3058E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       640000   3.4278E-04 0.0032 0.0168  2.3  281050   4.3058E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       704000   3.4281E-04 0.0030 0.0144  2.2  281404   4.3053E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       768000   3.4310E-04 0.0030 0.0132  2.1  274160   4.3058E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       832000   3.4283E-04 0.0028 0.0117  2.2  279192   4.3056E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       896000   3.4277E-04 0.0027 0.0105  2.1  284827   4.3053E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       960000   3.4303E-04 0.0026 0.0093  2.1  285653   4.3055E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
      1000000   3.4295E-04 0.0025 0.0087  2.1  287655   4.3057E-05 0.0002 0.0000 10.0 5.5E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30

 ***********************************************************************************************************************

 dump no.    2 on file singles.ir     nps =     1000000     coll =        1690804     ctm =        0.55   nrn =         
 32635054

         6 warning messages so far.


 run terminated when     1000000  particle histories were done.

 computer time =    0.56 minutes

 mcnp     version 6.mpi 04/01/16                     02/04/20 11:52:42                     probid =  02/04/20 11:52:08 
