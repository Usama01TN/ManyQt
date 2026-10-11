# -*- coding: utf-8 -*-
"""
sip is a wrapper for the C++ library that provides Python bindings for Qt.
It also contains some helper functions and classes.
"""
from sys import modules, path
from os.path import dirname


try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6

if USED_API == QT_API_PYQT4:
    try:
        from PyQt4 import sip as __sip
    except:
        import sip as __sip
elif USED_API == QT_API_PYQT5:
    try:
        from PyQt5 import sip as __sip
    except:
        import sip as __sip
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6 import sip as __sip
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
        from PySide2 import shiboken2 as __sip
    except ImportError:
        import shiboken2 as __sip
elif USED_API == QT_API_PYSIDE6:
    # Never fall back to ``sip`` here: a PyQt sip used on PySide6 objects can crash the interpreter.
    try:
        from shiboken6 import Shiboken as __sip
    except ImportError:
        import shiboken6 as __sip
else:
    raise ImportError("ManyQt.sip")


# Like qtpy (``from shiboken6 import *``): re-export the binding's helper module, then add ManyQt's aliases
# to *this* module only. The binding's C module itself is never modified.
globals().update({__n: getattr(__sip, __n) for __n in dir(__sip) if not __n.startswith("_")})
_native_getCppPointer = getattr(__sip, "getCppPointer", None)
_native_unwrapinstance = getattr(__sip, "unwrapinstance", None) or getattr(__sip, "unwrapInstance", None)
_native_wrapinstance = getattr(__sip, "wrapinstance", None) or getattr(__sip, "wrapInstance", None)
_native_isdeleted = getattr(__sip, "isdeleted", None)
_native_isValid = getattr(__sip, "isValid", None)


def _unwrapinstance(obj):
    """
    :param obj: QObject
    :return: int
    """
    if _native_getCppPointer is not None:
        return _native_getCppPointer(obj)[0]
    return _native_unwrapinstance(obj)


def _isdeleted(obj):
    """
    :param obj: QObject
    :return: bool
    """
    if _native_isdeleted is not None:
        return _native_isdeleted(obj)
    return not _native_isValid(obj)


def _cast(obj, type_):
    """
    :param obj: QObject
    :param type_: QObject
    :return: QObject
    """
    return _native_wrapinstance(_unwrapinstance(obj), type_)


# Native implementations win; ManyQt's fallbacks only fill the gaps.
for __alias, __fallback in (
        ("cast", _cast),
        ("unwrapinstance", _unwrapinstance),
        ("unwrapInstance", _unwrapinstance),
        ("wrapinstance", _native_wrapinstance),
        ("wrapInstance", _native_wrapinstance),
        ("isdeleted", _isdeleted),
        ("isdelete", _isdeleted),
        ("deleted", _isdeleted),
        ("ispyowned", getattr(__sip, "ownedByPython", None)),
        ("ispycreated", getattr(__sip, "createdByPython", None)),
):
    if not hasattr(__sip, __alias) and __fallback is not None:
        globals()[__alias] = __fallback
del __alias, __fallback
