"""Test the OptionScreen class in optionscreen.py."""
#pylint: disable=import-error, invalid-name

# Get out of the test directory
import os
import sys
import unittest
from optionscreen import optionsscreen

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))


class TestOptionScreen(unittest.TestCase):
    """Test the OptionScreen class in optionscreen.py."""

    def setUp(self):
        """Set up the test."""
        self.option_screen = optionsscreen()

    def test_init(self):
        """Test the init method."""
        self.assertIsNotNone(self.option_screen)


if __name__ == "__main__":
    unittest.main()
