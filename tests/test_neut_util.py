import unittest
from unittest.mock import patch, mock_open
import neut_utilities as ut


class getlines_test_case(unittest.TestCase):
    """ tests get_lines function"""
    def test_get_lines(self):
        data = ut.get_lines("test_output/singles.io")
        self.assertEqual(len(data), 700)


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        with patch("neut_utilities.open", open_mock, create=True):
            ut.write_lines("output.txt", ["hello", "world"])

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_any_call("hello\n")


class writepoints_test_case(unittest.TestCase):
    """ tests write_points function"""

    def test_write_points(self):
        open_mock = mock_open()
        with patch("neut_utilities.open", open_mock, create=True):
            ut.write_points_file("output.txt", [1, 2], [3, 4], [5, 6])

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_any_call("1 3 5 1\n")


class string_cleaner_test_case(unittest.TestCase):
    """ tests string_cleaner function"""

    def test_spaces(self):
        test_string = "   hello"
        self.assertEqual(ut.string_cleaner(test_string), "hello")
        test_string = "   hello    "
        self.assertEqual(ut.string_cleaner(test_string), "hello")
        test_string = "   hello    world   "
        self.assertEqual(ut.string_cleaner(test_string), "hello world")
        test_string = "hello world"
        self.assertEqual(ut.string_cleaner(test_string), "hello world")


class find_ind_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_find_ind(self):
        data = ["hello world", "hello mars"]
        self.assertEqual(ut.find_ind(data, "mars"), 1)
        self.assertEqual(ut.find_ind(data, "world"), 0)
        self.assertEqual(ut.find_ind(data, "hello"), 0)


class find_line_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_line(self):
        test_lines = ["", "hello", "world"]
        self.assertEqual(ut.find_line("hel", test_lines, 3), 1)
        self.assertEqual(ut.find_line("wor", test_lines, 3), 2)
        self.assertEqual(ut.find_line("", test_lines, 1), 0)


class find_nonzero_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_nonzero(self):
        test_vals = [0, 0, 0, 1, 1]
        self.assertEqual(ut.find_first_non_zero(test_vals), 3)
        test_vals = [0, 0, 0, -1, 1]
        self.assertEqual(ut.find_first_non_zero(test_vals), 3)
        test_vals = [0, 0, 0, 0, 0.0, 0]
        self.assertEqual(ut.find_first_non_zero(test_vals), None)


class find_zero_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_zero(self):
        test_vals = [0, 0, 0, 1, 1]
        self.assertEqual(ut.find_first_zero(test_vals), 0)
        test_vals = [1, 1, 0.1, 0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 0.0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 1.0]
        self.assertEqual(ut.find_first_zero(test_vals), None)


if __name__ == '__main__':
    unittest.main()
