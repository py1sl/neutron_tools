import json
import argparse
import pandas
import os
import shutil
from pathlib import Path

import mcnp_output_reader as mor
import mcnp_input_reader as mir
import fispact_output_reader as fisor
import neut_utilities as ut
import fispact_fluxes_writer as ffw


class usr_inputs:
    """ """
    def __init__(self):
        self.mc_input = None
        self.mc_ouput = None
        self.mc_gamma_input = None
        self.mc_code = "MCNP"
        self.files_file = None
        self.fispact_template = None
        self.tallies = None
        self.cells = None
        self.fispact_path = None
        self.cooling_step = 1


def read_config(config_fp):
    """ """
    if not Path(config_fp).exists():
        raise FileNotFoundError(f"config file {config_fp} not found")

    with open(config_fp) as f:
        config = json.load(f)
    
    inputs = usr_inputs()    
    for key in config.keys():
        if key == "mc_input":
            inputs.mc_input = config["mc_input"]
        elif key == "mc_output":
            inputs.mc_output = config["mc_output"]
        elif key == "mc_gamma_input":
            inputs.mc_gamma_input = config["mc_gamma_input"]
        elif key == "mc_code":
            inputs.mc_code = config["mc_code"]
        elif key == "files_file":
            inputs.files_file = config["files_file"]
        elif key == "fispact_template":
            inputs.fisact_template = config["fispact_template"]
        elif key == "tallies":
            inputs.tallies = config["tallies"]
        elif key == "cells":
            inputs.cells = config["cells"]
        elif key == "fispact_path":
            inputs.fispact_path = config["fispact_path"]
        elif key == "cooling_step":
            inputs.cooling_step = config["cooling_step"]
        else:
            raise ValueError('input not recognised')
 
    return inputs


def get_cells_mcnp(mcnp_output, particle="neutron"):
    """ """
    cell_list = []
    for tal in mcnp_output.tally_data:
        if tal.tally_type == 4:
            if tal.particle == particle:
                cell_list = cell_list + tal.cells
       
    return cell_list
    
    
def get_cell_data(mc_input, cell_list):
    """ """
    for cell in cell_list:
        
    
    return cell_data


def write_collapse(path):
    """ """
    lines = []
    ut.write_lines()
    return 0


def write_array(path):
    """ """
    lines = []
    ut.write_lines()
    return 0    


def write_fispact(path):
    """ """
    lines = []
    ut.write_lines()
    return 0
    
    
def copy_files_file(inputs, path):
    """ """
    shutil.copyfile(inputs.files_files, path+"/FILES")
    return 0


def write_fluxes(path):
    """ """
    return 0


def check_files_file():
    """ """
    return 0
    
    
def check_fispact_errors(log_file):
    """ """
    log = ut.get_lines(log_file)
    return 0

    
def cleanup_fispact_run(path):
    """ """
    return 0


def run_fispact(fispath, path):
    """ """
    # move into folder
    # run collapse
    # check collapse run
    # run array
    # check array run
    
    # run fispact main
    # check main run
    
    # remember to move out of folder
    
    return 0
    
    
def fispact_setup(cell, inputs):
    """ """
    path = "cell"+str(cell)
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
    
    write_collapse(path)    
    write_array(path)
    write_fispact(path)
    copy_files_file(inputs, path)
    
    return 0
 
 
def main(config_fp):
    """ """
    # read config
    inputs = read_config(config_fp)          

    # read mc output
    if inputs.mc_code.upper() == "MCNP":
        mc_output = mor.read_output_file(inputs.mc_output)
        if mc_output.fatal == True:
            raise ValueError('MCNP output contains a fatal error')
            
        cells = get_cells_mcnp(mc_output)
    else:
        raise NotImplementedError()
        
    # read mc input
    if inputs.mc_code.upper() == "MCNP":
        mc_input = mir.read_input_file(inputs.mc_input)
        cell_data = get_cell_data(mc_input, cells)
    else:
        raise NotImplementedError()
    
    
    # generate fispact inputs
    
    # run fispact
    
    # read fispact outputs
    
    # generate new mc gamma source
    

if __name__ == "__main__":
    desc_txt1 = "Cell based 2 step activation script"
    desc_txt2 = " using fispact"
    parser = argparse.ArgumentParser(description=desc_txt1 + desc_txt2)
    parser.add_argument("input", help="path to the input file")

    args = parser.parse_args()
    
    main(args.input)