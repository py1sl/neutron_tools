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
  
1mcnp     version 6.mpi ld=01/13/25                     07/24/25 09:39:58 
 *************************************************************************                 probid =  07/24/25 09:39:58 
 n=multiple.i XSDIR=/home/vol03/scarf473/neutronic_data1/mcnpx_data/xsdir        

 
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
        24-       f2:p 1 2 3 4 5 6                                                                
        25-       f4:p 2 3 4 5 6                                                                  
        26-       f5:p 15 0 0 1                                                                   
        27-       f6:p 2 3 4 5 6                                                                  
        28-       f8:p 2 3 4 5 6                                                                  
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

         3 warning messages so far.
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

 dump no.    1 on file multiple.ir     nps =           0     coll =              0     ctm =        0.00   nrn =        
         0

         4 warning messages so far.
 master starting      11 MPI slave tasks with       1 threads each  07/24/25 09:39:58 
 master set rendezvous nps =        1000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        2000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        3000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        4000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        5000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        6000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        7000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        8000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =        9000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       10000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       11000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       12000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       13000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       14000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       15000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       16000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       17000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       18000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       19000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       20000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       22000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       24000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       26000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       28000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       30000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       32000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       34000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       36000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       38000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       40000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       44000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       48000,  work chunks =    11    07/24/25 09:39:58 
 master set rendezvous nps =       52000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       56000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       60000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       64000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       68000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       72000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       76000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       80000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       88000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =       96000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      104000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      112000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      120000,  work chunks =    11    07/24/25 09:39:59 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.1494E-01 1.0000E+00 1.3980E+00 1.2061E-01 7.2513E-01 1.0000E+00 9.9314E-01     3      116024    1                  21         7   
 master set rendezvous nps =      128000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      136000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      144000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      152000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      160000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      176000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      192000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      208000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      224000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      240000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      256000,  work chunks =    11    07/24/25 09:39:59 
 master set rendezvous nps =      272000,  work chunks =    11    07/24/25 09:40:00 
 master set rendezvous nps =      288000,  work chunks =    11    07/24/25 09:40:00 
 master set rendezvous nps =      304000,  work chunks =    11    07/24/25 09:40:00 
 master set rendezvous nps =      320000,  work chunks =    11    07/24/25 09:40:00 
 master set rendezvous nps =      352000,  work chunks =    11    07/24/25 09:40:00 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.2161E-01 1.0000E+00 1.1915E+00 1.5570E-01 8.8393E-01 1.0000E+00 8.8136E-01     3      331811    2                  37         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1197E-01 1.0000E+00 1.2278E+00 2.3788E-01 8.5766E-01 1.0000E+00 3.1048E-01     3      348527    2                  43         7   
 master set rendezvous nps =      384000,  work chunks =    11    07/24/25 09:40:00 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.0490E+00 1.0000E+00 8.6460E+01 1.1080E+00 2.0813E+00 1.0000E+00 8.2178E-02     3      379875   10                 156         6   
 master set rendezvous nps =      416000,  work chunks =    11    07/24/25 09:40:00 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 9.3537E-01 1.0000E+00 2.1127E+00 1.5089E-01 9.8646E-01 1.0000E+00 1.1731E+00     3      411577    2                  37         7   
 master set rendezvous nps =      448000,  work chunks =    11    07/24/25 09:40:00 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.6960E-01 1.0000E+00 1.2966E+00 1.1753E-01 6.9558E-01 1.0000E+00 9.6106E-01     3      428213    1                  18         7   
 master set rendezvous nps =      480000,  work chunks =    11    07/24/25 09:40:00 
 master set rendezvous nps =      512000,  work chunks =    11    07/24/25 09:40:01 
 master set rendezvous nps =      544000,  work chunks =    11    07/24/25 09:40:01 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 2.2248E+00 1.0000E+00 1.8094E+02 9.1676E-01 2.2749E+00 1.0000E+00 1.2650E-01     3      517734    7                 116         6   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.2863E-01 1.0000E+00 1.4796E+00 1.8074E-01 7.5876E-01 1.0000E+00 4.4982E-01     3      533359    2                  33         7   
 master set rendezvous nps =      576000,  work chunks =    11    07/24/25 09:40:01 
 master set rendezvous nps =      608000,  work chunks =    11    07/24/25 09:40:01 
 master set rendezvous nps =      640000,  work chunks =    11    07/24/25 09:40:01 
 master set rendezvous nps =      704000,  work chunks =    11    07/24/25 09:40:01 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 4.9554E-01 1.0000E+00 1.1315E+00 1.7453E-01 9.9520E-01 1.0000E+00 8.8946E-01     3      683349    1                  18         7   
 master set rendezvous nps =      768000,  work chunks =    11    07/24/25 09:40:02 
                                                                                                                                        
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
 master set rendezvous nps =      832000,  work chunks =    11    07/24/25 09:40:02 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.7558E-01 1.0000E+00 1.5333E+00 6.0166E-02 3.6937E-01 1.0000E+00 1.0354E+00     3      770515    1                  21         7   
 master set rendezvous nps =      896000,  work chunks =    11    07/24/25 09:40:02 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 6.5995E-01 1.0000E+00 1.5005E+00 1.1994E-01 7.2017E-01 1.0000E+00 9.9038E-01     3      836063    2                  36         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 4.8602E-01 1.0000E+00 1.1626E+00 2.0595E-01 7.5724E-01 1.0000E+00 3.2596E-01     3      877218    2                  45         7   
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.1754E+00 1.0000E+00 2.6429E+00 1.1418E-01 7.9440E-01 1.0000E+00 1.3260E+00     3      890127    1                  21         7   
 master set rendezvous nps =      960000,  work chunks =    11    07/24/25 09:40:02 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 5.1224E-01 1.0000E+00 1.1682E+00 1.4497E-01 8.3904E-01 1.0000E+00 9.1751E-01     3      898040    2                  34         7   
 master set rendezvous nps =     1000000,  work chunks =    11    07/24/25 09:40:03 
                                                                                                                                        
 det     t         wgt        psc       amfp       ddetx     radius       erg     cell         nps  nch   p             nrn      ipsc   
  1 1.9351E+00 1.0000E+00 5.4875E+00 3.3889E-01 5.2944E-01 1.0000E+00 6.8145E-02     3      986108    6                 101         6   
