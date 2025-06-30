# -*- coding: utf-8 -*-
"""
Provides QtDataVisualization classes and functions.
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
        from PyQt5.QtDataVisualization import *
    except:
        raise QtModuleNotInstalledError(name="QtDataVisualization", missing_package="PyQtDataVisualization")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.QtDataVisualization import *
    except:
        raise QtModuleNotInstalledError(name="QtDataVisualization", missing_package="PyQt6-DataVisualization")
elif USED_API == QT_API_PYSIDE2:
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    import PySide2.QtDataVisualization as __temp
    from inspect import getmembers

    for __name in getmembers(__temp.QtDataVisualization):
        globals()[__name[0]] = __name[1]
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtDataVisualization import *
    except:
        raise QtModuleNotInstalledError(
            name="QtDataVisualization", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtDataVisualization' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
