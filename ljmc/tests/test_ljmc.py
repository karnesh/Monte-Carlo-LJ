"""
Unit and regression test for the ljmc package.
"""

# Import package, test suite, and other packages as needed
import ljmc
import pytest
import sys

def test_ljmc_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "ljmc" in sys.modules
