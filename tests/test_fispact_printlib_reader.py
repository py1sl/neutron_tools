import unittest
import tempfile
import os
import pandas as pd
from neutron_tools.fispact import fispact_printlib_reader
from neutron_tools.utilities import neut_utilities as ut


class data_frame_test_case(unittest.TestCase):
    """ test for reading the energy and particle data """

    def setUp(self):
        """ creates a sample data frame to check that the filters work """
        self.df = pd.DataFrame({
                "energy_ev": [100, 200, 300, 400, 500],
                "particle": ["neutron", "muon", "neutron", "neutron", "neutrino"]
            })

    @staticmethod
    def _sample_printlib_contents():
        def emission_line(nuclide, particle, energy, intensity):
            return f"  {nuclide:<6}{'':17}{particle:<9}{'':9}{energy:11.3f}{'':17}{intensity:11.3f}\n"

        return (
            "header\n"
            " FD \n"
            + emission_line("V52", "neutron", 1.0, 0.1)
            + emission_line("Sc43", "gamma", 2.0, 0.2)
            + emission_line("Co60", "beta", 3.0, 0.3)
            + "fispact run time\n"
        )

    def test_read_fispact_printlib_logs_file_read(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as tmp_file:
            tmp_file.write(self._sample_printlib_contents())
            self.example_printlib = tmp_file.name

        logger_name = ut.get_ntlogger().name
        try:
            with self.assertLogs(logger_name, level="INFO") as cm:
                fispact_printlib_reader.read_fispact_printlib(str(self.example_printlib))
        finally:
            os.remove(self.example_printlib)

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
