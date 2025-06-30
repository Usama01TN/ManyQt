# -*- coding: utf-8 -*-
"""
Provides Qt3DExtras classes and functions.
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
        from PyQt5.Qt3DExtras import *
    except:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PyQt3D")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.Qt3DExtras import *
    except:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PyQt6-3D")
elif USED_API == QT_API_PYSIDE2:
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    from inspect import getmembers
    import PySide2.Qt3DExtras as __temp

    for __name in getmembers(__temp.Qt3DExtras):
        globals()[__name[0]] = __name[1]
elif USED_API == QT_API_PYSIDE6:
    try:
        # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
        from inspect import getmembers
        import PySide6.Qt3DExtras as __temp

        for __name in getmembers(__temp.Qt3DExtras):
            globals()[__name[0]] = __name[1]
    except:
        raise QtModuleNotInstalledError(name="Qt3DExtras", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'Qt3DExtras' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
