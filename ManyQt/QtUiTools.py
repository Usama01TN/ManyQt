# -*- coding: utf-8 -*-
"""
Provides QtUiTools classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYSIDE, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYSIDE, QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYSIDE:
    from PySide.QtUiTools import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtUiTools import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtUiTools import *
else:
    raise ImportError("No module named 'QtUiTools' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
