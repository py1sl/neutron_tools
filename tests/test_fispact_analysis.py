import unittest
from unittest.mock import patch, mock_open, call
import os
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

        self.assertRaises(ValueError, fa.reduce_to_non_zero, [1, 2, 3], [1, 2])


class output_function_tests(unittest.TestCase):

    def test_mcnp_mat_output(self):
        inv = pd.DataFrame()
        inv["element"] = ["H", "C"]
        inv["A"] = [1, 8]
        inv["atoms"] = [1000, 2000]

        mat = fa.output_mcnp_mat(inv)
        self.assertEqual(len(mat["ZAID"]), len(inv["A"]))


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

    def test_plot_summary(self, mock_show, mock_savefig):
        """ testing that the plot_summary function can generate and save plots for every
        column currently existing in the data frame """
        # creating a test data frame
        test_data = pd.DataFrame()

        test_data["time_years"] = [10, 20, 30, 40]
        test_data["time_days"] = test_data["time_years"] * 365.4
        test_data["time_hours"] = test_data["time_years"] * 365.4 * 24
        test_data["time_secs"] = test_data["time_years"] * 365.4 * 24 * 3600

        test_data["act"] = [5, 6, 7, 8]
        test_data["dose_rate"] = [1, 2, 3, 4]
        test_data["heat_output"] = [9, 10, 11, 12]
        test_data["ingestion_dose"] = [0.1, 0.2, 0.3, 0.4]
        test_data["inhalation_dose"] = [0.5, 0.6, 0.7, 0.8]
        test_data["tritium_activity"] = [13, 14, 15, 16]


        #testing that plots can be generated for every column
        fa.plot_summary(test_data, column ="act")
        mock_show.assert_called()
        fa.plot_summary(test_data, column = "dose_rate")
        mock_show.assert_called()
        fa.plot_summary(test_data, column = "heat_output")
        mock_show.assert_called()
        fa.plot_summary(test_data, column = "ingestion_dose")
        mock_show.assert_called()
        fa.plot_summary(test_data, column = "inhalation_dose")
        mock_show.assert_called()
        fa.plot_summary(test_data, column = "tritium_activity")
        mock_show.assert_called()

        mock_show.assert_has_calls([call()] * 6)
        mock_show.reset_mock()

        #testing that plots can be saved for every column
        fa.plot_summary(test_data, column ="act", fname = "test")
        fa.plot_summary(test_data, column = "dose_rate", fname = "test1")
        fa.plot_summary(test_data, column = "heat_output", fname = "test2")
        fa.plot_summary(test_data, column = "ingestion_dose", fname = "test3")
        fa.plot_summary(test_data, column = "inhalation_dose", fname = "test4")
        fa.plot_summary(test_data, column = "tritium_activity", fname = "test5")

        # Assert that savefig was called with the specified filename
        expected_calls = [call("test"), call("test1"), call("test2"), call("test3"), call("test4"), call("test5")]
        mock_savefig.assert_has_calls(expected_calls, any_order=True)
        self.assertEqual(mock_savefig.call_count, 6)


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

        # called with a file name
        fname = "test"
        fa.plot_pie(test_data, "", fname=fname)
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_spectra(self, mock_show, mock_savefig):
        # stub
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)
        fa.plot_spectra(output.timestep_data[3])
        mock_show.assert_called_once()

        # called with a file name
        fname = "test"
        fa.plot_spectra(output.timestep_data[3], fname=fname)
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_nuc_cont(self, mock_show, mock_savefig):
        # stub
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)
        plot = fa.plot_nuc_cont(output, ["V52", "Sc43"])
        mock_show.assert_called_once()

        # called with a file name
        fname = "test"
        plot = fa.plot_nuc_cont(output, ["V52", "Sc43"], fname=fname)
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_plot_nuc_chart(self, mock_show, mock_savefig):
        # stub
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)
        fa.plot_nuc_chart(output.timestep_data[3].inventory)
        mock_show.assert_called_once()

        # called with a file name
        fname = "test"
        fa.plot_nuc_chart(output.timestep_data[3].inventory, fname=fname)
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    def test_create_nuc_chart_gif(self):
        """tests that the correct number of frames is in the gif"""

        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)

        frames = fa.create_nuc_chart_gif(output)

        self.assertEqual(len(frames), 9)


if __name__ == '__main__':
    unittest.main()
