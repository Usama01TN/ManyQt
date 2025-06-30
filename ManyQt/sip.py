# -*- coding: utf-8 -*-
"""
sip is a wrapper for the C++ library that provides Python bindings for Qt.
It also contains some helper functions and classes.
"""
from sys import modules, path
from os.path import dirname

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6

if USED_API == QT_API_PYQT5:
    try:
        from PyQt5 import sip as __sip
    except:
        import sip as __sip
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6 import sip as __sip
    except:
        import sip as __sip
elif USED_API == QT_API_PYQT4:
    try:
        from PyQt4 import sip as __sip
    except:
        import sip as __sip
elif USED_API == QT_API_PYSIDE:
    try:
        from PySide import sip as __sip
    except:
        try:
            import sip as __sip
        except:
            try:
                from . import shiboken as __sip
            except:
                import shiboken as __sip
elif USED_API == QT_API_PYSIDE2:
    try:
        from PySide2 import sip as __sip
    except:
        try:
            import sip as __sip
        except:
            import shiboken2 as __sip
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6 import sip as __sip
    except:
        try:
            import sip as __sip
        except:
            import shiboken6 as __sip
else:
    raise ImportError("ManyQt.sip")

modules["ManyQt.sip"] = __sip
