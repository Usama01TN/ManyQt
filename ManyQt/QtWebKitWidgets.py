# -*- coding: utf-8 -*-
"""
QtWebKitWidgets provides a widgets for accessing web contents.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE6, \
        apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE6, \
        apply_global_fixes

# Names imported from Qt4's QtWebKit module.
__Qt4_QtWebKit = [
    'QGraphicsWebView', 'QWebFrame', 'QWebHitTestResult', 'QWebInspector', 'QWebPage', 'QWebView']  # type: list[str]
if USED_API == QT_API_PYQT4:
    from PyQt4.QtWebKit import QGraphicsWebView, QWebFrame, QWebHitTestResult, QWebInspector, QWebPage, QWebView
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtWebKitWidgets import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtWebKitWidgets import *
elif USED_API == QT_API_PYSIDE:
    from PySide.QtWebKit import QGraphicsWebView, QWebFrame, QWebHitTestResult, QWebInspector, QWebPage, QWebView
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtWebKitWidgets import *
else:
    raise ImportError("No module named 'QtWebKitWidgets' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
