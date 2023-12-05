"""Test the main.py file."""
#pylint: disable=import-error, invalid-name

# Get out of the test directory
import os
import sys
import unittest
from main import craftclash

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))


class TestCraftClash(unittest.TestCase):
    """Test the CraftClash class in main.py."""
    
    def setUp(self):
        """Set up the test."""
        self.app = craftclash()

    def test_window_title(self):
        """Test the window title."""
        self.assertEqual(self.app.title(), "CraftClash - Windows - 0.0.4 BETA")


if __name__ == "__main__":
    unittest.main()
