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
  
1mcnp     version 6.mpi ld=01/13/25                     07/24/25 09:41:12 
 *************************************************************************                 probid =  07/24/25 09:41:12 
 n=multiple_et.i XSDIR=/home/vol03/scarf473/neutronic_data1/mcnpx_data/xsdir     

 
  warning.  Physics models disabled.
         1-       c test input to generate output for MCNP output reader                          
         2-       1 0 -1 imp:p=1                                                                  
         3-       2 1 -2.7 1 -2 imp:p=1                                                           
         4-       3 1 -2.7 -3 2 imp:p=1                                                           
         5-       4 1 -2.7 -4 3 imp:p=1                                                           
         6-       5 1 -2.7 -5 4 imp:p=1                                                           
         7-       6 1 -2.7 -6 5 imp:p=1                                                           
         8-       99 0 6 imp:p=0                                                                  
         9-                                                                                       
        10-       c                                                                               
        11-       1 so 5                                                                          
        12-       2 so 10                                                                         
        13-       3 so 20                                                                         
        14-       4 so 30                                                                         
        15-       5 so 40                                                                         
        16-       6 so 50                                                                         
        17-                                                                                       
        18-       c                                                                               
        19-       mode p                                                                          
        20-       nps 1e6                                                                         
        21-       m1 13027.24c 1  $ Al27                                                          
  warning.  neutron table inconsistent with mode will be ignored.
        22-       sdef erg=1.332 par=p                                                            
        23-       f1:p 1 2 3 4 5 6                                                                
        24-       e1  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        25-       t1 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        26-       f2:p 1 2 3 4 5 6                                                                
        27-       e2  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        28-       t2 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        29-       f4:p 2 3 4 5 6                                                                  
        30-       e4  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        31-       t4 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        32-       f5:p 15 0 0 1                                                                   
        33-       e5  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        34-       t5 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        35-       f6:p 2 3 4 5 6                                                                  
        36-       e6  0.1 0.2 0.3 0.4 0.5 0.6 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5                       
        37-       t6 0 1 2 3 4 5 6 7 8 9 10 50 100                                                
        38-       f8:p 2 3 4 5 6                                                                  
        39-                                                                                       
 
  warning.  last time bin of tally        1 is less than time cutoff.
 
  warning.  last time bin of tally        2 is less than time cutoff.
 
  warning.  last time bin of tally        4 is less than time cutoff.
 
  warning.  last time bin of tally        5 is less than time cutoff.
 
  warning.  last time bin of tally        6 is less than time cutoff.
1cells                                                                                                  print table 60

                               atom        gram                                            photon                                      
              cell      mat   density     density     volume       mass            pieces importance                                   

        1        1        0  0.00000E+00 0.00000E+00 5.23599E+02 0.00000E+00           1  1.0000E+00                                   
        2        2        1  6.02616E-02 2.70000E+00 3.66519E+03 9.89602E+03           1  1.0000E+00                                   
        3        3        1  6.02616E-02 2.70000E+00 2.93215E+04 7.91681E+04           1  1.0000E+00                                   
        4        4        1  6.02616E-02 2.70000E+00 7.95870E+04 2.14885E+05           1  1.0000E+00                                   
        5        5        1  6.02616E-02 2.70000E+00 1.54985E+05 4.18460E+05           1  1.0000E+00                                   
        6        6        1  6.02616E-02 2.70000E+00 2.55516E+05 6.89894E+05           1  1.0000E+00                                   
        7       99        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00                                   

 total                                               5.23599E+05 1.41230E+06

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

         8 warning messages so far.
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

 dump no.    1 on file multiple_et.ir     nps =           0     coll =              0     ctm =        0.00   nrn =     
            0

         9 warning messages so far.
 master starting      11 MPI slave tasks with       1 threads each  07/24/25 09:41:12 
 master set rendezvous nps =        1000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        2000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        3000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        4000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        5000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        6000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        7000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        8000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =        9000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       10000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       11000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       12000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       13000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       14000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       15000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       16000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       17000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       18000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       19000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       20000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       22000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       24000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       26000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       28000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       30000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       32000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       34000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       36000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       38000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       40000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       44000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       48000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       52000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       56000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       60000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       64000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       68000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       72000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       76000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       80000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       88000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =       96000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =      104000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =      112000,  work chunks =    11    07/24/25 09:41:12 
 master set rendezvous nps =      120000,  work chunks =    11    07/24/25 09:41:12 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.1494E-01 1.0000E+00 1.3980E+00 1.2061E-01 7.2513E-01 1.0000E+00 9.9314E-01     3      116024    1                  21         7   
 master set rendezvous nps =      128000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      136000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      144000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      152000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      160000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      176000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      192000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      208000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      224000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      240000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      256000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      272000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      288000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      304000,  work chunks =    11    07/24/25 09:41:13 
 master set rendezvous nps =      320000,  work chunks =    11    07/24/25 09:41:14 
 master set rendezvous nps =      352000,  work chunks =    11    07/24/25 09:41:14 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.2161E-01 1.0000E+00 1.1915E+00 1.5570E-01 8.8393E-01 1.0000E+00 8.8136E-01     3      331811    2                  37         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1197E-01 1.0000E+00 1.2278E+00 2.3788E-01 8.5766E-01 1.0000E+00 3.1048E-01     3      348527    2                  43         7   
 master set rendezvous nps =      384000,  work chunks =    11    07/24/25 09:41:14 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.0490E+00 1.0000E+00 8.6460E+01 1.1080E+00 2.0813E+00 1.0000E+00 8.2178E-02     3      379875   10                 156         6   
 master set rendezvous nps =      416000,  work chunks =    11    07/24/25 09:41:14 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 9.3537E-01 1.0000E+00 2.1127E+00 1.5089E-01 9.8646E-01 1.0000E+00 1.1731E+00     3      411577    2                  37         7   
 master set rendezvous nps =      448000,  work chunks =    11    07/24/25 09:41:14 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.6960E-01 1.0000E+00 1.2966E+00 1.1753E-01 6.9558E-01 1.0000E+00 9.6106E-01     3      428213    1                  18         7   
 master set rendezvous nps =      480000,  work chunks =    11    07/24/25 09:41:14 
 master set rendezvous nps =      512000,  work chunks =    11    07/24/25 09:41:14 
 master set rendezvous nps =      544000,  work chunks =    11    07/24/25 09:41:15 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 2.2248E+00 1.0000E+00 1.8094E+02 9.1676E-01 2.2749E+00 1.0000E+00 1.2650E-01     3      517734    7                 116         6   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.2863E-01 1.0000E+00 1.4796E+00 1.8074E-01 7.5876E-01 1.0000E+00 4.4982E-01     3      533359    2                  33         7   
 master set rendezvous nps =      576000,  work chunks =    11    07/24/25 09:41:15 
 master set rendezvous nps =      608000,  work chunks =    11    07/24/25 09:41:15 
 master set rendezvous nps =      640000,  work chunks =    11    07/24/25 09:41:15 
 master set rendezvous nps =      704000,  work chunks =    11    07/24/25 09:41:15 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 4.9554E-01 1.0000E+00 1.1315E+00 1.7453E-01 9.9520E-01 1.0000E+00 8.8946E-01     3      683349    1                  18         7   
 master set rendezvous nps =      768000,  work chunks =    11    07/24/25 09:41:16 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 9.2458E-01 1.0000E+00 2.0943E+00 1.4486E-01 9.1212E-01 1.0000E+00 1.0886E+00     3      705442    2                  36         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1281E-01 1.0000E+00 5.4132E+01 1.2642E+00 2.1784E+00 1.0000E+00 7.4772E-02     3      730019   12                 171         6   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.7757E-01 1.0000E+00 1.5639E+00 1.7409E-01 8.8090E-01 1.0000E+00 6.8916E-01     3      733455    2                  42         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.0015E+00 1.0000E+00 2.2652E+00 1.4303E-01 9.1817E-01 1.0000E+00 1.1311E+00     3      742456    3                  58         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1495E-01 1.0000E+00 1.2302E+00 2.1885E-01 8.1306E-01 1.0000E+00 3.3432E-01     3      758051    3                  56         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 4.8589E-01 1.0000E+00 1.1379E+00 2.1326E-01 9.3646E-01 1.0000E+00 5.0084E-01     3      767536    3                  53         7   
 master set rendezvous nps =      832000,  work chunks =    11    07/24/25 09:41:16 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.7558E-01 1.0000E+00 1.5333E+00 6.0166E-02 3.6937E-01 1.0000E+00 1.0354E+00     3      770515    1                  21         7   
 master set rendezvous nps =      896000,  work chunks =    11    07/24/25 09:41:16 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.5995E-01 1.0000E+00 1.5005E+00 1.1994E-01 7.2017E-01 1.0000E+00 9.9038E-01     3      836063    2                  36         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 4.8602E-01 1.0000E+00 1.1626E+00 2.0595E-01 7.5724E-01 1.0000E+00 3.2596E-01     3      877218    2                  45         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.1754E+00 1.0000E+00 2.6429E+00 1.1418E-01 7.9440E-01 1.0000E+00 1.3260E+00     3      890127    1                  21         7   
 master set rendezvous nps =      960000,  work chunks =    11    07/24/25 09:41:17 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1224E-01 1.0000E+00 1.1682E+00 1.4497E-01 8.3904E-01 1.0000E+00 9.1751E-01     3      898040    2                  34         7   
 master set rendezvous nps =     1000000,  work chunks =    11    07/24/25 09:41:17 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.9351E+00 1.0000E+00 5.4875E+00 3.3889E-01 5.2944E-01 1.0000E+00 6.8145E-02     3      986108    6                 101         6   
