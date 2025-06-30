# -*- coding: utf-8 -*-
"""
Test QAction setMenu method.
"""
from unittest import TestCase
from os.path import dirname
from weakref import ref
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtWidgets import QMenu, QApplication
    from .ManyQt.QtGui import QAction
except:
    from ManyQt.QtWidgets import QMenu, QApplication
    from ManyQt.QtGui import QAction


class TestQActionSetMenu(TestCase):
    """
    TestQActionSetMenu class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestQActionSetMenu, cls).setUpClass()
        app = QApplication.instance()  # type: QApplication
        if app is None:
            app = QApplication([])  # type: QApplication
        cls.app = app  # type: QApplication

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.app = None  # type: QApplication | None
        super(TestQActionSetMenu, cls).tearDownClass()

    def test(self):
        """
        :return:
        """
        ac = QAction(None)  # type: QAction
        menu = QMenu()  # type: QMenu
        wRef = ref(menu)  # type: QMenu
        ac.setMenu(menu)
        self.assertIs(ac.menu(), menu)
        ac.setMenu(None)
        self.assertIs(ac.menu(), None)
        menu.setParent(None)  # Parent is None but without this PySide2 fails??
        del menu
        self.assertIsNone(wRef())
