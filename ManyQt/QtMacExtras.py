# -*- coding: utf-8 -*-
"""
QtMacExtras is a Python wrapper around Qt's Mac Extras C++ library.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

# Names imported from Qt4's QtGui module.
__Qt4_QtGui = ['QMacPasteboardMime']  # type: list[str]
if USED_API == QT_API_PYQT6:
    from PyQt6.QtMacExtras import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtMacExtras import *
elif USED_API == QT_API_PYQT4:
    from PyQt4.QtGui import QMacPasteboardMime
elif USED_API == QT_API_PYSIDE:
    from PySide.QtGui import QMacPasteboardMime
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtGui import QMacPasteboardMime
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtGui import QMacPasteboardMime
else:
    raise ImportError("No module named 'QtMacExtras' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