1problem summary                                                                                                           

      run terminated when     1000000  particle histories were done.
+                                                                                                    07/24/25 09:41:17 
      c test input to generate output for MCNP output reader                               probid =  07/24/25 09:41:12 

 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source             1000000    1.0000E+00    1.3320E+00          escape               23412    2.3412E-02    1.3233E-02
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            5.6963E-05
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 from neutrons            0    0.            0.                  compton scatter          0    0.            1.2430E+00
 bremsstrahlung      215317    2.1532E-01    6.3617E-03          capture            1232773    1.2328E+00    8.1706E-02
 p-annihilation        2736    2.7360E-03    1.3981E-03          pair production       1368    1.3680E-03    1.8171E-03
 photonuclear             0    0.            0.                  photonuclear abs         0    0.            0.        
 electron x-rays          0    0.            0.                  loss to photofis         0    0.            0.        
 compton fluores          0    0.            0.                                                                        
 muon capt fluores        0    0.            0.                                                                        
 1st fluorescence     39500    3.9500E-02    5.8044E-05                                                                
 2nd fluorescence         0    0.            0.                                                                        
 cerenkov                 0    0.            0.                                                                        
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total          1257553    1.2576E+00    1.3398E+00              total          1257553    1.2576E+00    1.3398E+00

   number of photons banked                   218053        average time of (shakes)              cutoffs
   photon tracks per source particle      1.2576E+00          escape            1.8676E-01          tco   1.0000E+33
   photon collisions per source particle  1.0414E+01          capture           1.0956E-01          eco   1.0000E-03
   total photon collisions                  10413845          capture or escape 1.1099E-01          wc1   0.0000E+00
                                                              any termination   1.1092E-01          wc2   0.0000E+00

 computer time so far in this run     1.07 minutes            maximum number ever in bank         4
 computer time in mcrun               0.83 minutes            bank overflows to backup file       0
 source particles per minute            1.2030E+06
 random numbers generated                179108174            most random numbers used was         696 in history      973139

 range of sampled source weights = 1.0000E+00 to 1.0000E+00

 estimated system efficiency for MPI usage =  9%

 number of histories processed by each MPI task
           0       90866       90916       90897       90926       90906       90902       90906       90926       90897
       90916       90942
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1     1099615      1000976            0    0.0000E+00   1.1988E+00   1.1988E+00   1.0000E+00   0.0000E+00
        2        2     1259653      1077623      2185853    2.1859E+00   7.6851E-01   7.6851E-01   1.0000E+00   4.9327E+00
        3        3     1128922      1019050      4460672    4.4607E+00   5.3081E-01   5.3081E-01   1.0000E+00   4.0599E+00
        4        4      597112       535477      2438904    2.4389E+00   4.2445E-01   4.2445E-01   1.0000E+00   3.6627E+00
        5        5      240910       215113       998093    9.9809E-01   3.8252E-01   3.8252E-01   1.0000E+00   3.5045E+00
        6        6       78563        75809       330323    3.3032E-01   3.7341E-01   3.7341E-01   1.0000E+00   3.4837E+00

           total       4404775      3924048     10413845    1.0414E+01

