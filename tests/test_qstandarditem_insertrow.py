# -*- coding: utf-8 -*-
"""
Test QStandardItem module.
"""
from unittest import TestCase
from os.path import dirname
from gc import collect
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtGui import QStandardItem, QStandardItemModel
except:
    from ManyQt.QtGui import QStandardItem, QStandardItemModel


class TestQStandardItem(TestCase):
    """
    TestQStandardItem class.
    """

    def test(self):
        """
        :return:
        """
        model = QStandardItemModel()  # type: QStandardItemModel
        itemParent = QStandardItem("parent")  # type: QStandardItem
        itemChild = QStandardItem("child")  # type: QStandardItem
        model.insertRow(0, itemParent)
        itemParent.insertRow(0, itemChild)
        self.assertEqual(model.index(0, 0).data(), "parent")
        self.assertEqual(model.index(0, 0, model.index(0, 0)).data(), "child")
        del itemChild
        del itemParent
        collect()
        self.assertEqual(model.index(0, 0).data(), "parent")
        self.assertEqual(model.index(0, 0, model.index(0, 0)).data(), "child")
