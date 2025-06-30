# -*- coding: utf-8 -*-
"""
QtMultimediaWidgets is a wrapper for the QtMultimediaWidgets module of a specific Qt binding. It provides an easy way to
import all classes and functions of this module without having to worry about which binding is used.
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

if USED_API == QT_API_PYQT6:
    from PyQt6.QtMultimediaWidgets import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtMultimediaWidgets import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtMultimediaWidgets import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtMultimediaWidgets import *
    except:
        raise QtModuleNotInstalledError(name="QtMultimediaWidgets", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtMultimediaWidgets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
