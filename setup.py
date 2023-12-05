"""Setup file for Craft Clash."""
#pylint: disable=import-error, invalid-name

from setuptools import setup, find_packages


def readme():
    """Return the README.md file."""
    with open("README.md", encoding="UTF-8") as f:
        return f.read()


setup(
    name="craftclash",
    version="0.4.0",
    description="A game that is a cross of Minecraft and Clash of Clans, written in Python!",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
    ],
    keywords="minecraft clash of clans royale game food items blocks defense attack battle gui",
    url="https://github.com/Dog-Face-Development/Craft-Clash",
    author="willtheorangeguy",
    packages=find_packages(where="craftclash"),
    package_dir={"": "craftclash"},
    include_package_data=True,
    py_modules=["main", "aboutscreen", "optionsscreen", "playscreen.old"],
    entry_points={"console_scripts": ["craftclash=main:craftclash"]},
)
