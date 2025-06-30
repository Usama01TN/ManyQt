# -*- coding: utf-8 -*-
"""
Test exports modules.
"""
from unittest import TestCase


class TestExports(TestCase):
    """
    TestExports class.
    """
    names = [
        "ManyQt.QtCore:Signal",
        "ManyQt.QtCore:Slot",
        "ManyQt.QtCore:Property",
        "ManyQt.QtGui:QUndoCommand",
        "ManyQt.QtGui:QUndoGroup",
        "ManyQt.QtGui:QUndoStack",
        "ManyQt.QtGui:QShortcut",
        "ManyQt.QtGui:QAction",
        "ManyQt.QtGui:QActionGroup",
        "ManyQt.QtGui:QFileSystemModel",
    ]  # type: list[str]

    def testExports(self):
        """
        :return:
        """
        for name in self.names:
            pkg, _, item = name.rpartition(":")  # type: str, str, str
            getattr(__import__(pkg, fromlist=[item]), item)
