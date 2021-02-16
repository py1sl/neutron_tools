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
  
1mcnp     version 6.mpi ld=04/01/16                     02/16/21 11:46:56 
 *************************************************************************                 probid =  02/16/21 11:46:56 
 n=singles_et.i XSDIR=/home/vol03/scarf473/my_mcnp/mcnpx_data/xsdir              

 
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
        20-       f2:p 1                                                                          
        21-       e2  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        22-       t2     1 5 10 15 20 25 30 35 40 45 50 60 100 1000                               
        23-       f4:p 2                                                                          
        24-       e4  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        25-       f5:p 15 0 0 1                                                                   
        26-       e5  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        27-       f6:p 2                                                                          
        28-       e6  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        29-       f8:p 2                                                                          
        30-       e8  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
 
  warning.  last time bin of tally        2 is less than time cutoff.
 
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

         5 warning messages so far.
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

 dump no.    1 on file singles_et.ir     nps =           0     coll =              0     ctm =        0.00   nrn =      
           0

         6 warning messages so far.

 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc
  1 5.6889E-01 1.0000E+00 5.0064E+02 5.6665E-01 8.9149E+00 1.0000E+00 6.0729E-01     2       79378    3                  44         6
1problem summary                                                                                                           

      run terminated when     1000000  particle histories were done.
+                                                                                                    02/16/21 11:47:31 
      c test input to generate output for MCNP output reader                               probid =  02/16/21 11:46:56 

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
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total          1079646    1.0796E+00    1.3352E+00              total          1079646    1.0796E+00    1.3352E+00

   number of photons banked                    74916        average time of (shakes)              cutoffs
   photon tracks per source particle      1.0796E+00          escape            2.5070E+01          tco   1.0000E+33
   photon collisions per source particle  1.6901E+00          capture           2.4244E+01          eco   1.0000E-03
   total photon collisions                   1690149          capture or escape 2.4956E+01          wc1   0.0000E+00
                                                              any termination   2.4956E+01          wc2   0.0000E+00

 computer time so far in this run     0.58 minutes            maximum number ever in bank         4
 computer time in mcrun               0.57 minutes            bank overflows to backup file       0
 source particles per minute            1.7515E+06
 random numbers generated                 35178899            most random numbers used was         491 in history      921363

 range of sampled source weights = 1.0000E+00 to 1.0000E+00
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
      energy   
    1.0000E-01   2.90820E-02 0.0095
    2.0000E-01   5.83040E-02 0.0062
    3.0000E-01   7.27660E-02 0.0052
    4.0000E-01   2.85000E-03 0.0265
    5.0000E-01   5.00000E-05 0.2000
    6.0000E-01   2.78000E-04 0.0848
    8.0000E-01   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000
    1.4000E+00   1.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000
      total      1.16333E+00 0.0006


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
      figure of merit                 5.27006E+06             5.26853E+06                    -0.000289

 the estimated slope of the  49 largest  tallies starting at  1.00000E+01 appears to be decreasing at least exponentially.
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.752E+06)*( 1.735E+00)**2 = (1.752E+06)*(3.009E+00) = 5.270E+06

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
      figure of merit                 7.68706E+05             7.67297E+05                    -0.001834

 the estimated inverse power slope of the 198 largest  tallies starting at 4.62355E+01 is 4.4927
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.752E+06)*( 6.625E-01)**2 = (1.752E+06)*(4.389E-01) = 7.687E+05

