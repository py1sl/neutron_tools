import unittest
from unittest.mock import patch, mock_open
import fispact_fluxes_writer as fw
import numpy as np


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        data = np.asarray([1, 2.0])
        with patch("neut_utilities.open", open_mock, create=True):
            fw.write_fluxes_file("output.txt", data)

        open_mock.assert_called_with("output.txt", "w")


class fluxes_writer_test_case(unittest.TestCase):
    """ tests for reading the version of output file"""

    def test_get_group_pos(self):
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          "1.00E+03"), 0)  # top edge of bins
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          "9.60E+02"), 0)  # 1st bin edge
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          "9.20E+02"), 1)  # 2nd bin edge
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          "9.40E+02"), 1)  # 2nd bin mid
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          9.20E+02), 1)  # 2nd bin mid as float
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          920), 1)  # 2nd bin mid as int
        self.assertEqual(fw.get_group_pos(fw.get_group_struct("709"),
                                          "1.05E-11"), 707)  # last bin edge

    def test_correct_gs_length(self):
        self.assertEqual(len(fw.get_group_struct("709")), 709)
        self.assertEqual(len(fw.get_group_struct("162")), 162)
        self.assertFalse(fw.get_group_struct("153"))

    def test_gs_check(self):
        self.assertTrue(fw.check_group_struct("709"))
        self.assertTrue(fw.check_group_struct("162"))
        self.assertFalse(fw.check_group_struct("710"))


class create_fluxes_data_test_case(unittest.TestCase):
    """ tests for creating the fluxes data """

    def test_create_fluxes(self):
        data = fw.create_fluxes_data([1, 1, 1, 1], 1)
        self.assertEqual(len(data), 5)
        self.assertEqual(data[1], 1)
        self.assertEqual(data[-1], 1)
        self.assertEqual(data[0], 0)

    def test_create_fluxes_mcnp(self):
        data = fw.create_fluxes_from_mcnp_spect([1, 2, 3, 4, 5])
        self.assertEqual(len(data), 6)
        self.assertEqual(data[1], 4)
        self.assertEqual(data[-1], 1)
        self.assertEqual(data[0], 5)

    def test_upper_bound(self):
        groups = [10, 9, 8, 7]
        self.assertTrue(fw.check_upper_bound(groups, 3))
        self.assertTrue(fw.check_upper_bound(groups, 10))
        self.assertFalse(fw.check_upper_bound(groups, 20.2))


if __name__ == '__main__':
    unittest.main()
