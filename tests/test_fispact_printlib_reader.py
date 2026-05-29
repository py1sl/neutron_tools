import unittest
import pandas as pd
from neutron_tools.fispact import fispact_printlib_reader


class data_frame_test_case(unittest.TestCase):
    """ test for reading the energy and particle data """

    def setUp(self):
        """ creates a sample data frame to check that the filters work """
        self.df = pd.DataFrame({
                "energy_ev": [100, 200, 300, 400, 500],
                "particle": ["neutron", "muon", "neutron", "neutron", "neutrino"]
            })


    def test_read_fispact_printlib_logs_file_read(self):
        logger_name = ut.get_ntlogger().name
        with self.assertLogs(logger_name, level="INFO") as cm:
            read_fispact_printlib(str(self.example_printlib))

        log_output = "\n".join(cm.output)
        self.assertIn(f"reading FISPACT printlib file {self.example_printlib}", log_output)
        self.assertIn(f"loaded 3 discrete emission lines from FISPACT printlib file {self.example_printlib}", log_output)

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