1tally        1        nps =     1000000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  1                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   4.27940E-02 0.0078   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   7.55500E-02 0.0054   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   7.74340E-02 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   3.06600E-03 0.0256   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   5.20000E-05 0.1961   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   3.34000E-04 0.0774   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   1.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.19923E+00 0.0006   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.27940E-02 0.0078
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.55500E-02 0.0054
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.74340E-02 0.0050
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.06600E-03 0.0256
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.20000E-05 0.1961
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.34000E-04 0.0774
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.19923E+00 0.0006
 
 surface  2                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.16537E-01 0.0035   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.77897E-01 0.0026   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   9.34930E-02 0.0033   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   3.77360E-02 0.0052   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   3.27030E-02 0.0055   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   3.04480E-02 0.0057   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   5.48860E-02 0.0041   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.59820E-02 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.60230E-02 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.62010E-02 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.62880E-02 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.68970E-02 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   4.97970E-01 0.0010   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.17306E+00 0.0006   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.16537E-01 0.0035
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.77897E-01 0.0026
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.34930E-02 0.0033
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.77360E-02 0.0052
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.27030E-02 0.0055
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.04480E-02 0.0057
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.48860E-02 0.0041
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.59820E-02 0.0061
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.60230E-02 0.0061
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.62010E-02 0.0061
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.62880E-02 0.0061
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.68970E-02 0.0060
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.97970E-01 0.0010
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.17306E+00 0.0006
 
 surface  3                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   9.96140E-02 0.0038   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.38406E-01 0.0029   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   6.29830E-02 0.0040   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   3.34090E-02 0.0054   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   2.84380E-02 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   2.62550E-02 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   4.66000E-02 0.0045   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.11830E-02 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.05320E-02 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.03220E-02 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   1.98220E-02 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   1.97460E-02 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   1.22827E-01 0.0027   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   6.60137E-01 0.0013   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.96140E-02 0.0038
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.38406E-01 0.0029
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.29830E-02 0.0040
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.34090E-02 0.0054
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.84380E-02 0.0059
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.62550E-02 0.0061
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.66000E-02 0.0045
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.11830E-02 0.0068
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.05320E-02 0.0069
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.03220E-02 0.0069
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.98220E-02 0.0070
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.97460E-02 0.0070
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.22827E-01 0.0027
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.60137E-01 0.0013
 
 surface  4                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   4.65300E-02 0.0056   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   6.34000E-02 0.0044   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   2.80530E-02 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   1.58270E-02 0.0079   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.33270E-02 0.0086   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.20570E-02 0.0091   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.13280E-02 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   9.40300E-03 0.0103   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   8.97100E-03 0.0105   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   8.53900E-03 0.0108   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   8.29500E-03 0.0109   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   8.08400E-03 0.0111   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.04530E-02 0.0056   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   2.74267E-01 0.0023   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.65300E-02 0.0056
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.34000E-02 0.0044
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.80530E-02 0.0060
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.58270E-02 0.0079
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.33270E-02 0.0086
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.20570E-02 0.0091
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.13280E-02 0.0068
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.40300E-03 0.0103
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.97100E-03 0.0105
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.53900E-03 0.0108
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.29500E-03 0.0109
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.08400E-03 0.0111
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.04530E-02 0.0056
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.74267E-01 0.0023
 
 surface  5                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.75650E-02 0.0092   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.36060E-02 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.03900E-02 0.0100   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   5.92400E-03 0.0130   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   5.02200E-03 0.0141   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   4.65000E-03 0.0146   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   7.88400E-03 0.0112   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   3.48600E-03 0.0169   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   3.22000E-03 0.0176   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   3.09700E-03 0.0179   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.92000E-03 0.0185   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.79200E-03 0.0189   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   7.52400E-03 0.0115   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   9.80800E-02 0.0041   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.75650E-02 0.0092
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.36060E-02 0.0073
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.03900E-02 0.0100
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.92400E-03 0.0130
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.02200E-03 0.0141
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.65000E-03 0.0146
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.88400E-03 0.0112
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.48600E-03 0.0169
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.22000E-03 0.0176
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.09700E-03 0.0179
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.92000E-03 0.0185
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.79200E-03 0.0189
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.52400E-03 0.0115
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.80800E-02 0.0041
 
 surface  6                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.08300E-03 0.0219   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   4.21100E-03 0.0154   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   2.38000E-03 0.0205   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   1.85900E-03 0.0232   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.64300E-03 0.0247   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.57900E-03 0.0251   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.73500E-03 0.0191   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   1.19400E-03 0.0289   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.06100E-03 0.0307   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   9.98000E-04 0.0316   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   8.91000E-04 0.0335   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   8.73000E-04 0.0338   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   1.90500E-03 0.0229   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   2.34120E-02 0.0065   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.08300E-03 0.0219
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.21100E-03 0.0154
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.38000E-03 0.0205
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.85900E-03 0.0232
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.64300E-03 0.0247
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.57900E-03 0.0251
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.73500E-03 0.0191
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.19400E-03 0.0289
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.06100E-03 0.0307
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.98000E-04 0.0316
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.91000E-04 0.0335
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.73000E-04 0.0338
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.90500E-03 0.0229
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.34120E-02 0.0065


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       3.75
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.1985E+00 to 1.2000E+00; 1.1978E+00 to 1.2007E+00; 1.1970E+00 to 1.2014E+00
 estimated  symmetric confidence interval(1,2,3 sigma): 1.1985E+00 to 1.2000E+00; 1.1978E+00 to 1.2007E+00; 1.1970E+00 to 1.2014E+00

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        1 with nps =     1000000  print table 160


 normed average tally per history  = 1.19923E+00          unnormed average tally per history  = 1.19923E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =       14112          largest  unnormalized history tally = 1.50000E+01
 (largest  tally)/(average tally)  = 1.25080E+01          (largest  tally)/(avg nonzero tally)= 1.25080E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.19923E+00


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.19923E+00             1.19924E+00                     0.000012
      relative error                  6.14990E-04             6.15090E-04                     0.000163
      variance of the variance        2.64457E-05             2.65487E-05                     0.003894
      shifted center                  1.19923E+00             1.19923E+00                     0.000000
      figure of merit                 3.18085E+06             3.17981E+06                    -0.000325

 the estimated inverse power slope of the  62 largest  tallies starting at 1.08214E+01 is 3.7480
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.203E+06)*( 1.626E+00)**2 = (1.203E+06)*(2.644E+00) = 3.181E+06

