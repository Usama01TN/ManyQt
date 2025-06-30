# -*- coding: utf-8 -*-
"""
Test QPDFWriter setPageSize method.
"""
from unittest import TestCase
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtGui import QPdfWriter, QPageSize
    from .ManyQt.QtCore import QBuffer, QSizeF
except:
    from ManyQt.QtGui import QPdfWriter, QPageSize
    from ManyQt.QtCore import QBuffer, QSizeF


class TestQPDFWriter(TestCase):
    """
    TestQPDFWriter class.
    """

    def test(self):
        """
        :return:
        """
        b = QBuffer()  # type: QBuffer
        w = QPdfWriter(b)  # type: QPdfWriter
        size = QPageSize(QSizeF(10, 10), QPageSize.Millimeter)  # type: QPageSize
        _ = w.setPageSize(size)  # type: bool
        self.assertTrue(w.setPageSize(size))
