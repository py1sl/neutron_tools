# Neutron Tools

All to be considered work in progress

## Installation

```bash
pip install -e .
```

## Package structure

```
src/neutron_tools/
├── mcnp/                  # MCNP related tools
├── fispact/               # FISPACT related tools
├── nuclear_data_readers/  # Nuclear data file readers (xsdir etc.)
└── utilities/             # Shared utilities and constants
```

## Modules

### 1. MCNP (`neutron_tools.mcnp`)

The MCNP team has now released their MCNP tools https://github.com/lanl/mcnptools which is far more comprehensive than this project, but it still has a few useful parts to it.

 - `lost_points` :- simple script to read MCNP output file and create a list of x,y,z co-ordinates where particles were lost which can be plotted in visit
 - `mcnp_run_plot` :- read the dump to std out from MCNP6 and plots graphs of nps vs time, coll, nrn, ctm
 - `ofile_reduce` :- reduces mcnp output file to just the last rendevous data, can be useful if the file size exceeds that of most text editors
 - `mcnp_input_reader` :- work in progress, some basic ability to read and extract data from MCNP input file
 - `mcnp_output_reader` :- work in progress, can read some f2, f4 and f5 tally results
 - `mcnp_analysis` :- work in progress tools to analyse and plot MCNP output when read by mcnp_output_reader
 - `meshtal_analysis` :- reads MCNP meshtal file, can plot a slice, do some statistics, plot histogram of the rel err, count zeros etc
 - `mcnp_ptrac_reader` :- reads MCNP ptrac files
 - `magic` :- mesh based magic variance reduction method
 - `r2s_cell` :- cell based two step activation tool, currently set for using mcnp and fispact

Example import:
```python
from neutron_tools.mcnp import mcnp_output_reader
```

### 2. Fispact (`neutron_tools.fispact`)

It should be noted that these are now mostly for historic usage as UKAEA have released a python fispact API which is superior for most cases.

 - `fispact_input_reader` :- currently just template stuff - do not use
 - `fispact_output_reader` :- currently just template stuff - do not use
 - `fispact_analysis` :- a few plotting routines for fispact data
 - `fispact_fluxes_writer` :- useful functions for generating fluxes files
 - `fispact_printlib_reader` :- reads fispact printlib files

Example import:
```python
from neutron_tools.fispact import fispact_analysis
```

### 3. Nuclear Data Readers (`neutron_tools.nuclear_data_readers`)

 - `xsdir_reader` :- reads MCNP xsdir files

Example import:
```python
from neutron_tools.nuclear_data_readers import xsdir_reader
```

### 4. Utilities (`neutron_tools.utilities`)

 - `neut_utilities` :- simple functions used by multiple modules
 - `neut_constants` :- set of useful constants and unit conversions
 - `geom_utils` :- set of geometry functions, distance between planes, area, volumes, intersections etc
 - `output_utilities` :- common output formatting utilities

Example import:
```python
from neutron_tools.utilities import neut_utilities as ut
from neutron_tools.utilities import neut_constants
```
