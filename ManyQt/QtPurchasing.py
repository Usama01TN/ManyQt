# -*- coding: utf-8 -*-
"""
Provides QtPurchasing classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, QtModuleNotInstalledError, \
        apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, QtModuleNotInstalledError, \
        apply_global_fixes

if USED_API == QT_API_PYQT5:
    try:
        from PyQt5.QtPurchasing import *
    except:
        raise QtModuleNotInstalledError(name="QtPurchasing", missing_package="PyQtPurchasing")
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtPurchasing import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtPurchasing import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtPurchasing import *
else:
    raise ImportError("No module named 'QtPurchasing' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
