# -*- coding: utf-8 -*-
"""
Calls undefined methods from qt libraries.

The real implementation lives in ``_native_helpers`` and needs ``ctypes`` plus the native Qt libraries. It is
imported only when one of these helpers is actually called, so that ``import ManyQt.QtWidgets`` stays free of
ctypes / native-library side effects (like qtpy). Such side effects at import time are a known cause of
"Segmentation fault" when the QApplication is created on Android (Pydroid 3).
"""

__all__ = [
    "qt_blurImage", "qt_halfScaled", "qScrollEffect", "qt_graphicsItemHighlightSelected", "qGeomCalc",
    "qFadeEffect", "qDrawBorderPixmap", "qDrawPlainRect", "qDrawPlainRect2", "qDrawShadeLine", "qDrawShadeLine2",
    "qDrawShadePanel", "qDrawShadePanel2", "qDrawShadeRect", "qDrawShadeRect2", "qDrawWinButton", "qDrawWinButton2",
    "qDrawWinPanel", "qDrawWinPanel2",
]  # type: list[str]


def _native():
    """
    :return: module
    """
    try:
        from . import _native_helpers
    except ImportError:
        from ManyQt import _native_helpers
    return _native_helpers


def _lazy(name):
    """
    :param name: str
    :return: function
    """

    def helper(*args, **kwargs):
        """
        :param args: any
        :param kwargs: any
        :return: any
        """
        return getattr(_native(), name)(*args, **kwargs)

    helper.__name__ = name
    helper.__doc__ = "Lazy wrapper around ManyQt._native_helpers.{}.".format(name)
    return helper


for __name in __all__:
    globals()[__name] = _lazy(__name)
del __name


def __getattr__(name):
    """
    Lazy access to the remaining names (e.g. QLayoutStruct), Python >= 3.7.
    :param name: str
    :return: any
    """
    if name.startswith("__"):
        raise AttributeError(name)
    return getattr(_native(), name)
