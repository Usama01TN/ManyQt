# -*- coding: utf-8 -*-
"""
Every ManyQt module whose Qt module exists in the selected binding must import, and must expose what the
binding exposes (regression test for Qt3D namespaces, QtPrintSupport, QtWebChannel, QtAsyncio.run, ...).
"""
from importlib import import_module
from unittest import TestCase, skipUnless

from ManyQt._api import USED_API, QT_API_PYSIDE6

QT3D_MODULES = ["Qt3DAnimation", "Qt3DCore", "Qt3DExtras", "Qt3DInput", "Qt3DLogic", "Qt3DRender"]  # type: list[str]
SIMPLE_MODULES = ["QtPrintSupport", "QtWebChannel", "QtWebEngineWidgets", "QtAsyncio"]  # type: list[str]


def _binding_module(name):
    """
    :param name: str
    :return: module | None
    """
    try:
        return import_module("PySide6." + name)
    except ImportError:
        return None


@skipUnless(USED_API == QT_API_PYSIDE6, "PySide6 only")
class TestModuleWrappers(TestCase):
    """
    TestModuleWrappers class.
    """

    def testQt3DNamespaces(self):
        """
        `from ManyQt.Qt3DCore import Qt3DCore` (PySide layout) and `from ManyQt.Qt3DCore import QEntity`
        (PyQt layout) must both work.
        :return:
        """
        for name in QT3D_MODULES:
            original = _binding_module(name)
            if original is None:
                continue
            wrapper = import_module("ManyQt." + name)
            namespace = getattr(original, name)
            self.assertIs(getattr(wrapper, name), namespace, name)
            for member in dir(namespace):
                if not member.startswith("_"):
                    self.assertIs(getattr(wrapper, member), getattr(namespace, member), name + "." + member)
            self.assertTrue(wrapper.__doc__.strip().startswith("Provides " + name), name + ".__doc__ clobbered")

    def testModulesImport(self):
        """
        :return:
        """
        for name in SIMPLE_MODULES:
            original = _binding_module(name)
            if original is None:
                continue
            wrapper = import_module("ManyQt." + name)
            for member in getattr(original, "__all__", None) or [n for n in dir(original) if not n.startswith("_")]:
                self.assertTrue(hasattr(wrapper, member), name + "." + member)

    def testQtAsyncioRun(self):
        """
        :return:
        """
        if _binding_module("QtAsyncio") is not None:
            self.assertTrue(callable(import_module("ManyQt.QtAsyncio").run))
