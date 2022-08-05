#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import meshtal_analysis as ma
import neut_utilities as ut
import unittest

path = "test_output/cup_low_res.imsht"


class calc_mid_points_test(unittest.TestCase):

    def test_calc_mid_points(self):
        test_data_1 = [1.0, 9.0]
        test_data_2 = [0.0, 1.0]
        test_data_3 = [1.0, 1.5]
        test_data_4 = [-1.0, 1.0]
        test_data_5 = [-1.0, -1.5]
        test_data_6 = [1.0, 2.0, 3.0, 4.0]

        self.assertEqual(ma.calc_mid_points(test_data_1), [5.0])
        self.assertEqual(ma.calc_mid_points(test_data_2), [0.5])
        self.assertEqual(ma.calc_mid_points(test_data_3), [1.25])
        self.assertEqual(ma.calc_mid_points(test_data_4), [0.0])
        self.assertEqual(ma.calc_mid_points(test_data_5), [-1.25])
        self.all(assertEqual(ma.calc_mid_points(test_data_6), [1.5, 2.5, 3.5]))


class convert_to_df_test(unittest.TestCase):

    def test_count_zeros_6col(self):
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "6col_e"
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00',
                                '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00',
                                '9.00']]
        meshtally_test.data = ma.convert_to_df(meshtally_test)
        self.assertEqual(meshtally_test.data['value'].iloc[0], 0.00)
        self.assertEqual(meshtally_test.data['x'].iloc[0], 3.00)
        self.assertEqual(meshtally_test.data['y'].iloc[0], -2.00)
        self.assertEqual(meshtally_test.data['z'].iloc[0], 5.00)
        self.assertEqual(meshtally_test.data['rel_err'].iloc[0], 1.00)

    def test_count_zeros_5col(self):
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "5col"
        meshtally_test.data = [['3.00', '-2.00', '5.00', '0.00',
                                '1.00'],
                               ['5.00', '3.00', '6.00', '0.00',
                                '9.00']]
        meshtally_test.data = ma.convert_to_df(meshtally_test)
        self.assertEqual(meshtally_test.data['value'].iloc[0], 0.00)
        self.assertEqual(meshtally_test.data['x'].iloc[0], 3.00)
        self.assertEqual(meshtally_test.data['y'].iloc[0], -2.00)
        self.assertEqual(meshtally_test.data['z'].iloc[0], 5.00)
        self.assertEqual(meshtally_test.data['rel_err'].iloc[0], 1.00)


class count_zeros_test(unittest.TestCase):

    def test_count_zeros_6col(self):
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "6col_e"
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00',
                                '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00',
                                '9.00']]
        meshtally_test.data = ma.convert_to_df(meshtally_test)
        self.assertEqual(ma.count_zeros(meshtally_test), 2)

    def test_count_zeros_5col(self):
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "5col"
        meshtally_test.data = [['3.00', '-2.00', '5.00', '0.00',
                                '1.00'],
                               ['5.00', '3.00', '6.00', '0.00',
                                '9.00']]
        meshtally_test.data = ma.convert_to_df(meshtally_test)
        self.assertEqual(ma.count_zeros(meshtally_test), 2)


class read_mesh_file_tests(unittest.TestCase):

    def test_read_mesh_file(self):
        mesh = ma.read_mesh_tally_file(path)
        length = len(mesh[0].data)

        self.assertEqual(mesh[0].x_bounds[1], '-8.00')
        self.assertAlmostEqual(mesh[0].x_mids[2], -5.0)
        self.assertEqual(mesh[0].e_bounds[1], '1.00E+36')
        self.assertEqual(mesh[0].y_bounds[2], '-6.00')
        self.assertAlmostEqual(mesh[0].y_mids[3], -3.00)
        self.assertEqual(mesh[0].z_bounds[2], '2.20')
        self.assertAlmostEqual(mesh[0].z_mids[1], 1.4)
        self.assertEqual(mesh[0].ptype, 'photon')
        self.assertEqual(mesh[0].idnum, 214)
        self.assertEqual(length, 1000)

    def test_read_mesh(self):
        data = ut.get_lines(path)
        read_mesh = ma.read_mesh(214, data, {214: 4})

        self.assertEqual(read_mesh.ptype, 'photon')
        self.assertEqual(read_mesh.idnum, 214)
        self.assertEqual(read_mesh.ctype, '6col_e')

    def test_read_time_bins_mesh(self):
        timepath = "test_output/time_msht"
        data = ut.get_lines(timepath)
        read_mesh = ma.read_mesh(314, data, {314: 4})

        self.assertEqual(read_mesh.ptype, 'neutron')
        self.assertEqual(read_mesh.idnum, 314)
        self.assertEqual(read_mesh.ctype, '6col_t')
        self.assertEqual(len(read_mesh.t_bounds), 5)
        self.assertEqual(read_mesh.t_bounds[0], "-1.00E+36")


