import unittest
import mcnp_input_reader


class cell_card_tests(unittest.TestCase):
    # test for reading the cells part of input file

    def test_1_line_mat_cells(self):
        # for mcnp input reader tests
        # test simple 1 line cell with material
        bloc = ["1 2 -2.3 (-1) imp:n=2"]
        cell = mcnp_input_reader.process_cell_block(bloc)[1]

        self.assertEqual(cell.number, 1)
        self.assertEqual(cell.mat, 2)
        self.assertEqual(cell.density, -2.3)
        self.assertEqual(cell.imp['n'], 2)
        self.assertEqual(len(cell.surfaces), 1)
        self.assertEqual(cell.surfaces, [1])

    def test_1_line_void_cell(self):
        # test simple 1 line void cell
        bloc = ["1 0 (-1:23) (3 4 -5) imp:n=2"]
        cell = mcnp_input_reader.process_cell_block(bloc)[1]
        self.assertEqual(cell.number, 1)
        self.assertEqual(cell.imp['n'], 2)
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


class input_validation_tests(unittest.TestCase):
    """ test for some of the card validation tests """
    def test_check_mat_num(self):
        self.assertTrue(mcnp_input_reader.is_valid_mat_num(1))
        self.assertFalse(mcnp_input_reader.is_valid_mat_num(1e10))

    def test_check_surf_num(self):
        self.assertTrue(mcnp_input_reader.is_valid_surf_num(1))
        self.assertFalse(mcnp_input_reader.is_valid_surf_num(1e10))

    def test_check_cell_num(self):
        self.assertTrue(mcnp_input_reader.is_valid_cell_num(1))
        self.assertFalse(mcnp_input_reader.is_valid_cell_num(10000000000))

    def test_mode_valid(self):
        """ """
        check = mcnp_input_reader.is_mode_valid(["p", "n"])
        self.assertTrue(check)  # check lower case

        check = mcnp_input_reader.is_mode_valid(["n", "P"])
        self.assertTrue(check)  # check upper case and order

        check = mcnp_input_reader.is_mode_valid(["p", "n", "r"])
        self.assertFalse(check)  # check false


class filter_tests(unittest.TestCase):
    """ tests for retrieving certain data objects """

    def test_get_cell(self):

        # check empty list
        self.assertEqual(mcnp_input_reader.get_cell(1, {}), None)

        # check working
        cell_1 = mcnp_input_reader.mcnp_cell()
        cell_1.number = 1
        cell_2 = mcnp_input_reader.mcnp_cell()
        cell_2.number = 2
        cells = {}
        cells[cell_1.number] = cell_1
        cells[cell_2.number] = cell_2
        final_cell = mcnp_input_reader.get_cell(1, cells)
        self.assertEqual(final_cell, cell_1)

        # check cell number not present
        final_cell = mcnp_input_reader.get_cell(10, cells)
        self.assertEqual(final_cell, None)

    def test_get_cells_with_mat(self):
        # check empty list
        self.assertEqual(mcnp_input_reader.cells_with_mat(1, {}), [])

        # set up test_list
        cell_1 = mcnp_input_reader.mcnp_cell()
        cell_1.number = 1
        cell_1.mat = 1
        cell_2 = mcnp_input_reader.mcnp_cell()
        cell_2.number = 2
        cell_2.mat = 1
        cell_3 = mcnp_input_reader.mcnp_cell()
        cell_3.number = 3
        cell_3.mat = 2

        cells = {}
        cells[cell_1.number] = cell_1
        cells[cell_2.number] = cell_2
        cells[cell_3.number] = cell_3
        # check working
        self.assertEqual(len(mcnp_input_reader.cells_with_mat(1, cells)), 2)
        self.assertEqual(len(mcnp_input_reader.cells_with_mat(2, cells)), 1)

        # check mat num not present
        self.assertEqual(mcnp_input_reader.cells_with_mat(10, cells), [])

    def test_get_cells_with_surf(self):
        # check empty list
        self.assertEqual(mcnp_input_reader.cells_with_mat(1, {}), [])

        # set up test_list
        cell_1 = mcnp_input_reader.mcnp_cell()
        cell_1.number = 1
        cell_1.surfaces = [1, 2, 3]
        cell_2 = mcnp_input_reader.mcnp_cell()
        cell_2.number = 2
        cell_2.surfaces = [1, 4, 5]
        cell_3 = mcnp_input_reader.mcnp_cell()
        cell_3.number = 3
        cell_3.surfaces = [2]

        cells = {}
        cells[cell_1.number] = cell_1
        cells[cell_2.number] = cell_2
        cells[cell_3.number] = cell_3
        # check working
        self.assertEqual(len(mcnp_input_reader.cells_with_surface(1, cells)), 2)
        self.assertEqual(len(mcnp_input_reader.cells_with_surface(3, cells)), 1)
        self.assertEqual(len(mcnp_input_reader.cells_with_surface(2, cells)), 2)       # check mat num not present
        self.assertEqual(mcnp_input_reader.cells_with_surface(10, cells), [])

    def test_cell_exists(self):
        # check working
        cell_1 = mcnp_input_reader.mcnp_cell()
        cell_1.number = 1
        cell_2 = mcnp_input_reader.mcnp_cell()
        cell_2.number = 2
        cells = {}
        cells[cell_1.number] = cell_1
        cells[cell_2.number] = cell_2
        self.assertTrue(mcnp_input_reader.check_cell_exists(1, cells))
        self.assertFalse(mcnp_input_reader.check_cell_exists(10, cells))


