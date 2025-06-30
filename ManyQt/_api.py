# -*- coding: utf-8 -*-
"""
NOTE: Importing this module will select and commit to a Qt API.
"""
from sys import version_info, modules, path
from os.path import dirname
from warnings import warn
from os import environ

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from . import ManyQt
except:
    import ManyQt

if version_info < (3,):
    _intern = intern
else:
    from sys import intern

    _intern = intern

USED_API = ManyQt.USED_API  # type: str | None
QT_API_PYQT6 = "pyqt6"  # type: str
QT_API_PYQT5 = "pyqt5"  # type: str
QT_API_PYQT4 = "pyqt4"  # type: str
QT_API_PYSIDE6 = "pyside6"  # type: str
QT_API_PYSIDE2 = "pyside2"  # type: str
QT_API_PYSIDE = "pyside"  # type: str
ALL_APIS = [QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE6, QT_API_PYSIDE2, QT_API_PYSIDE]  # type: list[str]


def comittoapi(api):
    """
    Commit to the use of specified Qt api.
    Raise an error if another Qt api is already loaded in modules
    :param api: str | unicode
    :return:
    """
    global USED_API
    assert USED_API is None, "committoapi called again!"
    assert api in ALL_APIS
    for n in ["PyQt4", "PyQt5", "PyQt6", "PySide", "PySide2", "PySide6"]:
        if n.lower() != api and n in modules:
            raise RuntimeError("{} was already imported. Cannot commit to {}!".format(n, api))
    else:
        api = _intern(api)  # type: str
        USED_API = api  # type: str
        ManyQt.__SELECTED_API = api
        ManyQt.USED_API = api


if ManyQt.__SELECTED_API is not None:
    comittoapi(ManyQt.__SELECTED_API)
elif "QT_API" in environ:
    api = environ["QT_API"].lower()  # type: str
    if api == "pyqt":
        # Qt.py allows both pyqt4 and pyqt to specify PyQt4.
        # When run from anaconda-navigator, pyqt is used.
        api = "pyqt4"  # type: str
    if api in ALL_APIS:
        comittoapi(api)
    else:
        warn("'QT_API' environment variable names an unknown Qt API ('{}').".format(environ["QT_API"]), RuntimeWarning,
             stacklevel=3)
        # Pass through.

if USED_API is None:
    # Check modules for existing imports.
    __existing = None  # type: str | None
    if "PyQt6" in modules:
        __existing = QT_API_PYQT6  # type: str
    elif "PyQt5" in modules:
        __existing = QT_API_PYQT5  # type: str
    elif "PyQt4" in modules:
        __existing = QT_API_PYQT4  # type: str
    elif "PySide6" in modules:
        __existing = QT_API_PYSIDE6  # type: str
    elif "PySide2" in modules:
        __existing = QT_API_PYSIDE2  # type: str
    elif "PySide" in modules:
        __existing = QT_API_PYSIDE  # type: str
    if __existing is not None:
        comittoapi(__existing)
    else:
        available = ManyQt.availableapi()  # type: list[str]
        __available = None  # type: str
        if ManyQt.__PREFERRED_API is not None and ManyQt.__PREFERRED_API.lower() in [
            name.lower() for name in available]:
            __available = ManyQt.__PREFERRED_API.lower()  # type: str
        elif "PyQt5" in available:
            __available = QT_API_PYQT5  # type: str
        elif "PyQt4" in available:
            __available = QT_API_PYQT4  # type: str
        elif "PySide6" in available:
            __available = QT_API_PYSIDE6  # type: str
        elif "PySide" in available:
            __available = QT_API_PYSIDE  # type: str
        elif "PySide2" in available:
            __available = QT_API_PYSIDE2  # type: str
        elif "PyQt6" in available:
            __available = QT_API_PYQT6  # type: str
        if __available is not None:
            comittoapi(__available)
        del __available
    del __existing
if USED_API is None:
    raise ImportError("PyQt4, PyQt5, PySide or PySide2 are not available for import")
if "MANYQT_HOOK_DENY" in environ:
    try:
        from .importhooks import install_deny_hook
    except:
        from importhooks import install_deny_hook

    for __denyapi in environ["MANYQT_HOOK_DENY"].split(","):
        if __denyapi.lower() != USED_API:
            install_deny_hook(__denyapi.lower())
    del install_deny_hook
if "MANYQT_HOOK_BACKPORT" in environ:
    try:
        from .importhooks import install_backport_hook
    except:
        from importhooks import install_backport_hook

    for __backportapi in environ["MANYQT_HOOK_BACKPORT"].split(","):
        if __backportapi.lower() != USED_API:
            install_backport_hook(__backportapi.lower())
    del install_backport_hook

try:
    from ._fixes import global_fixes as apply_global_fixes
except:
    from _fixes import global_fixes as apply_global_fixes


class PythonQtError(RuntimeError):
    """
    Generic error superclass.
    """


class PythonQtWarning(RuntimeWarning):
    """
    Warning class.
    """


class PythonQtValueError(ValueError):
    """
    Error raised if an invalid QT_API is specified.
    """


class QtBindingsNotFoundError(PythonQtError, ImportError):
    """
    Error raised if no bindings could be selected.
    """
    _msg = "No Qt bindings could be found"  # type: str

    def __init__(self):
        super(QtBindingsNotFoundError, self).__init__(self._msg)


class QtModuleNotFoundError(ImportError, PythonQtError):
    """
    Raised when a Python Qt binding submodule is not installed/supported.
    """
    _msg = "The {name} module was not found."  # type: str
    _msg_binding = "{binding}"  # type: str
    _msg_extra = ""  # type: str

    def __init__(self, name, msg=None, **msg_kwargs):
        """
        :param name: str | unicode
        :param msg: str | unicode | None
        :param msg_kwargs: any
        """
        global USED_API
        binding = self._msg_binding.format(binding=USED_API)  # type: str
        msg = msg or "{} {}".format(self._msg, self._msg_extra).strip()  # type: str
        super(QtModuleNotFoundError, self).__init__(msg.format(name=name, binding=binding, **msg_kwargs), name=name)


class QtModuleNotInstalledError(QtModuleNotFoundError):
    """
    Raise when a module is supported by the binding, but not installed.
    """
    _msg_extra = "It must be installed separately"  # type: str

    def __init__(self, missing_package=None, **superclass_kwargs):
        """
        :param missing_package: str | unicode | None
        :param superclass_kwargs: any
        """
        self.missing_package = missing_package  # type: str
        if missing_package is not None:
            self._msg_extra += " as {missing_package}."  # type: str
        super(QtModuleNotInstalledError, self).__init__(missing_package=missing_package, **superclass_kwargs)
