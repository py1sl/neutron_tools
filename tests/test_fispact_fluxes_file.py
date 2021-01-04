import unittest
import fispact_fluxes_writer as fw

class fluxes_writer_test_case(unittest.TestCase):
    """ test for reading the version of output file"""
    
    def test_get_group_pos(self):
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),"1.00E+03"), 0)  # top edge of bins
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),"9.60E+02"), 0)  # 1st bin edge
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),"9.20E+02"), 1)  # 2nd bin edge
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),"9.40E+02"), 1)  # 2nd bin mid
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),9.20E+02), 1)  # 2nd bin mid as float
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),920), 1)  # 2nd bin mid as int
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),"1.05E-11"), 707)  # last bin edge
        
    def test_correct_gs_length(self):
        self.assertEqual(len(fw.get_group_struct("709")), 709)
    
       
      
        
if __name__ == '__main__':
    unittest.main()