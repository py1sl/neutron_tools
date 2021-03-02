import unittest
import fispact_output_reader as fo
import neut_utilities as ut


class version_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_version(self):
        path = "test_output/fis_test1.out"
        lines = ut.get_lines(path)
        version = fo.check_fisp_version(lines)
        self.assertEqual(version, "FISPACT-II")

    def test_fis2version(self):
        path = "test_output/fis_test1.out"
        lines = ut.get_lines(path)
        version = fo.isFisII(lines)
        self.assertEqual(version, True)

        
class read_fis_out_test_case(unittest.TestCase):
    """ test for the read fis out function which tests many other functions """
    
    def test_fis_out_file1(self):
        path = "test_output/fis_test1.out"
        output = fo.read_fis_out(path)
        self.assertEqual(output.file_name, path)
        self.assertEqual(output.version, "FISPACT-II")
        self.assertEqual(output.isFisII, True)
        self.assertEqual(output.cpu_time, 8.2558)
        self.assertEqual(output.tot_irrad_time, 1.2e3)
        self.assertEqual(output.tot_fluence, 7.2e9)
        self.assertEqual(output.ave_flux, 6.0e6)

if __name__ == '__main__':
    unittest.main()
