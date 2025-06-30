# -*- coding: utf-8 -*-
"""
Compatibility functions.
"""
from functools import lru_cache
from os.path import dirname
from sys import path
import sys

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYQT6, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6
    from .QtCore import QObject, Property
    from .QtWidgets import QFileDialog
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYQT6, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6
    from QtCore import QObject, Property
    from QtWidgets import QFileDialog


TEXT_TYPES = (str,)  # type: tuple[type[str]]

@lru_cache(maxsize=200)
def _converter(type_):
    """
    :param type_: type, str, unicode
    :return: function
    """

    class Obj(QObject):
        """
        Obj class.
        """
        _f = None

        def _set(self, val):
            """
            :param val: any
            :return:
            """
            self._f = val

        def _get(self):
            """
            :return: any | None
            """
            return self._f

        prop = Property(type_, _get, _set)  # type: Property

    def convert(value):
        """
        :param value: any
        :return: any | None
        """
        inst = Obj()  # type: Obj
        ok = inst.setProperty('prop', value)
        return inst.property('prop') if ok else None

    return convert


def qvariant_cast(value, type_):
    """
    :param value: any
    :param type_: type, str, unicode
    :return: any
    """
    converter = _converter(type_)
    return converter(value)


def isTextString(obj):
    """
    Return True if `obj` is a text string, False if it is anything else, like binary data.
    :param obj: object
    :return: bool
    """
    return isinstance(obj, str)


def toTextString(obj, encoding=None):
    """
    Convert `obj` to (unicode) text string.
    :param obj: object
    :param encoding: str | None
    :return: str | unicode
    """
    if encoding is None:
        return str(obj)
    if isinstance(obj, str):
        # In case this function is not used properly, this could happen.
        return obj
    return str(obj, encoding)


# =============================================================================
# QVariant conversion utilities.
# =============================================================================
def to_qvariant(obj=None):  # analysis:ignore
    """
    Convert Python object to QVariant
    This is a transitional function from PyQt API#1 (QVariant exist)
    to PyQt API#2 and Pyside (QVariant does not exist).
    :param obj: QObject | None
    :return: QVariant | QObject | None
    """
    return obj


def from_qvariant(qobj=None, pytype=None):  # analysis:ignore
    """
    Convert QVariant object to Python object
    This is a transitional function from PyQt API #1 (QVariant exist)
    to PyQt API #2 and Pyside (QVariant does not exist)
    :param qobj: QVariant | None
    :param pytype: object | None
    :return: QVariant | None
    """
    return qobj


# =============================================================================
# Wrappers around QFileDialog static methods.
# =============================================================================
def getexistingdirectory(parent=None, caption="", basedir="", options=QFileDialog.ShowDirsOnly):
    """
    Wrapper around QtGui.QFileDialog.getExistingDirectory static method
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0
    :param parent: QWidget | None
    :param caption: str | unicode
    :param basedir: str | unicode
    :param options: QFileDialog.Option | QFileDialog.Options | int
    :return: str | unicode | QString
    """
    # Calling QFileDialog static method.
    if sys.platform == "win32":
        # On Windows platforms: redirect standard outputs.
        _temp1, _temp2 = sys.stdout, sys.stderr  # type: str, str
        sys.stdout, sys.stderr = None, None  # type str | None, str | None
    try:
        result = QFileDialog.getExistingDirectory(parent, caption, basedir, options)  # type: str
    finally:
        if sys.platform == "win32":
            # On Windows platforms: restore standard outputs.
            sys.stdout, sys.stderr = _temp1, _temp2  # type str, str
    if not isTextString(result):
        # PyQt API #1.
        result = toTextString(result)  # type: str
    return result


