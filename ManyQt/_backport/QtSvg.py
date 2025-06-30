# -*- coding: utf-8 -*-
"""
QtMultimedia module provides classes for multimedia functionality.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .._api import USED_API, QT_API_PYQT5
except:
    try:
        from ._api import USED_API, QT_API_PYQT5
    except:
        from _api import USED_API, QT_API_PYQT5

assert USED_API == QT_API_PYQT5
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgGenerator, QSvgRenderer, QSvgWidget
