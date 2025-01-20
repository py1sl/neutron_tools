import unittest
from unittest.mock import patch
import output_utilities
import os


class points_test_case(unittest.TestCase):
    """ tests ofile reduce function"""

    @patch("output_utilities.ut.write_lines")
    def test_with_data_val(self, mock_write_lines):
        x_vals = [1, 2]
        y_vals = [3, 4]
        z_vals = [5, 6]
        data_val = [10, 20]
        output_utilities.output_points(x_vals, y_vals, z_vals, data_val, outpath="test")
        expected_output = [
            "x y z temp",
            "1 3 5 10",
            "2 4 6 20"
        ]
        mock_write_lines.assert_called_with("test.3d", expected_output)

    @patch("output_utilities.ut.write_lines")
    def test_without_data_val(self, mock_write_lines):
        x_vals = [1, 2]
        y_vals = [3, 4]
        z_vals = [5, 6]
        output_utilities.output_points(x_vals, y_vals, z_vals, outpath="test")
        expected_output = [
            "x y z temp",
            "1 3 5 1",
            "2 4 6 1"
        ]
        mock_write_lines.assert_called_with("test.3d", expected_output)

    def test_unequal_length_inputs(self):
        x_vals = [1, 2]
        y_vals = [3, 4, 5]
        z_vals = [6, 7]
        with self.assertRaises(ValueError) as context:
            output_utilities.output_points(x_vals, y_vals, z_vals)
        self.assertEqual(str(context.exception), "Input lists must have the same length.")

    def test_mismatched_data_val_length(self):
        x_vals = [1, 2]
        y_vals = [3, 4]
        z_vals = [5, 6]
        data_val = [10]
        with self.assertRaises(ValueError) as context:
            output_utilities.output_points(x_vals, y_vals, z_vals, data_val)
        self.assertEqual(str(context.exception),
                         "data_val must have the same length as x_vals, y_vals, and z_vals.")




if __name__ == '__main__':
    unittest.main()
