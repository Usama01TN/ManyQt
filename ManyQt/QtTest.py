# -*- coding: utf-8 -*-
"""
QtTest is a wrapper around the QtTest library.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

if USED_API == QT_API_PYQT4:
    from PyQt4.QtTest import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtTest import *
elif USED_API == QT_API_PYQT6:
    from PyQt6.QtTest import *
elif USED_API == QT_API_PYSIDE:
    from PySide.QtTest import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtTest import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtTest import *
else:
    raise ImportError("No module named 'QtTest' in the selected Qt api ({})".format(USED_API))

def _QTest_qSleep(ms):
    """
    :param ms: int
    :return:
    """
    from time import sleep
    sleep(ms / 1000)


if not hasattr(QTest, "qSleep"):
    QTest.qSleep = _QTest_qSleep


def _QTest_qWaitForWindowExposed(widget, timeout=1000):
    """
    :param widget: QWidget
    :param timeout: int
    :return: bool
    """
    # A Qt5 compatible (probably) QTest.qWaitForWindowExposed(QWidget, int)
    # (mostly copied from qtestsystem.h in qt5/qtbase)
    try:
        from .QtCore import Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    except:
        from QtCore import Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    window = widget.window()
    timer = QElapsedTimer()  # type: QElapsedTimer
    timer.start()
    # Is widget.testAttribute(Qt.WA_Mapped) a suitable replacement for
    # QWindow.isExposed in Qt5??
    # Not exactly. In Qt5
    # window().testAttribute(Qt.WA_Mapped) == window().windowHandle.isExposed()
    # but both are False if a window is fully obscured by other windows,
    # in Qt4 there is no difference if a window is obscured.
    while not window.testAttribute(Qt.WA_Mapped):
        remaining = timeout - timer.elapsed()  # type: int
        if remaining <= 0:
            break
        QCoreApplication.processEvents(QEventLoop.AllEvents, remaining)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        QTest.qSleep(10)

    return window.testAttribute(Qt.WA_Mapped)


if not hasattr(QTest, "qWaitForWindowExposed"):
    QTest.qWaitForWindowExposed = _QTest_qWaitForWindowExposed


def _QTest_qWaitForWindowActive(widget, timeout=1000):
    """
    :param widget: QWidget
    :param timeout: int
    :return: bool
    """
    # A Qt5 compatible (probably) QTest.qWaitForWindowActive(QWidget, int)
    # (mostly copied from qtestsystem.h in qt5/qtbase)
    try:
        from .QtCore import Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    except:
        from QtCore import Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    window = widget.window()
    timer = QElapsedTimer()  # type: QElapsedTimer
    timer.start()
    while not window.isActiveWindow():
        remaining = timeout - timer.elapsed()
        if remaining <= 0:
            break
        QCoreApplication.processEvents(QEventLoop.AllEvents, remaining)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        QTest.qSleep(10)
    # See the explanation in qtestsystem.h
    if window.isActiveWindow():
        wait_no = 0  # type: int
        while window.pos().isNull():
            if wait_no > timeout // 10:
                break
            wait_no += 1  # type: int
            QTest.qWait(10)

    return window.isActiveWindow()


if not hasattr(QTest, "qWaitForWindowActive"):
    QTest.qWaitForWindowActive = _QTest_qWaitForWindowActive

if USED_API in {QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2}:
    try:
        from .QtCore import QObject, QByteArray as _QByteArray
    except:
        from QtCore import QObject, QByteArray as _QByteArray


    # Note that this implementation of QSignalSpy does not exposed in PyQt4 or PySide. Going by PyQt5 interface.
    class QSignalSpy(QObject):
        """
        QSignalSpy(boundsignal)
        """

        def __init__(self, boundsig, **kwargs):
            """
            :param boundsig: BoundSignal
            :param kwargs: any
            """
            super(QSignalSpy, self).__init__(**kwargs)
            try:
                from .QtCore import QEventLoop, QTimer
            except:
                from QtCore import QEventLoop, QTimer
            self.__boundsig = boundsig  # type BoundSignal
            self.__recorded = recorded = []  # type: list[list[any]]
            self.__loop = loop = QEventLoop()  # type: QEventLoop
            self.__timer = QTimer(self, singleShot=True)  # type: QTimer
            self.__timer.timeout.connect(self.__loop.quit)

            def record(*args):
                """
                :param args: any
                :return:
                """
                # Record the emitted arguments and quit the loop if running.
                # NOTE: not capturing self from parent scope.
                recorded.append(list(args))
                if loop.isRunning():
                    loop.quit()

            # Need to keep reference at least for PyQt4 4.11.4, sip 4.16.9 on
            # python 3.4 (if the signal is emitted during gc collection, and
            # the boundsignal is a QObject.destroyed signal).
            self.__record = record
            boundsig.connect(record)

        def signal(self):
            """
            :return: QByteArray
            """
            return _QByteArray(self.__boundsig.signal[1:].encode("latin-1"))

        def isValid(self):
            """
            :return: bool
            """
            return True

        def wait(self, timeout=5000):
            """
            :param timeout: int
            :return: bool
            """
            count = len(self)  # type: int
            self.__timer.stop()
            self.__timer.setInterval(timeout)
            self.__timer.start()
            self.__loop.exec_()
            self.__timer.stop()
            return len(self) != count

        def __getitem__(self, index):
            """
            :param index: int
            :return: list[list[any]]
            """
            return self.__recorded[index]

        def __setitem__(self, index, value):
            """
            :param index: int
            :param value: any
            :return:
            """
            self.__recorded.__setitem__(index, value)

        def __delitem__(self, index):
            """
            :param index: int
            :return:
            """
            self.__recorded.__delitem__(index)

        def __len__(self):
            """
            :return: int
            """
            return len(self.__recorded)


    del QObject


def _QTest_qWaitFor(predicate, timeout=5000):
    """
    :param predicate: callable
    :param timeout: int
    :return: bool
    """
    # type: (callable[[], bool], int) -> bool
    # Copied and adapted from Qt.
    try:
        from .QtCore import Qt, QCoreApplication, QEvent, QEventLoop, QDeadlineTimer
    except:
        from QtCore import Qt, QCoreApplication, QEvent, QEventLoop, QDeadlineTimer
    if predicate():
        return True
    deadline = QDeadlineTimer(Qt.PreciseTimer)  # type: QDeadlineTimer
    deadline.setRemainingTime(timeout)
    while True:
        QCoreApplication.processEvents(QEventLoop.AllEvents)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        if predicate():
            return True
        remaining = deadline.remainingTime()

        if remaining > 0:
            QTest.qSleep(min(10, remaining))
        remaining = deadline.remainingTime()
        if remaining <= 0:
            break
    return predicate()  # Last chance


if not hasattr(QTest, "qWaitFor"):  # Qt < 5.10
    QTest.qWaitFor = _QTest_qWaitFor


def _QTest_qWait(timeout):
    """
    :param timeout: int
    :return:
    """
    try:
        from .QtCore import Qt, QCoreApplication, QEvent, QEventLoop, QDeadlineTimer
    except:
        from QtCore import Qt, QCoreApplication, QEvent, QEventLoop, QDeadlineTimer
    remaining = timeout
    deadline = QDeadlineTimer(remaining, Qt.PreciseTimer)  # type: QDeadlineTimer
    while True:
        QCoreApplication.processEvents(QEventLoop.AllEvents, remaining)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        remaining = deadline.remainingTime()
        if remaining <= 0:
            break
        QTest.qSleep(min(10, remaining))
        remaining = deadline.remainingTime()
        if remaining <= 0:
            break


if not hasattr(QTest, "qWait"):  # PySide2
    QTest.qWait = _QTest_qWait

apply_global_fixes(globals())
