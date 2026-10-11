# -*- coding: utf-8 -*-
"""
Provides Qt3DRender classes and functions.

Both import styles work with every binding:
    from ManyQt.Qt3DRender import QSomeClass        # PyQt layout (classes at module level)
    from ManyQt.Qt3DRender import Qt3DRender               # PySide layout (namespace)
    Qt3DRender.QSomeClass
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
        import PyQt5.Qt3DRender as Qt3DRender
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DRender", missing_package="PyQt3D")
    from PyQt5.Qt3DRender import *
elif USED_API == QT_API_PYQT6:
    try:
        import PyQt6.Qt3DRender as Qt3DRender
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DRender", missing_package="PyQt6-3D")
    from PyQt6.Qt3DRender import *
elif USED_API in [QT_API_PYSIDE2, QT_API_PYSIDE6]:
    try:
        if USED_API == QT_API_PYSIDE6:
            import PySide6.Qt3DRender as __temp
        else:
            import PySide2.Qt3DRender as __temp
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DRender", missing_package="PySide6-Addons or PySide6-QtAds"
                                        if USED_API == QT_API_PYSIDE6 else "PySide2")
    # Everything PySide exports, including the `Qt3DRender` namespace class itself.
    globals().update({__name: getattr(__temp, __name) for __name in dir(__temp) if not __name.startswith("_")})
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    # PySide nests the classes inside the `Qt3DRender` namespace class: also expose them at module level, like PyQt.
    # Public names only, so the module's own __doc__, __name__, ... are not overwritten.
    __namespace = getattr(__temp, "Qt3DRender")
    globals().update({__name: getattr(__namespace, __name) for __name in dir(__namespace) if not __name.startswith("_")})
    del __temp, __namespace
else:
    raise ImportError("No module named 'Qt3DRender' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
