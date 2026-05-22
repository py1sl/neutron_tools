import unittest
from unittest.mock import patch, mock_open
import logging
import pandas as pd
import numpy as np
from neutron_tools.mcnp import mcnp_output_reader
from neutron_tools.utilities import neut_utilities as ut
import os


class version_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_is_version(self):
        """ test when a version is in the list of strings """
        list_a = ["          Code Name & Version = MCNP6, 1.0",
                  "  "]
        self.assertEqual(mcnp_output_reader.read_version(list_a), "MCNP6, 1.0")

    def test_is_version_none_given_other_list(self):
        """ test for only allocating if an actual  version not a random string"""
        list_a = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                  "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                  "ccccccccccccccccccccccccccccccccccccccccccccccccc",
                  "ddddddddddddddddddddddddddddddddddddddddddddddddd"]
        list_b = ["a", "b", "c", "d"]
        self.assertIsNone(mcnp_output_reader.read_version(list_a))
        self.assertIsNone(mcnp_output_reader.read_version(list_b))

    def test_is_version_none_given_string(self):
        """ test for version with string"""
        string_a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertIsNone(mcnp_output_reader.read_version(string_a))

    def test_empty_input(self):
        """ test for empty list given """
        empty_list = []
        self.assertIsNone(mcnp_output_reader.read_version(empty_list))


class read_warnings_test_case(unittest.TestCase):

    def test_read_comments_warnings_successful(self):
        """ Test when comments and warnings are present in the lines """
        lines = [
            "  comment. This is a comment.",
            "  warning. This is a warning.",
            "Some other line"
        ]
        result_comments, result_warnings = mcnp_output_reader.read_comments_warnings(lines)

        self.assertEqual(result_comments, ["  comment. This is a comment."])
        self.assertEqual(result_warnings, ["  warning. This is a warning."])

    def test_read_comments_warnings_no_comments_warnings(self):
        """ Test when there are no comments or warnings in the lines """
        lines = ["Some other line"]
        result_comments, result_warnings = mcnp_output_reader.read_comments_warnings(lines)

        self.assertEqual(result_comments, [])
        self.assertEqual(result_warnings, [])

    def test_read_multiple_comments_warnings_successful(self):
        """ Test when multiple comments and warnings are present in the lines """
        lines = [
            "  comment. This is a comment.",
            "  warning. This is a warning.",
            "Some other line",
            "  comment. This is a comment.",
            "  warning. This is a warning.",
        ]
        result_comments, result_warnings = mcnp_output_reader.read_comments_warnings(lines)

        self.assertEqual(len(result_comments), 2)
        self.assertEqual(len(result_warnings), 2)


class get_tally_nums_test_case(unittest.TestCase):
    """ test for get talyl num """

    @classmethod
    def setUpClass(cls):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        cls.data = ut.get_lines(path)
        cls.single = mcnp_output_reader.read_output_file(path)

    def test_get_tally_num(self):
        # test with a set of differnt tally types
        tnums = mcnp_output_reader.get_tally_nums(self.data)
        self.assertEqual(len(tnums), 6)
        self.assertIn("1", tnums)
        self.assertIn("2", tnums)
        self.assertIn("4", tnums)
        self.assertIn("5", tnums)
        self.assertIn("6", tnums)
        self.assertIn("8", tnums)

    def test_tally_count(self):
        # test assignment of mcnp output object num_tallies
        self.assertEqual(self.single.num_tallies, 6)


class rendevous_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    @classmethod
    def setUpClass(cls):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        cls.data = ut.get_lines(path)

    def test_count_rendevous_tests(self):

        # add test with a single core job count should be 0

        # need to add test for multicore job
        count = mcnp_output_reader.count_rendevous(self.data)
        self.assertEqual(count, 76)

    def test_index_rendevous_tests(self):

        # add test with a single core job should be 0
        # index = mcnp_output_reader.get_rendevous_index(self.data)
        # self.assertEqual(index, [])

        # need to add test for multicore job
        index = mcnp_output_reader.get_rendevous_index(self.data)
        self.assertEqual(len(index), 76)


class stat_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_read_stat_tests(self):
        self.assertTrue(True)
        # need to add test for tally with all 0.0 bins


