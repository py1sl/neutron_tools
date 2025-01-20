import unittest
from unittest.mock import patch, mock_open
import neut_utilities as ut
import os


class getlines_test_case(unittest.TestCase):
    """ tests get_lines function"""

    def test_get_lines(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        data = ut.get_lines(path)
        self.assertEqual(len(data), 700)


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        with patch("neut_utilities.open", open_mock, create=True):
            ut.write_lines("output.txt", ["hello", "world"])

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_any_call("hello\n")
        open_mock.return_value.write.assert_any_call("world\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_line_empty_list(self, mock_file):
        lines = []
        ut.write_lines("output.txt", lines)
        mock_file.assert_called_once_with('output.txt', 'w')
        mock_file().write.assert_not_called()


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


class string_replace_test_case(unittest.TestCase):
    """ tests for the string replace function """
    def test_string_replace_error(self):
        with self.assertRaises(FileNotFoundError):
            ut.text_replace('no_such_fname', 'old_string', 'new_string')


class same_value_test_case(unittest.TestCase):
    """test for the is_same_value function """
    def test_same_value(self):
        self.assertTrue(ut.is_same_value(1.0, 1.0))  # when same
        self.assertTrue(ut.is_same_value(1.00000001, 1.0))  # when nearly same
        self.assertFalse(ut.is_same_value(2.0, 1.0))  # when different
        self.assertFalse(ut.is_same_value(2.0, 1.0, tolerance=1e-3))  # custom tolerance
        self.assertTrue(ut.is_same_value(1.0001, 1.0, tolerance=1e-3))  # custom tolerance


if __name__ == '__main__':
    unittest.main()
