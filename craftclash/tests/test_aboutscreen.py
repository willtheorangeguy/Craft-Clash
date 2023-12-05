"""Test the AboutScreen class in aboutscreen.py."""
#pylint: disable=import-error, invalid-name

# Get out of the test directory
import os
import sys
import unittest
from aboutscreen import aboutscreen

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))


class TestAboutScreen(unittest.TestCase):
    """Test the AboutScreen class in aboutscreen.py."""
    
    def setUp(self):
        """Set up the test."""
        self.about_screen = aboutscreen()

    def test_init(self):
        """Test the init method."""
        self.assertIsNotNone(self.about_screen)


if __name__ == "__main__":
    unittest.main()