class tally_processing_tests(unittest.TestCase):
    """ tests for various generic tally processing functions """

    def test_process_time_bin_only(self):
        """ """
        lines = [
            "time 1.0 2.0 3.0",
            "1.5 0.01",
            "2.5 0.02",
            "3.5 0.03"
        ]
        expected_time_bins = ["1.0", "2.0", "3.0"]
        expected_results = [1.5, 2.5, 3.5]
        expected_errs = [0.01, 0.02, 0.03]

        df = mcnp_output_reader.process_time_bin_only(lines)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df["time"].tolist(), expected_time_bins)
        self.assertEqual(df["result"].tolist(), expected_results)
        self.assertEqual(df["rel_err"].tolist(), expected_errs)

    def test_process_eng_time_get_time_bins(self):
        "testing function to get the time bins when a tally has energy and time bins"
        # test for a single time line
        data = [
            "some irrelevant line",
            "time 1.0 2.0 3.0"
        ]
        expected = ['1.0', '2.0', '3.0']
        tbins = mcnp_output_reader.eng_time_get_time_bins(data)
        self.assertEqual(tbins, expected)

        # test for a multiple time lines with no duplicates
        data = [
            "some irrelevant line",
            "time 1.0 2.0 3.0",
            "time 4.0 5.0 6.0"
        ]
        expected = ['1.0', '2.0', '3.0', '4.0', '5.0', '6.0']
        tbins = mcnp_output_reader.eng_time_get_time_bins(data)
        self.assertEqual(tbins, expected)

        # test for multiple lines, with duplicates
        data = [
            "some irrelevant line",
            "time 1.0 2.0 3.0",
            "time 2.0 3.0 4.0"
        ]
        expected = ['1.0', '2.0', '3.0', '4.0']
        tbins = mcnp_output_reader.eng_time_get_time_bins(data)
        self.assertEqual(tbins, expected)

    def test_process_energy_lines(self):
        """ tests the section of the code that processes lines for tallies with only energy bins """
        lines = [
            "1.0 0.0 0.0 10.0 0.1",
            "2.0 0.0 0.0 20.0 0.05",
            "3.0 0.0 0.0 30.0 0.03"
        ]
        expected_erg = [1.0, 2.0, 3.0]
        expected_res = [10.0, 20.0, 30.0]
        expected_rel_err = [0.1, 0.05, 0.03]

        df = mcnp_output_reader.process_energy_lines(lines)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertListEqual(list(df.columns), ["energy", "result", "rel_err"])
        self.assertEqual(df["energy"].tolist(), expected_erg)
        self.assertEqual(df["result"].tolist(), expected_res)
        self.assertEqual(df["rel_err"].tolist(), expected_rel_err)

    def test_convert_et_tally_to_df(self):
        """ """
        # test valid data
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        time_bins = [0.1, 0.2, 0.3]
        energy_bins = [100, 200, 300]

        df = mcnp_output_reader.convert_energy_time_data_to_df(data, time_bins, energy_bins)
        expected_df = pd.DataFrame(data, index=time_bins, columns=energy_bins)
        pd.testing.assert_frame_equal(df, expected_df)

        # test data that won't convert
        data = np.array([[1, 2], [4, 5], [7, 8]])
        time_bins = [0.1, 0.2, 0.3]
        energy_bins = [100, 200, 300]

        result = mcnp_output_reader.convert_energy_time_data_to_df(data, time_bins, energy_bins)
        # Since conversion fails, the function should return the original data
        np.testing.assert_array_equal(result, data)


class tally_type1_tests(unittest.TestCase):
    """ tests for type 1 tally """

    def test_single_value_t1_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.tally_type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 1.16486E+00)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.0006)

    def test_ebined_t1_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.tally_type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertIsInstance(tn.result, dict)
                # After 1a: totals are folded into the DataFrame as a "total" row
                first_df = list(tn.result.values())[0]
                self.assertIsInstance(first_df, pd.DataFrame)
                total_rows = first_df[first_df["energy"] == "total"]
                self.assertEqual(len(total_rows), 1)

    def test_tbinned_t1_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_t.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.tally_type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 200000)
                self.assertEqual(tn.eng, None)
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                surf_df = list(tn.result.values())[0]
                self.assertIsInstance(surf_df, pd.DataFrame)
                self.assertEqual(len(surf_df), 14)
                self.assertAlmostEqual(surf_df.iloc[-1]["result"], 2.44655e-1)
                self.assertAlmostEqual(surf_df.iloc[-1]["rel_err"], 0.0039)


