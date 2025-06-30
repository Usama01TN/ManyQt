# -*- coding: utf-8 -*-
"""
QtWebSockets module provides access to the Qt Web Sockets API.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes, \
        QtModuleNotInstalledError
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes, \
        QtModuleNotInstalledError

if USED_API == QT_API_PYQT5:
    from PyQt5.QtWebSockets import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtWebSockets import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtWebSockets import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtWebSockets import *
    except:
        raise QtModuleNotInstalledError(name="QtWebSockets", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtWebSockets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