1tally        4        nps =     1000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2                                                                                   
                         3.66519E+03
 
 cell  2                                                                                                                               
      energy   
    1.0000E-01   1.20400E-04 0.0039
    2.0000E-01   2.41350E-04 0.0027
    3.0000E-01   1.88081E-04 0.0029
    4.0000E-01   9.50299E-05 0.0038
    5.0000E-01   5.57466E-05 0.0045
    6.0000E-01   4.13511E-05 0.0050
    8.0000E-01   6.14729E-05 0.0039
    9.0000E-01   2.67013E-05 0.0058
    1.0000E+00   2.51767E-05 0.0059
    1.1000E+00   2.45722E-05 0.0059
    1.2000E+00   2.38754E-05 0.0060
    1.3000E+00   2.38904E-05 0.0059
    1.4000E+00   9.82028E-04 0.0005
    1.5000E+00   0.00000E+00 0.0000
      total      1.90968E-03 0.0006


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
      figure of merit                 5.19992E+06             5.19935E+06                    -0.000110

 the estimated slope of the 200 largest  tallies starting at  3.62629E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.752E+06)*( 1.723E+00)**2 = (1.752E+06)*(2.969E+00) = 5.200E+06

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
      energy   
    1.0000E-01   1.18710E-05 0.0247
    2.0000E-01   2.87933E-05 0.0100
    3.0000E-01   1.83387E-05 0.0219
    4.0000E-01   1.37573E-05 0.0088
    5.0000E-01   1.32333E-05 0.0093
    6.0000E-01   1.20301E-05 0.0101
    8.0000E-01   2.16202E-05 0.0279
    9.0000E-01   9.87509E-06 0.0153
    1.0000E+00   9.77253E-06 0.0173
    1.1000E+00   9.82089E-06 0.0200
    1.2000E+00   9.59086E-06 0.0220
    1.3000E+00   9.81833E-06 0.0245
    1.4000E+00   1.75506E-04 0.0008
    1.5000E+00   0.00000E+00 0.0000
      total      3.44027E-04 0.0031
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
      energy   
    1.0000E-01   9.09977E-07 0.1413
    2.0000E-01   5.60339E-07 0.1372
    3.0000E-01   2.24422E-07 0.2082
    4.0000E-01   1.16595E-07 0.2368
    5.0000E-01   4.68935E-08 0.5245
    6.0000E-01   1.54900E-07 0.1019
    8.0000E-01   2.37648E-08 0.6604
    9.0000E-01   6.84638E-10 0.6311
    1.0000E+00   6.92184E-11 0.7071
    1.1000E+00   7.43651E-11 1.0000
    1.2000E+00   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000
    1.4000E+00   1.72673E-04 0.0000
    1.5000E+00   0.00000E+00 0.0000
      total      1.74710E-04 0.0009
 
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
      figure of merit                 1.80024E+05             1.40496E+05                    -0.219572

 the estimated inverse power slope of the 200 largest  tallies starting at 1.49554E-02 is 2.1802
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.752E+06)*( 3.206E-01)**2 = (1.752E+06)*(1.028E-01) = 1.800E+05

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
      energy   
    1.0000E-01   5.60112E-07 0.0043
    2.0000E-01   1.01791E-06 0.0028
    3.0000E-01   1.28110E-06 0.0029
    4.0000E-01   9.27749E-07 0.0038
    5.0000E-01   7.13903E-07 0.0045
    6.0000E-01   6.47539E-07 0.0050
    8.0000E-01   1.20736E-06 0.0039
    9.0000E-01   6.27328E-07 0.0058
    1.0000E+00   6.50469E-07 0.0059
    1.1000E+00   6.89658E-07 0.0059
    1.2000E+00   7.20776E-07 0.0060
    1.3000E+00   7.70126E-07 0.0059
    1.4000E+00   3.32349E-05 0.0005
    1.5000E+00   0.00000E+00 0.0000
      total      4.30489E-05 0.0002


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        6

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant   decrease     10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes         no         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

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
      figure of merit                 5.24065E+07             5.24001E+07                    -0.000123

 the estimated slope of the 200 largest  tallies starting at  8.49792E-01 appears to be decreasing at least exponentially.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.752E+06)*( 5.470E+00)**2 = (1.752E+06)*(2.992E+01) = 5.241E+07