1tally        2        nps =     1000000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): photons  

           areas   
                surface:       1            2            3            4            5            6                  
                         3.14159E+02  1.25664E+03  5.02655E+03  1.13097E+04  2.01062E+04  3.14159E+04
 
 surface  1                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.80437E-04 0.0112   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   4.95648E-04 0.0080   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   5.02773E-04 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   6.73295E-05 0.0331   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   6.85389E-07 0.3096   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   2.68835E-06 0.1214   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.18310E-03 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   4.53266E-03 0.0016   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.80437E-04 0.0112
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.95648E-04 0.0080
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.02773E-04 0.0073
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.73295E-05 0.0331
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.85389E-07 0.3096
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.68835E-06 0.1214
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.18310E-03 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.53266E-03 0.0016
 
 surface  2                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.82022E-04 0.0054   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.70974E-04 0.0042   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.42959E-04 0.0057   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   7.28964E-05 0.0096   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   4.70685E-05 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   3.59102E-05 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   5.52442E-05 0.0042   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.37212E-05 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.27665E-05 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.21986E-05 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.16979E-05 0.0061   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.17285E-05 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.96292E-04 0.0010   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.31548E-03 0.0015   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.82022E-04 0.0054
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.70974E-04 0.0042
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.42959E-04 0.0057
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.28964E-05 0.0096
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.70685E-05 0.0069
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.59102E-05 0.0061
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.52442E-05 0.0042
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.37212E-05 0.0061
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.27665E-05 0.0061
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.21986E-05 0.0061
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.16979E-05 0.0061
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.17285E-05 0.0060
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.96292E-04 0.0010
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.31548E-03 0.0015
 
 surface  3                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   3.88020E-05 0.0056   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   5.20893E-05 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   2.39340E-05 0.0066   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   1.34556E-05 0.0096   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   9.23167E-06 0.0076   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   7.23160E-06 0.0065   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   1.12298E-05 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   4.70785E-06 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   4.40422E-06 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   4.24640E-06 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   4.05498E-06 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   3.97402E-06 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   2.44384E-05 0.0027   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   2.01800E-04 0.0021   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.88020E-05 0.0056
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.20893E-05 0.0046
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.39340E-05 0.0066
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.34556E-05 0.0096
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.23167E-06 0.0076
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.23160E-06 0.0065
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.12298E-05 0.0046
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.70785E-06 0.0068
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.40422E-06 0.0069
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.24640E-06 0.0069
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.05498E-06 0.0070
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.97402E-06 0.0070
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.44384E-05 0.0027
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.01800E-04 0.0021
 
 surface  4                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   8.01069E-06 0.0079   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.06579E-05 0.0067   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   4.72805E-06 0.0098   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   2.73494E-06 0.0136   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.90213E-06 0.0117   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.46018E-06 0.0098   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.28099E-06 0.0069   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   9.25147E-07 0.0103   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   8.52570E-07 0.0105   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   7.90955E-07 0.0108   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   7.52712E-07 0.0109   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   7.22413E-07 0.0111   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   2.69306E-06 0.0056   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   3.85118E-05 0.0035   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.01069E-06 0.0079
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.06579E-05 0.0067
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.72805E-06 0.0098
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.73494E-06 0.0136
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.90213E-06 0.0117
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.46018E-06 0.0098
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.28099E-06 0.0069
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.25147E-07 0.0103
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.52570E-07 0.0105
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.90955E-07 0.0108
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.52712E-07 0.0109
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.22413E-07 0.0111
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.69306E-06 0.0056
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.85118E-05 0.0035
 
 surface  5                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.72110E-06 0.0131   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.24935E-06 0.0109   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   9.89719E-07 0.0157   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   5.56999E-07 0.0217   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   4.02044E-07 0.0190   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   3.16327E-07 0.0154   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   4.73338E-07 0.0114   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   1.92928E-07 0.0170   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.72036E-07 0.0176   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   1.61155E-07 0.0180   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   1.48963E-07 0.0185   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   1.40319E-07 0.0189   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.74293E-07 0.0115   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   7.89857E-06 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.72110E-06 0.0131
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.24935E-06 0.0109
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.89719E-07 0.0157
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.56999E-07 0.0217
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.02044E-07 0.0190
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.16327E-07 0.0154
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.73338E-07 0.0114
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.92928E-07 0.0170
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.72036E-07 0.0176
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.61155E-07 0.0180
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.48963E-07 0.0185
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.40319E-07 0.0189
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.74293E-07 0.0115
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.89857E-06 0.0060
 
 surface  6                                                                                                                            
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.15318E-07 0.0311   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.26346E-07 0.0207   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.30853E-07 0.0273   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   9.68921E-08 0.0316   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   8.12759E-08 0.0292   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   6.88297E-08 0.0268   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   1.06337E-07 0.0195   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   4.22715E-08 0.0290   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   3.63675E-08 0.0307   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   3.32757E-08 0.0317   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.90783E-08 0.0335   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.80783E-08 0.0338   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   6.06567E-08 0.0229   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.05558E-06 0.0083   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.15318E-07 0.0311
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.26346E-07 0.0207
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.30853E-07 0.0273
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.68921E-08 0.0316
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.12759E-08 0.0292
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.88297E-08 0.0268
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.06337E-07 0.0195
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.22715E-08 0.0290
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.63675E-08 0.0307
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.32757E-08 0.0317
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.90783E-08 0.0335
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.80783E-08 0.0338
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.06567E-08 0.0229
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.05558E-06 0.0083


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       4.52
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.5256E-03 to 4.5398E-03; 4.5186E-03 to 4.5468E-03; 4.5115E-03 to 4.5539E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 4.5256E-03 to 4.5397E-03; 4.5185E-03 to 4.5468E-03; 4.5115E-03 to 4.5539E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        2 with nps =     1000000  print table 160


 normed average tally per history  = 4.53266E-03          unnormed average tally per history  = 1.42398E+00
 estimated tally relative error    = 0.0016               estimated variance of the variance  = 0.0002
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0016

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      424677          largest  unnormalized history tally = 9.03830E+01
 (largest  tally)/(average tally)  = 6.34722E+01          (largest  tally)/(avg nonzero tally)= 6.34722E+01

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.53270E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.53266E-03             4.53294E-03                     0.000062
      relative error                  1.55859E-03             1.55974E-03                     0.000739
      variance of the variance        2.19889E-04             2.21752E-04                     0.008472
      shifted center                  4.53270E-03             4.53270E-03                     0.000000
      figure of merit                 4.95240E+05             4.94508E+05                    -0.001477

 the estimated inverse power slope of the 200 largest  tallies starting at 4.72133E+01 is 4.5157
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.203E+06)*( 6.416E-01)**2 = (1.203E+06)*(4.117E-01) = 4.952E+05

