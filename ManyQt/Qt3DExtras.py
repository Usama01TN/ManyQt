# -*- coding: utf-8 -*-
"""
Provides Qt3DExtras classes and functions.

Both import styles work with every binding:
    from ManyQt.Qt3DExtras import QSomeClass        # PyQt layout (classes at module level)
    from ManyQt.Qt3DExtras import Qt3DExtras               # PySide layout (namespace)
    Qt3DExtras.QSomeClass
"""
from os.path import dirname
from sys import path


try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, QtModuleNotInstalledError, \
        apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE2, QT_API_PYSIDE6, QtModuleNotInstalledError, \
        apply_global_fixes

if USED_API == QT_API_PYQT5:
    try:
        import PyQt5.Qt3DExtras as Qt3DExtras
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PyQt3D")
    from PyQt5.Qt3DExtras import *
elif USED_API == QT_API_PYQT6:
    try:
        import PyQt6.Qt3DExtras as Qt3DExtras
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PyQt6-3D")
    from PyQt6.Qt3DExtras import *
elif USED_API in [QT_API_PYSIDE2, QT_API_PYSIDE6]:
    try:
        if USED_API == QT_API_PYSIDE6:
            import PySide6.Qt3DExtras as __temp
        else:
            import PySide2.Qt3DExtras as __temp
    except ImportError:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PySide6-Addons or PySide6-QtAds"
                                        if USED_API == QT_API_PYSIDE6 else "PySide2")
    # Everything PySide exports, including the `Qt3DExtras` namespace class itself.
    globals().update({__name: getattr(__temp, __name) for __name in dir(__temp) if not __name.startswith("_")})
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    # PySide nests the classes inside the `Qt3DExtras` namespace class: also expose them at module level, like PyQt.
    # Public names only, so the module's own __doc__, __name__, ... are not overwritten.
    __namespace = getattr(__temp, "Qt3DExtras")
    globals().update({__name: getattr(__namespace, __name) for __name in dir(__namespace) if not __name.startswith("_")})
    del __temp, __namespace
else:
    raise ImportError("No module named 'Qt3DExtras' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
