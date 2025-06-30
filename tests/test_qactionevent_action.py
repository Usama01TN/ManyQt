# -*- coding: utf-8 -*-
"""
Test QActionEvent action.
"""
from unittest import TestCase
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtWidgets import QWidget, QApplication
    from .ManyQt.QtGui import QAction
except:
    from ManyQt.QtWidgets import QWidget, QApplication
    from ManyQt.QtGui import QAction


class TestQActionEvent_action(TestCase):
    """
    TestQActionEvent_action class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestQActionEvent_action, cls).setUpClass()
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
        super(TestQActionEvent_action, cls).tearDownClass()

    def testAction(self):
        """
        :return:
        """
        a = QAction(None)  # type: QAction
        b = QAction(None)  # type: QAction

        class Widget(QWidget):
            """
            Widget class.
            """

            def test(self, event):
                """
                :param event: QEvent
                :return:
                """

            def actionEvent(self, event):
                """
                :param event: QActionEvent
                :return:
                """
                super(Widget, self).actionEvent(event)
                self.test(event)

        widget = Widget()  # type: Widget

        def test(ev):
            """
            :param ev: QEvent
            :return:
            """
            assert ev.action() is b

        widget.test = test
        widget.addAction(b)

        def test(ev):
            """
            :param ev: QEvent
            :return:
            """
            assert ev.action() is a
            assert ev.before() is b

        widget.test = test
        widget.insertAction(b, a)
        del widget.test