class surface_card_tests(unittest.TestCase):
    """ test for reading the surfaces part of input file"""

    # test simple surface card
    def test_single_line_surface(self):
        self.assertTrue(True)

    # test multi line surface card
    def test_multi_line_surface(self):
        self.assertTrue(True)

    def test_is_surface(self):
        # test check surface type validity
        # check surfaces
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("px"))
        # check for possible escape characters
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("c/x"))
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("c/y"))
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("c/z"))
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("k/z"))
        # check macro body
        self.assertTrue(mcnp_input_reader.is_surface_type_valid("rpp"))
        # check not a surface
        self.assertFalse(mcnp_input_reader.is_surface_type_valid("nas"))

    def test_plane_valid(self):
        # test plane validity
        self.assertTrue(True)
        self.assertFalse(False)

    def test_sphere_valid(self):
        # test sphere validity
        self.assertTrue(True)
        self.assertFalse(False)

    def test_cyl_valid(self):
        # test cylinder validity
        self.assertTrue(True)
        self.assertFalse(False)

    def test_cone_valid(self):
        # test cone validity
        self.assertTrue(True)
        self.assertFalse(False)

    def test_gq_valid(self):
        # test general quadratic validity
        self.assertTrue(True)
        self.assertFalse(False)


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

    def test_read_material(self):
        lines = ["m1 $ a material", "      1000.21c 1",
                 "m2 $ next mat", "      1001.21c 1"]

        mat = mcnp_input_reader.read_material_lines(1, lines)
        self.assertEqual(mat.number, 1)
        self.assertEqual(mat.keywords, None)
        self.assertEqual(mat.composition["1000.21c"], 1)
    
    def test_mat_keyword(self):
        mat = mcnp_input_reader.mcnp_material()
        test_line = "plib=.70u"

        # test no previous keywords
        mat = mcnp_input_reader.process_material_keyword(test_line, mat)
        self.assertEqual(mat.keywords["plib"], ".70u")

        # test with previous keywords
        mat = mcnp_input_reader.mcnp_material()
        mat.keywords = {"test_key": "test_value"}
        mat = mcnp_input_reader.process_material_keyword(test_line, mat)
        self.assertEqual(mat.keywords["plib"], ".70u")
        self.assertEqual(mat.keywords["test_key"], "test_value")
    
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


class line_tests(unittest.TestCase):
    """ test for reading the misc part of input file"""

    def test_inline_comments(self):
        """ """
        # test not inline comment
        test_line = "no comment"
        line = mcnp_input_reader.remove_inline_comment(test_line)
        self.assertEqual(line, test_line)

        # test inline comment
        test_line = " 1 1 $ test"
        line = mcnp_input_reader.remove_inline_comment(test_line)
        self.assertEqual(line, " 1 1 ")

    def test_full_line_comment(self):
        """ """
        test_list = ["c cell cards",
                     "C surface ecards",
                     "c234",
                     "comment",
                     "c"]
        comments = mcnp_input_reader.get_full_line_comments(test_list)
        self.assertEqual(comments[0], test_list[0])  # test for lower case c
        self.assertEqual(comments[1], test_list[1])  # test for upper case c
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

        test_list = ["c cell cards",
                     "C surface" + 90 * "f",
                     "c234"]
        ll_index = mcnp_input_reader.long_line_index(test_list)
        self.assertEqual(ll_index, None)     # test checking long comment lines, return none

        test_list = ["c cell cards",
                     "       $ surface" + 100 * "f",
                     "c234"]
        ll_index = mcnp_input_reader.long_line_index(test_list)
        self.assertEqual(ll_index, None)     # test checking long inline comment, return none


if __name__ == '__main__':
    unittest.main()
