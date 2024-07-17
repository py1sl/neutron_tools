import unittest
import os
# from unittest.mock import patch, mock_open
import mcnp_ptrac_reader as mpr
import neut_utilities as ut


class header_test_case(unittest.TestCase):
    """ tests header function"""

    def test_header_lines(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        lines = ut.get_lines(path)
        head, lines = mpr.remove_header(lines)
        self.assertEqual(len(head), 9)


class event_test_case(unittest.TestCase):
    """ tests events functions"""

    def test_process_event(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        hists = mpr.read_ptrac(path)
        self.assertEqual(len(hists[0].events), 12)
        self.assertEqual(len(hists[-1].events), 12)
        self.assertEqual(len(hists[-2].events), 9)
        self.assertEqual(hists[0].events[0].type, 3000)
        self.assertEqual(hists[0].events[-1].type, 9000)
        self.assertEqual(hists[0].events[0].x, 0)
        self.assertEqual(hists[0].events[0].y, 0)
        self.assertEqual(hists[0].events[0].z, 0)
        self.assertEqual(hists[0].events[0].u, 0.50848)
        self.assertEqual(hists[0].events[0].v, 0.47328)
        self.assertEqual(hists[0].events[0].w, 0.71935)
        self.assertEqual(hists[0].events[0].wgt, 1)
        self.assertEqual(hists[0].events[0].energy, 1.332)

    def test_events_eq(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        hists = mpr.read_ptrac(path)
        self.assertTrue(hists[0].events[0] == hists[0].events[0])
        self.assertEqual(hists[0].events[0], hists[0].events[0])
        self.assertTrue(hists[0].events[0] != hists[0].events[1])
        self.assertFalse(hists[0].events[0] == hists[0].events[1])


class history_test_case(unittest.TestCase):
    """ tests history functions"""

    def test_mean_num_events(self):
        h1 = mpr.history()
        h2 = mpr.history()
        h1.events.append(1)
        h1.events.append(1)
        h1.events.append(1)
        h2.events.append(1)
        self.assertEqual(mpr.mean_num_events([h1, h2]), 2)


class tracks_test_case(unittest.TestCase):
    """ tests history functions"""

    def test_process_tracks(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        hists = mpr.read_ptrac(path)
        self.assertEqual(hists[0].nps, 1)
        self.assertEqual(hists[-1].nps, 20)


class read_ptrac_test_case(unittest.TestCase):
    """ tests read ptrac functions"""

    def test_read_asc_ptrac_from_file(self):
        path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        hist = mpr.read_ptrac(path)
        self.assertEqual(len(hist), 20)


if __name__ == '__main__':
    unittest.main()
