# -*- coding: utf-8 -*-
"""
QtGraphsWidgets is a collection of widgets for plotting graphs and charts.
It provides an easy way to create plots with minimal code.
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
    from PyQt5.QtGraphsWidgets import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtGraphsWidgets import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtGraphsWidgets import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtGraphsWidgets import *
    except:
        raise QtModuleNotInstalledError(name="QtGraphsWidgets", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtGraphsWidgets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
