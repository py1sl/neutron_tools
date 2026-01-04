import unittest
import os
import pandas as pd
import fispact_output_reader as fo
import neut_utilities as ut


class version_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_version(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        lines = ut.get_lines(path)
        version = fo.check_fisp_version(lines)
        self.assertEqual(version, "FISPACT-II")

    def test_fis2version(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        lines = ut.get_lines(path)
        version = fo.isFisII(lines)
        self.assertEqual(version, True)

    def test_old_version(self):
        """Test detection of old FISPACT version"""
        lines = ["FISPACT VERSION 07.0/0"] + [""] * 50
        version = fo.check_fisp_version(lines)
        self.assertEqual(version, "FISP07")
        self.assertFalse(fo.isFisII(lines))


class read_mass_tests(unittest.TestCase):
    """ tests for the read mass function """

    def test_mass_read(self):
        test_lines = ["", "test", "0 Mass of material input =  1.0000E+00 kg. "]
        mass = fo.read_mass(test_lines)
        self.assertEqual(mass, 1)

    def test_mass_not_found(self):
        """Test when mass line is not found"""
        test_lines = ["", "test", "no mass here"]
        mass = fo.read_mass(test_lines)
        self.assertEqual(mass, 0.0)


class read_fis_out_test_case(unittest.TestCase):
    """ test for the read fis out function which tests many other functions """

    def test_fis_out_file1(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)
        self.assertEqual(output.file_name, path)
        self.assertEqual(output.version, "FISPACT-II")
        self.assertEqual(output.isFisII, True)
        self.assertEqual(output.cpu_time, 8.2558)
        self.assertEqual(output.tot_irrad_time, 1.2e3)
        self.assertEqual(output.tot_fluence, 7.2e9)
        self.assertEqual(output.ave_flux, 6.0e6)
        self.assertEqual(output.num_cool_step, 0)
        self.assertEqual(output.num_irrad_step, 3)
        self.assertEqual(len(output.timestep_data), 9)
        self.assertEqual(output.mass_kg, 1)
        self.assertEqual(output.mass_g, 1000)

        # individual timestep checks
        ts1 = output.timestep_data[0]
        self.assertEqual(ts1.step_num, 2)
        self.assertEqual(ts1.step_length, 600)
        self.assertEqual(ts1.num_nuclides, 98)
        self.assertEqual(ts1.alpha_act, 0)
        self.assertEqual(ts1.beta_act, 5.166878E+07)
        self.assertEqual(ts1.gamma_act, 2.848809E+04)
        self.assertEqual(ts1.total_act, 5.16973E+07)
        self.assertEqual(ts1.total_act_no_trit, 5.16973E+07)
        self.assertEqual(ts1.alpha_heat, 0)
        self.assertEqual(ts1.beta_heat, 8.80936E-09)
        self.assertEqual(ts1.gamma_heat, 1.19804E-08)
        self.assertEqual(ts1.total_heat, 2.07898E-08)
        self.assertEqual(ts1.total_heat_no_trit, 2.07898E-08)
        self.assertEqual(ts1.initial_mass, 1)
        self.assertEqual(ts1.total_mass, 1)
        self.assertEqual(ts1.neutron_flux, 6.00000E+06)
        self.assertEqual(ts1.num_fissions, 0)
        self.assertEqual(ts1.actinide_burn, 0)
        self.assertEqual(ts1.density, 5.8)
        self.assertEqual(ts1.appm_he4, 1.5508E-11)
        self.assertEqual(ts1.appm_he3, 8.4730E-12)
        self.assertEqual(ts1.appm_h3, 2.7557E-12)
        self.assertEqual(ts1.appm_h2, 9.3281E-12)
        self.assertEqual(ts1.appm_h1, 5.4402E-11)

    def test_file_not_found(self):
        """Test error when file doesn't exist"""
        with self.assertRaises(FileNotFoundError):
            fo.read_fis_out("/nonexistent/path/file.out")

    def test_path_is_directory(self):
        """Test error when path is a directory"""
        with self.assertRaises(ValueError):
            fo.read_fis_out(os.path.dirname(__file__))


class read_summary_data_test_case(unittest.TestCase):
    """ tests for the summary data """

    def test_cooling(self):
        """ tests that the data is being accurately classified as irradiated or cooling"""
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)

        sum_data = output.sumdat
        expected_cooling_values = [False, False, False, False, True, True, True, True, True]
        actual_cooling_values = sum_data["is_cooling"].tolist()

        self.assertEqual(expected_cooling_values, actual_cooling_values)

    def test_find_summary(self):
        """ tests the find summary function """
        # for fisII is False
        data = ["text", "  COOLING STEPS", "more text", "0 Mass"]
        start_ind, end_ind = fo.find_summary_block(data, False)
        self.assertEqual(start_ind, 1)
        self.assertEqual(end_ind, 3)

        # for fisII is true
        data = ["text", " -----Irradiation Phase-----", "text2", "0 Mass"]
        start_ind, end_ind = fo.find_summary_block(data, True)
        self.assertEqual(start_ind, 1)
        self.assertEqual(end_ind, 3)

        # test raises error when cooling string not found
        data = ["text", " more text",  "0 Mass"]

        with self.assertRaises(ValueError) as context:
            fo.find_summary_block(data, True)


class retrieve_cooling_data_test_case(unittest.TestCase):
    """ tests the filtered summary data """

    def test_cooling_columns(self):
        """ tests that the right amount of data has been filtered """

        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)

        sum_data = output.sumdat
        cooling_data = fo.retrieve_cooling_data(sum_data)

        self.assertEqual(len(cooling_data), 5)


