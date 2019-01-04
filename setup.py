# Copyright (C) 2016 - 2019 Derpyface Developement Company

import sys
from cx_Freeze import setup, Executable
import setup_information

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = {'include_files' : ['PLANNING.txt', 'README.md', 'GNU General Public License - Project License', 'CHANGELOG.txt', 'craftclash.aboutscreen.py', 'craftclash.optionsscreen.py', 'craftclash.playscreen#.py'], 'includes' : [ 're' ]}
# Setup Info (Can also be found in the setup_information.py file)
setup( name = 'CraftClash',
       version = '0.0.3 BETA',
       description = 'Spend the day upgrading your buildings and walls, craft new items and tend to your world. Have fun spending the night fighting off monsters and hoping you and your world can endure the damage that they do! Written in Python 3 . Fully open source!!',
       author = 'Derpyface Developement Co.'
       options = { 'build_exe' : opts },
       executables = [Executable('main.py', base = base) ] )
