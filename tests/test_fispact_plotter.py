import os
import sys
import unittest
import matplotlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import fispact_analysis as fa
import fispact_output_reader as fisor


file = path = os.path.join(os.path.dirname(__file__), 'test_output', 'fis_test1.out')
output = fisor.read_fis_out(file)


fa.create_nuc_chart_gif(output, fname = "test.gif")