1problem summary                                                                                                           

      run terminated when     1000000  particle histories were done.
+                                                                                                    07/24/25 09:40:03 
      c test input to generate output for MCNP output reader                               probid =  07/24/25 09:39:58 

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

 computer time so far in this run     0.98 minutes            maximum number ever in bank         4
 computer time in mcrun               0.77 minutes            bank overflows to backup file       0
 source particles per minute            1.2981E+06
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
                 1.19923E+00 0.0006
 
 surface  2                                                                                                                            
                 1.17306E+00 0.0006
 
 surface  3                                                                                                                            
                 6.60137E-01 0.0013
 
 surface  4                                                                                                                            
                 2.74267E-01 0.0023
 
 surface  5                                                                                                                            
                 9.80800E-02 0.0041
 
 surface  6                                                                                                                            
                 2.34120E-02 0.0065


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
      figure of merit                 3.43214E+06             3.43102E+06                    -0.000325

 the estimated inverse power slope of the  62 largest  tallies starting at 1.08214E+01 is 3.7480
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.298E+06)*( 1.626E+00)**2 = (1.298E+06)*(2.644E+00) = 3.432E+06

1tally        2        nps =     1000000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): photons  

           areas   
                surface:       1            2            3            4            5            6                  
                         3.14159E+02  1.25664E+03  5.02655E+03  1.13097E+04  2.01062E+04  3.14159E+04
 
 surface  1                                                                                                                            
                 4.53266E-03 0.0016
 
 surface  2                                                                                                                            
                 1.31548E-03 0.0015
 
 surface  3                                                                                                                            
                 2.01800E-04 0.0021
 
 surface  4                                                                                                                            
                 3.85118E-05 0.0035
 
 surface  5                                                                                                                            
                 7.89857E-06 0.0060
 
 surface  6                                                                                                                            
                 1.05558E-06 0.0083


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
      figure of merit                 5.34365E+05             5.33576E+05                    -0.001477

 the estimated inverse power slope of the 200 largest  tallies starting at 4.72133E+01 is 4.5157
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.298E+06)*( 6.416E-01)**2 = (1.298E+06)*(4.117E-01) = 5.344E+05

