import unittest
import mcnp_analysis as ma


class normalise_test_case(unittest.TestCase):
    """ tests normalise function"""

    def test_norm_nice_data(self):
        data = [1, 2, 3, 4]
        self.assertEqual(ma.normalise(data, 10), [10, 20, 30, 40])


class calc_absolute_err_test(unittest.TestCase):
    """ test for absolute error calculation function"""

    def test_abs_err_calc(self):
        err = [1, 0.5, 0.1]
        res = [1, 1, 1]
        self.assertEqual(ma.calc_err_abs(res, err), [1, 0.5, 0.1])


class calc_bin_width_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_bin_widths(self):
        bins = [1, 1.5, 1.6]
        self.assertEqual(len(ma.calc_bin_width(bins)), 3)


if __name__ == '__main__':
    unittest.main()
