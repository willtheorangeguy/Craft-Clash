# Get out of the test directory
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))

import unittest
from aboutscreen import aboutscreen  # assuming AboutScreen is a class in aboutscreen.py

class TestAboutScreen(unittest.TestCase):
    def setUp(self):
        self.about_screen = aboutscreen()

    def test_init(self):
        self.assertIsNotNone(self.about_screen)

if __name__ == '__main__':
    unittest.main()