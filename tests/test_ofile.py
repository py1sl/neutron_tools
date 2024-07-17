import unittest
from unittest.mock import patch, mock_open
import ofile_reduce
import os


class ofile_test_case(unittest.TestCase):
    """ tests ofile reduce function"""

    def test_output(self):
        path1 = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')

        with open(path1) as f:
            inp = f.read()
        with patch("neut_utilities.open", mock_open(read_data=inp),
                   create=True) as open_mock:
            ofile_reduce.reduce_ofile("test_output/singles.io", "output.txt")

        open_mock.assert_called_with("output.txt", "w")


if __name__ == '__main__':
    unittest.main()