class add_time_columns_test_case(unittest.TestCase):
    """tests for the add_time_columns function"""

    def test_add_time_columns(self):
        """Test adding time columns to a dataframe"""
        df = pd.DataFrame()
        df["time_years"] = [1.0, 2.0, 3.0]

        result = fo.add_time_columns(df, "time_years")

        self.assertIn("time_days", result.columns)
        self.assertIn("time_hours", result.columns)
        self.assertIn("time_secs", result.columns)
        self.assertAlmostEqual(result["time_days"].iloc[0], 365.4, places=1)
        self.assertAlmostEqual(result["time_hours"].iloc[0], 365.4 * 24, places=1)

    def test_add_time_columns_invalid_df(self):
        """Test error when df is not a DataFrame"""
        with self.assertRaises(ValueError):
            fo.add_time_columns([1, 2, 3], "time_years")

    def test_add_time_columns_missing_column(self):
        """Test error when base column is missing"""
        df = pd.DataFrame()
        df["wrong_column"] = [1.0, 2.0, 3.0]
        with self.assertRaises(ValueError):
            fo.add_time_columns(df, "time_years")


class parse_functions_test_case(unittest.TestCase):
    """tests for parse functions with error handling"""

    def test_parse_dominant_empty_data(self):
        """Test parse_dominant with invalid input"""
        with self.assertRaises(ValueError):
            fo.parse_dominant([])

    def test_parse_composition_empty_data(self):
        """Test parse_composition with invalid input"""
        with self.assertRaises(ValueError):
            fo.parse_composition([])

    def test_parse_spectra_empty_data(self):
        """Test parse_spectra with invalid input"""
        with self.assertRaises(ValueError):
            fo.parse_spectra([])

    def test_parse_inventory_empty_data(self):
        """Test parse_inventory with invalid input"""
        with self.assertRaises(ValueError):
            fo.parse_inventory([])

    def test_read_time_step_empty_data(self):
        """Test read_time_step with invalid input"""
        with self.assertRaises(ValueError):
            fo.read_time_step([], 0)

    def test_read_parameter_empty_data(self):
        """Test read_parameter with invalid input"""
        with self.assertRaises(ValueError):
            fo.read_parameter([], "test")


class find_first_cooling_index_test_case(unittest.TestCase):
    """tests for find_first_cooling_index"""

    def test_no_cooling(self):
        """Test when there is no cooling phase"""
        df = pd.DataFrame()
        df["is_cooling"] = [False, False, False]
        result = fo.find_first_cooling_index(df)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
