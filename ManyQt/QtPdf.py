# -*- coding: utf-8 -*-
"""
Provides QtPdf classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT5:
    from PyQt5.QtPdf import *
elif USED_API == QT_API_PYQT6:
    # Available with version >=6.4.0
    from PyQt6.QtPdf import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtPdf import *
elif USED_API == QT_API_PYSIDE6:
    # Available with version >=6.4.0
    from PySide6.QtPdf import *
else:
    raise ImportError("No module named 'QtPdf' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
