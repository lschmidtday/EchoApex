# test_echoapex.py
"""
Tests for EchoApex module.
"""

import unittest
from echoapex import EchoApex

class TestEchoApex(unittest.TestCase):
    """Test cases for EchoApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoApex()
        self.assertIsInstance(instance, EchoApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
