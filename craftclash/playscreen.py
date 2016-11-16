## Copyright (C) 2016 Necti Co. and Dog Face Development Co.
## All rights reserved.
"""
CRAFT CLASH
Play screen project file.
"""

# Import Statements
from tkinter import *
import turtle
    
# Playscreen Function
def playscreen():
    # Window Elements
    window = Tk()
    window.title("Craft Clash - Windows - 0.0.1 BETA - Play!")
    window.resizable(0,0)
    # Widgets
    worldoneimg = PhotoImage(file = "D:/William/Documents/Necti Co/CraftClash/BETA_V1.0/assets/logo/titlethumbnail.gif") # Change absolute path on you own computer to the assets/logo/titlethumbnail.gif, for more infor se the README.
    btn_createnewworld = Button(window, text = "Create New World!", height = 2, width = 80, command = exit)
    worldinfo = Label(window, text= "We have already created two worlds for you to play in. Chose your pick of world or play in both of them. \n You can create another world by clicking the 'Create New World!' button at the top of the screen") 
    btn_worldone = Button(window, text = "World 1", height = 4, width = 50, command = exit)
    btn_worldoneimg = Button(window, image = worldoneimg)
    # Pack Statements
    btn_createnewworld.pack(side = TOP)
    worldinfo.pack(side = TOP, pady = 5)
    btn_worldoneimg.pack(side = LEFT, padx = 5)
    btn_worldone.pack(side = LEFT)
    # Sustain Window
    window.mainloop()

    
