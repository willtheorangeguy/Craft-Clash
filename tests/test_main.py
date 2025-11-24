"""Test the main application."""

# pylint: disable=import-error, wrong-import-position

import os
import sys
import unittest
from tkinter import Label, Button

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import craftclash


class TestApp(unittest.TestCase):
    """Test the main application."""

    def setUp(self):
        """Create the application."""
        self.app = craftclash()

    def tearDown(self):
        """Destroy the application."""
        self.app.window.destroy()

    def test_window_exists(self):
        """Test if the window exists."""
        self.assertIsNotNone(self.app)

    def test_window_background(self):
        """Test the window background color."""
        self.assertEqual(self.app.cget("bg"), "sky blue")

    def test_title_label_exists(self):
        """Test if the title label exists."""
        title_label = self.app.grid_slaves(row=1, column=2)[0]
        self.assertIsInstance(title_label, Label)

    def test_play_button_exists(self):
        """Test if the play button exists."""
        btn_play = self.app.grid_slaves(row=3, column=2)[0]
        self.assertIsInstance(btn_play, Button)
        self.assertEqual(btn_play.cget("text"), "Play!")

    def test_options_button_exists(self):
        """Test if the options button exists."""
        btn_options = self.app.grid_slaves(row=4, column=2)[0]
        self.assertIsInstance(btn_options, Button)
        self.assertEqual(btn_options.cget("text"), "Options")

    def test_about_button_exists(self):
        """Test if the about button exists."""
        btn_about = self.app.grid_slaves(row=5, column=2)[0]
        self.assertIsInstance(btn_about, Button)
        self.assertEqual(btn_about.cget("text"), "About")

    def test_copyright_label_exists(self):
        """Test if the copyright label exists."""
        copyright_label = self.app.grid_slaves(row=6, column=1)[0]
        self.assertIsInstance(copyright_label, Label)


if __name__ == "__main__":
    unittest.main()
