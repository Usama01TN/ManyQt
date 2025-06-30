# -*- coding: utf-8 -*-
"""
QtVirtualKeyboard module is a wrapper for Qt Virtual Keyboard library.
It provides an easy way to use Qt Virtual Keyboard with any of the supported APIs.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE6, \
        apply_global_fixes, QtModuleNotInstalledError
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE6, \
        apply_global_fixes, QtModuleNotInstalledError

if USED_API == QT_API_PYQT4:
    # https://stackoverflow.com/questions/40360033/does-pyqt5-pyqt4-already-supports-qtvirtualkeyboard-with-handwriting-recognition
    from PyQt4.QtVirtualKeyboard import *
elif USED_API == QT_API_PYQT5:
    # https://stackoverflow.com/questions/62473386/pyqt5-show-virtual-keyboard
    from PyQt5.QtVirtualKeyboard import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtVirtualKeyboard import *
if USED_API == QT_API_PYSIDE:
    from PySide.QtVirtualKeyboard import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtVirtualKeyboard import *
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtVirtualKeyboard import *
    except:
        raise QtModuleNotInstalledError(
            name="QtVirtualKeyboard", missing_package="PySide6-Addons or PySide6-QtAds or pyside6-virtual-keyboard")
else:
    raise ImportError("No module named 'QtVirtualKeyboard' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
