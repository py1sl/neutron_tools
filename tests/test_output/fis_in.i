<< -----get nuclear data----- >>
NOHEAD
CLOBBER
MONITOR  0
GETXS 0
SPEK
GETDECAY 0
FISPACT
* Calculation
<< -----set initial conditions----- >>
DENSITY 5.8
MASS   1.0   1
V 100
MIND 1E2
ATOMS
SORTDOMINANT 100 100
DOSE 2 0.3
UNCERT 3
<< ----- irradiation phase ----- >> 
<< ---1 day time --- >>
FLUX 6e6
TIME 10 MINS ATOMS
FLUX 0.0
TIME 10 MINS ATOMS
FLUX 6e6
TIME 10 MINS ATOMS
FLUX 0.0
TIME 10 MINS ATOMS
FLUX 6e6
TIME 10 MINS ATOMS
FLUX 6e8
TIME 10 MINS ATOMS
ATOMS
FLUX 0.0
ZERO
<< -----cooling phase----- >>
TIME 0.000001 MINS ATOMS
TIME 9.999999 MINS ATOMS
TIME 10 MINS ATOMS
TIME 10 MINS ATOMS
TIME 10 MINS ATOMS
TIME 10 MINS ATOMS
TIME 10 MINS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 1 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
TIME 12 HOURS ATOMS
END
* END