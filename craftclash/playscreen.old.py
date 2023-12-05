"""
Copyright (C) 2017-2022 Dog Face Development Co.

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
#pylint: disable=import-error, invalid-name, too-many-locals

# Creates the "Playscreen"

# Import Statements
from tkinter import Tk, Label, Button, PhotoImage, Entry, Frame, TOP, LEFT


# Playscreen Function
def playscreen():
    """Creates the Playscreen"""
    # Window Elements
    window = Tk()
    window.title("CraftClash - Windows - 0.0.2 BETA - Play!")
    window.resizable(0, 0)
    # Widgets
    worldoneimg = PhotoImage(file="titlethumbnail.gif")
    btn_createnewworld = Button(
        window, text="Create New World!", height=2, width=80, command=exit
    )
    worldinfo = Label(
        window,
        text="We have already created a world for you to play in. \
            \n You can create another world by clicking the 'Create New World!' \
            button at the top of the screen",
    )
    btn_worldone = Button(window, text="World 1", height=4, width=50, command=exit)
    btn_worldoneimg = Button(window, image=worldoneimg)
    # Pack Statements
    btn_createnewworld.pack(side=TOP)
    worldinfo.pack(side=TOP, pady=5)
    btn_worldoneimg.pack(side=LEFT, padx=5)
    btn_worldone.pack(side=LEFT)
    # Sustain Window
    window.mainloop()


# Create New World Function
def createworldscreen():
    """Creates the Create New World screen."""
    # Window Elements
    window = Tk()
    window.title("Creating New World")
    window.resizable(0, 0)
    # Widgets
    createnewworldinfo = Label(
        window,
        text="Enter a name for your new world and select difficulty. \
            \n\n Spawn in  world with randomly generated trees and \
            try to survive the night by building up your walls and \
                defending your castle from monsters.",
    )
    worldnameframe = Frame(window)
    worldnameentry = Entry(worldnameframe, width=20)

    # Test
    print(createnewworldinfo)
    print(worldnameframe)
    print(worldnameentry)
