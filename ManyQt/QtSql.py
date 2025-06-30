# -*- coding: utf-8 -*-
"""
QtSql is a wrapper for the Qt Sql library. It provides a simple interface to access databases.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT4:
    from PyQt4.QtSql import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtSql import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtSql import *
elif USED_API == QT_API_PYSIDE:
    from PySide.QtSql import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtSql import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtSql import *
else:
    raise ImportError("No module named 'QtSql' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
