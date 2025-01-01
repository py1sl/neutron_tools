import json
import argparse

import mcnp_output_reader as mor
import mcnp_input_reader as mir
import fispact_output_reader as fisor


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
 
    return inputs

def get_cells_mcnp(mcnp_output, particle="neutron"):
    """ """
    cell_list = []
    for tal in mcnp_output.tally_data:
        if tal.tally_type == 4:
            if tal.particle == particle:
                cell_list = cell_list + tal.cells
       
    return cell_list
    
def main(config_fp):
    """ """
    # read config
    inputs = read_config(config_fp)          

    # read mc output
    if inputs.mc_code.upper() == "MCNP":
        mc_output = mor.read_output_file(inputs.mc_output)
        cells = get_cells_mcnp(mc_output)
    else:
        raise NotImplementedError()
        
    # read mc input
    if inputs.mc_code.upper() == "MCNP":
        mc_input = mir.read_input_file(inputs.mc_input)
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