import unittest
import neut_utilities as ut


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
