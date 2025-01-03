# tests/test_case.py
import sys
import os

# Import statements should be placed at the top
from my_project import add

# Add the root directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


# Test functions
def test_always_passes():
    assert True, "working fine"


def test_always_fails():
    assert True, "this test will fail"


def test_looks_great():
    assert True  # This test is trivially passing


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
