# -*- coding: utf-8 -*-
"""
Provides QtAxContainer classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, \
        QtModuleNotInstalledError, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, \
        QtModuleNotInstalledError, apply_global_fixes

if USED_API == QT_API_PYQT4:
    try:
        from PyQt4.QAxContainer import *
    except:
        from PyQt4.QtAxContainer import *
elif USED_API == QT_API_PYQT5:
    try:
        from PyQt5.QAxContainer import *
    except:
        from PyQt5.QtAxContainer import *
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.QAxContainer import *
    except:
        from PyQt6.QtAxContainer import *
elif USED_API == QT_API_PYSIDE:
    try:
        from PySide.QtAxContainer import *
    except:
        from PySide.QAxContainer import *
elif USED_API == QT_API_PYSIDE2:
    try:
        from PySide2.QtAxContainer import *
    except:
        from PySide2.QAxContainer import *
elif USED_API == QT_API_PYSIDE6:
    try:
        try:
            from PySide6.QtAxContainer import *
        except:
            from PySide6.QAxContainer import *
    except:
        raise QtModuleNotInstalledError(name="QAxContainer", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QAxContainer' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
