# -*- coding: utf-8 -*-
"""
Provides QtPdfWidgets classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, QtModuleNotInstalledError, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, QtModuleNotInstalledError, apply_global_fixes

if USED_API == QT_API_PYQT6:
    # Available with version >=6.4.0
    from PyQt6.QtPdfWidgets import *
elif USED_API == QT_API_PYSIDE6:
    try:
        # Available with version >=6.4.0
        from PySide6.QtPdfWidgets import *
    except:
        raise QtModuleNotInstalledError(name="QtPdfWidgets", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtPdfWidgets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
