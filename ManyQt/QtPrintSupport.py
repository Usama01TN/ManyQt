# -*- coding: utf-8 -*-
"""
QtPrintSupport module compatibility layer for multiple Qt bindings.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        apply_global_fixes

# Names imported from Qt'4 QtGui module.
__Qt4_QtGui = [
    'QAbstractPrintDialog',
    'QPageSetupDialog',
    'QPrintDialog',
    'QPrintEngine',
    'QPrintPreviewDialog',
    'QPrintPreviewWidget',
    'QPrinter',
    'QPrinterInfo'
]  # type: list[str]
if USED_API == QT_API_PYQT6:
    from PyQt6.QtPrintSupport import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtPrintSupport import *
elif USED_API == QT_API_PYQT4:
    from PyQt4.QtGui import (
        QAbstractPrintDialog,
        QPageSetupDialog,
        QPrintDialog,
        QPrintEngine,
        QPrintPreviewDialog,
        QPrintPreviewWidget,
        QPrinter,
        QPrinterInfo
    )
elif USED_API == QT_API_PYSIDE:
    from PySide.QtGui import (
        QAbstractPrintDialog,
        QPageSetupDialog,
        QPrintDialog,
        QPrintEngine,
        QPrintPreviewDialog,
        QPrintPreviewWidget,
        QPrinter,
        QPrinterInfo
    )
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtPrintSupport import *
else:
    raise ImportError("No module named 'QtPrintSupport' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
