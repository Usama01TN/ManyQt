# encoding: utf-8
"""
Setup script for ManyQt.
"""
from setuptools import setup, find_packages
from os.path import exists, join, dirname
import io

NAME = "ManyQt"  # type: str
VERSION = "0.4.0"  # type: str
DEVELOPER = "UsamaTN"  # type: str
DEVELOPER_EMAIL = "ininou.oussematn@gmail.com"  # type: str
PACKAGES = find_packages(".", include="ManyQt*")  # type: list[str]
DESCRIPTION = "PyQt/PySide compatibility layer."  # type: str
with io.open("README.rst" if exists("README.rst") else join(dirname(__file__), "README.rst"), encoding="utf-8") as f:
    README = f.read()  # type: str
LICENSE = "GPLv3"  # type: str
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]  # type: list[str]
KEYWORDS = ["GUI", "PyQt4", "PyQt5", "PyQt6", "PySide", "PySide2", "PySide6", "compatibility"]  # type: list[str]

if __name__ == "__main__":
    setup(name=NAME, version=VERSION, author=DEVELOPER, description=DESCRIPTION, long_description=README,
          license=LICENSE, keywords=KEYWORDS, classifiers=CLASSIFIERS, packages=PACKAGES)

