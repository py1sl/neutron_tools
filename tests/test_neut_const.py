import unittest
import neut_constants as nc


class constants_test_case(unittest.TestCase):
    """ tests constants function"""

    def test_const(self):

        self.assertEqual(nc.get_e(), 1.60217662e-19)
        self.assertEqual(nc.get_p_mass(), 1.672623e-24)
        self.assertEqual(nc.get_n_mass(), 1.674929e-24)
        self.assertEqual(nc.get_e_mass(), 9.10938e-28)



class conversion_test_case(unittest.TestCase):
    """ test for conversions"""

    def test_time_conv(self):
        self.assertEqual(nc.years_to_seconds(1), 365*24*60*60)
        self.assertEqual(nc.years_to_hrs(1), 365*24)
        self.assertEqual(nc.years_to_days(1), 365)
        self.assertEqual(nc.second_to_hour(1), (1/3600))
        self.assertEqual(nc.second_to_day(1), (1/86400))
        self.assertEqual(nc.second_to_year(1), (1/3.1536e07))
        self.assertEqual(nc.hour_to_second(1), 3600)
        self.assertEqual(nc.day_to_second(1), 86400)

    def test_act_conv(self):
        self.assertEqual(nc.bq_to_curie(1), 2.703e11)
        self.assertEqual(nc.curie_to_bq(1), 3.7e-12)

    def test_dose_conv(self):
        self.assertEqual(nc.sv_to_rem(1), 100)
        self.assertEqual(nc.rem_to_Sv(100), 1)

    def test_energy_conv(self):
        self.assertEqual(nc.eV_to_joule(1), 1.602e-19)
        self.assertEqual(nc.eV_to_wavelength_photon(1), 1.24e-6)
        self.assertEqual(nc.wavelength_to_meV_neutron(1), 81.81)
        self.assertEqual(nc.joule_to_ev(1), (1/1.602e-19))


class Z_dict_test_case(unittest.TestCase):
    """ test for periodic table """

    def test_table_len(self):
        self.assertEqual((len(nc.Z_dict()), 118)
                         
    def test_last_value(self):
        z = nc.Z_dict()
        self.assertEqual(max(z.values()), 118)

if __name__ == '__main__':
    unittest.main()