1tally        4        nps =     1000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:       2            3            4            5            6                               
                         3.66519E+03  2.93215E+04  7.95870E+04  1.54985E+05  2.55516E+05
 
 cell  2                                                                                                                               
                 2.19878E-03 0.0006
 
 cell  3                                                                                                                               
                 4.68163E-04 0.0006
 
 cell  4                                                                                                                               
                 8.76616E-05 0.0013
 
 cell  5                                                                                                                               
                 1.78780E-05 0.0024
 
 cell  6                                                                                                                               
                 3.60573E-06 0.0043


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
      figure of merit                 3.11954E+06             3.11927E+06                    -0.000086

 the estimated slope of the 198 largest  tallies starting at  3.93632E+01 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.298E+06)*( 1.550E+00)**2 = (1.298E+06)*(2.403E+00) = 3.120E+06

1tally        5        nps =     1000000
           tally type 5    particle flux at a point detector.           units   1/cm**2        
           particle(s): photons  
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
                 4.96162E-04 0.0168
 
 detector located at x,y,z = 1.50000E+01 0.00000E+00 0.00000E+00
 uncollided photon flux
                 8.51809E-05 0.0017
 
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
      figure of merit                 4.61036E+03             4.33341E+03                    -0.060073

 the estimated inverse power slope of the 200 largest  tallies starting at 2.61109E-01 is 8.5241
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.298E+06)*( 5.960E-02)**2 = (1.298E+06)*(3.552E-03) = 4.610E+03

1tally        6        nps =     1000000
           tally type 6    track length estimate of heating.            units   mev/gram       
           particle(s): photons  

           masses  
                   cell:       2            3            4            5            6                               
                         9.89602E+03  7.91681E+04  2.14885E+05  4.18460E+05  6.89894E+05
 
 cell  2                                                                                                                               
                 4.44873E-05 0.0002
 
 cell  3                                                                                                                               
                 6.83677E-06 0.0006
 
 cell  4                                                                                                                               
                 1.05903E-06 0.0014
 
 cell  5                                                                                                                               
                 1.98253E-07 0.0026
 
 cell  6                                                                                                                               
                 3.91975E-08 0.0046


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
      figure of merit                 3.03985E+07             3.03957E+07                    -0.000091

 the estimated inverse power slope of the 200 largest  tallies starting at 9.41286E-01 is 9.5177
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.298E+06)*( 4.839E+00)**2 = (1.298E+06)*(2.342E+01) = 3.040E+07

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

 relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 1.298E+06

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        1   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     6 tally bins all have relative errors less than 0.10 with no zero bins

        2   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     6 tally bins all have relative errors less than 0.10 with no zero bins

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     5 tally bins all have relative errors less than 0.10 with no zero bins

        5   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     2 tally bins all have relative errors less than 0.05 with no zero bins

        6   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     5 tally bins all have relative errors less than 0.10 with no zero bins

        8   passed the 10 statistical checks for the tally fluctuation chart bin result               
         passed all bin error check:     5 tally bins all have relative errors less than 0.10 with no zero bins


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