class tally_type2_tests(unittest.TestCase):
    """ tests for type 2 tally """

    def test_single_value_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.surfaces), 1)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 4.31795E-03)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.0015)

    def test_multiple_value_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.surfaces), 6)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.surfaces))

    def test_ebined_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.surfaces), 1)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertEqual(len(tn.result), len(tn.surfaces))
                # total row is folded into each DataFrame
                first_df = list(tn.result.values())[0]
                self.assertEqual(len(first_df[first_df["energy"] == "total"]), 1)

    def test_multiple_ebined_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.surfaces), 6)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertEqual(len(tn.result), len(tn.surfaces))
                # total row is folded into each DataFrame
                first_df = list(tn.result.values())[0]
                self.assertEqual(len(first_df[first_df["energy"] == "total"]), 1)

    def test_etbinned_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_et.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.eng[-1], 1.5)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], 1000)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.surfaces), 1)
                self.assertEqual(len(tn.surfaces), len(tn.areas))

    def test_multiple_etbinned_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_et.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.eng[-1], 1.5)
                self.assertEqual(len(tn.times), 13)
                self.assertEqual(tn.times[-1], 100)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.surfaces), 6)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertEqual(len(tn.result), len(tn.surfaces))

    def test_tbinned_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_t.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 200000)
                self.assertEqual(tn.eng, None)
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                surf_df = list(tn.result.values())[0]
                self.assertIsInstance(surf_df, pd.DataFrame)
                self.assertEqual(len(surf_df), 14)
                self.assertAlmostEqual(surf_df.iloc[-1]["result"], 2.69842E-04)
                self.assertAlmostEqual(surf_df.iloc[-1]["rel_err"], 0.0054)
                self.assertEqual(len(tn.surfaces), 1)
                self.assertEqual(len(tn.surfaces), len(tn.areas))

    def test_multiple_tbinned_t2_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_t.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.tally_type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 6)
                self.assertEqual(len(tn.surfaces), 6)
                self.assertEqual(len(tn.surfaces), len(tn.areas))
                self.assertEqual(len(tn.result), len(tn.surfaces))


