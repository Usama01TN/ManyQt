# -*- coding: utf-8 -*-
"""
Test Draw Pixmap Fragments.
"""
from unittest import TestCase, skipIf
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtGui import QPainter, QPixmap, QImage, QColor
    from .ManyQt.QtCore import Qt, QPointF, QRectF
    from .ManyQt.QtWidgets import QApplication
    from .ManyQt import USED_API
except:
    from ManyQt.QtGui import QPainter, QPixmap, QImage, QColor
    from ManyQt.QtCore import Qt, QPointF, QRectF
    from ManyQt.QtWidgets import QApplication
    from ManyQt import USED_API


class TestDrawPixmapFragments(TestCase):
    """
    TestDrawPixmapFragments class.
    """

    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        super(TestDrawPixmapFragments, cls).setUpClass()
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
        super(TestDrawPixmapFragments, cls).tearDownClass()

    @skipIf(USED_API.lower().startswith("pyside"), "PyQt only")
    def test(self):
        """
        :return:
        """
        img = QImage(100, 100, QImage.Format_ARGB32)  # type: QImage
        img.fill(Qt.green)
        p = QPainter(img)  # type: QPainter
        pix = QPixmap(10, 10)  # type: QPixmap
        pix.fill(Qt.red)
        frags = [
            QPainter.PixmapFragment.create(QPointF(25, 25), QRectF(0, 0, 10, 10), 5., 5.),
            QPainter.PixmapFragment.create(QPointF(75, 75), QRectF(0, 0, 10, 10), 5., 5.)
        ]  # type list[QPainter.PixmapFragmen]
        # PyQt and other bindings might use different signatures.
        try:
            p.drawPixmapFragments(frags, pix)
        except:
            try:
                p.drawPixmapFragments(frags, len(frags), pix)
            except:
                # Fallback to drawing one by one.
                for frag in frags:
                    p.drawPixmapFragments([frag], pix)
        p.end()
        self.assertEqual(QColor(img.pixel(10, 10)), QColor(Qt.red))
        self.assertEqual(QColor(img.pixel(80, 80)),  QColor(Qt.red))
        self.assertEqual(QColor(img.pixel(90, 10)), QColor(Qt.green))
        self.assertEqual(QColor(img.pixel(10, 90)), QColor(Qt.green))

    @skipIf(not USED_API.lower().startswith("pyside"), "PySide only")
    def testPySide(self):
        """
        :return:
        """
        img = QImage(100, 100, QImage.Format_ARGB32)  # type: QImage
        img.fill(Qt.green)
        p = QPainter(img)  # type: QPainter
        pix = QPixmap(10, 10)  # type: QPixmap
        pix.fill(Qt.red)
        try:
            p.drawPixmapFragments(p.PixmapFragment.create(QPointF(25, 25), QRectF(0, 0, 10, 10), 5., 5.), 1, pix)
        except:
            try:
                p.drawPixmapFragments([p.PixmapFragment.create(QPointF(25, 25), QRectF(0, 0, 10, 10), 5., 5.)], 1, pix)
            except:
                p.drawPixmapFragments([p.PixmapFragment.create(QPointF(25, 25), QRectF(0, 0, 10, 10), 5., 5.)], pix)
        p.end()
        self.assertEqual(QColor(img.pixel(10, 10)), QColor(Qt.red))
