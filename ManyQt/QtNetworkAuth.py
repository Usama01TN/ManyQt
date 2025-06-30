# -*- coding: utf-8 -*-
"""
Provides QtNetworkAuth classes and functions.
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
        from PyQt5.QtNetworkAuth import *
    except:
        raise QtModuleNotInstalledError(name="QtNetworkAuth", missing_package="PyQtNetworkAuth")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.QtNetworkAuth import *
    except:
        raise QtModuleNotInstalledError(name="QtNetworkAuth", missing_package="PyQt6-NetworkAuth")
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtNetworkAuth import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtNetworkAuth import *
    except:
        raise QtModuleNotInstalledError(name="QtNetworkAuth", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtNetworkAuth' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
