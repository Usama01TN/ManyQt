# -*- coding: utf-8 -*-
"""
uic is a backport of uic from PyQt5 to support older versions of PyQt.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2,\
            QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes


if USED_API == QT_API_PYQT5:
    from PyQt5.QtCore import QFile
    from PyQt5.uic import *

    QUiLoader = loadUi
    QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
elif USED_API == QT_API_PYQT6:
    try:
        from PyQt6.uic import *

        QUiLoader = loadUi
        QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
    except:
        from PyQt6.QtUiTools import *

        loadUi = QUiLoader().load
elif USED_API == QT_API_PYQT4:
    from PyQt4.uic import *

    QUiLoader = loadUi
    QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
elif USED_API == QT_API_PYSIDE:
    # This will fail with an ImportError (as it should).
    try:
        from PySide.uic import *

        QUiLoader = loadUi
        QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
    except:
        from PySide.QtUiTools import *

        loadUi = QUiLoader().load
elif USED_API == QT_API_PYSIDE2:
    # This will fail with an ImportError (as it should).
    try:
        from PySide2.uic import *

        QUiLoader = loadUi
        QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
    except:
        from PySide2.QtUiTools import *

        loadUi = QUiLoader().load
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.uic import *

        QUiLoader = loadUi
        QUiLoader.load = lambda f, *args, **kwargs: loadUi(f.fileName() if isinstance(f, QFile) else f, *args, **kwargs)
    except:
        from PySide6.QtUiTools import *

        loadUi = QUiLoader().load
else:
    raise ImportError("No module named 'uic' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
