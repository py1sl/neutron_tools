import unittest
import mcnp_input_checker as checker
import neut_utilities as ut

# declaring file path for testing
fpath = r'test_output/singles.i'


class test_linecheck(unittest.TestCase):
    """ tests the line_checker function """
    def test_line_checker(self):
        lines = ut.get_lines(fpath)
        new_lines = checker.line_checker(fpath)
        self.assertEqual(len(new_lines), len(lines))


class test_input_summary(unittest.TestCase):
    """ tests the function to make sure it returns the
    correct information """
    def test_print_input(self):
        into = checker.input_summary(fpath)
        filename = into.filename
        self.assertEqual(filename, fpath)
        tallies = into.tally_list
        test_tally_len = 6
        self.assertEqual(tallies, test_tally_len)
        cells = into.cell_list
        test_cell_len = 4
        self.assertEqual(cells, test_cell_len)


class test_duplicate_data(unittest.TestCase):
    """ tests the duplicate checker function to make sure it picks up
    duplicates and returns lists of tuples, the index and the
    duplicate entry """
    def test_dup_checker(self):
        ifile = ['mode p',
                 'nps 1e6',
                 'mode n',
                 'sdef erg=1.13']
        mode, nps, sdef, mphys, prdmp = checker.dup_data_checker(ifile)
        self.assertEqual(mode, [(1, ['p']), (3, ['n'])])
        self.assertEqual(len(nps), 1)
        self.assertEqual(len(sdef), 1)
        self.assertEqual(len(mphys), 0)
        self.assertEqual(len(prdmp), 0)


if __name__ == '__main__':
    unittest.main()
