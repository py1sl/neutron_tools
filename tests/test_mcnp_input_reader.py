import unittest
import mcnp_input_reader

# declaring file paths. If tests return error check files/paths are unchanged.
fname = (r"test_output/singles_erg.i")
ferror = (r"test_output/error_singles_erg.i")
surface_file = (r"test_output/singles_t.i")


class cell_card_tests(unittest.TestCase):
    # test for reading the cells part of input file

    def test_1_line_mat_cells(self):
        # for mcnp input reader tests
        # test simple 1 line cell with material
        bloc = ["1 2 -2.3 (-1) imp:n=2"]
        cell = mcnp_input_reader.process_cell_block(bloc)[0]

        self.assertEqual(cell.number, 1)
        self.assertEqual(cell.mat, 2)
        self.assertEqual(cell.density, -2.3)
        self.assertEqual(cell.imp_n, 2)
        self.assertEqual(len(cell.surfaces), 1)
        self.assertEqual(cell.surfaces, [1])

    def test_1_line_void_cell(self):
        # test simple 1 line void cell
        bloc = ["1 0 (-1:23) (3 4 -5) imp:n=2"]
        cell = mcnp_input_reader.process_cell_block(bloc)[0]

        self.assertEqual(cell.number, 1)
        self.assertEqual(cell.imp_n, 2)
        self.assertEqual(len(cell.surfaces), 5)
        self.assertEqual(cell.surfaces[0], 1)
        self.assertEqual(cell.surfaces[1], 23)
        self.assertEqual(cell.mat, 0)
        self.assertIsNone(cell.density)

    """
    def test_multiline_mat_cell(self):
        # test multiple line cell
        self.assertEqual(cell.num, 1)
        self.assertEqual(cell.mat, 2)
        self.assertEqual(cell.density, -2.3)
        self.assertEqual(cell.imp_n, 1.0)
    """


class surface_card_tests(unittest.TestCase):
    """ test for reading the surfaces part of input file"""
    # tests the surface number of inputs
    # ferror is file with bad inputs for surface types
    def test_check_surfaces(self):
        df_error = mcnp_input_reader.surface_reader(ferror)
        df = mcnp_input_reader.surface_reader(fname)
        bad_result = mcnp_input_reader.check_surfaces(df_error)
        self.assertFalse(bad_result)
        good_result = mcnp_input_reader.check_surfaces(df)
        self.assertTrue(good_result)

    def test_surface_reader(self):
        """ tests that outputs from dataframe are correct type"""
        df = mcnp_input_reader.surface_reader(fname)
        Type = df.loc[:, 'Type']
        Num = df.loc[:, 'Num']
        Params = df.loc[:, 'Parameters']
        Transform = df.loc[:, 'Transform']
        Comments = df.loc[:, 'Comments']

        for i in Num:
            x = float(i)
            self.assertEqual(type(x), float)
        for i in Type:
            self.assertEqual(type(i), str)
        for i in (Params):
            self.assertEqual(type(i), list)
        for i in Transform:
            # just returns true if i is '--'
            if i == '--':
                self.assertEqual(i, '--')
            else:
                x = float(i)
                self.assertEqual(type(x), float)
        for i in Comments:
            if i == '--':
                self.assertEqual(i, '--')
            else:
                self.assertEqual(type(i), str)

    def test_unused_surfaces(self):
        unused = mcnp_input_reader.unused_surfaces(fname)
        self.assertFalse(unused)
        all_used = mcnp_input_reader.unused_surfaces(surface_file)
        self.assertTrue(all_used)


