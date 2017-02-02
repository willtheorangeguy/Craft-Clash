"""
Copyright (C) 2016 Derpyface Development Co. and Dog Face Development Co.

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
## All rights reserved.
# Import Statements
from tkinter import *
import turtle
import tkinter.messagebox as box
    
def optionsscreen():
    # Windows Statements
    window = Tk()
    window.title("Options - CraftClash - Windows - Version 0.0.2 BETA")

    # Widgets
    titlelabel = Label(window, text = "Welcome to the options screen. Here you can change the volume of the game,\n music, & some other options.")
    musicsectiontitle = Label(window, text = "Sounds:")
    volumetitle = Label(window, text = "\n\tVolume")
    volumeslider = Scale(window, from_ = 0.0, to = 100.0, tickinterval = 0.25, orient="horizontal")
    musictitle = Label(window, text = "\n\tMusic")
    musicslider = Scale(window, from_ = 0.0, to = 100.0, tickinterval = 0.25, orient="horizontal")
            
    # Pack Statements
    titlelabel.pack(side = TOP)
    musicsectiontitle.pack(side = TOP)
    volumetitle.pack(side = LEFT)
    volumeslider.pack(side = LEFT)
    musictitle.pack(side = LEFT)
    musicslider.pack(side = LEFT)

    # Sustain Window
    window.mainloop()
