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
        
 
class stat_test_case(unittest.TestCase):
    """ test for reading the version of output file"""
     
    def test_read_stat_tests(self):
        self.assertTrue(True)
        # need to add test for tally with all 0.0 bins
        
        
class tally_type1_tests(unittest.TestCase):
    """ tests for type 1 tally """
       
    def test_single_value_t1_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 1.16486E+00)
                self.assertEqual(tn.err[0], 0.0006)
                
    def test_ebined_t1_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 2.92000E-02)
   
   
class tally_type2_tests(unittest.TestCase):
    """ tests for type 2 tally """
       
    def test_single_value_t2_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 4.31795E-03)  
                self.assertEqual(tn.err[0], 0.0015)

    def test_ebined_t2_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 1.92767E-04)

class tally_type4_tests(unittest.TestCase):
    """ tests for type 4 tally """
       
    def test_single_value_t4_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(tn.result[0], 1.91076E-03)
                self.assertEqual(tn.err[0], 0.0006)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['3.66519E+03'])

    def test_ebined_t4_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 1.20226E-04)   
                self.assertEqual(tn.cells, ['2']) 
                self.assertEqual(tn.vols, ['3.66519E+03'])                
                

class tally_type5_tests(unittest.TestCase):
    """ tests for type 5 tally """
       
    def test_single_value_t5_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 3.42950E-04)
                self.assertEqual(tn.err[0], 0.0025)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.x, 15.0)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)

    def test_ebined_t5_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 1.20831E-05)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)                

class tally_type6_tests(unittest.TestCase):
    """ tests for type 6 tally """
       
    def test_single_value_t6_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 4.30567E-05) 
                self.assertEqual(tn.err[0], 0.0002)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['9.89602E+03'])
                
    def test_ebined_t6_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 5.60997E-07) 
                self.assertEqual(tn.cells, ['2'])                
                self.assertEqual(tn.vols, ['9.89602E+03'])

                
class tally_type8_tests(unittest.TestCase):
    """ tests for type 8 tally """
       
    def test_single_value_t8_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 1.00000E+00)                
                self.assertEqual(tn.err[0], 0.00)
  
    def test_ebined_t8_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles_erg.io")
        for tn in single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0],  5.16461E-01)
  
if __name__ == '__main__':
    unittest.main()