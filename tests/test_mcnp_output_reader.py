import unittest
from unittest.mock import patch, mock_open
import logging
import mcnp_output_reader
import neut_utilities as ut


class version_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_is_version(self):
        """ """
        list_a = ["          Code Name & Version = MCNP6, 1.0",
                  "  "]
        self.assertEqual(mcnp_output_reader.read_version(list_a), "MCNP6, 1.0")

    def test_is_version_none_given_other_list(self):
        """ test for version """
        list_a = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                  "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                  "ccccccccccccccccccccccccccccccccccccccccccccccccc",
                  "ddddddddddddddddddddddddddddddddddddddddddddddddd"]
        list_b = ["a", "b", "c", "d"]
        self.assertEqual(mcnp_output_reader.read_version(list_a), None)
        self.assertEqual(mcnp_output_reader.read_version(list_b), None)

    def test_is_version_none_given_string(self):
        """ test for version with string"""
        string_a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertEqual(mcnp_output_reader.read_version(string_a), None)


class get_tally_nums_test_case(unittest.TestCase):
    """ test for get talyl num """

    def test_get_tally_num(self):
        # test with a set of differnt tally types
        data = ut.get_lines("test_output/singles.io")
        tnums = mcnp_output_reader.get_tally_nums(data)
        self.assertEqual(len(tnums), 6)
        self.assertIn("1", tnums)
        self.assertIn("2", tnums)
        self.assertIn("4", tnums)
        self.assertIn("5", tnums)
        self.assertIn("6", tnums)
        self.assertIn("8", tnums)


class rendevous_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_count_rendevous_tests(self):

        # test with a single core job count should be 0
        data = ut.get_lines("test_output/singles.io")
        count = mcnp_output_reader.count_rendevous(data)
        self.assertEqual(count, 0)

        # need to add test for multicore job

    def test_index_rendevous_tests(self):

        # test with a single core job should be 0
        data = ut.get_lines("test_output/singles.io")
        index = mcnp_output_reader.get_rendevous_index(data)
        self.assertEqual(index, [])

        # need to add test for multicore job


class stat_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_read_stat_tests(self):
        self.assertTrue(True)
        # need to add test for tally with all 0.0 bins


class tally_type1_tests(unittest.TestCase):
    """ tests for type 1 tally """

    def test_single_value_t1_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 1.16486E+00)
                self.assertEqual(tn.err[0], 0.0006)

    def test_ebined_t1_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 1:
                self.assertEqual(tn.type, '1')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 2.92000E-02)


class tally_type2_tests(unittest.TestCase):
    """ tests for type 2 tally """

    def test_single_value_t2_tally(self):
        path = "test_output/singles.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 4.31795E-03)
                self.assertEqual(tn.err[0], 0.0015)

    def test_ebined_t2_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 1.92767E-04)

    def test_etbinned_t2_tally(self):
        path = "test_output/singles_et.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 2:
                self.assertEqual(tn.type, '2')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 15)
                self.assertEqual(tn.eng[-1], "total")
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 15)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.ang_bins, None)
                self.assertEqual(tn.result.shape, tn.err.shape)
                self.assertEqual(tn.result.shape, (15, 15))


class tally_type4_tests(unittest.TestCase):
    """ tests for type 4 tally """

    def test_single_value_t4_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(tn.result[0], 1.91076E-03)
                self.assertEqual(tn.err[0], 0.0006)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['3.66519E+03'])

    def test_ebined_t4_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result[0]), 14)
                self.assertEqual(len(tn.err[0]), 14)
                self.assertEqual(tn.result[0][0], 1.20226E-04)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['3.66519E+03'])

    def test_etbinned_t4_tally(self):
        path = "test_output/singles_et.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 4:
                self.assertEqual(tn.type, '4')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 15)
                self.assertEqual(tn.eng[-1], "total")
                self.assertNotEqual(tn.times, None)
                self.assertEqual(len(tn.times), 15)
                self.assertEqual(tn.times[-1], "total")
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(tn.result.shape, tn.err.shape)
                self.assertEqual(tn.result.shape, (15, 15))


class tally_type5_tests(unittest.TestCase):
    """ tests for type 5 tally """

    def test_single_value_t5_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 3.42950E-04)
                self.assertEqual(tn.err[0], 0.0025)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.x, 15.0)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)
                self.assertEqual(tn.largest_score, 2.32897E-01)
                self.assertEqual(tn.largest_score_nps, 492485)
                self.assertEqual(tn.average_per_history, 3.42950E-04)
                self.assertEqual(tn.misses["russian roulette on pd"], 0)
                self.assertEqual(tn.misses["psc=0"], 0)
                self.assertEqual(tn.misses["russian roulette in transmission"], 935317)
                self.assertEqual(tn.misses["underflow in transmission"], 39376)
                self.assertEqual(tn.misses["hit a zero-importance cell"], 0)
                self.assertEqual(tn.misses["energy cutoff"], 0)
                

    def test_ebined_t5_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 5:
                self.assertEqual(tn.type, '5')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0], 1.20831E-05)
                self.assertEqual(tn.x, 15)
                self.assertEqual(tn.y, 0.00)
                self.assertEqual(tn.z, 0.00)


class tally_type6_tests(unittest.TestCase):
    """ tests for type 6 tally """

    def test_single_value_t6_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 4.30567E-05)
                self.assertEqual(tn.err[0], 0.0002)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['9.89602E+03'])

    def test_ebined_t6_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 6:
                self.assertEqual(tn.type, '6')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result[0]), 14)
                self.assertEqual(len(tn.err[0]), 14)
                self.assertEqual(tn.result[0][0], 5.60997E-07)
                self.assertEqual(tn.cells, ['2'])
                self.assertEqual(tn.vols, ['9.89602E+03'])


class tally_type8_tests(unittest.TestCase):
    """ tests for type 8 tally """

    def test_single_value_t8_tally(self):
        single = mcnp_output_reader.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertEqual(tn.eng, None)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 1)
                self.assertEqual(len(tn.err), 1)
                self.assertEqual(tn.result[0], 1.00000E+00)
                self.assertEqual(tn.err[0], 0.00)

    def test_ebined_t8_tally(self):
        path = "test_output/singles_erg.io"
        single = mcnp_output_reader.read_output_file(path)
        for tn in single.tally_data:
            if tn.number == 8:
                self.assertEqual(tn.type, '8')
                self.assertEqual(tn.particle, "photons")
                self.assertEqual(tn.nps, 1000000)
                self.assertNotEqual(tn.eng, None)
                self.assertEqual(len(tn.eng), 14)
                self.assertEqual(tn.times, None)
                self.assertEqual(tn.user_bins, None)
                self.assertEqual(len(tn.result), 14)
                self.assertEqual(len(tn.err), 14)
                self.assertEqual(tn.result[0],  5.16461E-01)


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        logger = logging.getLogger()
        logger.level = logging.DEBUG
        with patch("neut_utilities.open", open_mock, create=True):
            mcnp_output_reader.print_tally_lines_to_file(["hello", "world"],
                                                          "output", 1)

        open_mock.assert_called_with("output1.txt", "w")
        open_mock.return_value.write.assert_any_call("hello\n")


if __name__ == '__main__':
    unittest.main()
