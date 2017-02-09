# CraftClash
A dynamic cross of [Clash of Clans](http://supercell.com/en/games/clashofclans/) and [Minecraft](https://minecraft.net/en/). Spend the day upgrading your buildings and walls, craft new items and tend to your world. Have fun spending the night fighting off monsters and hoping you and your world can endure the damage that they do! Written in Python 3 with ❤. Fully open source!!

![Total Downloads](https://img.shields.io/github/downloads/Derpyface-Development-Co/Craft-Clash/total.svg)
![Release Version](https://img.shields.io/github/release/Derpyface-Development-Co/Craft-Clash.svg)
![Issues](https://img.shields.io/github/issues/Derpyface-Development-Co/Craft-Clash.svg)
![Pull Requests](https://img.shields.io/github/issues-pr/Derpyface-Development-Co/Craft-Clash.svg)
![Contributors](https://img.shields.io/github/contributors/Derpyface-Development-Co/Craft-Clash.svg)
![License](https://img.shields.io/github/license/Derpyface-Development-Co/Craft-Clash.svg)

![Welcome Screen](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/doc/mainscreen.PNG)

## Features
- Cool and Clean GUI
- Easy to play
- Combines to very popular games right now.
- Let's you put your problem solving skills and survival skills to the test.
- Use your creativity for everything in the game.
- Great documentation and wiki 
- Open source
- Written in Python and works with Python 3.5 and up (guaranteed)
- Not available on any app store - only available [here](https://github.com/Derpyface-Development-Co/Craft-Clash/archive/beta-v0.0.2.zip) for those who can find it!!

You craft items to fight monsters such as swords and bows, pickaxes and shovels to mine minerals and other items such as fences to protect your buildings. Use your pickax or shovel to find minerals underground such as coal, copper ore or iron ore. Then use your coal to turn the iron ore into iron nuggets. Now using your iron you can build some Iron Armour to protect you from mob damage and a Iron Sword to fight the monsters at night, gaining elixir to upgrade your walls that way you are safe from other monster attacks. Any of your other iron nuggets or copper nuggets can them be added to your walls to make them even stronger. 

Enough said here, see more in the [wiki](https://github.com/Derpyface-Development-Co/Craft-Clash/wiki).

## Purpose
The purpose of this project is a fun game that you can play to level up your survival and problem solving skills. You can use this game to practice for when you play Minecraft and as pre-battle practice for battling in Clash of Clans. 

We also created this project to see if two beginner programmers could create a mash up game of the two most popular games for kids right now, in Python which is a language not used (usually!) for games.

## Contributors
- [@willtheorangeguy](https://github.com/willtheorangeguy)
- [@derpyface](https://github.com/derpyface)
- [@Derpyface-Development-Co](https://github.com/Derpyface-Development-Co/)
- [@Dog-Face-Developement](https://github.com/dog-face-development)

## Installation and Startup Instructions
### Through the Python Module (IDLE)
- Download the Python module if you haven’t already: [Download Link](https://www.python.org/downloads), and install it,
- Extract the files from your GitHub Download,
- Double click the `main.py` file in File Explorer,
- And the app will open for you to use!

**THE FOLLOWING TWO OPTIONS CURRENTLY DO NOT WORK:** 

### Creating and Executable File with cx_Freeze (Windows Only)
- Download cx_Freeze if you haven’t already: [Download Link](https://pypi.python.org/packages/38/ae/2cf4f13f42d54b01e26b0b713298722b351ca5a2408b2a77953be67ffb25/cx_Freeze-5.0.win32-py3.5.exe#md5=05e531d442cb9e27d093ca1ee37a03f4), and install it,
- Extract the files from your GitHub download to this location on your computer: `C:\Users\YOUR_USERNAME`,
- Open Command Prompt and type the following command: `python setup.py bdist_msi`
- Run the .msi file that the process creates in a dist sub-directory to create an executable,
- Run the executable and the app will open for you to use!

### Run the Executable File (PyInstaller Required) 
- Extract the files from the GitHub download.
- Navigate to the `exe` file folder
- Extract the `dist.zip` file folder.
- Go to the `main` file folder.
- Run the Executable file named: `main.exe`

## Game Play Instructions
**NOT ALL OF THE BUTTONS WORK RIGHT NOW, WE ARE STILL IN BETA**

After you have opened the app using one of the above options. You will see the apps main welcome interface (GUI/UI). There are three buttons, two of which work right now. The *Play!* button currently does not work but will launch you into your world when it works so you can play the game. Yes, currently there is only one world, because we want to be able to ship new updates faster. Later there will be a screen that lets you choose your world and create new ones.  
The *Options* button will bring you to the options screen which currently only lets you change the volume of the game sounds and the volume of the music. Soon you will be able to change the difficulty, and change your in-game name.

![Options Screen](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/doc/optionsscreen.PNG)

The *Exit* button does exactly what it says it does. It exits the game. Due to a minor bug sometimes the game will reopen after you press this button, to fix this just click the red *X* in the top right hand corner. 

To find more information about how to play the game, such as crafting recipes for the world and keyboard controls, see the [wiki](https://github.com/Derpyface-Development-Co/Craft-Clash/wiki).

## Releases
**WE ARE STILL IN BETA. SOME FEATURES DO NOT WORK!**

The most recent stable release is version *v0.0.2*. Version *0.0.2* added: 
- Options screen
- New README.md and website
- New assets

The next release, version *0.0.3* is coming out soon with new bug fixes and features. Here are some bellow: 
- Finished Options screen.
- *Exit* button renamed to *About*.
- New *About* screen, telling about the program.
- When the game launches you get the Welcome screen rather than the Options screen.

Sending in a [pull reques](https://github.com/Derpyface-Development-Co/Craft-Clash/pulls) for new features you want to implement and bugs you want to help fix are always welcome. Creating a [new issue](https://github.com/Derpyface-Development-Co/Craft-Clash/issues) for a new feature is always welcome, too. Look to see your contributions in future updates.

## Bugs and Issues
Who likes bugs in their software? (We don’t think anybody does! 😉) That’s why we try hard to make sure that there are no bugs in our software, but sometimes a few slip through the system. If you have found any, feel free to let us know on the [Issues page](https://github.com/Derpyface-Development-Co/Craft-Clash/issues)! We will try to have these issues fixed as soon as possible.  
Note: Please check the known issues list below before posting an issue to see if your issue is already on the list!

### Known Issues:
- Options screen opens rather than the main welcome screen.
- Program opens again after clicking the *Exit* button. **Solved:** Click the red *X* int he right hand corner to close the app.
- *Play* button doesn't work. **Solved:** Not a bug, we haven't gotten there yet, remember we are still in devlopment mode.

## License, Assets & Legal Stuff
Below is alot of licensing stuff that says what you can't and can do with the software. All you need to know is that you **CAN NOT** claim the software as you own. You can do just about anything else. For more info keep reading...
### License
This software has been released as open source under the *GNU General Public License V3.0* license.  
You can view the license in the [`LICENSE.md`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/LICENSE) file in this projects repository.  
By using this software you agree to this license. Please adhere to this license when using, distributing, and making changes to the software.

### Assets
Our assets are copyright and license under the *Creative Commons Attribution 4.0 International* license.  
You can view the license in the [`Creative Commons Attribution 4.0 - Assets License.txt`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/assets/Creative%20Commons%20Attribution%204.0%20-%20Assets%20License.txt) file in the assets folder.

The GUI is Copyright (C) 2016:
Mojang Development (some GUI copied from Minecraft: Windows 10 Edition Beta and then modified) and Derpyface Development Co. You can view the license file in [`assets\gui\gui License.txt`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/assets/gui/gui%20License.txt). 

The Logos are Copyright (C) 2016 Derpyface Development Co. You can view the license file in [`logo\Logo_Copyrights`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/assets/logo/Logo_Copyrights.txt).

The Music is Copyright (C) 2016: Mojang Developemt (some music copied from Minecraft: Windows 10 Edition Beta and then modified) and Derpyface Development Co. You can vies the license file in [`assets\music\music License.txt`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/assets/music/music%20License.txt).   
The following songs are copyright by the following individual people:   
*fun.m4a Copyright (C) 2015 William V. (aka: @willtheorangeguy on GitHub)*   
*fun2.mp3 Copyright (C) Mr. Scruff (Album: Ninja Tuna, #1)*    
*calm4.mp3 Copyright (C) Richard Stoltzman, and Slovak Radio Symphony Orchestra (Album: Fine Music, Vol. 1, #2)*

The Textures are Copyright (C) Derpyface Development Co. and Mojang Development. Some textures copied from Minecraft and Terraria texture packs. The textures have been made with: BDCraft Cubix, and also made with Microsoft Paint. We also made some with [Piskel](https://piskelapp.com). You can vies the license file in [`assets\textures\Textures_Info`](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/assets/textures/Textures_Info.txt).

You can learn more about the licensing and legal stuff in the [wiki](https://github.com/Derpyface-Development-Co/Craft-Clash/wiki).

## Other Links
Visit these other links to learn more about *CraftClash*:

[Latest Version Download](https://github.com/Derpyface-Development-Co/Craft-Clash/archive/beta-v0.0.2.zip), [Issues Page](https://github.com/Derpyface-Development-Co/Craft-Clash/issues), [Pull Request Page](https://github.com/Derpyface-Development-Co/Craft-Clash/pulls), [Wiki](https://github.com/Derpyface-Development-Co/Craft-Clash/wiki), and [Documentation](https://github.com/Derpyface-Development-Co/Craft-Clash/blob/master/README.md).
