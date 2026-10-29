import unittest
import os
import tempfile
from neutron_tools.mcnp import ofile_reduce


class ofile_test_case(unittest.TestCase):
    """ tests ofile reduce function"""

    def test_output(self):
        input_lines = [
            "initial output",
            "      run terminated when first run",
            "final rendezvous data",
            "trailing output",
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            infile = os.path.join(tmpdir, "input.io")
            outfile = os.path.join(tmpdir, "reduced.io")
            with open(infile, "w") as file:
                file.write("\n".join(input_lines))

            ofile_reduce.reduce_ofile(infile, outfile)

            with open(outfile) as file:
                self.assertEqual(file.read().splitlines(), input_lines[1:])

    def test_missing_termination_line_exits(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            infile = os.path.join(tmpdir, "input.io")
            outfile = os.path.join(tmpdir, "reduced.io")
            with open(infile, "w") as file:
                file.write("output without a termination line\n")

            with self.assertRaises(SystemExit):
                ofile_reduce.reduce_ofile(infile, outfile)

            self.assertFalse(os.path.exists(outfile))


if __name__ == '__main__':
    unittest.main()
