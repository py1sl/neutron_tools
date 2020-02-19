import unittest
import mcnp_input_reader

class cell_card_tests(unittest.TestCase):
    """ test for reading the cells part of input file"""
    
    def test_is_version(self):
        self.assertTrue(True)
  
  
class surface_card_tests(unittest.TestCase):
    """ test for reading the surfaces part of input file"""
    
    def test_is_version(self):
        self.assertTrue(True)

       
class data_card_tests(unittest.TestCase):
    """ test for reading the data part of input file"""
    
    def test_get_mat_nums(self):
        """ """
        test_list = ["M1",
                     "m10",
                     "m ",
                     "m",
                     "a "]
        mnums = mcnp_input_reader.get_material_numbers(test_list)
        self.assertEqual(mnums[0], 1)    # test for lower case m
        self.assertEqual(mnums[1], 10)   # test for upper case m
        self.assertEqual(len(mnums), 2)  # check nothing else added 
       
    def test_get_tal_nums(self):
        """ """
        test_list = ["f1",
                     "F10",
                     "f ",
                     "f",
                     "a "]
        tnums = mcnp_input_reader.get_tally_numbers(test_list)
        self.assertEqual(tnums[0], 1)    # test for lower case f
        self.assertEqual(tnums[1], 10)   # test for upper case f
        self.assertEqual(len(tnums), 2)  # check nothing else added
       
       
    def test_get_mode(self):
        """ """
        mode = mcnp_input_reader.read_mode_card(["Mode n"])
        self.assertEqual(mode, ["n"])   # test for mixed case mode
        self.assertEqual(len(mode), 1)  # check nothing else added
        
        mode = mcnp_input_reader.read_mode_card(["mode p"])
        self.assertEqual(mode, ["p"])   # test for lower case mode
        self.assertEqual(len(mode), 1)  # check nothing else added
        
        mode = mcnp_input_reader.read_mode_card(["MODE n p", "m34 32000"])
        self.assertEqual(mode, ["n", "p"])  # test for upper case mode 
        self.assertEqual(len(mode), 2)      # check multipe particles else added
        
        mode = mcnp_input_reader.read_mode_card(["m23 1001.21c 1", "m34 32000"])
        self.assertIsNone(mode)  # test for upper case mode
       
       
    def test_mode_valid(self):
        """ """
        check = mcnp_input_reader.check_mode_valid(["p", "n"])
        self.assertTrue(check)  # check lower case
        
        check = mcnp_input_reader.check_mode_valid(["n", "P"])
        self.assertTrue(check) # check upper case and order
        
        check = mcnp_input_reader.check_mode_valid(["p", "n", "r"])
        self.assertFalse(check) # check false
        
       
class misc_tests(unittest.TestCase):
    """ test for reading the misc part of input file"""
    
    def test_full_line_comment(self):
        """ """
        test_list = ["c cell cards",
                     "C surface ecards",
                     "c234",
                     "comment",
                     "c"]
        comments = mcnp_input_reader.get_full_line_comments(test_list)
        self.assertEqual(comments[0], test_list[0])  # test for lower case c
        self.assertEqual(comments[1], test_list[1])  # test for upper case c
        self.assertEqual(len(comments), 2)  # check nothing else added as comment
        
if __name__ == '__main__':
    unittest.main()