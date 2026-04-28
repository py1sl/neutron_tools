import os
import pytest


@pytest.fixture(autouse=True)
def change_to_tests_dir(monkeypatch):
    """Ensure the working directory is the tests directory for all tests.

    Some tests use paths relative to the tests/ directory (e.g. test_r2s_cell.py).
    This fixture restores the behaviour of running pytest from within tests/.
    """
    monkeypatch.chdir(os.path.dirname(__file__))
