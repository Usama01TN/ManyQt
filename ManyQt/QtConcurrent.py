# -*- coding: utf-8 -*-
"""
Provides QtConcurrent classes and functions.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6, apply_global_fixes

try:
    if USED_API == QT_API_PYSIDE:
        try:
            from PySide.QtConcurrent import *
        except:
            from PySide.QConcurrent import *
    elif USED_API == QT_API_PYSIDE2:
        from PySide2.QtConcurrent import *
    elif USED_API == QT_API_PYSIDE6:
        from PySide6.QtConcurrent import *
except:
    try:
        from .QtCore import QObject, pyqtSignal, QThread, pyqtSlot, QThreadPool, QEventLoop, QRunnable
    except:
        from QtCore import QObject, pyqtSignal, QThread, pyqtSlot, QThreadPool, QEventLoop, QRunnable


    # # Method 1:
    # from traceback import format_exc

    # try:
    #     from .QtCore import QObject, pyqtSignal, QThread, pyqtSlot
    # except:
    #     from QtCore import QObject, pyqtSignal, QThread, pyqtSlot

    # class WorkerThread(QThread):
    #     """
    #     WorkerThread runs a target function in a background thread.
    #     """
    #     finished = pyqtSignal(object)  # type: pyqtSignal # Emitted with result.
    #     failed = pyqtSignal(Exception, 'QString')  # type: pyqtSignal # Emitted with exception and traceback.

    #     def __init__(self, fn, *args, **kwargs):
    #         """
    #         :param fn: Callable.
    #         :param args: (any) Arguments for callable.
    #         :param kwargs: (any) Keyword arguments for callable.
    #         """
    #         super(WorkerThread, self).__init__()
    #         self._fn = fn
    #         self._args = args
    #         self._kwargs = kwargs
    #         self._cancelled = False  # type: bool

    #     @pyqtSlot()
    #     def run(self):
    #         """
    #         :return: None
    #         """
    #         try:
    #             if self._cancelled:
    #                 return
    #             result = self._fn(*self._args, **self._kwargs)
    #             if not self._cancelled:
    #                 self.finished.emit(result)
    #         except Exception as e:
    #             self.failed.emit(e, format_exc())

    #     @pyqtSlot()
    #     def cancel(self):
    #         """
    #         :return:
    #         """
    #         self._cancelled = True  # type: bool

    # class QtConcurrent(QObject):
    #     """
    #     A class that mimics QtConcurrent behavior using QThread.
    #     """

    #     finished = pyqtSignal(object)  # type: pyqtSignal # Emits result when done.
    #     failed = pyqtSignal(Exception, str)  # type: pyqtSignal # Emits error with traceback.
    #     started = pyqtSignal()  # type: pyqtSignal # Emits when thread starts.
    #     canceled = pyqtSignal()  # type: pyqtSignal # Emits when task is cancelled.

    #     def __init__(self, *args, **kwargs):
    #         """
    #         :param args: any
    #         :param kwargs: any
    #         """
    #         super(QtConcurrent, self).__init__(*args, **kwargs)
    #         self._thread = None  # type: WorkerThread | None

    #     def run(self, fn, *args, **kwargs):
    #         """
    #         Run a function in a background thread.
    #         :param fn: Function to run.
    #         :param args: Positional arguments.
    #         :param kwargs: Keyword arguments.
    #         :return:
    #         """
    #         self.cancel()  # Cancel existing if any
    #         self._thread = WorkerThread(fn, *args, **kwargs)  # type: WorkerThread
    #         self._thread.finished.connect(self._onFinished)
    #         self._thread.failed.connect(self._onFailed)
    #         self.started.emit()
    #         self._thread.start()

    #     @pyqtSlot(object)
    #     def _onFinished(self, result):
    #         """
    #         :param result: object
    #         :return:
    #         """
    #         self.finished.emit(result)
    #         self._cleanup()

    #     @pyqtSlot(Exception, str)
    #     def _onFailed(self, exc, tb):
    #         self.failed.emit(exc, tb)
    #         self._cleanup()

    #     @pyqtSlot()
    #     def cancel(self):
    #         """
    #         :return:
    #         """
    #         if self._thread is not None and self._thread.isRunning():
    #             self._thread.cancel()
    #             self._thread.quit()
    #             self._thread.wait()
    #             self.canceled.emit()
    #             self._cleanup()

    #     def _cleanup(self):
    #         """
    #         :return:
    #         """
    #         self._thread = None  # type: WorkerThread | None
    class _Runnable(QRunnable):
        """
        _Runnable class.
        """

        def __init__(self, fn, arg, concurrent, *args, **kwargs):
            """
            :param fn: callable
            :param arg: any
            :param concurrent: QtConcurrent
            :param args: any
            :param kwargs: any
            """
            super(_Runnable, self).__init__(*args, **kwargs)
            self.__m_fn = fn
            self.__m_args = arg
            self.__m_concurrent = concurrent  # type: QtConcurrent

        @pyqtSlot()
        def run(self):
            """
            :return:
            """
            try:
                self.__m_concurrent._setResult(self.__m_fn(*self.__m_args))
            except Exception as e:
                self.__m_concurrent._setError(e)


    class QtConcurrent(QObject):
        """
        QtConcurrent class.
        """
        finished = pyqtSignal()  # type: pyqtSignal

        def __init__(self, *args, **kwargs):
            """
            :param args: any
            :param kwargs: any
            """
            super(QtConcurrent, self).__init__(*args, **kwargs)
            self.__m_result = None  # type: str | None
            self.__m_error = None  # type: str | None
            self.__m_isFinished = False  # type: bool
            self.__m_pool = QThreadPool.globalInstance()  # type: QThreadPool

        def run(self, fn, *args):
            """
            Run function.
            :param fn: callable function.
            :param args: (any) function arguments.
            :return: QtConcurrent
            """
            self.__m_isFinished = False  # type: bool
            self.__m_pool.start(_Runnable(fn, args, self))
            return self

        def _setResult(self, result):
            """
            :param result: str | unicode | QString
            :return:
            """
            self.__m_result = result  # type: str
            self.__m_isFinished = True  # type: bool
            self.finished.emit()

        def _setError(self, error):
            """
            :param error: str | unicode | QString
            :return:
            """
            self.__m_error = error  # type: str
            self.__m_isFinished = True  # type: bool
            self.finished.emit()

        @pyqtSlot()
        def waitForFinished(self):
            """
            :return: None
            """
            if self.__m_isFinished:
                return
            loop = QEventLoop()  # type: QEventLoop
            self.finished.connect(loop.quit)
            loop.exec_()

        def result(self):
            """
            :return: any
            """
            if self.__m_error:
                raise self.__m_error
            return self.__m_result

        def isFinished(self):
            """
            :return: bool
            """
            return self.__m_isFinished

apply_global_fixes(globals())