1tally        4        nps =     1000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2            3            4            5            6                               
                         3.66519E+03  2.93215E+04  7.95870E+04  1.54985E+05  2.55516E+05
 
 cell  2                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   2.31217E-04 0.0028   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   3.71011E-04 0.0022   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   2.34564E-04 0.0026   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   9.69313E-05 0.0037   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   5.59965E-05 0.0045   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   4.14792E-05 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   6.14137E-05 0.0039   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.63769E-05 0.0058   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.52803E-05 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.44470E-05 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.39176E-05 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.39109E-05 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   9.82236E-04 0.0005   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   2.19878E-03 0.0006   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.31217E-04 0.0028
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.71011E-04 0.0022
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.34564E-04 0.0026
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.69313E-05 0.0037
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.59965E-05 0.0045
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.14792E-05 0.0050
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.14137E-05 0.0039
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.63769E-05 0.0058
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.52803E-05 0.0059
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.44470E-05 0.0059
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.39176E-05 0.0060
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.39109E-05 0.0059
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.82236E-04 0.0005
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.19878E-03 0.0006
 
 cell  3                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   7.90347E-05 0.0016   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.10774E-04 0.0014   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   5.33123E-05 0.0020   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   2.89443E-05 0.0028   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.94779E-05 0.0034   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.51554E-05 0.0038   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.35826E-05 0.0030   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   9.99584E-06 0.0047   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   9.45785E-06 0.0048   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   9.19814E-06 0.0049   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   8.94829E-06 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   8.86192E-06 0.0051   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   9.14192E-05 0.0014   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   4.68163E-04 0.0006   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.90347E-05 0.0016
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.10774E-04 0.0014
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.33123E-05 0.0020
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.89443E-05 0.0028
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.94779E-05 0.0034
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.51554E-05 0.0038
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.35826E-05 0.0030
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.99584E-06 0.0047
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.45785E-06 0.0048
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.19814E-06 0.0049
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.94829E-06 0.0050
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.86192E-06 0.0051
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.14192E-05 0.0014
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.68163E-04 0.0006
 
 cell  4                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.75763E-05 0.0022   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.34667E-05 0.0020   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.05187E-05 0.0029   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   6.00659E-06 0.0039   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   4.17331E-06 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   3.28528E-06 0.0051   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   5.02967E-06 0.0042   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.08370E-06 0.0065   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.93115E-06 0.0067   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   1.82427E-06 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   1.75458E-06 0.0072   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   1.70234E-06 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   8.30899E-06 0.0033   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   8.76616E-05 0.0013   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.75763E-05 0.0022
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.34667E-05 0.0020
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.05187E-05 0.0029
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.00659E-06 0.0039
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.17331E-06 0.0046
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.28528E-06 0.0051
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.02967E-06 0.0042
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.08370E-06 0.0065
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.93115E-06 0.0067
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.82427E-06 0.0070
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.75458E-06 0.0072
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.70234E-06 0.0073
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.30899E-06 0.0033
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.76616E-05 0.0013
 
 cell  5                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   3.81909E-06 0.0036   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   4.99575E-06 0.0033   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   2.20625E-06 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   1.27563E-06 0.0062   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   9.07766E-07 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   6.93954E-07 0.0082   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   1.06322E-06 0.0067   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   4.28038E-07 0.0104   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   3.93040E-07 0.0109   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   3.64772E-07 0.0114   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   3.45594E-07 0.0118   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   3.25940E-07 0.0121   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   1.05899E-06 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.78780E-05 0.0024   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.81909E-06 0.0036
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.99575E-06 0.0033
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.20625E-06 0.0046
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.27563E-06 0.0062
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.07766E-07 0.0073
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.93954E-07 0.0082
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.06322E-06 0.0067
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.28038E-07 0.0104
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.93040E-07 0.0109
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.64772E-07 0.0114
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.45594E-07 0.0118
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.25940E-07 0.0121
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.05899E-06 0.0068
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.78780E-05 0.0024
 
 cell  6                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   7.50250E-07 0.0065   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.00683E-06 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   4.57874E-07 0.0081   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   2.71364E-07 0.0105   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.90908E-07 0.0124   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.49477E-07 0.0138   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.32846E-07 0.0113   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   9.40988E-08 0.0176   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   8.28688E-08 0.0186   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   7.53696E-08 0.0196   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   6.93619E-08 0.0205   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   6.57105E-08 0.0211   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   1.58774E-07 0.0138   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   3.60573E-06 0.0043   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.50250E-07 0.0065
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.00683E-06 0.0059
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.57874E-07 0.0081
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.71364E-07 0.0105
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.90908E-07 0.0124
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.49477E-07 0.0138
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.32846E-07 0.0113
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.40988E-08 0.0176
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.28688E-08 0.0186
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.53696E-08 0.0196
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.93619E-08 0.0205
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.57105E-08 0.0211
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.58774E-07 0.0138
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.60573E-06 0.0043


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

 estimated asymmetric confidence interval(1,2,3 sigma): 2.1974E-03 to 2.2002E-03; 2.1959E-03 to 2.2016E-03; 2.1945E-03 to 2.2030E-03
 estimated  symmetric confidence interval(1,2,3 sigma): 2.1974E-03 to 2.2002E-03; 2.1959E-03 to 2.2016E-03; 2.1945E-03 to 2.2030E-03

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =     1000000  print table 160


 normed average tally per history  = 2.19878E-03          unnormed average tally per history  = 8.05895E+00
 estimated tally relative error    = 0.0006               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0006

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      550118          largest  unnormalized history tally = 6.03797E+01
 (largest  tally)/(average tally)  = 7.49225E+00          (largest  tally)/(avg nonzero tally)= 7.49225E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.19878E-03


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            2.19878E-03             2.19880E-03                     0.000006
      relative error                  6.45067E-04             6.45095E-04                     0.000043
      variance of the variance        6.08308E-06             6.09182E-06                     0.001437
      shifted center                  2.19878E-03             2.19878E-03                     0.000000
      figure of merit                 2.89114E+06             2.89089E+06                    -0.000086

 the estimated slope of the 198 largest  tallies starting at  3.93632E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.203E+06)*( 1.550E+00)**2 = (1.203E+06)*(2.403E+00) = 2.891E+06

