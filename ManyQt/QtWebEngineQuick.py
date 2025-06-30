# -*- coding: utf-8 -*-
"""
Provides QtWebEngineQuick classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT6:
    try:
        from PyQt6.QtWebEngineQuick import *
    except:
        raise QtModuleNotInstalledError(name="QtWebEngineQuick", missing_package="PyQt6-WebEngine")
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtWebEngineQuick import *
    except:
        raise QtModuleNotInstalledError(name="QtWebEngineQuick", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtWebEngineQuick' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
