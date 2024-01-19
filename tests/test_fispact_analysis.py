import unittest
from unittest.mock import patch, mock_open, call
import fispact_analysis as fa
import fispact_output_reader as fo
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


class filtering_functions_tests(unittest.TestCase):
    """ test for the inventoryfilters"""

    def test_act_filter(self):
        inv = pd.DataFrame()
        inv["act"] = [10, 20, 30, 0, 40]
        inv = fa.remove_stable(inv)
        self.assertEqual(len(inv["act"]), 4)

    def test_alpha_filter(self):
        inv = pd.DataFrame()
        inv["a_energy"] = [10, 20, 30, 0, 40]
        inv = fa.filter_emits_alpha(inv)
        self.assertEqual(len(inv["a_energy"]), 4)

    def test_beta_filter(self):
        inv = pd.DataFrame()
        inv["b_energy"] = [10, 20, 30, 0, 40]
        inv = fa.filter_emits_beta(inv)
        self.assertEqual(len(inv["b_energy"]), 4)

    def test_gamma_filter(self):
        inv = pd.DataFrame()
        inv["g_energy"] = [10, 20, 30, 0, 40]
        inv = fa.filter_emits_gamma(inv)
        self.assertEqual(len(inv["g_energy"]), 4)

    def test_is_nuc_present(self):
        inv = pd.DataFrame()
        inv["nuclide"] = ["Ta181", "W180"]
        self.assertEqual(fa.is_nuc_present(inv, "Ta181"), True)
        self.assertEqual(fa.is_nuc_present(inv, "N45"), False)


class plotting_tests(unittest.TestCase):
    """ tests for plotting functions """
   
    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_dose_plot(self, mock_show, mock_savefig):
        test_data = pd.DataFrame()

        test_data["time_years"] = [10, 20, 30, 40]
        test_data["time_days"] = test_data["time_years"] * 365.4
        test_data["time_hours"] = test_data["time_years"] * 365.4 * 24
        test_data["time_secs"] = test_data["time_years"] * 365.4 * 24 * 3600
        test_data["dose_rate"] = [1, 2, 3, 4]

        plot = fa.plot_dose(test_data)
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_pie(self, mock_show, mock_savefig):
        test_data = pd.DataFrame()
        test_data["act"] = [5, 20, 50, 25]
        test_data["act_percent"] = [5, 20, 50, 25]
        test_data["act_nuc"] = ["H3", "W180", "Ta182", "Co60"]

        self.assertRaises(ValueError, fa.plot_pie, test_data, "", param="pyth")
        fa.plot_pie(test_data, "")
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_nuc_cont(self, mock_show, mock_savefig):
        # stub
        path = "test_output/fis_test1.out"
        output = fo.read_fis_out(path)
        plot=fa.plot_nuc_cont(output, ["co60", "fe55"])
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_nuc_chart(self, mock_show, mock_savefig):
        # stub
        path = "test_output/fis_test1.out"
        output = fo.read_fis_out(path)
        fa.plot_nuc_chart(output.timestep[3].inventory)
        mock_show.assert_called_once()
        
        
if __name__ == '__main__':
    unittest.main()
