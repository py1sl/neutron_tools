import json
import argparse
import pandas as pd
import os
import shutil
from pathlib import Path

import mcnp_output_reader as mor
import mcnp_input_reader as mir
import fispact_output_reader as fisor
import neut_utilities as ut
import fispact_fluxes_writer as ffw


class usr_inputs:
    """ input from usr read from json file """
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
    """ reads the json file and assigns values """
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
            inputs.fispact_template = config["fispact_template"]
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


def get_cells_mcnp(mcnp_output, particle="neutrons", tallies=None):
    """ reads from mcnp output and gets cell numbers from tallies"""
    cell_list = []
    tally_data = []
    for tal in mcnp_output.tally_data:
        if tal.tally_type == '4' and tal.particle == particle:
            if tallies != None:
                if tal.number in tallies:
                    cell_list = cell_list + tal.cells
                    tally_data.append(tal)
            else:
                cell_list = cell_list + tal.cells
                tally_data.append(tal)
    
    # convert to ints
    cell_list = [int(i) for i in cell_list]
    return cell_list, tally_data
    
    
def get_cell_data(mc_input, tally_cell_list):
    """ get the cll material, mass and volume data"""
    cell_data = []
    for cell_num in tally_cell_list:
     if mir.check_cell_exists(cell_num, mc_input.cell_list):
         cell = mir.get_cell(cell_num, mc_input.cell_list)
         cell_data.append(cell)
     else:
         raise ValueError(f"Cell: {cell_num} not found in input")         
    
    header = ["number", "material", "density"]
    cell_df = None
    for i, cell in enumerate(cell_data):
        cell_series = {"number":cell.number, "material":cell.mat, "density":cell.density}
        cell_series = pd.DataFrame(cell_series, columns=header, index=[i])
        if isinstance(cell_df, pd.DataFrame) :
            cell_df = pd.concat([cell_df, cell_series])
        else:
            cell_df = cell_series
    
    return cell_df


def write_collapse(path, groups_count):
    """ writes the collapse stage fispact input file"""
    lines = ["<< -----collapse cross section data----- >>",
             "CLOBBER"
             "GETXS 1 " + str(groups_count),
             "FISPACT",
             "* COLLAPSE",  
             "END",
             "* END OF RUN"]
    ut.write_lines(path, lines)
    return 0


def write_array(path):
    """ writes the array stage fispact input file"""
    lines = ["<< -----condense decay data----- >>",
             "CLOBBER",
             "SPEK",
             "GETDECAY 1",
             "FISPACT",
             "* CONDENSE", 
             "END",
             "* END OF RUN"]
    ut.write_lines(path, lines)
    return 0    


def write_fispact(inputs, cell_data, path):
    """ writes the main fispact runner """
    lines = []
    ut.write_lines(path, lines)
    return 0
    
    
def copy_files_file(inputs, path):
    """ copy the files file into the folder for the current cell"""
    if not Path(inputs.files_file).exists():
        raise FileNotFoundError(f" Files file {inputs.files_file} not found")
    shutil.copyfile(inputs.files_files, path+"/FILES")
    return 0


def write_fluxes(cell_data, path):
    """ write the fluxes file for the current cell"""
    ut.write_lines(path, lines)
    return 0


def check_files_file(files_file):
    """ check the files file matches the data library with the current particle and group structure"""
    if not Path(files_file).exists():
        raise FileNotFoundError(f" Files file {files_file} not found")
    
    return 0
    
    
def check_fispact_errors(log_file):
    """ check the fispact log files for any fatal errors"""
    if not Path(log_file).exists():
        raise FileNotFoundError(f" Fispact log file {log_file} not found")
    
    log = ut.get_lines(log_file)
    return 0

    
def cleanup_fispact_run(path):
    """ remove the fispact files after the run """
    return 0

   
def run_fispact(fispath, path):
    """ run the three fispact runs for a cell """
    # change directory into folder
    # run collapse
    # check collapse run
    # run array
    # check array run
    
    # run fispact main
    # check main run
    
    # remember to move out of folder
    
    return 0
    
    
def fispact_setup(path, inputs, cell_data):
    """ set up the different the parts of the fispact runs for a cell """
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
    
    # TODO: need to get the groups number for the collapse
    write_collapse(path+"/collapse.i")    
    write_array(path+"/array.i")
    
    write_fispact(inputs, cell_data, path+"/"+path+".i")
    copy_files_file(inputs, path)
    check_files_file(path+"/FILES")
    write_fluxes(cell_data, path+"/fluxes")
    
    return 0


def read_data_from_mcnp_output(inputs):
    """ """
    if not Path(inputs.mc_output).exists():
        raise FileNotFoundError(f"MCNP output file {inputs.mc_output} not found")
        
    mc_output = mor.read_output_file(inputs.mc_output)
    if mc_output.fatal == True:
        raise ValueError('MCNP output contains a fatal error')
            
    cells, tally_data = get_cells_mcnp(mc_output)
        
    return cells, tally_data
        
        
def read_data_from_mcnp_input(inputs, tally_cell_list):
    """ reads the data from an mcnp input file """
    if not Path(inputs.mc_input).exists():
        raise FileNotFoundError(f"MCNP input file {inputs.mc_input} not found")
        
    mc_input = mir.read_mcnp_input(inputs.mc_input)
    cell_data = get_cell_data(mc_input, tally_cell_list)
    
    material_data = []
    
    for mat_num in set(cell_data["material"]):

        mat = mir.read_material_lines(mat_num, mc_input.data_block)
        material_data.append(mat)
     
    return cell_data, material_data
 
 
def main(config_fp):
    """  main calculation flow """
    # read config
    inputs = read_config(config_fp)          

    # read mc output
    if inputs.mc_code.upper() == "MCNP":
        cells, tally_data = read_data_from_mcnp_output(inputs)
        print(cells)
    else:
        raise NotImplementedError()
        
    # read mc input
    if inputs.mc_code.upper() == "MCNP":
       cell_data, material_data = read_data_from_mcnp_input(inputs, cells)
       print(cell_data)
    else:
        raise NotImplementedError()
    
    
    # generate fispact inputs
    # TODO: loop over the cell_data object
    for cell in cells:
        path = "cell"+str(cell)
        fispact_setup(path, inputs, cell_data)
    
        # run fispact
        fispath = inputs.fispact_path
        run_fispact(fispath, path)
        
    # read fispact outputs
    
    # generate new mc gamma source
    

if __name__ == "__main__":
    desc_txt1 = "Cell based 2 step activation script"
    desc_txt2 = " using fispact"
    parser = argparse.ArgumentParser(description=desc_txt1 + desc_txt2)
    parser.add_argument("input", help="path to the json input file")

    args = parser.parse_args()
    
    main(args.input)