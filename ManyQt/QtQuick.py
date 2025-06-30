# -*- coding: utf-8 -*-
"""
QtQuick is a Python binding for Qt's Quick library.
It provides a set of classes and functions that allow you to create graphical user interfaces (GUIs)
using the Qt framework.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT6:
    from PyQt6.QtQuick import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtQuick import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtQuick import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtQuick import *
else:
    raise ImportError("No module named 'QtQuick' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
