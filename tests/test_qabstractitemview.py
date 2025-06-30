# -*- coding: utf-8 -*-
"""
Test QAbstractItemView.
"""
from warnings import catch_warnings
from unittest import TestCase
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtWidgets import QApplication, QTableView, QStyledItemDelegate, QStyleOptionViewItem
    from .ManyQt.QtCore import QStringListModel, QModelIndex
except:
    from ManyQt.QtWidgets import QApplication, QTableView, QStyledItemDelegate, QStyleOptionViewItem
    from ManyQt.QtCore import QStringListModel, QModelIndex


class TestQAbstractItemViewItemDelegate(TestCase):
    """
    TestQAbstractItemViewItemDelegate class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestQAbstractItemViewItemDelegate, cls).setUpClass()
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
        super(TestQAbstractItemViewItemDelegate, cls).tearDownClass()

    def testQAbstractItemViewItemDelegateForIndex(self):
        """
        :return:
        """
        view = QTableView()  # type: QTableView
        model = QStringListModel()  # type: QStringListModel
        model.setStringList(["AA", "BB"])
        view.setModel(model)
        idx1 = model.index(0, 0)  # type: QModelIndex
        idx2 = model.index(1, 0)  # type: QModelIndex
        delegate = QStyledItemDelegate()  # type: QStyledItemDelegate
        view.setItemDelegate(delegate)
        with catch_warnings(record=True):
            self.assertIs(view.itemDelegate(idx1), delegate)
            self.assertIs(view.itemDelegate(idx2), delegate)

    def testQAbstractItemViewViewOptions(self):
        """
        :return:
        """
        view = QTableView()  # type: QTableView
        with catch_warnings(record=True):
            opt1 = view.viewOptions()  # type: QStyleOptionViewItem
        self.assertIs(opt1.widget, view)
        self.assertTrue(opt1.showDecorationSelected)
        opt2 = QStyleOptionViewItem()  # type: QStyleOptionViewItem
        view.initViewItemOption(opt2)
        self.assertIs(opt2.widget, view)
        self.assertTrue(opt2.showDecorationSelected)
