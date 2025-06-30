# -*- coding: utf-8 -*-
"""
QtHttpServer is a Python wrapper for Qt's HttpServer library.
It provides a simple HTTP server that can be used to serve files and data over the network.
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
    # https://github.com/addisonElliott/HttpServer
    from PyQt5.QtHttpServer import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtHttpServer import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtHttpServer import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtHttpServer import *
    except:
        raise QtModuleNotInstalledError(name="QtHttpServer", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtHttpServer' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
