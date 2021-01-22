import unittest
import fispact_output_reader as fo


class find_ind_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_find_ind(self):
        data = ["hello world", "hello mars"]
        self.assertEqual(fo.find_ind(data, "mars"), 1)
        self.assertEqual(fo.find_ind(data, "world"), 0)
        self.assertEqual(fo.find_ind(data, "hello"), 1)


if __name__ == '__main__':
    unittest.main()
