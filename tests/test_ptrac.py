import unittest
from unittest.mock import patch, mock_open
import mcnp_ptrac_reader as mpr


class header_test_case(unittest.TestCase):
    """ tests header function"""
    def test_header_lines(self):
        self.assertEqual(1, 1)


class event_test_case(unittest.TestCase):
    """ tests events functions"""
    def test_process_event(self):
        self.assertEqual(1, 1)


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
        self.assertEqual(1, 1)


class read_ptrac_test_case(unittest.TestCase):
    """ tests read ptrac functions"""
    def test_read_ptrac(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
