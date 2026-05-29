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
        self.assertIsInstance(lines, list)
        self.assertGreater(len(lines), 0)


    def test_read_fispact_files_file_logs_file_read(self):
        logger_name = ut.get_ntlogger().name
        with self.assertLogs(logger_name, level="INFO") as cm:
            ffr.read_fispact_files_file(str(self.example_files_file))

        log_output = "\n".join(cm.output)
        self.assertIn(f"reading FISPACT files file {self.example_files_file}", log_output)
        self.assertIn(f"loaded 12 lines from FISPACT files file {self.example_files_file}", log_output)

    def test_output_files_file_logs_file_write(self):
        parsed = ffr.process_files_file(ffr.read_fispact_files_file(str(self.example_files_file)))
        logger_name = ut.get_ntlogger().name
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "written_files_file"
            with self.assertLogs(logger_name, level="INFO") as cm:
                parsed.output_files_file(str(output_path))

            log_output = "\n".join(cm.output)
            self.assertIn(f"wrote FISPACT files file to {output_path}", log_output)
            self.assertTrue(output_path.exists())

    def test_process_example_files_file_to_files_file_object(self):
        lines = ffr.read_fispact_files_file(str(self.example_files_file))
        parsed = ffr.process_files_file(lines)

        self.assertIsInstance(parsed, ffr.files_file)
        self.assertEqual(parsed.lines, lines)
        self.assertEqual(parsed.parameters["absorp"], "/work/fispact_nd/ENDFdata/decay/abs_2012")
        self.assertEqual(parsed.parameters["fluxes"], "fluxes")
        self.assertEqual(parsed.parameters["arrayx"], "ARRAYX")
