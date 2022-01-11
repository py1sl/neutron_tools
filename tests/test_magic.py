import unittest
from unittest.mock import patch, mock_open
import magic
import pandas as pd
import meshtal_analysis as ma


class magic_method_tests(unittest.TestCase):
    # tests for magic method functions
    def test_normalise_mesh(self):
        df = pd.DataFrame()
        df["value"] = [10, 5, 10, 10, 20] 
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "6col"
        meshtally_test.data = df
        result = magic.normalise_to_half(meshtally_test)
        self.assertEqual(max(result), 0.5)
        self.assertEqual(min(result), 0.125)
        self.assertEqual(len(result), 5)
        
    def test_do_magic(self):
        self.assertEqual(1, 1)
    
class output_tests(unittest.TestCase):
    # test for outputing wwinp file
    def test_header(self):
        self.assertEqual(1, 1)
        
    def test_mesh_header(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
