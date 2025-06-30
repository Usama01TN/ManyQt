# -*- coding: utf-8 -*-
"""
Provides QtStateMachine classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, apply_global_fixes, QtModuleNotInstalledError
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, apply_global_fixes, QtModuleNotInstalledError

if USED_API == QT_API_PYQT6:
    from PyQt6.QtStateMachine import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtStateMachine import *
    except:
        raise QtModuleNotInstalledError(name="QtStateMachine", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtStateMachine' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
