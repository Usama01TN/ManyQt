# -*- coding: utf-8 -*-
"""
QtWebView is a wrapper for Qt's web view widgets. It provides a unified interface to all supported APIs.
It also includes some fixes and workarounds.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT4:
    try:
        try:
            from PyQt4.QtWebKit import *
        except:
            from PyQt4.QtWebKitWidgets import *
    except:
        try:
            from PyQt4.QWebView import *
        except:
            from PyQt4.QtWebView import *
elif USED_API == QT_API_PYQT5:
    try:
        try:
            from PyQt5.QtWebKit import *
        except:
            from PyQt5.QtWebKitWidgets import *
    except:
        try:
            from PyQt5.QWebView import *
        except:
            try:
                from PyQt5.QtWebView import *
            except:
                try:
                    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage as QWebPage
                    from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
                except:
                    raise QtModuleNotInstalledError(name="QtWebView", missing_package="PyQtWebKit or PyQtWebEngine")
elif USED_API == QT_API_PYQT6:
    try:
        try:
            from PyQt6.QtWebKit import *
        except:
            from PyQt6.QtWebKitWidgets import *
    except:
        try:
            from PyQt6.QWebView import *
        except:
            from PyQt6.QtWebView import *
elif USED_API == QT_API_PYSIDE:
    try:
        from PySide.QtWebView import *
    except:
        try:
            from PySide.QWebView import *
        except:
            try:
                from PySide.QtWebKit import *
            except:
                from PySide.QtWebKitWidgets import *
elif USED_API == QT_API_PYSIDE2:
    try:
        from PySide2.QtWebView import *
    except:
        try:
            from PySide2.QWebView import *
        except:
            try:
                from PySide2.QtWebKit import *
            except:
                from PySide2.QtWebKitWidgets import *
elif USED_API == QT_API_PYSIDE6:
    try:
        try:
            from PySide6.QtWebView import *
        except:
            try:
                from PySide6.QWebView import *
            except:
                try:
                    from PySide6.QtWebKit import *
                except:
                    from PySide6.QtWebKitWidgets import *
    except:
        raise QtModuleNotInstalledError(name="QtWebView", missing_package="PySide6-Addons or PySide6-QtAds")
else:
    raise ImportError("No module named 'QtWebView' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
