# Get out of the test directory
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir))

# Import send file to test
import unittest
from tkinter import Tk
from main import craftclash

class TestCraftClash(unittest.TestCase):
    def setUp(self):
        self.app = craftclash()

    def test_window_title(self):
        self.assertEqual(self.app.title(), "CraftClash - Windows - 0.0.4 BETA")

if __name__ == '__main__':
    unittest.main()
