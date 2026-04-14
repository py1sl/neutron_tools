import unittest
from unittest.mock import patch, mock_open, call, MagicMock
import mcnp_analysis as ma
import mcnp_output_reader as mor
import os
import numpy as np


class normalise_test_case(unittest.TestCase):
    """ tests normalise function"""

    def test_norm_nice_data(self):
        data = [1, 2, 3, 4]
        np.testing.assert_array_equal(ma.normalise(data, 10), np.array([10, 20, 30, 40]))
        np.testing.assert_array_equal(ma.normalise(data, 1), np.array(data))
        
        result = ma.normalise(data, 0.1)
        np.testing.assert_allclose(result, [0.1, 0.2, 0.3, 0.4], rtol=1e-7)        

        # empty list
        result = ma.normalise([], 1)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.size, 0)

        # non numeric
        with self.assertRaises(ValueError):
            ma.normalise([1, "two", 3], 1)


class calc_absolute_err_test(unittest.TestCase):
    """ test for absolute error calculation function"""

    def test_abs_err_calc(self):
        err = [1, 0.5, 0.1]
        res = [1, 1, 1]
        self.assertEqual(ma.calc_err_abs(res, err), [1, 0.5, 0.1])


class calc_bin_width_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_bin_widths(self):
        bins = [1, 1.5, 1.6]
        self.assertEqual(len(ma.calc_bin_width(bins)), 3)


class calc_bin_mid_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_bin_mids(self):
        bins = [1, 3, 5]
        self.assertEqual(len(ma.calc_mid_points(bins)), 2)
        self.assertEqual(ma.calc_mid_points(bins), [2, 4])


class csv_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_csv(self):
        open_mock = mock_open()
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mor.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                data = tn
        with patch("neut_utilities.open", open_mock, create=True):
            ma.csv_out(data, "output.txt")

        open_mock.assert_called_with("output.txt", "w")


class plotting_test_cases(unittest.TestCase):
    """ tests for different plotting functions """

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_raw_spec_plot(self, mock_show, mock_savefig):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mor.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                data = tn
        fname = "test"
        ma.plot_raw_spectra(data, fname, "")
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spec_plot(self, mock_show, mock_savefig):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mor.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                data = tn
        fname = "test"
        ma.plot_spectra(data, fname, "")
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spec_ratio_plot(self, mock_show, mock_savefig):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mor.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                tn.result = [[1, 2, 3, 4, 5, 6], [1]]
                tn.eng = [10, 20, 30, 40, 50, 60]
                data = tn
        fname = "test"
        ma.plot_spectra_ratio(data, data, fname, "")
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_run_comp_plot(self, mock_show, mock_savefig):
        data = [1, 2, 3, 4]
        err = [0.1, 0.1, 0.1, 0.1]
        fname = "test"
        ma.plot_run_comp(data, err, fname, "")
        # Assert that savefig was called with the specified filename
        mock_savefig.assert_called_once_with(fname)


class calc_absolute_err_errors_test(unittest.TestCase):
    """ additional tests for calc_err_abs error handling """

    def test_abs_err_length_mismatch(self):
        with self.assertRaises(ValueError):
            ma.calc_err_abs([1, 2, 3], [0.1, 0.2])


class calc_bin_width_errors_test(unittest.TestCase):
    """ additional tests for calc_bin_width error handling """

    def test_bin_width_too_few_bins(self):
        with self.assertRaises(ValueError):
            ma.calc_bin_width([1])

        with self.assertRaises(ValueError):
            ma.calc_bin_width([])


def _make_surface_tally(tally_type, eng, result_dict, surfaces=None, ang_bins=None):
    """ helper to build a mock tally-like object """
    t = MagicMock()
    t.tally_type = tally_type
    t.eng = eng
    t.result = result_dict
    t.err = [0.01] * len(eng)
    if surfaces is not None:
        t.surfaces = surfaces
    if ang_bins is not None:
        t.ang_bins = ang_bins
    return t


