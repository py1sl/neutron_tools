import unittest
import tempfile
from unittest.mock import patch, mock_open
import neut_utilities as ut
import os
import logging
from datetime import datetime


class getlines_test_case(unittest.TestCase):
    """ tests get_lines function"""

    def test_get_lines(self):
        sample_lines = ["Line 1\n", "line 2\n", "line 3\n"]
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.writelines(sample_lines)
            temp_file_path = temp_file.name
        
        try:
            lines = ut.get_lines(temp_file_path)
            self.assertEqual(len(lines), 3)
        finally:
            os.remove(temp_file_path)


class writelines_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_lines(self):
        open_mock = mock_open()
        with patch("neut_utilities.open", open_mock, create=True):
            ut.write_lines("output.txt", ["hello", "world"])

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_any_call("hello\n")
        open_mock.return_value.write.assert_any_call("world\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_line_empty_list(self, mock_file):
        lines = []
        ut.write_lines("output.txt", lines)
        mock_file.assert_called_once_with('output.txt', 'w')
        mock_file().write.assert_not_called()


class string_cleaner_test_case(unittest.TestCase):
    """ tests string_cleaner function"""

    def test_spaces(self):
        test_string = "   hello"
        self.assertEqual(ut.string_cleaner(test_string), "hello")
        test_string = "   hello    "
        self.assertEqual(ut.string_cleaner(test_string), "hello")
        test_string = "   hello    world   "
        self.assertEqual(ut.string_cleaner(test_string), "hello world")
        test_string = "hello world"
        self.assertEqual(ut.string_cleaner(test_string), "hello world")


class find_ind_test_case(unittest.TestCase):
    """ test for reading the version of output file"""

    def test_find_ind(self):
        data = ["hello world", "hello mars"]
        self.assertEqual(ut.find_ind(data, "mars"), 1)
        self.assertEqual(ut.find_ind(data, "world"), 0)
        self.assertEqual(ut.find_ind(data, "hello"), 0)


class find_line_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_line(self):
        test_lines = ["", "hello", "world"]
        self.assertEqual(ut.find_line("hel", test_lines, 3), 1)
        self.assertEqual(ut.find_line("wor", test_lines, 3), 2)
        self.assertEqual(ut.find_line("", test_lines, 1), 0)


class find_nonzero_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_nonzero(self):
        test_vals = [0, 0, 0, 1, 1]
        self.assertEqual(ut.find_first_non_zero(test_vals), 3)
        test_vals = [0, 0, 0, -1, 1]
        self.assertEqual(ut.find_first_non_zero(test_vals), 3)
        test_vals = [0, 0, 0, 0, 0.0, 0]
        self.assertEqual(ut.find_first_non_zero(test_vals), None)


class find_zero_test_case(unittest.TestCase):
    """ tests for find line function"""

    def test_find_zero(self):
        test_vals = [0, 0, 0, 1, 1]
        self.assertEqual(ut.find_first_zero(test_vals), 0)
        test_vals = [1, 1, 0.1, 0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 0.0]
        self.assertEqual(ut.find_first_zero(test_vals), 3)
        test_vals = [-1, 1, 0.1, 1.0]
        self.assertEqual(ut.find_first_zero(test_vals), None)


class string_replace_test_case(unittest.TestCase):
    """ tests for the string replace function """
    def test_string_replace_error(self):
        with self.assertRaises(FileNotFoundError):
            ut.text_replace('no_such_fname', 'old_string', 'new_string')


class same_value_test_case(unittest.TestCase):
    """test for the is_same_value function """
    def test_same_value(self):
        self.assertTrue(ut.is_same_value(1.0, 1.0))  # when same
        self.assertTrue(ut.is_same_value(1.00000001, 1.0))  # when nearly same
        self.assertFalse(ut.is_same_value(2.0, 1.0))  # when different
        self.assertFalse(ut.is_same_value(2.0, 1.0, tolerance=1e-3))  # custom tolerance
        self.assertTrue(ut.is_same_value(1.0001, 1.0, tolerance=1e-3))  # custom tolerance


class logger_test_case(unittest.TestCase):
    """tests for the NeutronToolsLogger / setup_ntlogger behavior"""

    def tearDown(self):
        # Clear handlers after each test to avoid cross-test interference
        logger = logging.getLogger('nt_logger')
        for h in list(logger.handlers):
            logger.removeHandler(h)
            h.close()

    def test_console_only(self):
        # console only: no file handler should be attached
        logger = ut.NeutronToolsLogger().setup_logging(log_file=None)
        # Expect at least a StreamHandler and no RotatingFileHandler
        self.assertTrue(any('StreamHandler' in type(h).__name__ for h in logger.handlers))
        self.assertFalse(any('RotatingFileHandler' in type(h).__name__ for h in logger.handlers))

    def test_explicit_file(self):
        # explicit file path should attach a RotatingFileHandler (mocked)
        path = 'explicit_test.log'
        with patch('logging.handlers.RotatingFileHandler') as mock_rotating:
            mock_handler = mock_rotating.return_value
            logger = ut.NeutronToolsLogger().setup_logging(log_file=path)
            # RotatingFileHandler should have been constructed with the given path
            mock_rotating.assert_called_once()
            called_args, called_kwargs = mock_rotating.call_args
            self.assertEqual(called_args[0], path)
            # Expect the same maxBytes/backupCount as configured in neut_utilities
            self.assertEqual(called_kwargs.get('maxBytes'), 10*1024*1024)
            self.assertEqual(called_kwargs.get('backupCount'), 5)
            # The mock handler should be present in logger.handlers
            self.assertIn(mock_handler, logger.handlers)

    def test_auto_file(self):
        # 'auto' should result in a RotatingFileHandler constructed with a date-based filename
        date_str = datetime.now().strftime('%Y%m%d')
        expected_fname = f'neutron_tools_{date_str}.log'
        with patch('logging.handlers.RotatingFileHandler') as mock_rotating:
            mock_handler = mock_rotating.return_value
            logger = ut.NeutronToolsLogger().setup_logging(log_file='auto')
            mock_rotating.assert_called_once()
            called_args, called_kwargs = mock_rotating.call_args
            self.assertEqual(called_args[0], expected_fname)
            self.assertIn(mock_handler, logger.handlers)

if __name__ == '__main__':
    unittest.main()
