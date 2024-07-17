import unittest
from unittest.mock import patch, mock_open, call
import os
import mcnp_run_plot as mrp


class plotting_tests(unittest.TestCase):
    """ tests for plotting functions """

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_run_plot(self, mock_show, mock_savefig):

        test_path = os.path.join(os.path.dirname(__file__), 'test_output', 'run_output')
        mrp.plot_nps_stats(test_path)
        mock_show.assert_called_once()

        # called with a file name
        fname = "test"
        mrp.plot_nps_stats(test_path, fname=fname)
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)


if __name__ == '__main__':
    unittest.main()