class find_mesh_tally_num_test(unittest.TestCase):

    def test_find_mesh_tally_num(self):
        data = ut.get_lines(path)

        self.assertEqual(ma.find_mesh_tally_numbers(data), {214: 4})


class add_mesh_test(unittest.TestCase):

    def test_add_mesh_error(self):
        mesh1_test = ma.meshtally()
        mesh1_test.ctype = "6col_e"
        mesh2_test = ma.meshtally()
        mesh2_test.ctype = "6col_e"

        mesh1_test.x_bounds = (-9.0, -9.1)
        mesh1_test.y_bounds = (-9.0, -9.1)
        mesh1_test.z_bounds = (1.4, 1.5)
        mesh2_test.x_bounds = (9.0, 9.1)
        mesh2_test.y_bounds = (9.0, 9.1)
        mesh2_test.z_bounds = (7.8, 7.9)

        with self.assertRaises(ValueError):
            ma.add_mesh(mesh1_test, mesh2_test)

    def test_add_mesh(self):
        mesh3_test = ma.meshtally()
        mesh3_test.ctype = "6col_e"
        mesh4_test = ma.meshtally()
        mesh4_test.ctype = "6col_e"

        mesh3_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4',
                            '7.329430e-07', '0.017765']]
        mesh4_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4',
                            '6.566330e-07', '0.018680']]
        mesh3_test.data = ma.convert_to_df(mesh3_test)
        mesh4_test.data = ma.convert_to_df(mesh4_test)

        mesh3_test.x_bounds = (-8.9, -9.1)
        mesh3_test.y_bounds = (-8.9, -9.1)
        mesh3_test.z_bounds = (1.3, 1.5)
        mesh4_test.x_bounds = (-8.9, -9.1)
        mesh4_test.y_bounds = (-8.9, -9.1)
        mesh4_test.z_bounds = (1.3, 1.5)

        new_mesh_test = ma.add_mesh(mesh3_test, mesh4_test)

        self.assertEqual(new_mesh_test.x_bounds, (-8.9, -9.1))
        self.assertEqual(new_mesh_test.y_bounds, (-8.9, -9.1))
        self.assertEqual(new_mesh_test.z_bounds, (1.3, 1.5))
        self.assertEqual(new_mesh_test.data['value'].iloc[0],
                         1.3895760275772773e-06)
        self.assertEqual(new_mesh_test.data['rel_err'].iloc[0],
                         0.025778627023100853)

    def test_add_mesh_file(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        new_mesh_test = ma.add_mesh(mesh, mesh)
        self.assertEqual(new_mesh_test.x_bounds, mesh.x_bounds)
        self.assertEqual(new_mesh_test.y_bounds, mesh.y_bounds)
        self.assertEqual(new_mesh_test.z_bounds, mesh.z_bounds)
        self.assertEqual(new_mesh_test.data['value'].iloc[0],
                         2*mesh.data['value'].iloc[0])


class find_nearest_mid_test(unittest.TestCase):

    def test_find_nearest_mid(self):
        test_val_1 = 4.6
        test_mids_1 = [4, 5]
        test_val_2 = 10
        test_mids_2 = [2, 11, 12]
        test_val_3 = 3.2
        test_mids_3 = [3.1, 3.35]
        test_val_4 = 2
        test_mids_4 = [1, 3]
        test_val_5 = -3.1
        test_mids_5 = [-3.5, -3.9]

        self.assertEqual(ma.find_nearest_mid(test_val_1, test_mids_1), 5)
        self.assertEqual(ma.find_nearest_mid(test_val_2, test_mids_2), 11)
        self.assertEqual(ma.find_nearest_mid(test_val_3, test_mids_3), 3.1)
        self.assertEqual(ma.find_nearest_mid(test_val_4, test_mids_4), 1)
        self.assertEqual(ma.find_nearest_mid(test_val_5, test_mids_5), -3.5)

    def test_find_nearest_mid_energy(self):
        test_val_1 = 7.2
        test_mids_1 = [7,11]
        self.assertEqual(ma.find_nearest_mid(test_val_1, test_mids_1), 7)


class find_point_test(unittest.TestCase):

    def test_get_point(self):
        mesh3_test = ma.meshtally()
        mesh4_test = ma.meshtally()

        mesh3_test.ctype = "6col_e"
        mesh4_test.ctype = "6col_t"

        mesh3_test.x_mids = [-9.0]
        mesh4_test.x_mids = [5.0]

        mesh3_test.y_mids = [-9.0]
        mesh4_test.y_mids = [5.0]

        mesh3_test.z_mids = [1.4]
        mesh4_test.z_mids = [3.1]

        mesh3_test.data = [['1.000E+36', '-9.0', '-9.0', '1.4',
                            '7.329430e-07', '0.017765']]
        mesh4_test.data = [['12.2', '5.0', '5.0', '3.1', '5.035e-6', '0.0014']]
        mesh3_test.data = ma.convert_to_df(mesh3_test)
        mesh4_test.data = ma.convert_to_df(mesh4_test)
        result1 = ma.pick_point(-9, -9, 1.4, mesh3_test)
        result2 = ma.pick_point(5.0,5.0,3.1, mesh4_test)
        self.assertAlmostEqual(float(result1[0]), 7.329430e-07, 7)
        self.assertAlmostEqual(float(result2[0]), 5.035e-6, 7)

    def test_get_point_file(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        result = ma.pick_point(-9, -9, 1.4, mesh).iloc[0]
        self.assertAlmostEqual(result, 7.329430e-07, 7)
        result = ma.pick_point(-8.9, -8.9, 1.4, mesh).iloc[0]
        self.assertAlmostEqual(result, 7.329430e-07, 7)
        result = ma.pick_point(-9, -9, 9.4, mesh).iloc[0]
        self.assertAlmostEqual(result, 5.54340E-07, 7)


class find_line_test(unittest.TestCase):

    def test_extract_line(self):

        mesh1_test = ma.meshtally()
        mesh1_test.ctype = "6col_e"
        mesh1_test.x_mids = [5.0]
        mesh1_test.y_mids = [5.0]
        mesh1_test.z_mids = [7.1]
        mesh1_test.data = [['5e35', '5.0', '5.0', '7.1', '5.2e-7', '0.01']]
        mesh1_test.data = ma.convert_to_df(mesh1_test)
        result = ma.extract_line(mesh1_test, ((5.0,5.0,7.1)), ((5.0,5.1,7.0)))
        self.assertAlmostEqual(float(result[0]), 5.2e-7, 7)

        mesh2_test = ma.meshtally()
        mesh2_test.ctype = "6col_t"
        mesh2_test.x_mids = [3.0]
        mesh2_test.y_mids = [7.2]
        mesh2_test.z_mids = [7.2]
        mesh2_test.data = [['5e35', '3.0', '7.2', '7.2', '4.4e-7', '0.01']]
        mesh2_test.data = ma.convert_to_df(mesh2_test)
        result = ma.extract_line(mesh2_test, ((3.0,7.2,7.2)), ((3.0,7.2,7.2)))
        self.assertAlmostEqual(float(result[0]), 4.4e-7, 7)


class upper_vals_test(unittest.TestCase):

    def test_upper_vals_file(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        mesh = ma.calculate_upper_mesh_vals(mesh)
        value = mesh.data["max_vals"].iloc[0]
        self.assertAlmostEqual(value, 6.50278e-7)


class lower_vals_test(unittest.TestCase):

    def test_lower_vals_file(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        mesh = ma.calculate_lower_mesh_vals(mesh)
        value = mesh.data["min_vals"].iloc[0]
        self.assertAlmostEqual(value, 6.2608e-7)


class err_hist_tests(unittest.TestCase):

    def test_err_hist(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        plot = ma.rel_err_hist(mesh.data)
        # x_plot, y_plot = plot.get_xydata().T
        self.assertEqual(plot.get_xlabel(), "Relative error")
        self.assertEqual(plot.get_ylabel(), "Number of voxels")


'''
class slice_tests(unittest.TestCase):

    def test_slice_plot(self):
        mesh = ma.read_mesh_tally_file(path)[0]
        plot = ma.plot_slice(mesh, 1)
        # x_plot, y_plot = plot.get_xydata().T
        self.assertEqual(plot.get_xlabel(), "X co-ord (cm)")
        self.assertEqual(plot.get_ylabel(), "Y co-ord (cm)")
'''

if __name__ == '__main__':
    unittest.main()
