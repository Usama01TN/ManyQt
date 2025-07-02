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
        from shiboken6 import Shiboken as __shiboken
    except:
        try:
            from PySide6 import sip as __shiboken
        except:
            try:
                import sip as __shiboken
            except:
                try:
                    import shiboken6 as __shiboken
                except:
                    try:
                        import PySide6.shiboken6.Shiboken as __shiboken
                    except:
                        import PySide6.shiboken6 as __shiboken
else:
    raise ImportError("ManyQt.shiboken")

# if hasattr(__shiboken, 'wrapInstance') and not hasattr(__shiboken, 'cast'):
#     __shiboken.cast = __shiboken.wrapInstance
# if hasattr(__shiboken, 'cast') and not hasattr(__shiboken, 'wrapInstance'):
#     __shiboken.wrapInstance = __shiboken.cast

if not hasattr(__shiboken, "cast"):
    def cast(obj, type_):
        """
        :param obj: QObject
        :param type_: QObject
        :return: QObject
        """
        return __shiboken.wrapinstance(unwrapinstance(obj), type_)


    __shiboken.cast = cast

def unwrapinstance(obj):
    """
    :param obj: QObject
    :return: QObject
    """
    if hasattr(__shiboken, 'getCppPointer'):
        addr, = __shiboken.getCppPointer(obj)
        return addr
    elif hasattr(__shiboken, 'unwrapInstance'):
        return __shiboken.unwrapInstance(obj)
    return __shiboken.unwrapinstance(obj)

if not hasattr(__shiboken, "unwrapinstance"):
    __shiboken.unwrapinstance = unwrapinstance
if not hasattr(__shiboken, "unwrapInstance"):
    __shiboken.unwrapInstance = unwrapinstance
if not hasattr(__shiboken, "wrapinstance"):
    __shiboken.wrapinstance = __shiboken.wrapInstance
if not hasattr(__shiboken, "wrapInstance"):
    __shiboken.wrapInstance = __shiboken.wrapinstance


def isdeleted(obj):
    """
    :param obj: QObject
    :return: bool
    """
    if hasattr(__shiboken, "isdeleted"):
        return __shiboken.isdeleted(obj)
    return not __shiboken.isValid(obj)


if not hasattr(__shiboken, "ispyowned"):
    __shiboken.ispyowned = __shiboken.ownedByPython
if not hasattr(__shiboken, "isdeleted"):
    __shiboken.isdeleted = isdeleted
if not hasattr(__shiboken, "isdelete"):
    __shiboken.isdelete = isdeleted
if not hasattr(__shiboken, "deleted"):
    __shiboken.deleted = isdeleted
if not hasattr(__shiboken, "delete"):
    __shiboken.delete = isdeleted
if not hasattr(__shiboken, "ispycreated"):
    __shiboken.ispycreated = __shiboken.createdByPython
modules["ManyQt.shiboken"] = __shiboken
