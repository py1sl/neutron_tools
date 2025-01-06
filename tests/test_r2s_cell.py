import unittest
from unittest.mock import patch, mock_open
import r2s_cell



class json_read_test_case(unittest.TestCase):
    """ tests for checking the reading of json files for r2s"""
    def test_read(self):
        inputs = r2s_cell.read_config("test_output/r2s_1.json")
        self.assertEqual(inputs.mc_code, "mcnp")
        self.assertEqual(inputs.mc_input, "r2s_1.i")
        self.assertEqual(inputs.mc_output, "r2s_1.io")
        self.assertEqual(inputs.mc_gamma_input, "r2s_1g.i")
        self.assertEqual(inputs.files_file, "files")
        self.assertEqual(inputs.fispact_template, "fis_main.i")
        self.assertEqual(inputs.fispact_path, "fispact")
        self.assertEqual(inputs.cooling_step, 1)

    
      

if __name__ == '__main__':
    unittest.main()