class plot_spectra_additional_test_cases(unittest.TestCase):
    """ additional tests for plot_spectra covering more tally type branches """

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_type2(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        result = {1: {"result": np.array([1e-3, 2e-3, 3e-3, 4e-3])}}
        tally = _make_surface_tally('2', eng, result, surfaces=['1'])
        ma.plot_spectra(tally, "out.png", "test")
        mock_savefig.assert_called_once_with("out.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_type_else(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        tally = MagicMock()
        tally.tally_type = 'X'
        tally.eng = eng
        tally.result = np.array([1e-3, 2e-3, 3e-3, 4e-3])
        tally.err = [0.01, 0.01, 0.01, 0.01]
        ma.plot_spectra(tally, "out.png", "test")
        mock_savefig.assert_called_once_with("out.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_type1_single_surface_no_ang_bins(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        result = {1: {"result": np.array([1e-3, 2e-3, 3e-3, 4e-3])}}
        tally = _make_surface_tally('1', eng, result, surfaces=['1'], ang_bins=[1])
        ma.plot_spectra(tally, "out.png", "test")
        mock_savefig.assert_called_once_with("out.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_type1_multiple_surfaces(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        result = {
            1: {"result": np.array([1e-3, 2e-3, 3e-3, 4e-3])},
            2: {"result": np.array([0.5e-3, 1e-3, 1.5e-3, 2e-3])},
        }
        tally = _make_surface_tally('1', eng, result, surfaces=['1', '2'], ang_bins=[1])
        ma.plot_spectra(tally, "out.png", "test")
        mock_savefig.assert_called_once_with("out.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_xlow_set(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        result = {1: {"result": np.array([1e-3, 2e-3, 3e-3, 4e-3])}}
        tally = _make_surface_tally('2', eng, result, surfaces=['1'])
        ma.plot_spectra(tally, "out.png", "test", xlow=0.1)
        mock_savefig.assert_called_once_with("out.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("matplotlib.pyplot.show")
    def test_spectra_with_legend(self, mock_show, mock_savefig):
        eng = [0.1, 0.5, 1.0, 2.0]
        result = {1: {"result": np.array([1e-3, 2e-3, 3e-3, 4e-3])}}
        tally = _make_surface_tally('2', eng, result, surfaces=['1'])
        ma.plot_spectra(tally, "out.png", "test", legend=["surf 1"])
        mock_savefig.assert_called_once_with("out.png")


class plot_ET_heatmap_test(unittest.TestCase):
    """ tests for plot_ET_heatmap """

    @patch("matplotlib.pyplot.savefig")
    def test_et_heatmap(self, mock_savefig):
        energy_arr = np.array([0.1, 0.5, 1.0, 2.0, 5.0])
        time_arr = np.array([10.0, 20.0, 30.0])
        ET_results = np.random.rand(5, 4)
        ma.plot_ET_heatmap(energy_arr, time_arr, ET_results, "heatmap.png")
        mock_savefig.assert_called_once_with("heatmap.png")


class time_slice_test(unittest.TestCase):
    """ tests for time_slice """

    @patch("matplotlib.pyplot.savefig")
    def test_time_slice(self, mock_savefig):
        energy_arr = np.array([0.1, 0.5, 1.0, 2.0])
        time_arr = np.array([10.0, 20.0, 30.0])
        ET_results = np.random.rand(4, 3)
        ma.time_slice(15.0, energy_arr, time_arr, ET_results, "slice.png")
        mock_savefig.assert_called_once_with("slice.png")


class energy_slice_test(unittest.TestCase):
    """ tests for energy_slice """

    @patch("matplotlib.pyplot.savefig")
    def test_energy_slice(self, mock_savefig):
        energy_arr = np.array([0.1, 0.5, 1.0, 2.0])
        time_arr = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
        ET_results = np.random.rand(4, 6)
        ma.energy_slice(0.5, energy_arr, time_arr, ET_results, "eslice.png")
        mock_savefig.assert_called_once_with("eslice.png")

    @patch("matplotlib.pyplot.savefig")
    def test_energy_slice_with_time_limits(self, mock_savefig):
        energy_arr = np.array([0.1, 0.5, 1.0, 2.0])
        time_arr = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
        ET_results = np.random.rand(4, 6)
        ma.energy_slice(0.5, energy_arr, time_arr, ET_results, "eslice.png",
                        min_time=5, max_time=45, wl=False)
        mock_savefig.assert_called_once_with("eslice.png")


class html_output_test(unittest.TestCase):
    """ tests for html_output """

    @patch("mcnp_analysis.ut.write_html", create=True)
    @patch("matplotlib.pyplot.savefig")
    def test_html_output_no_eng(self, mock_savefig, mock_write_html):
        mc_obj = MagicMock()
        mc_obj.file_name = "test.io"
        mc_obj.date = "2024/01/01"
        mc_obj.start_time = "12:00:00"
        mc_obj.num_rendevous = 10
        mc_obj.warnings = []

        tdat = MagicMock()
        tdat.number = 4
        tdat.particle = "neutrons"
        tdat.tally_type = "4"
        tdat.eng = None
        tdat.times = None
        tdat.stat_tests = None
        tdat.cells = ['2', '3']
        tdat.vols = ['100.0', '200.0']

        mc_obj.tally_data = [tdat]

        ma.html_output(mc_obj, "output.html")
        mock_write_html.assert_called_once()

    @patch("mcnp_analysis.ut.write_html", create=True)
    @patch("matplotlib.pyplot.savefig")
    def test_html_output_with_stat_tests(self, mock_savefig, mock_write_html):
        mc_obj = MagicMock()
        mc_obj.file_name = "test.io"
        mc_obj.date = "2024/01/01"
        mc_obj.start_time = "12:00:00"
        mc_obj.num_rendevous = 10
        mc_obj.warnings = ["warning 1"]

        tdat = MagicMock()
        tdat.number = 4
        tdat.particle = "photons"
        tdat.tally_type = "4"
        tdat.eng = None
        tdat.times = None
        tdat.stat_tests = ["passed"] * 10
        tdat.cells = ['2']
        tdat.vols = ['100.0']

        mc_obj.tally_data = [tdat]

        ma.html_output(mc_obj, "output.html")
        mock_write_html.assert_called_once()


class html_f4_tab_out_test(unittest.TestCase):
    """ tests for html_f4_tab_out """

    def test_html_f4_tab_single_tally(self):
        tally = MagicMock()
        tally.number = 4
        tally.cells = ['2', '3']
        tally.result = [1.0e-3, 2.0e-3]
        tally.err = [0.01, 0.02]

        fname = "/tmp/test_f4_tab_out.html"
        ma.html_f4_tab_out(tally, fname)

        with open(fname) as f:
            content = f.read()
        self.assertIn("<table>", content)
        self.assertIn("Tally Number", content)
        self.assertIn("CellNumber", content)

    def test_html_f4_tab_list_input(self):
        tally1 = MagicMock()
        tally1.number = 4
        tally1.cells = ['2']
        tally1.result = [1.0e-3]
        tally1.err = [0.01]

        tally2 = MagicMock()
        tally2.number = 6
        tally2.cells = ['2']
        tally2.result = [2.0e-3]
        tally2.err = [0.02]

        fname = "/tmp/test_f4_tab_out_list.html"
        ma.html_f4_tab_out([tally1, tally2], fname)

        with open(fname) as f:
            content = f.read()
        self.assertIn("<table>", content)


class csv_out_list_test(unittest.TestCase):
    """ additional tests for csv_out with list input """

    def test_csv_out_with_list(self):
        open_mock = mock_open()
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mor.read_output_file(path)
        tallies = [tn for tn in single.tally_data if tn.number in (4, 6)]

        with patch("neut_utilities.open", open_mock, create=True):
            ma.csv_out(tallies, "output_list.txt")

        open_mock.assert_called_with("output_list.txt", "w")


if __name__ == '__main__':
    unittest.main()
