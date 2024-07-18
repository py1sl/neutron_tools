import unittest
import pandas as pd
import fispact_printlib_reader


class data_frame_test_case(unittest.TestCase):
    """ test for reading the energy and particle data """

    def setUp(self):
        """ creates a sample data frame to check that the filters work """
        self.df = pd.DataFrame({
                "energy_ev": [100, 200, 300, 400, 500],
                "particle": ["neutron", "muon", "neutron", "neutron", "neutrino"]
            })

    def test_energy_filter(self):
        """ test the energy filter function """
        filtered_data = fispact_printlib_reader.energy_filter(self.df, 250)
        expected_data = pd.DataFrame({
            "energy_ev": [300, 400, 500],
            "particle": ["neutron", "neutron", "neutrino"]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(filtered_data.reset_index(drop=True), expected_data)

    def test_particle_filter(self):
        """ test particle filter function """
        filtered_data = fispact_printlib_reader.particle_filter(self.df, "neutron")
        expected_data = pd.DataFrame({
            "energy_ev": [100, 300, 400],
            "particle": ["neutron", "neutron", "neutron"]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(filtered_data.reset_index(drop=True), expected_data)


if __name__ == "main":
    unittest.main()
