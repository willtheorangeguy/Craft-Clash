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

## Creates the "Options" screen.

# Import Statements
from tkinter import *
import turtle
import tkinter.messagebox as box
    
def optionsscreen():
    # Windows Statements
    window = Tk()
    window.title("Options - CraftClash - Windows - Version 0.0.4 BETA")

    def gametagedit():
    # Widgets
        box.showinfo("Name Change Completed Sucsessfully", "Thank you for changing your GameTag to: " + gametagentry.get())

    # Widgets
    titlelabel = Label(window, text = "Welcome to the options screen. Here you can change the volume of the game,\n music and difficulty.")
    musicsectiontitle = Label(window, text = "Sounds:")
    volumetitle = Label(window, text = "\nVolume")
    volumeslider = Scale(window, from_ = 0.0, to = 100.0, tickinterval = 0.25, orient="horizontal")
    musictitle = Label(window, text = "\nMusic")
    musicslider = Scale(window, from_ = 0.0, to = 100.0, tickinterval = 0.25, orient="horizontal")
    difficultytitle = Label(window, text = "\n\nDifficulty:")
    difficultyframe = Frame(window)
    difficulty = StringVar()
    difficulty1 = Radiobutton(difficultyframe, text = 'Easy', variable = difficulty, value = 'easy')
    difficulty2 = Radiobutton(difficultyframe, text = 'Normal', variable = difficulty, value = 'normal')
    difficulty3 = Radiobutton(difficultyframe, text = 'Hard', variable = difficulty, value = 'hard')
    difficulty1.select()
    gametagtitle = Label(window, text = "\n\nChange or Create Your GameTag:")
    gametagframe = Frame(window)
    gametagentry = Entry(gametagframe)
    gametagbtn = Button(gametagframe, text = "Change GameTag", command = gametagedit)
            
    # Pack Statements
    titlelabel.pack(side = TOP)
    musicsectiontitle.pack(side = TOP)
    volumetitle.pack(side = TOP)
    volumeslider.pack(side = TOP)
    musictitle.pack(side = TOP)
    musicslider.pack(side = TOP)
    difficultytitle.pack(side = TOP)
    difficulty1.pack(side = LEFT)
    difficulty2.pack(side = LEFT)
    difficulty3.pack(side = LEFT)
    difficultyframe.pack(side = TOP)
    gametagtitle.pack(side = TOP)
    gametagbtn.pack(side = RIGHT)
    gametagentry.pack(side = LEFT)
    gametagframe.pack(side = TOP)

    # Sustain Window
    window.mainloop()

    
