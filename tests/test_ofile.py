import unittest
from unittest.mock import patch, mock_open
import ofile_reduce


class ofile_test_case(unittest.TestCase):
    """ tests ofile reduce function"""

    def test_output(self):
        with open("test_output/singles.io") as f:
            inp = f.read()
        with patch("neut_utilities.open", mock_open(read_data=inp),
                   create=True) as open_mock:
            ofile_reduce.reduce_ofile("test_output/singles.io", "output.txt")

        open_mock.assert_called_with("output.txt", "w")


if __name__ == '__main__':
    unittest.main()
