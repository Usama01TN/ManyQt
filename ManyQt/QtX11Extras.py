# -*- coding: utf-8 -*-
"""
QtX11Extras is a backport of the Qt 5 module with the same name.
It provides access to X11-specific functionality.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT4:
    from PyQt4.QtGui import QX11Info
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtX11Extras import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtX11Extras import *
elif USED_API == QT_API_PYSIDE:
    from PySide.QtGui import QX11Info
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtX11Extras import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtX11Extras import *
else:
    raise ImportError("No module named 'QtX11Extras' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
__all__ = ["QX11Info"]
