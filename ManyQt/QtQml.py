# -*- coding: utf-8 -*-
"""
QtQml is a wrapper for the QtQml module of the currently used API.
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
    from PyQt6.QtQml import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtQml import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtQml import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtQml import *
else:
    raise ImportError("No module named 'QtQml' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