1tally        5        nps =     1000000
           tally type 5    particle flux at a point detector.           units   1/cm**2        
           particle(s): photons  
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   8.40695E-05 0.0513   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.21597E-04 0.0342   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   5.58551E-05 0.0388   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   3.30678E-05 0.0538   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   2.06767E-05 0.0582   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.63688E-05 0.0661   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.32744E-05 0.0455   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   1.14989E-05 0.0930   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.22196E-05 0.1115   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   9.91175E-06 0.1215   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   1.00911E-05 0.1414   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   9.17376E-06 0.0625   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   8.83577E-05 0.0137   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   4.96162E-04 0.0168   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.40695E-05 0.0513
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.21597E-04 0.0342
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.58551E-05 0.0388
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.30678E-05 0.0538
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.06767E-05 0.0582
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.63688E-05 0.0661
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.32744E-05 0.0455
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.14989E-05 0.0930
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.22196E-05 0.1115
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.91175E-06 0.1215
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.00911E-05 0.1414
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.17376E-06 0.0625
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.83577E-05 0.0137
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.96162E-04 0.0168
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   3.82074E-07 0.3388   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.18122E-07 0.2098   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   7.21989E-08 0.2876   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   4.44229E-08 0.2896   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   2.07868E-08 0.2818   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.21445E-07 0.1211   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   1.91812E-08 0.8191   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   1.36819E-10 0.5503   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.79229E-10 0.6287   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   4.19282E-11 1.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   8.43023E-05 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   8.51809E-05 0.0017   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.82074E-07 0.3388
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.18122E-07 0.2098
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.21989E-08 0.2876
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.44229E-08 0.2896
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.07868E-08 0.2818
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.21445E-07 0.1211
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.91812E-08 0.8191
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.36819E-10 0.5503
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.79229E-10 0.6287
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.19282E-11 1.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.43023E-05 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.51809E-05 0.0017
 
 detector score diagnostics                  cumulative          tally         cumulative
                                             fraction of         per           fraction of
   times average score     transmissions     transmissions       history       total tally
        1.00000E-01            2932522         0.68026        1.37519E-05        0.02772
        1.00000E+00            1281447         0.97752        1.27894E-04        0.28548
        2.00000E+00              37711         0.98626        2.56360E-05        0.33715
        5.00000E+00              28670         0.99292        4.26805E-05        0.42317
        1.00000E+01              10173         0.99528        3.40965E-05        0.49189
        1.00000E+02               9337         0.99744        1.09129E-04        0.71184
        1.00000E+03                835         0.99763        1.25369E-04        0.96452
        1.00000E+38                 21         0.99764        1.71131E-05        0.99901
 before dd roulette              10175         1.00000        4.92434E-07        1.00000

 average tally per history = 4.96162E-04            largest score = 2.22478E+00
 (largest score)/(average tally) = 4.48398E+03      nps of largest score =      517734

 score contributions by cell
        cell      misses        hits    tally per history    weight per hit
     1     1           0     1000000       8.43023E-05         8.43023E-05
     2     2     1361009      677098       4.54100E-05         6.70657E-05
     3     3     2010064     2025490       3.64141E-04         1.79779E-04
     4     4     1574906      604054       2.29977E-06         3.80723E-06
     5     5      884601        3985       8.61551E-09         2.16198E-06
     6     6      294418         264       3.27451E-11         1.24035E-07
       total     6124998     4310891       4.96162E-04         1.15095E-04

 score misses
   russian roulette on pd                        0
   psc=0.                                        0
   russian roulette in transmission        5999373
   underflow in transmission                125625
   hit a zero-importance cell                    0
   energy cutoff                                 0


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        5

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.02      yes          yes            0.01      yes         yes            constant    random       8.52
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.8820E-04 to 5.0486E-04; 4.7987E-04 to 5.1319E-04; 4.7153E-04 to 5.2152E-04
 estimated  symmetric confidence interval(1,2,3 sigma): 4.8784E-04 to 5.0449E-04; 4.7951E-04 to 5.1281E-04; 4.7119E-04 to 5.2114E-04

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        5 with nps =     1000000  print table 160


 normed average tally per history  = 4.96162E-04          unnormed average tally per history  = 4.96162E-04
 estimated tally relative error    = 0.0168               estimated variance of the variance  = 0.0141
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0168

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      517734          largest  unnormalized history tally = 2.25950E+00
 (largest  tally)/(average tally)  = 4.55396E+03          (largest  tally)/(avg nonzero tally)= 4.55396E+03

 (confidence interval shift)/mean  = 0.0007               shifted confidence interval center  = 4.96529E-04


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.96162E-04             4.98421E-04                     0.004553
      relative error                  1.67796E-02             1.73076E-02                     0.031461
      variance of the variance        1.40664E-02             1.69057E-02                     0.201851
      shifted center                  4.96529E-04             4.96581E-04                     0.000105
      figure of merit                 4.27280E+03             4.01612E+03                    -0.060073

 the estimated inverse power slope of the 200 largest  tallies starting at 2.61109E-01 is 8.5241
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.203E+06)*( 5.960E-02)**2 = (1.203E+06)*(3.552E-03) = 4.273E+03

