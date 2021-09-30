import unittest
# from unittest.mock import patch, mock_open
import fispact_analysis as fa
import pandas as pd


class support_function_tests(unittest.TestCase):
    """ test for the supporting functions in fispact analysis"""

    def test_check_time(self):
        self.assertEqual(fa.check_time_units("s"), "time_secs")
        self.assertEqual(fa.check_time_units("time_secs"), "time_secs")
        self.assertEqual(fa.check_time_units("S"), "time_secs")
        self.assertEqual(fa.check_time_units("d"), "time_days")
        self.assertEqual(fa.check_time_units("time_days"), "time_days")
        self.assertEqual(fa.check_time_units("Days"), "time_days")
        self.assertEqual(fa.check_time_units("h"), "time_hours")
        self.assertEqual(fa.check_time_units("Hrs"), "time_hours")
        self.assertEqual(fa.check_time_units("yrs"), "time_years")
        self.assertEqual(fa.check_time_units("python"), "python")

    def test_zero_pos(self):

        v, t = fa.reduce_to_non_zero([20, 20, 20, 10, 0, 1, 1, 1],
                                     [20, 20, 20, 10, 0, 1, 1, 1])
        self.assertEqual(len(t), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(v, [20, 20, 20, 10])


class plotting_tests(unittest.TestCase):

    def test_dose_plot(self):
        test_data = pd.DataFrame()

        test_data["time_years"] = [10, 20, 30, 40]
        test_data["time_days"] = test_data["time_years"] * 365.4
        test_data["time_hours"] = test_data["time_years"] * 365.4 * 24
        test_data["time_secs"] = test_data["time_years"] * 365.4 * 24 * 3600
        test_data["dose_rate"] = [1, 2, 3, 4]

        # plot = fa.plot_dose(test_data)
        # x_plot, y_plot = plot.get_xydata().T
        # self.assertEqual(plot.get_xlabel(), "time_hours")
        # self.assertEqual(plot.get_ylabel(), r"Dose rate $\mu$Sv/h")


if __name__ == '__main__':
    unittest.main()
