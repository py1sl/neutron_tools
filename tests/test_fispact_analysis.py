import unittest
from unittest.mock import patch, mock_open
import fispact_analysis as fa


class plotting_tests(unittest.TestCase):

    def test_dose_plot(self):
        plot = fa.plot_dose([10, 20, 30, 40],[1, 2, 3, 4])
        # x_plot, y_plot = plot.get_xydata().T
        self.assertEqual(plot.get_xlabel(), "Time (hrs)")
        self.assertEqual(plot.get_ylabel(), r"Dose rate $\mu$Sv/h")


if __name__ == '__main__':
    unittest.main()