1tally        6        nps =     1000000
           tally type 6    track length estimate of heating.            units   mev/gram       
           particle(s): photons  

           masses  
                   cell:       2            3            4            5            6                               
                         9.89602E+03  7.91681E+04  2.14885E+05  4.18460E+05  6.89894E+05
 
 cell  2                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.13201E-06 0.0030   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   1.56173E-06 0.0022   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.58188E-06 0.0026   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   9.45627E-07 0.0037   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   7.16659E-07 0.0045   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   6.49226E-07 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   1.20624E-06 0.0039   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   6.19697E-07 0.0058   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   6.53029E-07 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   6.86132E-07 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   7.22046E-07 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   7.71022E-07 0.0059   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.32420E-05 0.0005   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   4.44873E-05 0.0002   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.13201E-06 0.0030
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.56173E-06 0.0022
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.58188E-06 0.0026
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.45627E-07 0.0037
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.16659E-07 0.0045
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.49226E-07 0.0050
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.20624E-06 0.0039
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.19697E-07 0.0058
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.53029E-07 0.0059
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.86132E-07 0.0059
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.22046E-07 0.0060
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.71022E-07 0.0059
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.32420E-05 0.0005
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.44873E-05 0.0002
 
 cell  3                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   3.94569E-07 0.0017   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   4.62122E-07 0.0014   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   3.59339E-07 0.0020   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   2.83688E-07 0.0028   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   2.49597E-07 0.0034   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   2.37674E-07 0.0038   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   4.63386E-07 0.0030   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.34815E-07 0.0047   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.44330E-07 0.0048   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.58130E-07 0.0049   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.70148E-07 0.0050   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.85711E-07 0.0051   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.09326E-06 0.0014   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   6.83677E-06 0.0006   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.94569E-07 0.0017
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.62122E-07 0.0014
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.59339E-07 0.0020
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.83688E-07 0.0028
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.49597E-07 0.0034
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.37674E-07 0.0038
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.63386E-07 0.0030
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.34815E-07 0.0047
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.44330E-07 0.0048
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.58130E-07 0.0049
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.70148E-07 0.0050
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.85711E-07 0.0051
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.09326E-06 0.0014
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   6.83677E-06 0.0006
 
 cell  4                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   8.86617E-08 0.0023   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   9.78622E-08 0.0020   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   7.09077E-08 0.0029   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   5.88923E-08 0.0039   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   5.34980E-08 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   5.15754E-08 0.0052   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   9.87329E-08 0.0042   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   4.89275E-08 0.0065   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   4.98869E-08 0.0067   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   5.11793E-08 0.0070   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   5.29786E-08 0.0072   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   5.48624E-08 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   2.81061E-07 0.0033   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.05903E-06 0.0014   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   8.86617E-08 0.0023
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.78622E-08 0.0020
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   7.09077E-08 0.0029
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.88923E-08 0.0039
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.34980E-08 0.0046
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.15754E-08 0.0052
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   9.87329E-08 0.0042
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.89275E-08 0.0065
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.98869E-08 0.0067
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.11793E-08 0.0070
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.29786E-08 0.0072
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.48624E-08 0.0073
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.81061E-07 0.0033
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.05903E-06 0.0014
 
 cell  5                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   1.94000E-08 0.0038   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   2.08670E-08 0.0034   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   1.48901E-08 0.0047   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   1.25321E-08 0.0062   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   1.16385E-08 0.0073   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   1.08914E-08 0.0082   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   2.08553E-08 0.0067   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   1.00471E-08 0.0104   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   1.01529E-08 0.0109   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   1.02328E-08 0.0114   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   1.04310E-08 0.0118   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   1.05023E-08 0.0121   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   3.58124E-08 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   1.98253E-07 0.0026   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.94000E-08 0.0038
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.08670E-08 0.0034
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.48901E-08 0.0047
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.25321E-08 0.0062
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.16385E-08 0.0073
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.08914E-08 0.0082
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.08553E-08 0.0067
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.00471E-08 0.0104
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.01529E-08 0.0109
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.02328E-08 0.0114
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.04310E-08 0.0118
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.05023E-08 0.0121
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.58124E-08 0.0068
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   1.98253E-07 0.0026
 
 cell  6                                                                                                                               
         time:       0.0000E+00           1.0000E+00           2.0000E+00           3.0000E+00           4.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   3.81435E-09 0.0068   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   4.21311E-09 0.0060   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   3.09475E-09 0.0082   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   2.66735E-09 0.0106   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   2.45018E-09 0.0125   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   2.34376E-09 0.0139   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   4.56993E-09 0.0114   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   2.20996E-09 0.0176   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   2.14072E-09 0.0186   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   2.11455E-09 0.0196   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   2.09414E-09 0.0205   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   2.11690E-09 0.0211   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   5.36776E-09 0.0138   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   3.91975E-08 0.0046   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       5.0000E+00           6.0000E+00           7.0000E+00           8.0000E+00           9.0000E+00
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
 
         time:       1.0000E+01           5.0000E+01           1.0000E+02             total                        
      energy   
    1.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.81435E-09 0.0068
    2.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.21311E-09 0.0060
    3.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.09475E-09 0.0082
    4.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.66735E-09 0.0106
    5.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.45018E-09 0.0125
    6.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.34376E-09 0.0139
    8.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   4.56993E-09 0.0114
    9.0000E-01   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.20996E-09 0.0176
    1.0000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.14072E-09 0.0186
    1.1000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.11455E-09 0.0196
    1.2000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.09414E-09 0.0205
    1.3000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   2.11690E-09 0.0211
    1.4000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   5.36776E-09 0.0138
    1.5000E+00   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000
      total      0.00000E+00 0.0000   0.00000E+00 0.0000   0.00000E+00 0.0000   3.91975E-08 0.0046


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        6

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       9.52
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 4.4478E-05 to 4.4496E-05; 4.4469E-05 to 4.4506E-05; 4.4460E-05 to 4.4515E-05
 estimated  symmetric confidence interval(1,2,3 sigma): 4.4478E-05 to 4.4496E-05; 4.4469E-05 to 4.4506E-05; 4.4460E-05 to 4.4515E-05

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        6 with nps =     1000000  print table 160


 normed average tally per history  = 4.44873E-05          unnormed average tally per history  = 4.40247E-01
 estimated tally relative error    = 0.0002               estimated variance of the variance  = 0.0000
 relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0002

 number of nonzero history tallies =     1000000          efficiency for the nonzero tallies  = 1.0000
 history number of largest  tally  =      377123          largest  unnormalized history tally = 1.33892E+00
 (largest  tally)/(average tally)  = 3.04131E+00          (largest  tally)/(avg nonzero tally)= 3.04131E+00

 (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.44873E-05


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            4.44873E-05             4.44874E-05                     0.000002
      relative error                  2.06645E-04             2.06654E-04                     0.000046
      variance of the variance        5.80628E-06             5.81448E-06                     0.001413
      shifted center                  4.44873E-05             4.44873E-05                     0.000000
      figure of merit                 2.81728E+07             2.81702E+07                    -0.000091

 the estimated inverse power slope of the 200 largest  tallies starting at 9.41286E-01 is 9.5177
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.203E+06)*( 4.839E+00)**2 = (1.203E+06)*(2.342E+01) = 2.817E+07

