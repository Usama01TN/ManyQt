# -*- coding: utf-8 -*-
"""
QtWebEngineCore module is a wrapper for QtWebEngineCore library.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE6, apply_global_fixes, \
        QtModuleNotInstalledError
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE6, apply_global_fixes, QtModuleNotInstalledError

if USED_API == QT_API_PYQT6:
    from PyQt6.QtWebEngineCore import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtWebEngineCore import *

    try:
        from PyQt5.QtWebEngineWidgets import (
            QWebEngineHistory,
            QWebEngineProfile,
            QWebEngineScript,
            QWebEngineScriptCollection,
            QWebEngineClientCertificateSelection,
            QWebEngineSettings,
            QWebEngineFullScreenRequest,
        )
    except:
        pass
elif USED_API == QT_API_PYSIDE6:
    try:
        from PySide6.QtWebEngineCore import *

        try:
            from PySide6.QtWebEngineWidgets import (
                QWebEngineHistory,
                QWebEngineProfile,
                QWebEngineScript,
                QWebEngineScriptCollection,
                QWebEngineClientCertificateSelection,
                QWebEngineSettings,
                QWebEngineFullScreenRequest,
            )
        except:
            pass
    except:
        raise QtModuleNotInstalledError(name="QtWebEngineCore", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtWebEngineCore' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
