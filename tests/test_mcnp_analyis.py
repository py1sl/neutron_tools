import unittest
import mcnp_analysis as ma


class normalise_test_case(unittest.TestCase):
    """ tests normalise function"""

    def test_norm_nice_data(self):
        data = [1, 2, 3, 4]
        self.assertEqual(ma.normalise(data, 10), [10, 20, 30, 40])


class calc_err_test(unittest.TestCase):
    """ test for absolute error calculation function"""

    def test_is_version(self):
        self.assertTrue(True)


class calc_bin_width_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_is_version(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
