# -*- coding: utf-8 -*-
"""
shiboken module provides access to the current pyside shiboken library.
"""
from sys import modules, path
from os.path import dirname

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6

if USED_API == QT_API_PYQT4:
    try:
        from PyQt4 import sip as __shiboken
    except:
        import sip as __shiboken
elif USED_API == QT_API_PYQT5:
    try:
        from PyQt5 import sip as __shiboken
    except:
        import sip as __shiboken
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6 import sip as __shiboken
    except:
        import sip as __shiboken
elif USED_API == QT_API_PYSIDE:
    try:
        from PySide import sip as __shiboken
    except:
        try:
            import sip as __shiboken
        except:
            try:
                from . import shiboken as __shiboken
            except:
                import shiboken as __shiboken
elif USED_API == QT_API_PYSIDE2:
    try:
        from PySide2 import shiboken2 as __shiboken
    except:
        try:
            import sip as __shiboken
        except:
            import shiboken2 as __shiboken
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6 import shiboken6 as __shiboken
    except:
        try:
            import sip as __shiboken
        except:
            import shiboken6 as __shiboken
else:
    raise ImportError("ManyQt.shiboken")

modules["ManyQt.shiboken"] = __shiboken
