# -*- coding: utf-8 -*-
"""
_ctypes is a module that provides some helper functions to deal with the loading of Qt libraries using ctypes.
"""
from sysconfig import get_config_vars
from os.path import dirname, join
from sys import path, platform
from itertools import chain
from ctypes import cdll
from glob import iglob

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from .QtCore import QLibraryInfo, QT_VERSION
except:
    from QtCore import QLibraryInfo, QT_VERSION


def shlib_ext():
    """
    Return possible platform shared library extension.
    """
    extensions = []  # type: list[str]
    if platform == "win32":
        extensions += [".dll"]  # type: list[str]
    elif platform == "darwin":
        extensions += ["", ".dylib"]  # type: list[str]
    else:
        extensions += [".so"]  # type: list[str]
    confv = get_config_vars()  # type dict[str, any]
    soExt = confv.get("SO", None)  # type: str | None
    if soExt is not None and soExt not in extensions:
        extensions += [soExt]  # type: list[str]
    return extensions


#
# NOTE: posix dlsym resolves references over linked libs
# `LoadLibrary(QtGui.__file__)` is sufficient. Windows?
# No. Only referenced lib is searched (LoadLibrary and GetProcAddress).
# But LoadLibrary("Qt5Gui.dll") might just do the trick.
#


def find_library(name, path):
    """
    :param name: (str | unicode | QString) name of the library.
    :param path: (str | unicode | QString) path to the library.
    :return: (iter[str | unicode | QString]) path to the library.
    """
    if platform == "darwin":
        test = [
            name,
            name + ".so",
            name + ".dylib"
                   "{name}.framework/{name}".format(name=name),
            "{name}.framework/Versions/Current/{name}".format(name=name),
            "{name}.framework/Versions/*/{name}".format(name=name),
        ]  # type: list[str]
    elif platform == "win32":
        test = [name, name + ".dll"]  # type: list[str]
    else:
        test = [
            name,
            name + ".so",
            "lib{name}.so".format(name=name),
            "lib{name}.so.*".format(name=name)
        ]  # type: list[str]
    for suffix in test:
        # yield from iglob(join(path, suffix))
        for m in iglob(join(path, suffix)):
            yield m
        # try:
        #     return next(iglob(join(path, suffix)))
        # except StopIteration:
        #     pass


def find_qtlib(name):
    """
    :param name: str | unicode
    :return: iter[str | unicode]
    """
    qtlibpath = QLibraryInfo.path(QLibraryInfo.LibrariesPath)  # type: str
    major_version = (QT_VERSION >> 16)  # type: int
    paths = find_library(name, qtlibpath)
    name_extra = 'Qt5'  # type: str
    if name.startswith("Qt"):
        # common case for Qt builds on windows
        name_extra = "Qt{}{}".format(major_version, name[2:])  # type: str
        extra = find_library(name_extra, qtlibpath)
    else:
        extra = []
    # return chain(paths, extra, (name, *((name_extra,) if extra else ())))
    return chain(paths, extra, (name,) + ((name_extra,) if extra else ()))


def load_qtlib(name):
    """
    :param name: str | unicode
    :return: CDLL | None
    """
    for pth in find_qtlib(name):
        try:
            return cdll.LoadLibrary(pth)
        except OSError:
            pass
    return None
