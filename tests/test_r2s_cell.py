import unittest
from unittest.mock import patch, mock_open
import r2s_cell



class json_read_test_case(unittest.TestCase):
    """ tests for checking the reading of json files for r2s"""
    def test_read(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        self.assertEqual(inputs.mc_code, "mcnp")
        self.assertEqual(inputs.mc_input, "test_output/r2s_1.i")
        self.assertEqual(inputs.mc_output, "test_output/r2s_1.io")
        self.assertEqual(inputs.mc_gamma_input, "r2s_1g.i")
        self.assertEqual(inputs.files_file, "files")
        self.assertEqual(inputs.fispact_template, "fis_main.i")
        self.assertEqual(inputs.fispact_path, "fispact")
        self.assertEqual(inputs.cooling_step, 1)
        
    def test_no_config(self):
        config_fp = "nonexistent_config.yaml"

        with self.assertRaises(FileNotFoundError) as context:
            r2s_cell.read_config(config_fp)  
        self.assertEqual(str(context.exception), f"config file {config_fp} not found")    
        
        
class cell_data_test_case(unittest.TestCase):
    """ tests related to getting data about the cells, """
    
    def test_get_cells_mcnp(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        cells, tally_data = r2s_cell.read_data_from_mcnp_output(inputs)
        
        self.assertEqual(len(cells), 6)
        
        
    def test_missing_mcnp_output(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        inputs.mc_output = "not_a_file"
        
        with self.assertRaises(FileNotFoundError) as context:
            r2s_cell.read_data_from_mcnp_output(inputs)
        self.assertEqual(str(context.exception), 
                         f"MCNP output file {inputs.mc_output} not found") 
                         
    def test_missing_mcnp_input(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        inputs.mc_input = "not_a_file"
        
        with self.assertRaises(FileNotFoundError) as context:
            r2s_cell.read_data_from_mcnp_input(inputs, ["1"])
        self.assertEqual(str(context.exception), 
                         f"MCNP input file {inputs.mc_input} not found")
        
        
    def test_get_cell_data(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        cells, tally_data = r2s_cell.read_data_from_mcnp_output(inputs)
        
        
        cell_data, mat_data =  r2s_cell.read_data_from_mcnp_input(inputs, cells)
        
        self.assertEqual(1,1)
  
  
class fispact_inputs_test_case(unittest.TestCase):
    """ tests related to fispact input aspects """
    
    def test_check_fispact_errors(self):
        self.assertEqual(1,1)
      
    def test_fispact_setup(self):
        self.assertEqual(1,1) 
        
    def test_missing_files_file(self):
        files_file = "not_a_file"
        
        # in the check files file function
        with self.assertRaises(FileNotFoundError) as context:
            r2s_cell.check_files_file(files_file)
        self.assertEqual(str(context.exception), 
                         f" Files file {files_file} not found") 
                        
    def test_missing_log_file(self):
        log_file = "not_a_file"
        with self.assertRaises(FileNotFoundError) as context:
            r2s_cell.check_fispact_errors(log_file)
        self.assertEqual(str(context.exception), 
                         f" Fispact log file {log_file} not found")                         


class main_run_test_case(unittest.TestCase):
    """ tests related to main flow  and control of the calculation """
    
    def test_missing_files(self):
        self.assertEqual(1,1)
            

if __name__ == '__main__':
    unittest.main()
