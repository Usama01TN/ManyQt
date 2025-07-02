# -*- coding: utf-8 -*-
"""
Test QtTest module.
"""
from unittest import TestCase
from itertools import count
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtCore import QObject, isdeleted
    from .ManyQt.QtWidgets import QApplication
    from .ManyQt.QtTest import QTest
except:
    from ManyQt.QtCore import QObject, isdeleted
    from ManyQt.QtWidgets import QApplication
    from ManyQt.QtTest import QTest


class TestQtTest(TestCase):
    """
    TestQtTest class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestQtTest, cls).setUpClass()
        app = QApplication.instance()  # type: QApplication
        if app is None:
            app = QApplication([])  # type: QApplication
        cls.app = app  # type: QApplication

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        if cls.app:
            cls.app.quit()
        cls.app = None  # type: QApplication | None
        super(TestQtTest, cls).tearDownClass()

    def testQWait(self):
        """
        :return:
        """
        obj = QObject()  # type: QObject
        obj.deleteLater()
        self.app.processEvents()  # Let deleteLater complete safely
        QTest.qWait(10)  # allow deletion
        self.assertTrue(isdeleted(obj))

    def testQWaitFor(self):
        """
        :return:
        """
        counter = count()  # type: int
        self.current = 0  # type: int

        def pred():
            """
            :return: bool
            """
            self.current = next(counter)  # type int
            return self.current > 4

        self.assertTrue(QTest.qWaitFor(pred, 100000))
        self.assertTrue(self.current == 5)
        self.assertFalse(QTest.qWaitFor(lambda: False, 10))
