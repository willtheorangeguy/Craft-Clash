"""
Copyright (C) 2017-2026 willtheorangeguy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# pylint: disable=import-error, invalid-name

# Main program window.

# Import Statements
import os
from tkinter import Tk, Label, Button, PhotoImage, RAISED
from craftclash.optionscreen import optionsscreen
from craftclash.aboutscreen import aboutscreen

# Resolve assets relative to this file so the app works regardless of the
# current working directory.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")


def craftclash():
    """Build and return the main program window.

    The window is returned without starting the Tk event loop so that it can
    be created and inspected by tests. Call ``mainloop()`` on the returned
    window (see ``__main__`` below) to actually run the game.
    """
    # Window Elements
    window = Tk()
    window.title("CraftClash - Windows - 0.0.4 BETA")
    window.configure(bg="sky blue")

    # Images
    titleimg = PhotoImage(file=os.path.join(ASSETS_DIR, "logo", "titlelogo.gif"))

    # Widgets
    title_label = Label(window, image=titleimg)
    # Keep a reference to the image so it is not garbage collected once this
    # function returns (Tk does not hold a Python reference of its own).
    title_label.image = titleimg
    btn_play = Button(
        window, text="Play!", height=3, width=60, bd=4, relief=RAISED, command=exit
    )
    btn_options = Button(
        window,
        text="Options",
        height=3,
        width=60,
        bd=4,
        relief=RAISED,
        command=optionsscreen,
    )
    btn_about = Button(
        window,
        text="About",
        height=3,
        width=60,
        bd=4,
        relief=RAISED,
        command=aboutscreen,
    )
    copyright_label = Label(
        window,
        text="Copyright © 2017 - 2026 willtheorangeguy. \t\t\t Version 0.0.4 BETA",
    )

    # Pack Statements
    title_label.grid(row=1, column=2, rowspan=2, pady=10)
    btn_play.grid(row=3, column=2, columnspan=2)
    btn_options.grid(row=4, column=2, columnspan=2)
    btn_about.grid(row=5, column=2, columnspan=2)
    copyright_label.grid(row=6, column=1, columnspan=5)

    return window


if __name__ == "__main__":
    craftclash().mainloop()
