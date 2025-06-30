# -*- coding: utf-8 -*-
"""
Provides Qsci classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QtModuleNotInstalledError, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QtModuleNotInstalledError, apply_global_fixes

if USED_API == QT_API_PYQT5:
    try:
        from PyQt5.Qsci import *
    except:
        raise QtModuleNotInstalledError(name="Qsci", missing_package="QScintilla")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.Qsci import *
    except:
        raise QtModuleNotInstalledError(name="Qsci", missing_package="PyQt6-QScintilla")
else:
    raise ImportError("No module named 'Qsci' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
