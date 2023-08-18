import unittest
import mcnp_input_checker
import neut_utilities as ut

# declaring file path for testing
fname = r'test_output\error_singles_erg.i'


class linecheck_test(unittest.TestCase):
    """ checks the line_checker function """
    def test_line_checker(self):
        lines = ut.get_lines(fname)
        new_lines = mcnp_input_checker.line_checker(fname)
        self.assertEqual(len(new_lines), len(lines))


class duplicate_data_test(unittest.TestCase):
    """ checks the duplicate checker function to make sure it picks up
    duplicates and returns lists of tuples, the index and the
    duplicate entry """
    def test_dup_checker(self):
        ifile = ut.get_lines(fname)
        mode, nps, sdef = mcnp_input_checker.dup_data_checker(ifile)
        self.assertEqual(mode, [(16, 'p'), (32, 'n')])
        self.assertEqual(len(nps), 1)
        self.assertEqual(len(sdef), 1)


if __name__ == '__main__':
    unittest.main()
