import unittest
import mcnp_output_reader

class version_test_case(unittest.TestCase):
    """ test for reading the version of output file"""
    
    def test_is_version(self):
        """ """
        list_a = ["          Code Name & Version = MCNP6, 1.0",
                  "  ",
                  "     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/"
                  "    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       "
                  "   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    "
                  "  _/      _/      _/             _/    _/_/       _/           _/    _/   "
                  " _/      _/        _/_/_/       _/      _/       _/             _/_/    "]
        self.assertEqual(mcnp_output_reader.read_version(list_a), "MCNP6, 1.0")
    
    def test_is_version_none_given_other_list(self):
        """ test for version """
        list_a = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
                  "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", 
                  "ccccccccccccccccccccccccccccccccccccccccccccccccccccccc", 
                  "ddddddddddddddddddddddddddddddddddddddddddddddddddddddd"]
        list_b = ["a","b","c","d"]
        self.assertEqual(mcnp_output_reader.read_version(list_a), None)
        self.assertEqual(mcnp_output_reader.read_version(list_b), None)
     
    def test_is_version_none_given_string(self):
        """ test for version with string"""
        string_a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertEqual(mcnp_output_reader.read_version(string_a), None)
        
if __name__ == '__main__':
    unittest.main()