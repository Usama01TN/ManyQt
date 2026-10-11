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
        from PySide2 import sip as __sip
    except:
        try:
            import sip as __sip
        except:
            import shiboken2 as __sip
elif USED_API == QT_API_PYSIDE6:
    try:
        from shiboken6 import Shiboken as __sip
    except:
        try:
            from PySide6 import sip as __sip
        except:
            try:
                import sip as __sip
            except:
                try:
                    import shiboken6 as __sip
                except:
                    try:
                        import PySide6.shiboken6.Shiboken as __sip
                    except:
                        import PySide6.shiboken6 as __sip
else:
    raise ImportError("ManyQt.sip")


# if hasattr(__sip, 'wrapInstance') and not hasattr(__sip, 'cast'):
#     __sip.cast = __sip.wrapInstance
# if hasattr(__sip, 'cast') and not hasattr(__sip, 'wrapInstance'):
#     __sip.wrapInstance = __sip.cast

if not hasattr(__sip, "cast"):
    def cast(obj, type_):
        """
        :param obj: QObject
        :param type_: QObject
        :return: QObject
        """
        return __sip.wrapinstance(unwrapinstance(obj), type_)


    __sip.cast = cast

# Bind the *native* implementations once. The fallbacks below are installed on the binding module itself, so
# looking them up on ``__sip`` at call time would make the wrappers call themselves (infinite recursion).
_native_getCppPointer = getattr(__sip, 'getCppPointer', None)
_native_unwrapinstance = getattr(__sip, 'unwrapinstance', None) or getattr(__sip, 'unwrapInstance', None)
_native_isdeleted = getattr(__sip, 'isdeleted', None)
_native_isValid = getattr(__sip, 'isValid', None)


def unwrapinstance(obj):
    """
    :param obj: QObject
    :return: int
    """
    if _native_getCppPointer is not None:
        return _native_getCppPointer(obj)[0]
    return _native_unwrapinstance(obj)

if not hasattr(__sip, "unwrapinstance"):
    __sip.unwrapinstance = unwrapinstance
if not hasattr(__sip, "unwrapInstance"):
    __sip.unwrapInstance = unwrapinstance
if not hasattr(__sip, "wrapinstance"):
    __sip.wrapinstance = __sip.wrapInstance
if not hasattr(__sip, "wrapInstance"):
    __sip.wrapInstance = __sip.wrapinstance


def isdeleted(obj):
    """
    :param obj: QObject
    :return: bool
    """
    if _native_isdeleted is not None:
        return _native_isdeleted(obj)
    return not _native_isValid(obj)


if not hasattr(__sip, "ispyowned"):
    __sip.ispyowned = __sip.ownedByPython
if not hasattr(__sip, "isdeleted"):
    __sip.isdeleted = isdeleted
if not hasattr(__sip, "isdelete"):
    __sip.isdelete = isdeleted
if not hasattr(__sip, "deleted"):
    __sip.deleted = isdeleted
if not hasattr(__sip, "ispycreated"):
    __sip.ispycreated = __sip.createdByPython
modules["ManyQt.sip"] = __sip
