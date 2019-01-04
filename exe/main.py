"""
Copyright (C) 2016-2019 Necti Co. and Dog Face Development Co.

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
"""
CRAFT CLASH
Main project file.
"""
# Import Statements
from tkinter import *
import turtle

# Window Elements
window = Tk()
window.title("Craft Clash - Windows - 0.0.1 BETA")
window.configure(bg = "sky blue")
#if "nt" == os.name:
#    window.wm_iconbitmap(bitmap = "assets/logo/titletumbnail.gif")

# Images
titleimg = PhotoImage(file = "D:/William/Documents/Necti Co/CraftClash/BETA_V1.0/assets/logo/titlelogo.gif")

#Widgets
titlelabel = Label(window, image = titleimg)
btn_play = Button(window, text = "Play!", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
btn_options = Button(window, text = "Options", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
btn_exit = Button(window, text = "Exit", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
copyright_label = Label(window, text = "Copyright (C) 2016-2019 Necti Co. and Dog Face Development Co. \t\t\t Version 0.0.1 BETA")

# Pack Statements
titlelabel.pack(side = TOP, pady = 20)
btn_play.pack(side = TOP, padx = 300, pady = 5)
btn_options.pack(side = TOP, padx = 300, pady = 5)
btn_exit.pack(side = TOP, padx = 300, pady = 5)
copyright_label.pack(side = BOTTOM, padx = 100, pady = 50)

# Sustain Window
window.mainloop()
