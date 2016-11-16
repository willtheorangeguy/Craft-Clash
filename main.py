## Copyright (C) 2016 Necti Co. and Dog Face Development Co.
## All rights reserved.
"""
CRAFT CLASH
Main project file.
"""
# Import Statements
from tkinter import *
import turtle
from craftclash.playscreen import *
from craftclash.optionscreen import *

# Window Elements
window = Tk()
window.title("Craft Clash - Windows - 0.0.1 BETA")
window.configure(bg = "sky blue")
#if "nt" == os.name:
#    window.wm_iconbitmap(bitmap = "assets/logo/titletumbnail.gif")

# Images
titleimg = PhotoImage(file = "assets/logo/titlelogo.gif")

#Widgets
titlelabel = Label(window, image = titleimg)
btn_play = Button(window, text = "Play!", height = 3, width = 60, bd = 4, relief = RAISED, command = playscreen)
btn_options = Button(window, text = "Options", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
btn_exit = Button(window, text = "Exit", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
copyright_label = Label(window, text = "Copyright (C) 2016 Necti Co. and Dog Face Development Co. \t\t\t\t Version 0.0.1 BETA")

# Pack Statements
titlelabel.pack(side = TOP, pady = 20)
btn_play.pack(side = TOP, padx = 300, pady = 5)
btn_options.pack(side = TOP, padx = 300, pady = 5)
btn_exit.pack(side = TOP, padx = 300, pady = 5)
copyright_label.pack(side = BOTTOM, padx = 100, pady = 50)

# Sustain Window
window.mainloop()
