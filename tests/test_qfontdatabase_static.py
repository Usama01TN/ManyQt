# -*- coding: utf-8 -*-
"""
Test QFontDatabase static.
"""
from unittest import TestCase
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtWidgets import QApplication
    from .ManyQt.QtGui import QFontDatabase
except:
    from ManyQt.QtWidgets import QApplication
    from ManyQt.QtGui import QFontDatabase


class TestQFontDatabase(TestCase):
    """
    TestQFontDatabase class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestQFontDatabase, cls).setUpClass()
        app = QApplication.instance()  # type: QApplication
        if app is None:
            app = QApplication([])  # type: QApplication
        cls.app = app  # type: QApplication

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        # cls.app = None  # type: QApplication | None
        super(TestQFontDatabase, cls).tearDownClass()

    def testQFontDataBaseStatic(self):
        """
        :return:
        """
        families = QFontDatabase.families()  # type: list[str]
        styles = QFontDatabase.styles(families[0])  # type: list[str]
        systems = QFontDatabase.writingSystems()  # type: list[str]
        systems = QFontDatabase.writingSystems(families[0])  # type: list[str]
