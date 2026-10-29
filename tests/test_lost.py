import unittest
import os
import tempfile
from unittest.mock import patch
from neutron_tools.mcnp import lost_points


def lost_point_line(x, y, z):
    return f"{'x,y,z coordinates:':<28}{x:>12}   {y:>12}   {z:>12}"


class lost_points_test_case(unittest.TestCase):
    def test_outputs_all_lost_points(self):
        lines = [
            "unrelated output",
            lost_point_line("-1.25", "2.5", "300"),
            lost_point_line("4", "-5.75", "6"),
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            infile = os.path.join(tmpdir, "output")
            with open(infile, "w") as file:
                file.write("\n".join(lines))

            with patch.object(lost_points.o_ut, "output_points") as output_points:
                count = lost_points.output_lost_points(infile, "custom.lost")

        self.assertEqual(count, 2)
        output_points.assert_called_once_with(
            [-1.25, 4.0], [2.5, -5.75], [300.0, 6.0], outpath="custom.lost"
        )

    def test_no_lost_points_does_not_write_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            infile = os.path.join(tmpdir, "output")
            with open(infile, "w") as file:
                file.write("ordinary output\n")

            with patch.object(lost_points.o_ut, "output_points") as output_points:
                with patch("builtins.print") as print_mock:
                    count = lost_points.output_lost_points(infile)

        self.assertEqual(count, 0)
        output_points.assert_not_called()
        print_mock.assert_called_once_with("No lost points found")


if __name__ == '__main__':
    unittest.main()
