from neutron_tools.fispact import fispact_files_file_reader as ffr
from neutron_tools.utilities import neut_utilities as ut
from pathlib import Path
import tempfile
import unittest


class read_fispact_files_file_test_case(unittest.TestCase):
    """ tests for reading a fispact files file """

    @classmethod
    def setUpClass(cls):
        cls.example_files_file = Path(__file__).parent / "test_output" / "example_files_file"

    def test_read_fispact_files_file(self):
        with self.assertRaises(FileNotFoundError):
            ffr.read_fispact_files_file("non_existent_file.txt")

        with self.assertRaises(ValueError):
            ffr.read_fispact_files_file(".")

        lines = ffr.read_fispact_files_file(str(self.example_files_file))
        self.assertIsInstance(lines, ffr.files_file)




    def test_process_example_files_file_to_files_file_object(self):
        parsed = ffr.read_fispact_files_file(str(self.example_files_file))

        self.assertIsInstance(parsed, ffr.files_file)
        self.assertEqual(parsed.parameters["absorp"], "/work/fispact_nd/ENDFdata/decay/abs_2012")
        self.assertEqual(parsed.parameters["fluxes"], "fluxes")
        self.assertEqual(parsed.parameters["arrayx"], "ARRAYX")
