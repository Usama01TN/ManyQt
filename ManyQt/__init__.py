# -*- coding: utf-8 -*-
"""
Initialize ManyQt module.
"""
from sys import version_info

__version__ = '0.3.0'  # type: str
__PREFERRED_API = None  # type: str | None
__SELECTED_API = None  # type: str | None
#: A string indicating which Qt api is used (will be `None` *until* a api is selected and commited to.
USED_API = None  # type: str | None


def setpreferredapi(api):
    """
    Set the preferred Qt API.
    Will raise a RuntimeError if a Qt API was already selected.
    Note that QT_API environment variable (if set) will take precedence.
    """
    global __PREFERRED_API
    if __SELECTED_API is not None:
        raise RuntimeError("A Qt api {} was already selected".format(__SELECTED_API))
    if api.lower() not in {"pyqt4", "pyqt5", "pyside", "pyside2", "pyside6"}:
        raise ValueError(api)
    __PREFERRED_API = api.lower()  # type: str


def selectapi(api):
    """
    Select a Qt API to use.
    This can only be set once and before any of the Qt modules are explicitly imported.
    param api: str | unicode
    :return:
    """
    global __SELECTED_API, USED_API
    if api.lower() not in {"pyqt4", "pyqt5", "pyside", "pyside2", "pyside6"}:
        raise ValueError(api)
    if __SELECTED_API is not None and __SELECTED_API.lower() != api.lower():
        raise RuntimeError("A Qt API {} was already selected".format(__SELECTED_API))
    elif __SELECTED_API is None:
        __SELECTED_API = api.lower()  # type: str
        from os.path import dirname
        from sys import path

        path.append(dirname(__file__))

        try:
            from . import _api
        except:
            import _api
        USED_API = _api.USED_API  # type: str


if version_info < (3, 4):
    from imp import find_module


    def __islocatable(name):
        """
        :type name: str | unicode
        :rtype: bool
        """
        try:
            find_module(name)
        except ImportError:
            return False
        else:
            return True
else:
    from importlib.util import find_spec


    def __islocatable(name):
        """
        :type name: str | unicode
        :rtype: bool
        """
        try:
            return find_spec(name) is not None
        except (ValueError, ImportError):
            return False


def availableapi():
    """
    Return a list of available Qt interfaces.
    :return: list[str | unicode| QString]
    """
    return [name for name in ['PyQt5', 'PyQt6', 'PyQt4', 'PySide2', 'PySide6', 'PySide'] if __islocatable(name)]
