# -*- coding: utf-8 -*-
"""
shiboken module provides access to the current pyside shiboken library.
"""
from sys import modules, path
from os.path import dirname


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
    except ImportError:
        import shiboken2 as __shiboken
elif USED_API == QT_API_PYSIDE6:
    # Never fall back to ``sip`` here: a PyQt sip used on PySide6 objects can crash the interpreter.
    try:
        from shiboken6 import Shiboken as __shiboken
    except ImportError:
        import shiboken6 as __shiboken
else:
    raise ImportError("ManyQt.shiboken")

# Like qtpy (``from shiboken6 import *``): re-export the binding's helper module, then add ManyQt's aliases
# to *this* module only. The binding's C module itself is never modified.
globals().update({__n: getattr(__shiboken, __n) for __n in dir(__shiboken) if not __n.startswith("_")})
_native_getCppPointer = getattr(__shiboken, "getCppPointer", None)
_native_unwrapinstance = getattr(__shiboken, "unwrapinstance", None) or getattr(__shiboken, "unwrapInstance", None)
_native_wrapinstance = getattr(__shiboken, "wrapinstance", None) or getattr(__shiboken, "wrapInstance", None)
_native_isdeleted = getattr(__shiboken, "isdeleted", None)
_native_isValid = getattr(__shiboken, "isValid", None)


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
        ("ispyowned", getattr(__shiboken, "ownedByPython", None)),
        ("ispycreated", getattr(__shiboken, "createdByPython", None)),
):
    if not hasattr(__shiboken, __alias) and __fallback is not None:
        globals()[__alias] = __fallback
del __alias, __fallback