1tally fluctuation charts                              

                            tally        1                          tally        2                          tally        4
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   1.2026E+00 0.0025 0.0004  3.2 3334598   4.5214E-03 0.0060 0.0032 10.0  560065   2.1868E-03 0.0025 0.0001 10.0 3149729
       128000   1.2029E+00 0.0017 0.0002  3.7 3338920   4.5349E-03 0.0043 0.0016 10.0  548374   2.1929E-03 0.0018 0.0000 10.0 3111840
       192000   1.2009E+00 0.0014 0.0001  3.7 3379197   4.5193E-03 0.0035 0.0011  8.4  559158   2.1950E-03 0.0015 0.0000 10.0 3114926
       256000   1.2010E+00 0.0012 0.0001  4.2 3345677   4.5283E-03 0.0030 0.0008  6.6  541540   2.1957E-03 0.0013 0.0000 10.0 3092670
       320000   1.2010E+00 0.0011 0.0001  4.9 3365621   4.5368E-03 0.0027 0.0007  6.7  535906   2.1966E-03 0.0011 0.0000 10.0 3107873
       384000   1.1997E+00 0.0010 0.0001 10.0 3396925   4.5269E-03 0.0025 0.0006  3.4  539238   2.1965E-03 0.0010 0.0000 10.0 3119675
       448000   1.1995E+00 0.0009 0.0001  3.1 3393245   4.5226E-03 0.0023 0.0005  3.5  541683   2.1963E-03 0.0010 0.0000 10.0 3106729
       512000   1.1991E+00 0.0009 0.0001  3.1 3415099   4.5226E-03 0.0022 0.0004  4.1  541968   2.1962E-03 0.0009 0.0000 10.0 3115511
       576000   1.1993E+00 0.0008 0.0000  3.1 3396476   4.5259E-03 0.0020 0.0004  4.0  539856   2.1965E-03 0.0008 0.0000 10.0 3097088
       640000   1.1993E+00 0.0008 0.0000  3.2 3392689   4.5315E-03 0.0019 0.0003  3.7  532791   2.1972E-03 0.0008 0.0000 10.0 3089366
       704000   1.1995E+00 0.0007 0.0000  3.2 3396498   4.5320E-03 0.0019 0.0003  3.3  530339   2.1978E-03 0.0008 0.0000 10.0 3096772
       768000   1.1994E+00 0.0007 0.0000  3.4 3401691   4.5300E-03 0.0018 0.0003  3.3  533472   2.1983E-03 0.0007 0.0000 10.0 3097485
       832000   1.1994E+00 0.0007 0.0000  3.4 3409344   4.5291E-03 0.0017 0.0003  3.7  535914   2.1983E-03 0.0007 0.0000 10.0 3106076
       896000   1.1996E+00 0.0007 0.0000  3.6 3419304   4.5319E-03 0.0016 0.0002  4.4  536524   2.1986E-03 0.0007 0.0000 10.0 3113034
       960000   1.1995E+00 0.0006 0.0000  3.8 3426074   4.5335E-03 0.0016 0.0002  4.5  533456   2.1989E-03 0.0007 0.0000 10.0 3116227
      1000000   1.1992E+00 0.0006 0.0000  3.7 3432138   4.5327E-03 0.0016 0.0002  4.5  534365   2.1988E-03 0.0006 0.0000 10.0 3119543
 

                            tally        5                          tally        6                          tally        8
          nps      mean     error   vov  slope    fom      mean     error   vov  slope    fom      mean     error   vov  slope    fom
        64000   4.8489E-04 0.0667 0.0962  2.2    4526   4.4428E-05 0.0008 0.0001 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       128000   4.8821E-04 0.0433 0.0414  2.1    5362   4.4411E-05 0.0006 0.0000  9.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       192000   4.8059E-04 0.0343 0.0274  2.5    5737   4.4448E-05 0.0005 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       256000   4.7850E-04 0.0290 0.0195  6.8    5954   4.4457E-05 0.0004 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       320000   4.7972E-04 0.0258 0.0147 10.0    6045   4.4467E-05 0.0004 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       384000   4.7676E-04 0.0239 0.0143 10.0    5896   4.4467E-05 0.0003 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       448000   4.7476E-04 0.0223 0.0129 10.0    5785   4.4472E-05 0.0003 0.0000  9.4 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       512000   4.7496E-04 0.0208 0.0121  8.5    5841   4.4474E-05 0.0003 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       576000   4.8041E-04 0.0214 0.0285  6.0    4864   4.4479E-05 0.0003 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       640000   4.8166E-04 0.0200 0.0244  7.4    4996   4.4481E-05 0.0003 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       704000   4.8048E-04 0.0189 0.0214  8.6    5104   4.4481E-05 0.0002 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       768000   4.8556E-04 0.0185 0.0175  8.0    4881   4.4485E-05 0.0002 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       832000   4.8483E-04 0.0177 0.0157 10.0    4943   4.4484E-05 0.0002 0.0000 10.0 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       896000   4.9086E-04 0.0173 0.0132 10.0    4849   4.4482E-05 0.0002 0.0000  8.5 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
       960000   4.9324E-04 0.0166 0.0117 10.0    4876   4.4486E-05 0.0002 0.0000  8.8 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30
      1000000   4.9616E-04 0.0168 0.0141  8.5    4610   4.4487E-05 0.0002 0.0000  9.5 3.0E+07   1.0000E+00 0.0000 0.0000 10.0 1.0E+30

 ***********************************************************************************************************************

 dump no.    2 on file multiple.ir     nps =     1000000     coll =       10413845     ctm =        0.77   nrn =        
 179108174

         4 warning messages so far.


 run terminated when     1000000  particle histories were done.

 computer time =    0.98 minutes

 mcnp     version 6.mpi 01/13/25                     07/24/25 09:40:03                     probid =  07/24/25 09:39:58 
