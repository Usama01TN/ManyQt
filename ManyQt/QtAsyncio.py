# -*- coding: utf-8 -*-
"""
QtAsyncio is a Python package that provides asyncio support for Qt applications.
It allows you to use async/await syntax with Qt's event loop and signals/slots mechanism.
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
        from PyQt5.QtAsyncio import *
    except:
        raise QtModuleNotInstalledError(name="QtAsyncio", missing_package="qasync or qt-async-threads")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.QtAsyncio import *
    except:
        raise QtModuleNotInstalledError(name="QtAsyncio", missing_package="qasync or qt-async-threads")
elif USED_API == QT_API_PYSIDE2:
    try:
        from PySide2.QtAsyncio import *
    except:
        raise QtModuleNotInstalledError(name="QtAsyncio", missing_package="qasync or qt-async-threads")
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtAsyncio import *
    except:
        raise QtModuleNotInstalledError(
            name="QtAsyncio", missing_package="PySide6-Addons or PySide6-QtAds or qt-async-threads")
else:
    raise ImportError("No module named 'QtAsyncio' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
