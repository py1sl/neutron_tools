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
        self.assertEqual(ma.calc_mid_points(test_data_6), [1.5, 2.5, 3.5])


class count_zeros_test(unittest.TestCase):

    def test_count_zeros(self):
        meshtally_test = ma.meshtally()
        meshtally_test.ctype = "6col"
        meshtally_test.data = [['1.00', '3.00', '-2.00', '5.00', '0.00',
                                '1.00'],
                               ['1.00', '5.00', '3.00', '6.00', '0.00',
                                '9.00']]
        meshtally_test.data = ma.convert_to_df(meshtally_test)
        self.assertEqual(ma.count_zeros(meshtally_test), 2)
        # looks for zeros in 5th column as thats the 'results'


class read_mesh_file_tests(unittest.TestCase):

    def test_read_mesh_file(self):
        mesh = ma.read_mesh_tally_file(path)
        length = len(mesh[0].data)

        self.assertEqual(mesh[0].x_bounds[1], '-8.00')
        self.assertEqual(mesh[0].x_mids[2], -5.0)
        self.assertEqual(mesh[0].e_bounds[1], '1.00E+36')
        self.assertEqual(mesh[0].y_bounds[2], '-6.00')
        self.assertEqual(mesh[0].y_mids[3], -3.00)
        self.assertEqual(mesh[0].z_bounds[2], '2.20')
        self.assertEqual(mesh[0].z_mids[1], 1.4)
        self.assertEqual(mesh[0].ptype, 'photon')
        self.assertEqual(mesh[0].idnum, 214)
        self.assertEqual(length, 1000)

    def test_read_mesh(self):
        data = ut.get_lines(path)
        read_mesh = ma.read_mesh(214, data, {214: 4})

        self.assertEqual(read_mesh.ptype, 'photon')
        self.assertEqual(read_mesh.idnum, 214)
        self.assertEqual(read_mesh.ctype, '6col')


class find_mesh_tally_num_test(unittest.TestCase):

    def test_find_mesh_tally_num(self):
        data = ut.get_lines(path)

        self.assertEqual(ma.find_mesh_tally_numbers(data), {214: 4})


class add_mesh_test(unittest.TestCase):

    def test_add_mesh_error(self):
        mesh1_test = ma.meshtally()
        mesh1_test.ctype = "6col"
        mesh2_test = ma.meshtally()
        mesh2_test.ctype = "6col"

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
        mesh3_test.ctype = "6col"
        mesh4_test = ma.meshtally()
        mesh4_test.ctype = "6col"

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
        self.assertEqual(new_mesh_test.data['value'].item(),
                         1.3895760275772773e-06)
        self.assertEqual(new_mesh_test.data['rel_err'].item(),
                         0.025778627023100853)


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


if __name__ == '__main__':
    unittest.main()
