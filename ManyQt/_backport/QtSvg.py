# -*- coding: utf-8 -*-
"""
QtMultimedia module provides classes for multimedia functionality.
"""
from os.path import dirname
from sys import path


try:
    from .._api import USED_API, QT_API_PYQT5
except:
    try:
        from ._api import USED_API, QT_API_PYQT5
    except:
        from _api import USED_API, QT_API_PYQT5

assert USED_API == QT_API_PYQT5
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgGenerator, QSvgRenderer, QSvgWidget