1tally        8        nps =     1000000
           tally type 8    pulse height distribution.                   units   number         
           particle(s): photons  
 
 cell  2                                                                                                                               
                 1.00000E+00 0.0000
 
 cell  3                                                                                                                               
                 9.23113E-01 0.0003
 
 cell  4                                                                                                                               
                 4.97192E-01 0.0010
 
 cell  5                                                                                                                               
                 2.01848E-01 0.0020
 
 cell  6                                                                                                                               
                 7.15770E-02 0.0036


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
 history number of largest  tally  =          91          largest  unnormalized history tally = 1.00000E+00
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

 relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 1.203E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:  1260 tally bins had  1104 bins with zeros and     2 bins with relative errors exceeding 0.10

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:  1260 tally bins had  1104 bins with zeros and     4 bins with relative errors exceeding 0.10

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:  1050 tally bins had   910 bins with zeros and     0 bins with relative errors exceeding 0.10

        5   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   420 tally bins had   368 bins with zeros and    38 bins with relative errors exceeding 0.05

        6   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:  1050 tally bins had   910 bins with zeros and     0 bins with relative errors exceeding 0.10

        8   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     5 tally bins all have relative errors less than 0.10 with no zero bins


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       3 of the     6 tallies had bins with relative errors greater than recommended.
1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   1.2026E+00 0.0025 0.0004  3.2 3101865   4.5214E-03 0.0060 0.0032 10.0  520976   2.1868E-03 0.0025 0.0001 10.0 2929899
       128000   1.2029E+00 0.0017 0.0002  3.7 3140301   4.5349E-03 0.0043 0.0016 10.0  515753   2.1929E-03 0.0018 0.0000 10.0 2926729
       192000   1.2009E+00 0.0014 0.0001  3.7 3165009   4.5193E-03 0.0035 0.0011  8.4  523716   2.1950E-03 0.0015 0.0000 10.0 2917489
       256000   1.2010E+00 0.0012 0.0001  4.2 3130036   4.5283E-03 0.0030 0.0008  6.6  506636   2.1957E-03 0.0013 0.0000 10.0 2893336
       320000   1.2010E+00 0.0011 0.0001  4.9 3124384   4.5368E-03 0.0027 0.0007  6.7  497494   2.1966E-03 0.0011 0.0000 10.0 2885110
       384000   1.1997E+00 0.0010 0.0001 10.0 3150240   4.5269E-03 0.0025 0.0006  3.4  500078   2.1965E-03 0.0010 0.0000 10.0 2893124
       448000   1.1995E+00 0.0009 0.0001  3.1 3135451   4.5226E-03 0.0023 0.0005  3.5  500530   2.1963E-03 0.0010 0.0000 10.0 2870702
       512000   1.1991E+00 0.0009 0.0001  3.1 3150192   4.5226E-03 0.0022 0.0004  4.1  499928   2.1962E-03 0.0009 0.0000 10.0 2873842
       576000   1.1993E+00 0.0008 0.0000  3.1 3155885   4.5259E-03 0.0020 0.0004  4.0  501615   2.1965E-03 0.0008 0.0000 10.0 2877704
       640000   1.1993E+00 0.0008 0.0000  3.2 3142977   4.5315E-03 0.0019 0.0003  3.7  493576   2.1972E-03 0.0008 0.0000 10.0 2861979
       704000   1.1995E+00 0.0007 0.0000  3.2 3149164   4.5320E-03 0.0019 0.0003  3.3  491719   2.1978E-03 0.0008 0.0000 10.0 2871264
       768000   1.1994E+00 0.0007 0.0000  3.4 3156546   4.5300E-03 0.0018 0.0003  3.3  495027   2.1983E-03 0.0007 0.0000 10.0 2874263
       832000   1.1994E+00 0.0007 0.0000  3.4 3162625   4.5291E-03 0.0017 0.0003  3.7  497133   2.1983E-03 0.0007 0.0000 10.0 2881303
       896000   1.1996E+00 0.0007 0.0000  3.6 3170001   4.5319E-03 0.0016 0.0002  4.4  497406   2.1986E-03 0.0007 0.0000 10.0 2886061
       960000   1.1995E+00 0.0006 0.0000  3.8 3175796   4.5335E-03 0.0016 0.0002  4.5  494487   2.1989E-03 0.0007 0.0000 10.0 2888584
      1000000   1.1992E+00 0.0006 0.0000  3.7 3180845   4.5327E-03 0.0016 0.0002  4.5  495240   2.1988E-03 0.0006 0.0000 10.0 2891137
 

                            tally        5                          tally        6                          tally        8
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   4.8489E-04 0.0667 0.0962  2.2    4211   4.4428E-05 0.0008 0.0001 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       128000   4.8821E-04 0.0433 0.0414  2.1    5043   4.4411E-05 0.0006 0.0000  9.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       192000   4.8059E-04 0.0343 0.0274  2.5    5373   4.4448E-05 0.0005 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       256000   4.7850E-04 0.0290 0.0195  6.8    5570   4.4457E-05 0.0004 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       320000   4.7972E-04 0.0258 0.0147 10.0    5612   4.4467E-05 0.0004 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       384000   4.7676E-04 0.0239 0.0143 10.0    5468   4.4467E-05 0.0003 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       448000   4.7476E-04 0.0223 0.0129 10.0    5346   4.4472E-05 0.0003 0.0000  9.4 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       512000   4.7496E-04 0.0208 0.0121  8.5    5388   4.4474E-05 0.0003 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       576000   4.8041E-04 0.0214 0.0285  6.0    4520   4.4479E-05 0.0003 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       640000   4.8166E-04 0.0200 0.0244  7.4    4628   4.4481E-05 0.0003 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       704000   4.8048E-04 0.0189 0.0214  8.6    4732   4.4481E-05 0.0002 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       768000   4.8556E-04 0.0185 0.0175  8.0    4530   4.4485E-05 0.0002 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       832000   4.8483E-04 0.0177 0.0157 10.0    4585   4.4484E-05 0.0002 0.0000 10.0 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       896000   4.9086E-04 0.0173 0.0132 10.0    4495   4.4482E-05 0.0002 0.0000  8.5 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       960000   4.9324E-04 0.0166 0.0117 10.0    4520   4.4486E-05 0.0002 0.0000  8.8 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
      1000000   4.9616E-04 0.0168 0.0141  8.5    4273   4.4487E-05 0.0002 0.0000  9.5 2.8E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30

 ***********************************************************************************************************************

 dump no.    2 on file multiple_et.ir     nps =     1000000     coll =       10413845     ctm =        0.83   nrn =     
    179108174

        10 warning messages so far.


 run terminated when     1000000  particle histories were done.

 computer time =    1.08 minutes

 mcnp     version 6.mpi 01/13/25                     07/24/25 09:41:17                     probid =  07/24/25 09:41:12 
