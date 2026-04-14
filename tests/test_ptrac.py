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

    @classmethod
    def setUpClass(cls):
        ptrac_path = os.path.join(os.path.dirname(__file__), 'test_output', 'ptrak_asc_all')
        cls.hists = mpr.read_ptrac(ptrac_path)

    def test_process_event(self):
        self.assertEqual(len(self.hists[0].events), 12)
        self.assertEqual(len(self.hists[-1].events), 12)
        self.assertEqual(len(self.hists[-2].events), 9)
        self.assertEqual(self.hists[0].events[0].type, 3000)
        self.assertEqual(self.hists[0].events[-1].type, 9000)
        self.assertEqual(self.hists[0].events[0].x, 0)
        self.assertEqual(self.hists[0].events[0].y, 0)
        self.assertEqual(self.hists[0].events[0].z, 0)
        self.assertEqual(self.hists[0].events[0].u, 0.50848)
        self.assertEqual(self.hists[0].events[0].v, 0.47328)
        self.assertEqual(self.hists[0].events[0].w, 0.71935)
        self.assertEqual(self.hists[0].events[0].wgt, 1)
        self.assertEqual(self.hists[0].events[0].energy, 1.332)

    def test_events_eq(self):
        self.assertTrue(self.hists[0].events[0] == self.hists[0].events[0])
        self.assertEqual(self.hists[0].events[0], self.hists[0].events[0])
        self.assertTrue(self.hists[0].events[0] != self.hists[0].events[1])
        self.assertFalse(self.hists[0].events[0] == self.hists[0].events[1])

    def _make_event(self, **kwargs):
        """ helper to build an event with defaults that can be overridden """
        e = mpr.event()
        e.x = kwargs.get('x', 1.0)
        e.y = kwargs.get('y', 2.0)
        e.z = kwargs.get('z', 3.0)
        e.type = kwargs.get('type', 3000)
        e.u = kwargs.get('u', 0.5)
        e.v = kwargs.get('v', 0.5)
        e.w = kwargs.get('w', 0.7)
        e.wgt = kwargs.get('wgt', 1.0)
        e.energy = kwargs.get('energy', 1.0)
        e.par = kwargs.get('par', 2)
        e.cell = kwargs.get('cell', 5)
        e.time = kwargs.get('time', 0.0)
        return e

    def test_event_eq_x_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(x=99.0)
        self.assertFalse(e1 == e2)

    def test_event_eq_y_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(y=99.0)
        self.assertFalse(e1 == e2)

    def test_event_eq_z_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(z=99.0)
        self.assertFalse(e1 == e2)

    def test_event_eq_type_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(type=9000)
        self.assertFalse(e1 == e2)

    def test_event_eq_u_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(u=0.99)
        self.assertFalse(e1 == e2)

    def test_event_eq_v_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(v=0.99)
        self.assertFalse(e1 == e2)

    def test_event_eq_w_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(w=0.99)
        self.assertFalse(e1 == e2)

    def test_event_eq_wgt_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(wgt=2.0)
        self.assertFalse(e1 == e2)

    def test_event_eq_par_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(par=1)
        self.assertFalse(e1 == e2)

    def test_event_eq_cell_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(cell=10)
        self.assertFalse(e1 == e2)

    def test_event_eq_time_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(time=99.9)
        self.assertFalse(e1 == e2)

    def test_event_eq_energy_differs(self):
        e1 = self._make_event()
        e2 = self._make_event(energy=99.9)
        self.assertFalse(e1 == e2)

    def test_event_eq_not_event_type(self):
        e1 = self._make_event()
        result = e1.__eq__("not an event")
        # returns NotImplementedError class (not an instance) for non-event types
        self.assertIs(result, NotImplementedError)

    def test_process_event_else_branch(self):
        """ test process_event with 17-element data (else branch) """
        # 17 elements triggers the else branch
        data = [str(float(i)) for i in range(17)]
        ev = mpr.process_event(data)
        self.assertIsInstance(ev, mpr.event)
        # else branch: cell=data[3], x=data[8], y=data[9], z=data[10]
        self.assertEqual(ev.cell, 3.0)
        self.assertEqual(ev.x, 8.0)
        self.assertEqual(ev.y, 9.0)
        self.assertEqual(ev.z, 10.0)
        self.assertEqual(ev.u, 11.0)
        self.assertEqual(ev.v, 12.0)
        self.assertEqual(ev.w, 13.0)
        self.assertEqual(ev.energy, 14.0)
        self.assertEqual(ev.wgt, 15.0)
        self.assertEqual(ev.par, 4.0)
        self.assertEqual(ev.time, 16.0)


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
