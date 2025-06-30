# -*- coding: utf-8 -*-
"""
QtWebEngineWidgets is a wrapper around Qt's WebEngineWidgets library.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT6:
    from PyQt6.QtWebEngineWidgets import *
    from PyQt6.QtWebEngineCore import (
        QWebEngineHistory,
        QWebEngineProfile,
        QWebEngineScript,
        QWebEngineScriptCollection,
        QWebEngineClientCertificateSelection,
        QWebEngineSettings,
        QWebEngineFullScreenRequest,
    )
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtWebEngineWidgets import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtWebEngineWidgets import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtWebEngineWidgets import *
    from PySide6.QtWebEngineCore import (
        QWebEngineHistory,
        QWebEngineProfile,
        QWebEngineScript,
        QWebEngineScriptCollection,
        QWebEngineClientCertificateSelection,
        QWebEngineSettings,
        QWebEngineFullScreenRequest,
    )
else:
    raise ImportError("No module named 'QtWebEngineWidgets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