class tally_type4_tests(unittest.TestCase):
    """ tests for type 4 tally """

    def test_single_value_t4_tally(self):
        """ test case - f4 tally with a single cell and single flux """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 1.91076E-03)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.0006)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['3.66519E+03'])

    def test_multiple_value_t4_tally(self):
        """ test case - f4 tally with a multiple cells and single flux value for each cell """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple.io')
        multiple = mcnp_output_reader.read_output_file(path)
        for tn in multiple.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.cells, ['2', '3', '4', '5', '6'])
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertEqual(len(tn.vols), 5)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.cells))
                first_df = tn.result[int(tn.cells[0])]
                last_df = tn.result[int(tn.cells[-1])]
                self.assertAlmostEqual(first_df["result"].iloc[0], 2.19878E-03)
                self.assertAlmostEqual(first_df["rel_err"].iloc[0], 0.0006)
                self.assertAlmostEqual(last_df["result"].iloc[0], 3.60573E-06)
                self.assertAlmostEqual(last_df["rel_err"].iloc[0], 0.0043)

    def test_ebined_t4_tally(self):
        """ test case - f4 tally with a single cell with energy bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['3.66519E+03'])
                self.assertIsInstance(tn.result, dict)
                # total row is folded into each DataFrame
                first_df = list(tn.result.values())[0]
                self.assertEqual(len(first_df[first_df["energy"] == "total"]), 1)

    def test_multiple_value_ebined_t4_tally(self):
        """ test case - f4 tally with a multiple cells each with energy bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_erg.io')
        multiple = mcnp_output_reader.read_output_file(path)
        for tn in multiple.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.cells, ['2', '3', '4', '5', '6'])
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertEqual(len(tn.vols), 5)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.vols))
                self.assertEqual(list(tn.result.keys()), [int(s) for s in tn.cells])
                # total row is folded into each DataFrame
                first_df = tn.result[int(tn.cells[0])]
                self.assertEqual(len(first_df[first_df["energy"] == "total"]), 1)

    def test_etbinned_t4_tally(self):
        """ test case - f4 tally with a single cell with energy and time bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_et.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.eng[-1], 1.5)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], 1000)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.cells), 1)
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.cells))
                self.assertIsInstance(tn.err, dict)
                self.assertEqual(len(tn.err), len(tn.cells))

    def test_multiple_value_etbinned_t4_tally(self):
        """ test case - f4 tally with multiple cells with energy and time bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_et.io')
        multiple = mcnp_output_reader.read_output_file(path)
        for tn in multiple.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.cells, ['2', '3', '4', '5', '6'])
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertEqual(len(tn.vols), 5)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.cells))
                self.assertIsInstance(tn.err, dict)
                self.assertEqual(len(tn.err), len(tn.cells))

    def test_tbinned_t4_tally(self):
        """ test case - f4 tally with a single cell with times bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_t.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 200000)
                self.assertEqual(tn.eng, None)
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.cells))
                cell_df = list(tn.result.values())[0]
                self.assertIsInstance(cell_df, pd.DataFrame)
                self.assertEqual(len(cell_df), 14)
                self.assertAlmostEqual(cell_df.iloc[-1]["result"], 1.70644e-03, places=7)
                self.assertAlmostEqual(cell_df.iloc[-1]["rel_err"], 0.0008)

    def test_multiple_value_tbinned_t4_tally(self):
        """ test case - f4 tally with multiple cells with time bins """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_t.io')
        multiple = mcnp_output_reader.read_output_file(path)
        for tn in multiple.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.tally_type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertNotEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.cells, ['2', '3', '4', '5', '6'])
                self.assertEqual(len(tn.vols), len(tn.cells))
                self.assertEqual(len(tn.vols), 5)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), len(tn.cells))
                # each cell gives a DataFrame with time rows
                first_cell_df = list(tn.result.values())[0]
                self.assertIsInstance(first_cell_df, pd.DataFrame)


class tally_type5_tests(unittest.TestCase):
    """ tests for type 5 tally """

    def test_single_value_t5_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.tally_type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 3.42950E-04)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.0025)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.x, 15.0)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)
                self.assertEqual(tn.largest_score, 2.32897E-01)
                self.assertEqual(tn.largest_score_nps, 492485)
                self.assertEqual(tn.average_per_history, 3.42950E-04)
                self.assertEqual(tn.misses["russian roulette on pd"], 0)
                self.assertEqual(tn.misses["psc=0"], 0)
                tstring = "russian roulette in transmission"
                self.assertEqual(tn.misses[tstring], 935317)
                self.assertEqual(tn.misses["underflow in transmission"], 39376)
                self.assertEqual(tn.misses["hit a zero-importance cell"], 0)
                self.assertEqual(tn.misses["energy cutoff"], 0)
                self.assertIsInstance(tn.cell_scores, pd.DataFrame)
                self.assertEqual(list(tn.cell_scores.columns),
                                 ["cell", "misses", "hits", "tally_per_history", "weight_per_hit"])
                self.assertEqual(len(tn.cell_scores), 3)  # 2 cells + total
                self.assertEqual(tn.cell_scores.iloc[-1]["cell"], "total")
                self.assertEqual(tn.cell_scores.iloc[0]["cell"], "1")
                self.assertEqual(tn.cell_scores.iloc[0]["misses"], 0)
                self.assertEqual(tn.cell_scores.iloc[0]["hits"], 1000000)
                self.assertAlmostEqual(tn.cell_scores.iloc[0]["tally_per_history"], 1.72673E-04)
                self.assertAlmostEqual(tn.cell_scores.iloc[-1]["tally_per_history"], 3.42950E-04)

    def test_ebined_t5_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.tally_type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 1.20831E-05)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)
                self.assertEqual(tn.largest_score, 2.32897E-01)
                self.assertEqual(tn.largest_score_nps, 492485)
                self.assertEqual(tn.average_per_history, 3.42950E-04)
                self.assertEqual(tn.misses["russian roulette on pd"], 0)
                self.assertEqual(tn.misses["psc=0"], 0)
                tstring = "russian roulette in transmission"
                self.assertEqual(tn.misses[tstring], 935317)
                self.assertEqual(tn.misses["underflow in transmission"], 39376)
                self.assertEqual(tn.misses["hit a zero-importance cell"], 0)
                self.assertEqual(tn.misses["energy cutoff"], 0)
                self.assertIsInstance(tn.cell_scores, pd.DataFrame)
                self.assertEqual(len(tn.cell_scores), 3)  # 2 cells + total
                self.assertEqual(tn.cell_scores.iloc[-1]["cell"], "total")
                self.assertAlmostEqual(tn.cell_scores.iloc[-1]["tally_per_history"], 3.42950E-04)

    def test_etbined_t5_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_et.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.tally_type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(len(tn.times), 14)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                res_df = list(tn.result.values())[0]
                self.assertIsInstance(res_df, pd.DataFrame)
                self.assertEqual(res_df.shape[0], 14)  # 14 energy rows
                self.assertEqual(res_df.shape[1], 14)  # 14 time columns
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)
                self.assertIsInstance(tn.cell_scores, pd.DataFrame)
                self.assertEqual(len(tn.cell_scores), 3)  # 2 cells + total
                self.assertEqual(tn.cell_scores.iloc[-1]["cell"], "total")
                self.assertEqual(tn.cell_scores.iloc[-1]["misses"], 976331)
                self.assertEqual(tn.cell_scores.iloc[-1]["hits"], 1643329)
                self.assertAlmostEqual(tn.cell_scores.iloc[-1]["tally_per_history"], 3.44027E-04)

    def test_multiple_ebined_t5_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'multiple_erg.io')
        multiple = mcnp_output_reader.read_output_file(path)
        for tn in multiple.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.tally_type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)
                self.assertAlmostEqual(tn.average_per_history, 4.96162E-04)
                self.assertAlmostEqual(tn.largest_score, 2.22478E+00)
                self.assertEqual(tn.largest_score_nps, 517734)
                self.assertEqual(tn.misses["russian roulette in transmission"], 5999373)
                self.assertEqual(tn.misses["underflow in transmission"], 125625)
                self.assertIsInstance(tn.cell_scores, pd.DataFrame)
                self.assertEqual(len(tn.cell_scores), 7)  # 6 cells + total
                self.assertEqual(tn.cell_scores.iloc[-1]["cell"], "total")
                self.assertEqual(tn.cell_scores.iloc[0]["cell"], "1")
                self.assertEqual(tn.cell_scores.iloc[0]["misses"], 0)
                self.assertEqual(tn.cell_scores.iloc[0]["hits"], 1000000)
                self.assertAlmostEqual(tn.cell_scores.iloc[0]["tally_per_history"], 8.43023E-05)
                self.assertAlmostEqual(tn.cell_scores.iloc[-1]["tally_per_history"], 4.96162E-04)
                self.assertAlmostEqual(tn.cell_scores.iloc[-1]["weight_per_hit"], 1.15095E-04)

class tally_type6_tests(unittest.TestCase):
    """ tests for type 6 tally """

    def test_single_value_t6_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.tally_type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 4.30567E-05)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.0002)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['9.89602E+03'])

    def test_ebined_t6_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.tally_type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                # total row folded into DataFrame
                first_df = list(tn.result.values())[0]
                self.assertEqual(len(first_df[first_df["energy"] == "total"]), 1)
                self.assertEqual(tn.vols, ['9.89602E+03'])


class tally_type5_helper_function_tests(unittest.TestCase):
    """Unit tests for type 5 tally helper functions using crafted input lines."""

    CELL_SCORE_LINES = [
        " score contributions by cell",
        "        cell      misses        hits    tally per history    weight per hit",
        "     1     1           0     1000000       1.72673E-04         1.72673E-04",
        "     2     2      974693      645404       1.70277E-04         2.63830E-04",
        "       total      974693     1645404       3.42950E-04         2.08429E-04",
    ]

    DIAGNOSTICS_LINES = [
        " detector score diagnostics                  cumulative          tally         cumulative",
        "                                             fraction of         per           fraction of",
        "   times average score     transmissions     transmissions       history       total tally",
        "        1.00000E-01             246684         0.14992        8.46227E-06        0.02467",
        "        1.00000E+00            1290278         0.93409        2.06874E-04        0.62789",
        "        1.00000E+38                  0         0.99853        0.00000E+00        0.99899",
        " before dd roulette               2411         1.00000        3.47496E-07        1.00000",
        "",
    ]

    GENERAL_STATS_LINES = [
        " average tally per history = 3.42950E-04            largest score = 2.32897E-01",
        " (largest score)/(average tally) = 6.79099E+02      nps of largest score =      492485",
    ]

    SCORE_MISSES_LINES = [
        " score misses",
        "   russian roulette on pd                        0",
        "   psc=0.                                        0",
        "   russian roulette in transmission         935317",
        "   underflow in transmission                 39376",
        "   hit a zero-importance cell                    0",
        "   energy cutoff                                 0",
    ]

    def test_cell_scores_returns_dataframe(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertIsInstance(df, pd.DataFrame)

    def test_cell_scores_columns(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertListEqual(list(df.columns),
                             ["cell", "misses", "hits", "tally_per_history", "weight_per_hit"])

    def test_cell_scores_row_count(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertEqual(len(df), 3)  # 2 cell rows + total

    def test_cell_scores_total_row_is_last(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertEqual(df.iloc[-1]["cell"], "total")

    def test_cell_scores_first_cell_values(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertEqual(df.iloc[0]["cell"], "1")
        self.assertEqual(df.iloc[0]["misses"], 0)
        self.assertEqual(df.iloc[0]["hits"], 1000000)
        self.assertAlmostEqual(df.iloc[0]["tally_per_history"], 1.72673E-04)
        self.assertAlmostEqual(df.iloc[0]["weight_per_hit"], 1.72673E-04)

    def test_cell_scores_second_cell_values(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertEqual(df.iloc[1]["cell"], "2")
        self.assertEqual(df.iloc[1]["misses"], 974693)
        self.assertEqual(df.iloc[1]["hits"], 645404)
        self.assertAlmostEqual(df.iloc[1]["tally_per_history"], 1.70277E-04)
        self.assertAlmostEqual(df.iloc[1]["weight_per_hit"], 2.63830E-04)

    def test_cell_scores_total_values(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        self.assertEqual(df.iloc[-1]["misses"], 974693)
        self.assertEqual(df.iloc[-1]["hits"], 1645404)
        self.assertAlmostEqual(df.iloc[-1]["tally_per_history"], 3.42950E-04)
        self.assertAlmostEqual(df.iloc[-1]["weight_per_hit"], 2.08429E-04)

    def test_cell_scores_numeric_columns(self):
        df = mcnp_output_reader.read_type5_cell_scores(self.CELL_SCORE_LINES)
        for col in ["misses", "hits", "tally_per_history", "weight_per_hit"]:
            self.assertTrue(pd.api.types.is_numeric_dtype(df[col]),
                            msg=f"column '{col}' is not numeric")

    def test_diagnostics_returns_dataframe(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        self.assertIsInstance(df, pd.DataFrame)

    def test_diagnostics_columns(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        expected = ["times_average_score", "transmissions",
                    "cumulative_fraction_transmissions", "tally_per_history",
                    "cumulative_fraction_total"]
        self.assertListEqual(list(df.columns), expected)

    def test_diagnostics_row_count(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        self.assertEqual(len(df), 4)  # 3 numeric rows + before dd roulette

    def test_diagnostics_first_row_values(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        self.assertAlmostEqual(df.iloc[0]["times_average_score"], 1.0E-01)
        self.assertEqual(df.iloc[0]["transmissions"], 246684)
        self.assertAlmostEqual(df.iloc[0]["cumulative_fraction_transmissions"], 0.14992)
        self.assertAlmostEqual(df.iloc[0]["tally_per_history"], 8.46227E-06)
        self.assertAlmostEqual(df.iloc[0]["cumulative_fraction_total"], 0.02467)

    def test_diagnostics_before_dd_roulette_nan(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        self.assertTrue(pd.isna(df.iloc[-1]["times_average_score"]))

    def test_diagnostics_numeric_columns(self):
        df = mcnp_output_reader.read_type5_diagnostics(self.DIAGNOSTICS_LINES)
        for col in ["transmissions", "cumulative_fraction_transmissions",
                    "tally_per_history", "cumulative_fraction_total"]:
            self.assertTrue(pd.api.types.is_numeric_dtype(df[col]),
                            msg=f"column '{col}' is not numeric")

    def test_general_stats_average_per_history(self):
        tally_data = mcnp_output_reader.MCNP_type5_tally()
        tally_data = mcnp_output_reader.read_type5_general_stats(tally_data, self.GENERAL_STATS_LINES)
        self.assertAlmostEqual(tally_data.average_per_history, 3.42950E-04)

    def test_general_stats_largest_score(self):
        tally_data = mcnp_output_reader.MCNP_type5_tally()
        tally_data = mcnp_output_reader.read_type5_general_stats(tally_data, self.GENERAL_STATS_LINES)
        self.assertAlmostEqual(tally_data.largest_score, 2.32897E-01)

    def test_general_stats_largest_score_nps(self):
        tally_data = mcnp_output_reader.MCNP_type5_tally()
        tally_data = mcnp_output_reader.read_type5_general_stats(tally_data, self.GENERAL_STATS_LINES)
        self.assertAlmostEqual(tally_data.largest_score_nps, 492485)

    def test_score_misses_returns_dict(self):
        misses = mcnp_output_reader.read_type5_score_misses(self.SCORE_MISSES_LINES)
        self.assertIsInstance(misses, dict)

    def test_score_misses_keys(self):
        misses = mcnp_output_reader.read_type5_score_misses(self.SCORE_MISSES_LINES)
        expected_keys = [
            "russian roulette on pd", "psc=0",
            "russian roulette in transmission", "underflow in transmission",
            "hit a zero-importance cell", "energy cutoff",
        ]
        for key in expected_keys:
            self.assertIn(key, misses)

    def test_score_misses_values(self):
        misses = mcnp_output_reader.read_type5_score_misses(self.SCORE_MISSES_LINES)
        self.assertEqual(misses["russian roulette on pd"], 0)
        self.assertEqual(misses["psc=0"], 0)
        self.assertEqual(misses["russian roulette in transmission"], 935317)
        self.assertEqual(misses["underflow in transmission"], 39376)
        self.assertEqual(misses["hit a zero-importance cell"], 0)
        self.assertEqual(misses["energy cutoff"], 0)


class tally_type8_tests(unittest.TestCase):
    """ tests for type 8 tally """

    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        self.single = mcnp_output_reader.read_output_file(path)

    def test_single_value_t8_tally(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles.io')
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.tally_type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 1.00000E+00)
                self.assertAlmostEqual(df["rel_err"].iloc[0], 0.00)

    def test_ebined_t8_tally(self):
        for tn in self.single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.tally_type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertIsInstance(tn.result, dict)
                self.assertEqual(len(tn.result), 1)
                df = list(tn.result.values())[0]
                self.assertIsInstance(df, pd.DataFrame)
                self.assertAlmostEqual(df["result"].iloc[0], 5.16461E-01)


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        logger = logging.getLogger()
        logger.level = logging.DEBUG
        with patch("neutron_tools.utilities.neut_utilities.open", open_mock, create=True):
            mcnp_output_reader.print_tally_lines_to_file(["hello", "world"],
                                                         "output", 1)

        open_mock.assert_called_with("output1.txt", "w")
        open_mock.return_value.write.assert_any_call("hello\n")


class tables_testing(unittest.TestCase):
    """ test for output tables """

    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'singles_erg.io')
        self.single = mcnp_output_reader.read_output_file(path)
        self.t60 = self.single.t60

    def test_table_numbers(self):
        # tests getting all the  print table numbers
        self.assertEqual(len(self.single.tables), 4)
        self.assertEqual(self.single.tables['60'], 69)

    def test_t60(self):
        # tests print table 60 - cell information
        self.assertEqual(len(self.t60["mass"]), 4)
        self.assertEqual(len(self.t60.columns), 8)
        self.assertFalse(self.t60.empty)

    def test_t101(self):
        # tests print table 101 - particles and energy limits
        self.assertEqual(len(self.single.t101['particle_name']), 2)
        self.assertFalse(self.single.t101.empty)

    def test_t126(self):
        # test print table 126 - activity in cells
        self.assertTrue(True)


class str_method_tests(unittest.TestCase):
    """ tests for __str__ methods on tally classes """

    def test_type5_tally_str_no_bins(self):
        t = mcnp_output_reader.MCNP_type5_tally()
        t.number = 5
        t.particle = "photons"
        t.x = 10.0
        t.y = 0.0
        t.z = 0.0
        result = str(t)
        self.assertIn("5", result)
        self.assertIn("photons", result)
        self.assertIn("Energy Bins: False", result)
        self.assertIn("Time Bins: False", result)

    def test_type5_tally_str_with_bins(self):
        t = mcnp_output_reader.MCNP_type5_tally()
        t.number = 5
        t.particle = "neutrons"
        t.x = 5.0
        t.y = 5.0
        t.z = 0.0
        t.eng = [0.1, 1.0]
        t.times = [10, 100]
        result = str(t)
        self.assertIn("Energy Bins: True", result)
        self.assertIn("Time Bins: True", result)

    def test_surface_tally_str_no_bins(self):
        t = mcnp_output_reader.MCNP_surface_tally()
        t.number = 2
        t.particle = "photons"
        t.surfaces = ['1', '2', '3']
        result = str(t)
        self.assertIn("3", result)
        self.assertIn("Energy Bins: False", result)
        self.assertIn("Time Bins: False", result)
        self.assertIn("Angular Bins: False", result)

    def test_surface_tally_str_with_bins(self):
        t = mcnp_output_reader.MCNP_surface_tally()
        t.number = 2
        t.particle = "neutrons"
        t.surfaces = ['1']
        t.eng = [0.1, 1.0]
        t.times = [10, 100]
        t.ang_bins = [-1.0, 0.0]
        result = str(t)
        self.assertIn("Energy Bins: True", result)
        self.assertIn("Time Bins: True", result)
        self.assertIn("Angular Bins: True", result)

    def test_cell_tally_str_no_bins(self):
        t = mcnp_output_reader.MCNP_cell_tally()
        t.number = 4
        t.particle = "photons"
        t.cells = ['2', '3']
        result = str(t)
        self.assertIn("2", result)
        self.assertIn("Energy Bins: False", result)
        self.assertIn("Time Bins: False", result)

    def test_cell_tally_str_with_bins(self):
        t = mcnp_output_reader.MCNP_cell_tally()
        t.number = 4
        t.particle = "neutrons"
        t.cells = ['2']
        t.eng = [0.1, 1.0]
        t.times = [10, 100]
        result = str(t)
        self.assertIn("Energy Bins: True", result)
        self.assertIn("Time Bins: True", result)

    def test_pulse_tally_str_no_bins(self):
        t = mcnp_output_reader.MCNP_pulse_tally()
        t.number = 8
        t.particle = "photons"
        t.cells = ['2']
        result = str(t)
        self.assertIn("8", result)
        self.assertIn("Energy Bins: False", result)
        self.assertIn("Time Bins: False", result)

    def test_pulse_tally_str_with_bins(self):
        t = mcnp_output_reader.MCNP_pulse_tally()
        t.number = 8
        t.particle = "photons"
        t.cells = ['2']
        t.eng = [0.1, 1.0]
        t.times = [10, 100]
        result = str(t)
        self.assertIn("Energy Bins: True", result)
        self.assertIn("Time Bins: True", result)

    def test_summary_data_str(self):
        s = mcnp_output_reader.MCNP_summary_data()
        s.nps = 1000000
        s.particle = "Neutron"
        result = str(s)
        self.assertIn("1000000", result)
        self.assertIn("Neutron", result)


class process_ang_string_test(unittest.TestCase):
    """ tests for process_ang_string """

    def test_process_ang_string(self):
        # format: "... angle  bin: X to Y mu" - [-2] is the upper bound float
        line = " angle  bin: -1.0000E+00 to  0.0000E+00 mu"
        result = mcnp_output_reader.process_ang_string(line)
        self.assertAlmostEqual(result, 0.0)

    def test_process_ang_string_negative(self):
        line = " angle  bin: -1.0000E+00 to -2.5000E-01 mu"
        result = mcnp_output_reader.process_ang_string(line)
        self.assertAlmostEqual(result, -0.25)


class eng_time_get_eng_bins_test(unittest.TestCase):
    """ tests for eng_time_get_eng_bins """

    def test_basic_energy_bins(self):
        data = [
            "some header",
            "energy 1.0 2.0 3.0",
            "1.0 0.01",
            "2.0 0.02",
            "total 3.0 0.03",
        ]
        result = mcnp_output_reader.eng_time_get_eng_bins(data)
        self.assertIn("1.0", result)
        self.assertIn("2.0", result)
        self.assertEqual(result[-1], "total")

    def test_no_energy_line(self):
        data = ["line 1", "line 2"]
        result = mcnp_output_reader.eng_time_get_eng_bins(data)
        self.assertIn("total", result)


class find_term_line_test(unittest.TestCase):
    """ tests for find_term_line """

    def test_term_line_found(self):
        lines = ["some header",
                 "      run terminated when 1000000 particle histories were done.",
                 "more data"]
        result = mcnp_output_reader.find_term_line(lines)
        self.assertEqual(result, 1)

    def test_term_line_not_found(self):
        lines = ["no term line here", "just data"]
        result = mcnp_output_reader.find_term_line(lines)
        self.assertIsNone(result)


class read_stat_tests_test(unittest.TestCase):
    """ tests for read_stat_tests """

    def test_stat_tests_no_passed_line(self):
        lines = ["some tally data", "no stat info here"]
        result = mcnp_output_reader.read_stat_tests(lines)
        self.assertEqual(result, ["no"])

    def test_stat_tests_with_passed_line(self):
        lines = [
            "some data",
            " passed  ok ok ok ok ok ok ok ok ok",
            "more data",
        ]
        result = mcnp_output_reader.read_stat_tests(lines)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


class check_fatal_test(unittest.TestCase):
    """ tests for check_fatal """

    def test_check_fatal_true(self):
        lines = ["some data", " fatal error found", "end"]
        self.assertTrue(mcnp_output_reader.check_fatal(lines))

    def test_check_fatal_false(self):
        lines = ["some data", "no issues here", "end"]
        self.assertFalse(mcnp_output_reader.check_fatal(lines))


if __name__ == '__main__':
    unittest.main()
