# -*- coding: utf-8 -*-
"""
QtWinExtras provides access to Windows-specific functionality.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, apply_global_fixes

if USED_API == QT_API_PYQT5:
    from PyQt5.QtWinExtras import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtWinExtras import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtWinExtras import *
else:
    raise ImportError("No module named 'QtWinExtras' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
