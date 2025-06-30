# -*- coding: utf-8 -*-
"""
QtWebKit module provides access to the web pages.
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
    'QWebDatabase',
    'QWebElement',
    'QWebElementCollection',
    'QWebHistory',
    'QWebHistoryInterface',
    'QWebHistoryItem',
    'QWebPluginFactory',
    'QWebSecurityOrigin',
    'QWebSettings',
    'qWebKitMajorVersion',
    'qWebKitMinorVersion',
    'qWebKitVersion'
]  # type: list[str]
if USED_API == QT_API_PYQT6:
    from PyQt6.QtWebKit import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtWebKit import *
elif USED_API == QT_API_PYQT4:
    from PyQt4.QtWebKit import (
        QWebDatabase,
        QWebElement,
        QWebElementCollection,
        QWebHistory,
        QWebHistoryInterface,
        QWebHistoryItem,
        QWebPluginFactory,
        QWebSecurityOrigin,
        QWebSettings,
        qWebKitMajorVersion,
        qWebKitMinorVersion,
        qWebKitVersion
    )
elif USED_API == QT_API_PYSIDE:
    from PySide.QtWebKit import (
        QWebDatabase,
        QWebElement,
        QWebElementCollection,
        QWebHistory,
        QWebHistoryInterface,
        QWebHistoryItem,
        QWebPluginFactory,
        QWebSecurityOrigin,
        QWebSettings,
    )

    try:
        # Missing in current PySide 1.2.2.
        from PySide.QtWebKit import qWebKitMajorVersion, qWebKitMinorVersion, qWebKitVersion
    except ImportError:
        pass
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtWebKit import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtWebKit import *
else:
    raise ImportError("No module named 'QtWebKit' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