def _qfiledialogWrapper(attr, parent=None, caption="", basedir="", filters="", selectedfilter="", options=None):
    """
    :param attr: str | unicode
    :param parent: QWidget | None
    :param caption: str | unicode
    :param basedir: str | unicode
    :param filters: str | unicode
    :param selectedfilter: str | unicode
    :param options: QFileDialog.Option | QFileDialog.Options | int | None
    :return: tuple[str | unicode, str | unicode]
    """
    if options is None:
        options = QFileDialog.Option(0)  # type: QFileDialog.Option
    func = getattr(QFileDialog, attr)  # type object
    # Calling QFileDialog static method.
    if sys.platform == "win32":
        # On Windows platforms: redirect standard outputs.
        _temp1, _temp2 = sys.stdout, sys.stderr  # type str, str
        sys.stdout, sys.stderr = None, None  # type str | None, str | None
    result = func(parent, caption, basedir, filters, selectedfilter, options)  # type: str
    if sys.platform == "win32":
        # On Windows platforms: restore standard outputs.
        sys.stdout, sys.stderr = _temp1, _temp2  # type str, str
    output, selectedfilter = result  # type: str
    # Always returns the tuple (output, selectedfilter).
    return output, selectedfilter


def getopenfilename(parent=None, caption="", basedir="", filters="", selectedfilter="", options=None):
    """
    Wrapper around QtGui.QFileDialog.getOpenFileName static method
    Returns a tuple (filename, selectedfilter) -- when dialog box is canceled,
    returns a tuple of empty strings
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0
    :param parent: QWidget | None
    :param caption: str | unicode
    :param basedir: str | unicode
    :param filters: str | unicode
    :param selectedfilter: str | unicode
    :param options: QFileDialog.Option | QFileDialog.Options | int | None
    :return: tuple[str | unicode, str | unicode]
    """
    return _qfiledialogWrapper("getOpenFileName", parent=parent, caption=caption, basedir=basedir,
                               filters=filters, selectedfilter=selectedfilter, options=options)


def getopenfilenames(parent=None, caption="", basedir="", filters="", selectedfilter="", options=None):
    """
    Wrapper around QtGui.QFileDialog.getOpenFileNames static method
    Returns a tuple (filenames, selectedfilter) -- when dialog box is canceled,
    returns a tuple (empty list, empty string)
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0
    :param parent: QWidget | None
    :param caption: str | unicode
    :param basedir: str | unicode
    :param filters: str | unicode
    :param selectedfilter: str | unicode
    :param options: QFileDialog.Option | QFileDialog.Options | int | None
    :return: tuple[str | unicode, str | unicode]
    """
    return _qfiledialogWrapper("getOpenFileNames", parent=parent, caption=caption, basedir=basedir,
                               filters=filters, selectedfilter=selectedfilter, options=options)


def getsavefilename(parent=None, caption="", basedir="", filters="", selectedfilter="", options=None):
    """
    Wrapper around QtGui.QFileDialog.getSaveFileName static method
    Returns a tuple (filename, selectedfilter) -- when dialog box is canceled,
    returns a tuple of empty strings
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0
    :param parent: QWidget | None
    :param caption: str | unicode
    :param basedir: str | unicode
    :param filters: str | unicode
    :param selectedfilter: str | unicode
    :param options: QFileDialog.Option | QFileDialog.Options | int | None
    :return: tuple[str | unicode, str | unicode]
    """
    return _qfiledialogWrapper("getSaveFileName", parent=parent, caption=caption, basedir=basedir,
                               filters=filters, selectedfilter=selectedfilter, options=options)


# =============================================================================
def isalive(obj):
    """
    Wrapper around sip.isdeleted and shiboken.isValid which tests whether an object is currently alive.
    :param obj: QObject
    :return: bool | None
    """
    if USED_API in [QT_API_PYQT4, QT_API_PYQT5, QT_API_PYQT6]:
        try:
            from .sip import isdeleted
        except:
            from sip import isdeleted

        return not isdeleted(obj)
    elif USED_API in [QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6]:
        try:
            from .shiboken import isValid
        except:
            from shiboken import isValid

        return isValid(obj)
    return None