1unnormed tally density for tally        6          nonzero tally mean(m) = 4.260E-01   nps =     1000000  print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope=10.0)
  tally  number num den log den:d--------------d--------------d---------------d--------------d---------------d--------------d-------
 1.00-03      1 4.86-03  -2.313 ***************|**************|***************|****          |               |              |       
 1.26-03      0 0.00+00   0.000                |              |               |              |               |              |       
 1.58-03      0 0.00+00   0.000                |              |               |              |               |              |       
 2.00-03      0 0.00+00   0.000                |              |               |              |               |              |       
 2.51-03      1 1.94-03  -2.713 ***************|**************|*************  |              |               |              |       
 3.16-03      0 0.00+00   0.000                |              |               |              |               |              |       
 3.98-03      2 2.44-03  -2.612 ***************|**************|***************|              |               |              |       
 5.01-03      2 1.94-03  -2.712 ***************|**************|*************  |              |               |              |       
 6.31-03      0 0.00+00   0.000                |              |               |              |               |              |       
 7.94-03      1 6.12-04  -3.213 ***************|**************|******         |              |               |              |       
 1.00-02      3 1.46-03  -2.836 ***************|**************|************   |              |               |              |       
 1.26-02      5 1.93-03  -2.714 ***************|**************|*************  |              |               |              |       
 1.58-02      3 9.20-04  -3.036 ***************|**************|********       |              |               |              |       
 2.00-02     15 3.66-03  -2.437 ***************|**************|***************|**            |               |              |       
 2.51-02     16 3.10-03  -2.509 ***************|**************|***************|*             |               |              |       
 3.16-02     20 3.08-03  -2.512 ***************|**************|***************|*             |               |              |       
 3.98-02     51 6.23-03  -2.206 ***************|**************|***************|*****         |               |              |       
 5.01-02     87 8.44-03  -2.074 ***************|**************|***************|*******       |               |              |       
 6.31-02    184 1.42-02  -1.848 ***************|**************|***************|***********   |               |              |       
 7.94-02    379 2.32-02  -1.635 ***************|**************|***************|**************|               |              |       
 1.00-01   1215 5.91-02  -1.229 ***************|**************|***************|**************|******         |              |       
 1.26-01   3212 1.24-01  -0.906 ***************|**************|***************|**************|***********    |              |       
 1.58-01   6709 2.06-01  -0.687 ***************|**************|***************|**************|************** |              |       
 2.00-01  12729 3.10-01  -0.508 ***************|**************|***************|**************|***************|*             |       
 2.51-01  23000 4.45-01  -0.351 ***************|**************|***************|**************|***************|***           |       
 3.16-01  48119 7.40-01  -0.131 ***************|**************|***************|**************|***************|*******       |       
 3.98-01 113596 1.39+00   0.142 ***************|**************|***************|**************|***************|***********   |       
 5.01-01 748232 7.26+00   0.861 mmmmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmm
 6.31-01  34687 2.67-01  -0.573 ***************|**************|***************|**************|***************|              |       
 7.94-01   7194 4.40-02  -1.356 ***************|**************|***************|**************|****           |              |       
 1.00+00    518 2.52-03  -2.599 ***************|**************|***************|              |               |              |       
 1.26+00     18 6.95-05  -4.158 ***************|******        |               |              |               |              |       
 1.58+00      1 3.07-06  -5.513 *              |              |               |              |               |              |       
  total 1000000 1.00+00         d--------------d--------------d---------------d--------------d---------------d--------------d-------

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

 relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 1.752E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:    15 tally bins had     7 bins with zeros and     1 bins with relative errors exceeding 0.10

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   225 tally bins had   144 bins with zeros and    37 bins with relative errors exceeding 0.10

        4   missed  1 of 10 tfc bin checks: the estimated mean has a trend during the last half of the problem                        
         passed all bin error check:    15 tally bins had     1 bins with zeros and     0 bins with relative errors exceeding 0.10

        5   missed  1 of 10 tfc bin checks: the slope of decrease of largest tallies is less than the minimum acceptable value of 3.0 
         missed all bin error check:    30 tally bins had     4 bins with zeros and    10 bins with relative errors exceeding 0.05

        6   missed  1 of 10 tfc bin checks: the figure of merit has a trend during the last half of the problem                       
         passed all bin error check:    15 tally bins had     1 bins with zeros and     0 bins with relative errors exceeding 0.10

        8   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:    15 tally bins had     1 bins with zeros and     0 bins with relative errors exceeding 0.10


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       3 of the     6 tally fluctuation chart bins did not pass all 10 statistical checks.
 warning.       3 of the     6 tallies had bins with relative errors greater than recommended.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   1.1618E+00 0.0023 0.0005  4.2 5340190   4.2833E-03 0.0057 0.0036  3.2  836747   1.9070E-03 0.0023 0.0002 10.0 5208760
       128000   1.1603E+00 0.0016 0.0003  4.1 5371891   4.2761E-03 0.0041 0.0018 10.0  818823   1.9040E-03 0.0016 0.0001 10.0 5208506
       192000   1.1616E+00 0.0013 0.0002  4.9 5310337   4.2962E-03 0.0034 0.0013 10.0  774586   1.9048E-03 0.0013 0.0001 10.0 5221390
       256000   1.1618E+00 0.0011 0.0001  5.1 5329022   4.2916E-03 0.0029 0.0010 10.0  793899   1.9059E-03 0.0011 0.0000 10.0 5239338
       320000   1.1637E+00 0.0010 0.0001  4.1 5272005   4.3090E-03 0.0027 0.0008 10.0  778628   1.9081E-03 0.0010 0.0000 10.0 5218140
       384000   1.1638E+00 0.0009 0.0001  4.7 5282779   4.3131E-03 0.0024 0.0007 10.0  769046   1.9080E-03 0.0009 0.0000  9.5 5217774
       448000   1.1638E+00 0.0009 0.0001  4.2 5253643   4.3155E-03 0.0023 0.0006  4.1  764059   1.9082E-03 0.0009 0.0000 10.0 5220259
       512000   1.1636E+00 0.0008 0.0001 10.0 5258141   4.3131E-03 0.0021 0.0005  5.3  770384   1.9086E-03 0.0008 0.0000 10.0 5219080
       576000   1.1633E+00 0.0008 0.0001 10.0 5264878   4.3124E-03 0.0020 0.0004  5.6  768500   1.9081E-03 0.0008 0.0000 10.0 5219372
       640000   1.1631E+00 0.0007 0.0001 10.0 5263144   4.3132E-03 0.0019 0.0004  5.7  766088   1.9084E-03 0.0007 0.0000 10.0 5212119
       704000   1.1634E+00 0.0007 0.0000 10.0 5254766   4.3118E-03 0.0018 0.0003  6.0  769973   1.9086E-03 0.0007 0.0000 10.0 5207198
       768000   1.1633E+00 0.0007 0.0000 10.0 5269129   4.3109E-03 0.0017 0.0003  7.3  771472   1.9087E-03 0.0007 0.0000 10.0 5209161
       832000   1.1634E+00 0.0006 0.0000 10.0 5270219   4.3117E-03 0.0017 0.0003  6.9  771657   1.9092E-03 0.0006 0.0000 10.0 5206558
       896000   1.1633E+00 0.0006 0.0000 10.0 5264725   4.3100E-03 0.0016 0.0003  5.6  771465   1.9092E-03 0.0006 0.0000 10.0 5204363
       960000   1.1633E+00 0.0006 0.0000 10.0 5271305   4.3104E-03 0.0015 0.0003  4.9  769277   1.9094E-03 0.0006 0.0000 10.0 5202442
      1000000   1.1633E+00 0.0006 0.0000 10.0 5270057   4.3104E-03 0.0015 0.0002  4.5  768706   1.9097E-03 0.0006 0.0000 10.0 5199920
 

                            tally        5                          tally        6                          tally        8
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   3.3967E-04 0.0091 0.0076  4.7  329076   4.3069E-05 0.0007 0.0001 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       128000   3.4847E-04 0.0151 0.5389  2.6   60432   4.3076E-05 0.0005 0.0001 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       192000   3.4647E-04 0.0106 0.4472  2.6   81586   4.3055E-05 0.0004 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       256000   3.4604E-04 0.0083 0.3737  2.6   99119   4.3042E-05 0.0004 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       320000   3.4612E-04 0.0069 0.3225  2.4  114957   4.3036E-05 0.0003 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       384000   3.4555E-04 0.0060 0.2722  2.5  126234   4.3040E-05 0.0003 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       448000   3.4517E-04 0.0053 0.2393  2.5  137742   4.3040E-05 0.0003 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       512000   3.4463E-04 0.0048 0.2159  2.4  149020   4.3045E-05 0.0003 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       576000   3.4427E-04 0.0044 0.1942  2.3  158702   4.3051E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       640000   3.4401E-04 0.0040 0.1776  2.3  168334   4.3056E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       704000   3.4461E-04 0.0040 0.1296  2.1  151875   4.3054E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       768000   3.4409E-04 0.0038 0.1207  2.0  159347   4.3051E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       832000   3.4381E-04 0.0036 0.1126  2.1  166447   4.3053E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       896000   3.4397E-04 0.0034 0.1042  2.2  172458   4.3053E-05 0.0002 0.0000 10.0 5.3E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       960000   3.4409E-04 0.0032 0.0954  2.2  176878   4.3050E-05 0.0002 0.0000 10.0 5.2E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
      1000000   3.4403E-04 0.0031 0.0912  2.2  180024   4.3049E-05 0.0002 0.0000 10.0 5.2E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30

 ***********************************************************************************************************************

 dump no.    2 on file singles_et.ir     nps =     1000000     coll =        1690149     ctm =        0.57   nrn =      
    35178899

        11 warning messages so far.


 run terminated when     1000000  particle histories were done.

 computer time =    0.58 minutes

 mcnp     version 6.mpi 04/01/16                     02/16/21 11:47:31                     probid =  02/16/21 11:46:56 
