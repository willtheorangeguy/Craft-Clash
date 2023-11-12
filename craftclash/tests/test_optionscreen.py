# Get out of the test directory
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))

import unittest
from optionscreen import optionsscreen  # assuming OptionScreen is a class in optionscreen.py

class TestOptionScreen(unittest.TestCase):
    def setUp(self):
        self.option_screen = optionsscreen()

    def test_init(self):
        self.assertIsNotNone(self.option_screen)

if __name__ == '__main__':
    unittest.main()