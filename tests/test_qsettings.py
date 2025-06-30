# -*- coding: utf-8 -*-
"""
Test QSettings module.
"""
from unittest import TestCase
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtCore import QSettings, QStandardPaths
except:
    from ManyQt.QtCore import QSettings, QStandardPaths


class TestQSettings(TestCase):
    """
    TestQSettings class.
    """

    def setUp(self):
        """
        :return:
        """
        super(TestQSettings, self).setUp()
        QStandardPaths.setTestModeEnabled(True)
        QSettings.setDefaultFormat(QSettings.IniFormat)

    def tearDown(self):
        """
        :return:
        """
        QStandardPaths.setTestModeEnabled(False)
        QSettings.setDefaultFormat(QSettings.NativeFormat)
        super(TestQSettings, self).tearDown()

    def testQsettings(self):
        """
        :return:
        """
        s = QSettings()  # type: QSettings
        s.setValue("one", 1)
        s.setValue("one-half", 0.5)
        s.setValue("empty", "")
        s.setValue("true", True)
        s.sync()
        del s
        s = QSettings()  # type: QSettings
        self.assertEqual(s.value("one", type=int), 1)
        self.assertEqual(s.value("one-half", type=float), 0.5)
        self.assertEqual(s.value("empty", type=str), "")
        self.assertEqual(s.value("true", type=bool), True)
