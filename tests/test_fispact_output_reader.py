import unittest
import os
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


class read_summary_data_test_case(unittest.TestCase):
    """ tests for the summary data """

    def test_cooling(self):
        """ tests that the data is being accurately classified as irradiated or cooling """
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
        output = fo.read_fis_out(path)

        sum_data = output.sumdat
        expected_cooling_values = [False, True, False, False, True, True, True, True, True]
        actual_cooling_values = sum_data["is_cooling"].tolist()

        self.assertEqual(expected_cooling_values, actual_cooling_values)


if __name__ == '__main__':
    unittest.main()
