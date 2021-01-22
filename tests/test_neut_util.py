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


class find_line_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_is_version(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
