# -*- coding: utf-8 -*-
"""
import hooks is used to intercept the import of Qt modules in order to provide a backporting mechanism for PySide users.
"""
from importlib.abc import MetaPathFinder, Loader
from importlib.util import spec_from_loader
from sys import meta_path, path
from warnings import warn
from os.path import dirname

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE


class _FinderLoader(MetaPathFinder, Loader):
    """
    _FinderLoader class.
    """


class ImportHookBackport(_FinderLoader):
    """
    A python import hook (PEP-302) substituting Qt4 module imports, replacing them with a back compatible shim.
    """

    def __init__(self, whichapi):
        """
        :param whichapi: str | unicode
        """
        self.whichapi = whichapi  # type: str

    def find_spec(self, fullname, pth=None, target=None):
        """
        :param fullname: str | unicode
        :param pth: list[str | unicode] | None
        :param target: object | None
        :return: ModuleSpec | None
        """
        if USED_API != QT_API_PYQT5:
            return
        toplevel = fullname.split(".", 1)[0]  # type: str
        if toplevel == "PyQt4" and self.whichapi == QT_API_PYQT4:
            return spec_from_loader(fullname, self)
        elif toplevel == "PySide" and self.whichapi == QT_API_PYSIDE:
            return spec_from_loader(fullname, self)
        return

    def create_module(self, spec):
        """
        :param spec: ModuleSpec
        :return: ModuleType
        """
        pkgpath = spec.name.split(".")  # type: list[str]
        toplevel = pkgpath[0]  # type: str
        subpkg = pkgpath[1] if len(pkgpath) > 1 else None  # type: str | None
        assert toplevel.lower() == self.whichapi
        backportpkg = "ManyQt._backport"  # type: str
        if subpkg is not None:
            backportpkg += "." + subpkg  # type: str
        module = __import__(backportpkg, fromlist=["_"])
        warn("Loaded module {} as a substitute for {}".format(module.__name__, spec.name),
             RuntimeWarning, stacklevel=2)
        return module

    def exec_module(self, module):
        """
        :param module: ModuleType
        :return: ModuleType
        """
        return module


class ImportHookDeny(_FinderLoader):
    """
    A python import hook (PEP-302) preventing imports of a Qt api.

    Parameters
    ----------
    whichapi : str
        The Qt api whose import should be prevented.
    """

    def __init__(self, whichapi):
        """
        :param whichapi: str | unicode
        """
        self.whichapi = whichapi  # type: str

    def find_spec(self, fullname, pth=None, target=None):
        """
        :param fullname: str | unicode
        :param pth: list[str | unicode] | None
        :param target: object | None
        :return: ModuleSpec | None
        """
        toplevel = fullname.split(".")[0]  # type: str
        if self.whichapi == QT_API_PYQT5 and toplevel == "PyQt5" or \
                self.whichapi == QT_API_PYQT4 and toplevel == "PyQt4" or \
                self.whichapi == QT_API_PYSIDE and toplevel == "PySide":
            return spec_from_loader(fullname, self)
        return None

    def create_module(self, spec):
        """
        :param spec: ModuleSpec
        :return:
        """
        raise ImportError("Import of {} is denied.".format(spec.name))

    def exec_module(self, module):
        """
        :param module: ModuleType
        :return:
        """
        raise ImportError


def install_backport_hook(api):
    """
    Install a backport import hook for Qt4 api

    Parameters
    ----------
    api : str
        The Qt4 api whose structure should be intercepted
        ('pyqt4' or 'pyside').

    Example
    -------
    >>> install_backport_hook("pyqt4")
    >>> import PyQt4
    Loaded module ManyQt._backport as a substitute for PyQt4
    """
    if api == USED_API:
        raise ValueError
    meta_path.insert(0, ImportHookBackport(api))


def install_deny_hook(api):
    """
    Install a deny import hook for Qt api.

    Parameters
    ----------
    api : str
        The Qt api whose import should be prevented

    Example
    -------
    >>> install_deny_import("pyqt4")
    >>> import PyQt4
    Traceback (most recent call last):...
    ImportError: Import of PyQt4 is denied.
    """
    if api == USED_API:
        raise ValueError
    meta_path.insert(0, ImportHookDeny(api))
