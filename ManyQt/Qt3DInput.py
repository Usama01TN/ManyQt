# -*- coding: utf-8 -*-
"""
Provides Qt3DInput classes and functions.
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
        from PyQt5.Qt3DInput import *
    except:
        raise QtModuleNotInstalledError(name="Qt3DInput", missing_package="PyQt3D")
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.Qt3DInput import *
    except:
        raise QtModuleNotInstalledError(name="Qt3DInput", missing_package="PyQt6-3D")
elif USED_API == QT_API_PYSIDE2:
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    import PySide2.Qt3DInput as __temp
    from inspect import getmembers

    for __name in getmembers(__temp.Qt3DInput):
        globals()[__name[0]] = __name[1]
elif USED_API == QT_API_PYSIDE6:
    try:
        # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
        import PySide6.Qt3DInput as __temp
        from inspect import getmembers

        for __name in getmembers(__temp.Qt3DInput):
            globals()[__name[0]] = __name[1]
    except:
        raise QtModuleNotInstalledError(name="Qt3DInput", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'Qt3DInput' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