class data_card_tests(unittest.TestCase):
    """ test for reading the data part of input file"""

    def test_get_mat_nums(self):
        """ """
        test_list = ["M1",
                     "m10",
                     "m ",
                     "m",
                     "a "]
        mnums = mcnp_input_reader.get_material_numbers(test_list)
        self.assertEqual(mnums[0], 1)    # test for lower case m
        self.assertEqual(mnums[1], 10)   # test for upper case m
        self.assertEqual(len(mnums), 2)  # check nothing else added

    def test_get_tal_nums(self):
        """ """
        test_list = ["f1",
                     "F10",
                     "f ",
                     "f",
                     "a "]
        tnums = mcnp_input_reader.get_tally_numbers(test_list)
        self.assertEqual(tnums[0], 1)    # test for lower case f
        self.assertEqual(tnums[1], 10)   # test for upper case f
        self.assertEqual(len(tnums), 2)  # check nothing else added

    def test_get_mode(self):
        """ """
        mode = mcnp_input_reader.read_mode_card(["Mode n"])
        self.assertEqual(mode, ["n"])   # test for mixed case mode
        self.assertEqual(len(mode), 1)  # check nothing else added

        mode = mcnp_input_reader.read_mode_card(["mode p"])
        self.assertEqual(mode, ["p"])   # test for lower case mode
        self.assertEqual(len(mode), 1)  # check nothing else added

        mode = mcnp_input_reader.read_mode_card(["MODE n p", "m34 32000"])
        self.assertEqual(mode, ["n", "p"])  # test for upper case mode
        self.assertEqual(len(mode), 2)  # check multipe particles else added

        mode = mcnp_input_reader.read_mode_card(["m23 1001.21c 1",
                                                 "m34 32000"])
        self.assertIsNone(mode)  # test other lines starting with m

    def test_mode_valid(self):
        """ """
        check = mcnp_input_reader.check_mode_valid(["p", "n"])
        self.assertTrue(check)  # check lower case

        check = mcnp_input_reader.check_mode_valid(["n", "P"])
        self.assertTrue(check)  # check upper case and order

        check = mcnp_input_reader.check_mode_valid(["p", "n", "r"])
        self.assertFalse(check)  # check false


class misc_tests(unittest.TestCase):
    """ test for reading the misc part of input file"""

    def test_full_line_comment(self):
        """ """
        test_list = ["c cell cards",
                     "C surface ecards",
                     "c234",
                     "comment",
                     "c"]
        comments = mcnp_input_reader.get_full_line_comments(test_list)
        self.assertEqual(comments.get(1), test_list[0])  # test lower case c
        self.assertEqual(comments.get(2), test_list[1])  # test upper case c
        self.assertEqual(len(comments), 2)  # check nothing else added

    def test_long_line(self):
        """ """
        test_list = ["c cell cards",
                     "C surface ecards",
                     "c234",
                     "comment " + 90 * "f",
                     "c"]
        ll_index = mcnp_input_reader.long_line_index(test_list)
        self.assertEqual(len(ll_index), 1)  # test found a single long line
        self.assertEqual(ll_index, [3])     # check it found the right index

        test_list = ["c cell cards",
                     "C surface ecards",
                     "c234"]
        ll_index = mcnp_input_reader.long_line_index(test_list)
        self.assertEqual(ll_index, None)     # if no long lines, return none

    def test_tab_finder(self):
        """ """
        test_list = ["cell\t",
                     "\tSurface",
                     "c\t234",
                     "com\tme\nnt" + 9 * "f",
                     "c",
                     "\t"]
        tab_index = mcnp_input_reader.tab_finder(test_list)
        self.assertEqual(tab_index, [1, 2, 3, 4, 6])

    def test_tab_replacer(self):
        """ """
        test_list = ["cell\t",
                     "\tSurface",
                     "c\t234",
                     "com\tme\tnt" + 9 * "f",
                     "c",
                     "\t."]
        correct_list = ["cell     ",
                        "     Surface",
                        "c     234",
                        "com     me     nt" + 9 * "f",
                        "c",
                        "     ."]
        tab_replaced = mcnp_input_reader.tab_to_whitespace(test_list)
        self.assertEqual(tab_replaced, correct_list)


if __name__ == '__main__':
    unittest.main()
