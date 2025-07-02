# -*- coding: utf-8 -*-
"""
QtCore module.
"""
from math import sqrt, ceil, floor, fabs, sin, cos, tan, acos, asin, atan, atan2, log, exp, pow
from platform import system, architecture, uname
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

# List names imported from Qt4's QtCore module.
__Qt4_QtCore = [
    'QAbstractAnimation',
    'QAbstractEventDispatcher',
    'QAbstractFileEngine',
    'QAbstractFileEngineHandler',
    'QAbstractFileEngineIterator',
    'QAbstractItemModel',
    'QAbstractListModel',
    'QAbstractState',
    'QAbstractTableModel',
    'QAbstractTransition',
    'QAnimationGroup',
    'QBasicTimer',
    'QBitArray',
    'QBuffer',
    'QByteArray',
    'QByteArrayMatcher',
    'QChildEvent',
    'QCoreApplication',
    'QCryptographicHash',
    'QDataStream',
    'QDate',
    'QDateTime',
    'QDir',
    'QDirIterator',
    'QDynamicPropertyChangeEvent',
    'QEasingCurve',
    'QElapsedTimer',
    'QEvent',
    'QEventLoop',
    'QEventTransition',
    'QFSFileEngine',
    'QFile',
    'QFileInfo',
    'QFileSystemWatcher',
    'QFinalState',
    'QGenericArgument',
    'QGenericReturnArgument',
    'QHistoryState',
    'QIODevice',
    'QLibrary',
    'QLibraryInfo',
    'QLine',
    'QLineF',
    'QLocale',
    'QMargins',
    'QMetaClassInfo',
    'QMetaEnum',
    'QMetaMethod',
    'QMetaObject',
    'QMetaProperty',
    'QMetaType',
    'QMimeData',
    'QModelIndex',
    'QMutex',
    'QMutexLocker',
    'QObject',
    'QObjectCleanupHandler',
    'QParallelAnimationGroup',
    'QPauseAnimation',
    'QPersistentModelIndex',
    'QPluginLoader',
    'QPoint',
    'QPointF',
    'QProcess',
    'QProcessEnvironment',
    'QPropertyAnimation',
    'QPyNullVariant',
    'QReadLocker',
    'QReadWriteLock',
    'QRect',
    'QRectF',
    'QRegExp',
    'QResource',
    'QRunnable',
    'QSemaphore',
    'QSequentialAnimationGroup',
    'QSettings',
    'QSharedMemory',
    'QSignalMapper',
    'QSignalTransition',
    'QSize',
    'QSizeF',
    'QSocketNotifier',
    'QState',
    'QStateMachine',
    'QSysInfo',
    'QSystemLocale',
    'QSystemSemaphore',
    'QT_TRANSLATE_NOOP',
    'QT_TR_NOOP',
    'QT_TR_NOOP_UTF8',
    'QT_VERSION',
    'QT_VERSION_STR',
    'QTemporaryFile',
    'QTextBoundaryFinder',
    'QTextCodec',
    'QTextDecoder',
    'QTextEncoder',
    'QTextStream',
    'QTextStreamManipulator',
    'QThread',
    'QThreadPool',
    'QTime',
    'QTimeLine',
    'QTimer',
    'QTimerEvent',
    'QTranslator',
    'QUrl',
    'QUuid',
    'QVariant',
    'QVariantAnimation',
    'QWaitCondition',
    'QWriteLocker',
    'QXmlStreamAttribute',
    'QXmlStreamAttributes',
    'QXmlStreamEntityDeclaration',
    'QXmlStreamEntityResolver',
    'QXmlStreamNamespaceDeclaration',
    'QXmlStreamNotationDeclaration',
    'QXmlStreamReader',
    'QXmlStreamWriter',
    'Q_ARG',
    'Q_CLASSINFO',
    'Q_ENUMS',
    'Q_FLAGS',
    'Q_RETURN_ARG',
    'Qt',
    'QtCriticalMsg',
    'QtDebugMsg',
    'QtFatalMsg',
    'QtMsgType',
    'QtSystemMsg',
    'QtWarningMsg',
    'SIGNAL',
    'SLOT',
    'bin_',
    'bom',
    'center',
    'dec',
    'endl',
    'fixed',
    'flush',
    'forcepoint',
    'forcesign',
    'hex_',
    'left',
    'lowercasebase',
    'lowercasedigits',
    'noforcepoint',
    'noforcesign',
    'noshowbase',
    'oct_',
    'qAbs',
    'qAddPostRoutine',
    'qChecksum',
    'qCompress',
    'qCritical',
    'qDebug',
    'qErrnoWarning',
    'qFatal',
    'qFuzzyCompare',
    'qInf',
    'qInstallMsgHandler',
    'qIsFinite',
    'qIsInf',
    'qIsNaN',
    'qIsNull',
    'qQNaN',
    'qRegisterResourceData',
    'qRemovePostRoutine',
    'qRound',
    'qRound64',
    'qSNaN',
    'qSetFieldWidth',
    'qSetPadChar',
    'qSetRealNumberPrecision',
    'qSharedBuild',
    'qSwap',
    'qUncompress',
    'qUnregisterResourceData',
    'qVersion',
    'qWarning',
    'qrand',
    'qsrand',
    'reset',
    'right',
    'scientific',
    'showbase',
    'uppercasebase',
    'uppercasedigits',
    'ws'
]  # type: list[str]

# Extra PyQt4 defined names mapped from PyQt4 which are not present in.
# PySide
__PyQt4_QtCore = [
    'PYQT_CONFIGURATION',
    'PYQT_VERSION',
    'PYQT_VERSION_STR',
    'pyqtBoundSignal',
    'pyqtPickleProtocol',
    'pyqtProperty',
    'pyqtRemoveInputHook',
    'pyqtRestoreInputHook',
    'pyqtSetPickleProtocol',
    'pyqtSignal',
    'pyqtSignature',
    'pyqtSlot',
    'pyqtWrapperType',
]  # type: list[str]

# List names imported from Qt4's QtGui module.
__Qt4_QtGui = [
    'QAbstractProxyModel',
    'QIdentityProxyModel',
    'QItemSelection',
    'QItemSelectionModel',
    'QItemSelectionRange',
    'QSortFilterProxyModel',
    'QStringListModel',
]  # type: list[str]
#: Names in Qt4's QtCore module not in Qt5.
__Qt4_QtCore_missing_in_Qt5 = [
    'QAbstractFileEngine',
    'QAbstractFileEngineHandler',
    'QAbstractFileEngineIterator',
    'QFSFileEngine',
    'QPyNullVariant',
    'QSystemLocale',
    'SIGNAL',
    'SLOT',
    'qInstallMsgHandler',
    'qSwap'
]  # type: list[str]
# Extra names in PyQt4's QtCore not in Qt5.
__PyQt4_QtCore_missing_in_Qt5 = ['pyqtSignature']  # type: list[str]

if USED_API == QT_API_PYQT6:
    from PyQt6.QtCore import *

    Signal = pyqtSignal
    Slot = pyqtSlot
    Property = pyqtProperty
    BoundSignal = pyqtBoundSignal
    Qt.Alignment = Qt.AlignmentFlag
    Qt.ApplicationStates = Qt.ApplicationState
    Qt.DockWidgetAreas = Qt.DockWidgetArea
    Qt.Edges = Qt.Edge
    Qt.FindChildOptions = Qt.FindChildOption
    Qt.GestureFlags = Qt.GestureFlag
    Qt.ImageConversionFlags = Qt.ImageConversionFlag
    Qt.ItemFlags = Qt.ItemFlag
    Qt.KeyboardModifiers = Qt.KeyboardModifier
    Qt.MatchFlags = Qt.MatchFlag
    Qt.MouseButtons = Qt.MouseButton
    Qt.MouseEventFlags = Qt.MouseEventFlag
    Qt.Orientations = Qt.Orientation
    Qt.ScreenOrientations = Qt.ScreenOrientation
    # Qt.SplitBehavior = Qt.SplitBehaviorFlags
    Qt.TextInteractionFlags = Qt.TextInteractionFlag
    Qt.ToolBarAreas = Qt.ToolBarArea
    Qt.TouchPointStates = Qt.TouchPointState
    Qt.WindowFlags = Qt.WindowType
    Qt.WindowStates = Qt.WindowState
    QItemSelectionModel.SelectionFlags = QItemSelectionModel.SelectionFlag
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtCore import *

    try:
        # QSignalMapper.mapped[QWidget] does not work unless QtWidgets is
        # imported before QSignalMapper is touched (even hasattr(QSM, "aa"))
        # will cause QSignalMapper.mapped[QWidget] to fail with KeyError.
        import PyQt5.QtWidgets
    except ImportError:
        pass
    Signal = pyqtSignal
    Slot = pyqtSlot
    Property = pyqtProperty
    BoundSignal = pyqtBoundSignal

elif USED_API == QT_API_PYQT4:
    from PyQt4 import QtCore as _QtCore, QtGui as _QtGui

    globals().update({name: getattr(_QtCore, name) for name in __Qt4_QtCore + __PyQt4_QtCore if hasattr(_QtCore, name)})
    globals().update({name: getattr(_QtGui, name) for name in __Qt4_QtGui if hasattr(_QtCore, name)})
    Signal = _QtCore.pyqtSignal
    Slot = _QtCore.pyqtSlot
    Property = _QtCore.pyqtProperty
    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel
    del _QtCore, _QtGui

elif USED_API == QT_API_PYSIDE:
    from PySide import QtCore as _QtCore, QtGui as _QtGui

    globals().update({name: getattr(_QtCore, name) for name in __Qt4_QtCore if hasattr(_QtCore, name)})
    Signal = _QtCore.Signal
    Slot = _QtCore.Slot
    Property = _QtCore.Property

    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    if hasattr(_QtGui, "QIdentityProxyModel"):
        QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel
    _major, _minor, _micro = tuple(map(int, _QtCore.qVersion().split(".")[:3]))  # type: int, int, int
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro  # type: int
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)  # type: str
    del _QtCore, _QtGui, _major, _minor, _micro
    # Known to be in PyQt4 but missing in PySide: Q_ARG, Q_CLASSINFO, Q_ENUMS, Q_FLAGS, Q_RETURN_ARG, ...
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtCore import *

    _major, _minor, _micro = tuple(map(int, qVersion().split(".")[:3]))  # type: int, int, int
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro  # type: int
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)  # type: str
    BoundSignal = Signal
    pyqtSignal = Signal
    pyqtSlot = Slot
    pyqtProperty = Property
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtCore import *

    _major, _minor, _micro = tuple(map(int, qVersion().split(".")[:3]))  # type: int, int, int
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro  # type: int
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)  # type: str
    BoundSignal = Signal
    pyqtSignal = Signal
    pyqtSlot = Slot
    pyqtProperty = Property


def QString(text):
    """
    :param text: str | unicode | QString
    :return: str | unicode
    """
    try:
        return unicode(text)
    except:
        try:
            return str(text)
        except:
            return text


if 'QVariant' not in globals():
    from json import loads, dumps


    class QVariant(object):
        """
        Minimal QVariant compatibility wrapper for PySide2/PySide6.
        """

        class Type(object):
            """
            Type class.
            """
            Int = int
            Double = float
            String = str
            Bool = bool
            List = list
            Dict = dict
            None_ = None

        Int = Type.Int  # type int
        Double = Type.Double  # type float
        String = Type.String  # type str
        Bool = Type.Bool  # type bool
        List = Type.List  # type list
        Dict = Type.Dict  # type dict
        None_ = Type.None_  # type None

        def __init__(self, value=None):
            """
            :param value: any | None
            :return:
            """
            self.__m_value = value  # type: any

        def toString(self):
            """
            Returns the value converted to a string.
            :return: str | unicode | QString
            """
            try:
                return unicode(self.__m_value)
            except:
                return str(self.__m_value)

        def __str__(self):
            """
            Returns the value converted to a string.
            :return: str | unicode | QString
            """
            return self.toString()

        def __int__(self):
            """
            Returns the value converted to an int.
            :return: int
            """
            return self.toInt()

        def __bool__(self):
            """
            :return: bool
            """
            return self.toBool()

        def __float__(self):
            """
            Returns the value converted to a float.
            :return: float
            """
            return self.toFloat()

        def toInt(self):
            """
            Returns the value converted to an int.
            :return: int
            """
            try:
                return int(self.__m_value)
            except ValueError:
                return 0

        def toFloat(self):
            """
            Returns the value converted to a float.
            :return: float
            """
            try:
                return float(self.__m_value)
            except ValueError:
                return 0.0

        def toBool(self):
            """
            Returns the value converted to a boolean.
            :return: bool
            """
            return bool(self.__m_value)

        def toList(self):
            """
            Returns the value converted to a Python list.
            :return: list
            """
            return self.__m_value if isinstance(self.__m_value, list) else [self.__m_value]

        def value(self):
            """
            Returns the value stored in this QVariant.
            :return: any
            """
            return self.__m_value

        def toObject(self):
            """
            Returns the value stored in this QVariant.
            :return: any
            """
            return self.__m_value

        def isNull(self):
            """
            :return: bool
            """
            return self.__m_value is None

        def isValid(self):
            """
            :return: bool
            """
            return self.__m_value is not None

        def clear(self):
            """
            :return:
            """
            self.__m_value = None  # type: any

        def swap(self, other):
            """
            Swaps the contents of this QVariant with those of other.
            :param other: QVariant
            :return:
            """
            if isinstance(other, QVariant):
                self.__m_value, other.__m_value = other.__m_value, self.__m_value
            else:
                raise TypeError("swap expects a QVariant instance")

        def canConvert(self, typeName):
            """
            Returns True if the current value can be converted to the given type name.
            :type typeName: QVariant.Type
            :return: bool
            """
            if typeName is None:
                return False
            try:
                typeName(self.__m_value)
                return True
            except (ValueError, TypeError):
                return False

        def convert(self, typeName):
            """
            Converts the current value to the given type, if possible.
            Returns True on success.
            :param typeName: QVariant.Type
            :return: bool
            """
            if typeName is None:
                return False
            try:
                self.__m_value = typeName(self.__m_value)
                return True
            except (ValueError, TypeError):
                return False

        @staticmethod
        def nameToType(name):
            """
            Maps a type name to a Python type.
            :type name: QVariant.Type
            :return: QVariant.Type
            """
            return name

        def save(self):
            """
            Serializes the QVariant value to a JSON string.
            :return: str | unicode | QString | None
            """
            try:
                return dumps(self.__m_value)
            except (TypeError, ValueError):
                return None

        def load(self, data):
            """
            Loads the QVariant value from a JSON string.
            :param data: str | unicode | QString
            :return: bool
            """
            try:
                self.__m_value = loads(data)
                return True
            except (ValueError, TypeError):
                return False

        def __repr__(self):
            """
            Returns a string representation of the object.
            :return: str | unicode | QString
            """
            return "<QVariant({})>".format(repr(self.__m_value))
else:
    # Missing in QVariant.
    QVariant.value = QVariant.value if hasattr(QVariant, 'value') else (
        QVariant.toObject if hasattr(QVariant, 'toObject') else None)
    QVariant.toObject = QVariant.toObject if hasattr(QVariant, 'toObject') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value)
    QVariant.toInt = QVariant.toInt if hasattr(QVariant, 'toInt') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value)
    QVariant.toDouble = QVariant.toDouble if hasattr(QVariant, 'toDouble') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value)
    QVariant.toFloat = QVariant.toFloat if hasattr(QVariant, 'toFloat') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value)
    QVariant.toString = QVariant.toString if hasattr(QVariant, 'toString') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value)
    QVariant.toBool = bool(QVariant.toBool if hasattr(QVariant, 'toBool') else (QVariant.toObject if hasattr(
        QVariant, 'toObject') else QVariant.value))
# Missing in PyQt4 <= 4.11.3
if not hasattr(QEvent, "MacSizeChange"):
    QEvent.MacSizeChange = QEvent.Type(177)
if not hasattr(QEvent, "ContentsRectChange"):
    QEvent.ContentsRectChange = QEvent.Type(178)
if not hasattr(QEvent, "NonClientAreaMouseButtonDblClick"):
    QEvent.NonClientAreaMouseButtonDblClick = QEvent.Type(176)
if not hasattr(QEvent, "NonClientAreaMouseButtonPress"):
    QEvent.NonClientAreaMouseButtonPress = QEvent.Type(174)
if not hasattr(QEvent, "NonClientAreaMouseButtonRelease"):
    QEvent.NonClientAreaMouseButtonRelease = QEvent.Type(175)
if not hasattr(QEvent, "NonClientAreaMouseMove"):
    QEvent.NonClientAreaMouseMove = QEvent.Type(173)
if not hasattr(QSignalMapper, "mappedInt"):  # Qt < 5.15
    class QSignalMapper(QSignalMapper):
        """
        QSignalMapper class.
        """
        mappedInt = Signal(int)  # type: Signal
        mappedString = Signal(str)  # type: Signal
        mappedObject = Signal("QObject*")  # type: Signal
        mappedWidget = Signal("QWidget*")  # type: Signal

        def __init__(self, *args, **kwargs):
            """
            :param args: any
            :param kwargs: any
            """
            super(QSignalMapper, self).__init__(*args, **kwargs)
            self.mapped[int].connect(self.mappedInt)
            self.mapped[str].connect(self.mappedString)
            self.mapped["QObject*"].connect(self.mappedObject)
            try:
                self.mapped["QWidget*"].connect(self.mappedWidget)
            except (KeyError, TypeError):
                pass

if not hasattr(QLibraryInfo, "path"):
    QLibraryInfo.path = QLibraryInfo.location
if not hasattr(QLibraryInfo, "LibraryLocation"):
    QLibraryInfo.LibraryLocation = QLibraryInfo.LibraryPath
if not hasattr(QLibraryInfo, "location"):
    QLibraryInfo.location = QLibraryInfo.path
if USED_API == QT_API_PYSIDE2:
    class QSettings(QSettings):
        """
        A subclass of QSettings with a simulated `type` parameter in value method.
        """

        # QSettings.value does not have `type` type in PySide2
        def value(self, key, defaultValue=None, type=None):
            """
            Returns the value for setting key. If the setting doesn't exist, returns defaultValue.
            :param key: QByteArray | bytes | bytearray | memoryview | str | None
            :param defaultValue: any | None
            :param type: type | None
            :return: any | None
            """
            if not self.contains(key):
                return defaultValue
            value = super(QSettings, self).value(key)
            if type is not None:
                value = self.__qvariant_cast(value, type)
                if value is None:
                    value = defaultValue
            return value

        try:
            from ._compat import qvariant_cast as __qvariant_cast
        except:
            from _compat import qvariant_cast as __qvariant_cast
        __qvariant_cast = staticmethod(__qvariant_cast)


    try:
        QStringListModel
    except NameError:
        from PySide2.QtGui import QStringListModel

pyqtSignal = Signal
pyqtSlot = Slot
pyqtProperty = Property

if USED_API in [QT_API_PYSIDE, QT_API_PYSIDE2, QT_API_PYSIDE6]:
    if USED_API == QT_API_PYSIDE:
        try:
            from PySide import sip as __shiboken
        except:
            try:
                import sip as __shiboken
            except:
                try:
                    from . import shiboken as __shiboken
                except:
                    import shiboken as __shiboken
    elif USED_API == QT_API_PYSIDE2:
        try:
            from PySide2 import shiboken2 as __shiboken
        except:
            try:
                import sip as __shiboken
            except:
                import shiboken2 as __shiboken
    elif USED_API == QT_API_PYSIDE6:
        try:
            from shiboken6 import Shiboken as __shiboken
        except:
            try:
                from PySide6 import sip as __shiboken
            except:
                try:
                    import sip as __shiboken
                except:
                    try:
                        import shiboken6 as __shiboken
                    except:
                        try:
                            import PySide6.shiboken6.Shiboken as __shiboken
                        except:
                            import PySide6.shiboken6 as __shiboken
    else:
        raise ImportError("ManyQt.shiboken")


    # if hasattr(__shiboken, 'wrapInstance') and not hasattr(__shiboken, 'cast'):
    #     __shiboken.cast = __shiboken.wrapInstance
    # if hasattr(__shiboken, 'cast') and not hasattr(__shiboken, 'wrapInstance'):
    #     __shiboken.wrapInstance = __shiboken.cast

    def cast(obj, type_):
        """
        :param obj: QObject
        :param type_: QObject
        :return: QObject
        """
        return __shiboken.wrapinstance(unwrapinstance(obj), type_)


    def unwrapinstance(obj):
        """
        :param obj: QObject
        :return: QObject
        """
        if hasattr(__shiboken, 'getCppPointer'):
            addr, = __shiboken.getCppPointer(obj)
            return addr
        elif hasattr(__shiboken, 'unwrapInstance'):
            return __shiboken.unwrapInstance(obj)
        return __shiboken.unwrapinstance(obj)


    wrapinstance = __shiboken.wrapInstance


    def isdeleted(obj):
        """
        :param obj: QObject
        :return: bool
        """
        if hasattr(__shiboken, "isdeleted"):
            return __shiboken.isdeleted(obj)
        return not __shiboken.isValid(obj)


    ispyowned = __shiboken.ownedByPython
    delete = __shiboken.delete
    ispycreated = __shiboken.createdByPython
elif USED_API in [QT_API_PYQT5, QT_API_PYQT6]:
    if dirname(dirname(__file__)) not in path:
        path.append(dirname(dirname(__file__)))

    try:
        from .ManyQt.sip import cast, isdeleted, ispyowned, ispycreated, delete, unwrapinstance, wrapinstance
    except:
        from ManyQt.sip import cast, isdeleted, ispyowned, ispycreated, delete, unwrapinstance, wrapinstance

#: Qt version as a (major, minor, micro) tuple
QT_VERSION_INFO = tuple(map(int, qVersion().split(".")[:3]))  # type: tuple[int, ...]
apply_global_fixes(globals())


class QtMsgType(object):
    """
    QtMsgType enumeration class.
    This enum describes the messages that can be sent to a message handler (QtMessageHandler).
    You can use the enum to identify and associate the various message types with the appropriate actions.
    """
    QtDebugMsg = 0  # type: int # A message generated by the qDebug() function.
    QtWarningMsg = 1  # type: int # A message generated by the qWarning() function.
    QtCriticalMsg = 2  # type: int # A message generated by the qCritical() function.
    QtFatalMsg = 3  # type: int # A message generated by the qFatal() function.
    QtInfoMsg = 4  # type: int # A message generated by the qInfo() function.
    QtSystemMsg = QtCriticalMsg  # type: int


QtDebugMsg = QtMsgType.QtDebugMsg  # type: int
QtWarningMsg = QtMsgType.QtWarningMsg  # type: int
QtCriticalMsg = QtMsgType.QtCriticalMsg  # type: int
QtFatalMsg = QtMsgType.QtFatalMsg  # type: int
QtInfoMsg = QtMsgType.QtInfoMsg  # type: int
QtSystemMsg = QtMsgType.QtSystemMsg  # type: int

# RAND_MAX = 0x7fff  # type: int
RAND_MAX = 1  # type: int
EXIT_SUCCESS = 0  # type: int
EXIT_FAILURE = 1  # type: int
# Constants.
M_E = 2.7182818284590452354  # type: float
M_LOG2E = 1.4426950408889634074  # type: float
M_LOG10E = 0.43429448190325182765  # type: float
M_LN2 = 0.69314718055994530942  # type: float
M_LN10 = 2.30258509299404568402  # type: float
M_PI = 3.14159265358979323846  # type: float
M_PI_2 = 1.57079632679489661923  # type: float
M_PI_4 = 0.78539816339744830962  # type: float
M_1_PI = 0.31830988618379067154  # type: float
M_2_PI = 0.63661977236758134308  # type: float
M_2_SQRTPI = 1.12837916709551257390  # type: float
M_SQRT2 = 1.41421356237309504880  # type: float
M_SQRT1_2 = 0.70710678118654752440  # type: float

# Math objects:
# Functions
qMax = max
qMin = min
qAbs = abs
qCeil = ceil
qFloor = floor
qFabs = fabs
qSin = sin
qCos = cos
qTan = tan
qAcos = acos
qAsin = asin
qAtan = atan
qAtan2 = atan2
qSqrt = sqrt
qLn = log
qExp = exp
qPow = pow


def qDegreesToRadians(degrees):
    """
    :param degrees: float | int
    :return: float | int
    """
    return degrees * (M_PI / 180)


def qRadiansToDegrees(radians):
    """
    :param radians: float | int
    :return: float | int
    """
    return radians * (180 / M_PI)


def qNextPowerOfTwo(v):
    """
    :param v: int
    :return: int
    """
    if v == 0:
        return 1
    v -= 1  # type: int
    v |= v >> 1  # type: int
    v |= v >> 2  # type: int
    v |= v >> 4  # type: int
    v |= v >> 8  # type: int
    v |= v >> 16  # type: int
    v += 1  # type: int
    return v


# Qt-specific sine table approximation.
QT_SINE_TABLE_SIZE = 256  # type: int
qt_sine_table = [sin(2 * M_PI * i / QT_SINE_TABLE_SIZE) for i in range(QT_SINE_TABLE_SIZE)]  # type: list[float]


def qFastSin(x):
    """
    :param x: float | int
    :return: float | int
    """
    si = int(x * (0.5 * QT_SINE_TABLE_SIZE / M_PI))  # type: int
    d = x - si * (2.0 * M_PI / QT_SINE_TABLE_SIZE)  # type: float
    ci = int(si + QT_SINE_TABLE_SIZE / 4.0)  # type: int
    si &= QT_SINE_TABLE_SIZE - 1  # type: int
    ci &= QT_SINE_TABLE_SIZE - 1  # type: int
    return qt_sine_table[si] + (qt_sine_table[ci] - 0.5 * qt_sine_table[si] * d) * d


def qFastCos(x):
    """
    :param x: float | int
    :return: float | int
    """
    ci = int(x * (0.5 * QT_SINE_TABLE_SIZE / M_PI))  # type: int
    d = x - ci * (2.0 * M_PI / QT_SINE_TABLE_SIZE)  # type: float
    si = int(ci + QT_SINE_TABLE_SIZE / 4.0)  # type: int
    si &= QT_SINE_TABLE_SIZE - 1  # type: int
    ci &= QT_SINE_TABLE_SIZE - 1  # type: int
    return qt_sine_table[si] - (qt_sine_table[ci] + 0.5 * qt_sine_table[si] * d) * d


def qBound(value, lowerBound, upperBound):
    """
    :param value: int
    :param lowerBound: int
    :param upperBound: int
    :return: int
    """
    return max(min(value, upperBound), lowerBound)


def qFuzzyCompare(p1, p2):
    """
    :param p1: float | int
    :param p2: float | int
    :return: float | int
    """
    return abs(p1 - p2) * 1000000000000. <= min(abs(p1), abs(p2))


def qFuzzyIsNull(f):
    """
    Returns True if the absolute value of f is within 0.00001f of 0.0.
    :param f: float | int
    :return: bool
    """
    return abs(f) <= 0.00001


# OS Enums:
Q_OS_OPENBSD = 0  # type: int
Q_OS_NETBSD = 1  # type: int
Q_OS_FREEBSD = 2  # type: int
Q_OS_WINCE = 3  # type: int
Q_OS_WIN64 = 4  # type: int
Q_OS_UNIX = 5  # type: int
Q_OS_MAC = 6  # type: int
Q_OS_LINUX = 7  # type: int
Q_OS_BSD4 = 8  # type: int
Q_OS_WIN = 9  # type: int
UNKNOWN = "UNKNOWN"  # type: str


def defined(sys_name):
    """
    :param sys_name: str | unicode
    :return: bool
    """
    from os import name

    Q_OS_CACHE = []  # type: list
    if system().lower() in ['linux', 'darwin', 'freebsd', 'unix']:
        Q_OS_CACHE.append(Q_OS_UNIX)
    if system().lower() == 'windows':
        if name == 'ce':
            Q_OS_CACHE.append(Q_OS_WINCE)
        if architecture()[0].startswith('64'):
            Q_OS_CACHE.append(Q_OS_WIN64)
        if name == 'nt':
            Q_OS_CACHE.append(Q_OS_WIN)
    elif system().lower() in ['darwin', 'mac', 'macos']:
        Q_OS_CACHE.append(Q_OS_MAC)
    elif system().lower() == 'linux':
        Q_OS_CACHE.append(Q_OS_LINUX)
    uname_ = uname()
    system_ = uname_.system.lower() if hasattr(uname_, 'system') else uname_[0].lower()  # type: str
    if 'freebsd' in system_:
        Q_OS_CACHE.append(Q_OS_FREEBSD)
    elif 'openbsd' in system_:
        Q_OS_CACHE.append(Q_OS_OPENBSD)
    elif 'netbsd' in system_:
        Q_OS_CACHE.append(Q_OS_NETBSD)
    elif 'bsd' in system_ and '4' in (uname_.release if hasattr(uname_, 'release') else uname_[2]):
        # This is a heuristic check and may not be reliable for BSD/OS (BSDi)
        # as it is an older and less common variant.
        Q_OS_CACHE.append(Q_OS_WIN64)
    return sys_name in Q_OS_CACHE


def QT_VERSION_CHECK(major, minor, patch):
    """
    :param major: int
    :param minor: int
    :param patch: int
    :return: int
    """
    return (major << 16) | (minor << 8) | patch


if 'qEnvironmentVariable' not in globals():
    from os import environ

    qEnvironmentVariable = environ.get

if 'QRandomGenerator' not in globals():
    from random import Random


    class QRandomGenerator(object):
        """
        QRandomGenerator class.
        """
        # A global instance of the random generator.
        __globalInstance = None  # type: QRandomGenerator | None

        @classmethod
        def global_(cls):
            """
            Returns the global instance of the random generator.
            :return: QRandomGenerator
            """
            if cls.__globalInstance is None:
                cls.__globalInstance = QRandomGenerator()  # type: QRandomGenerator
            return cls.__globalInstance

        def __init__(self, seed=None):
            """
            Initialize the random generator with an optional seed.
            :param seed: (int | None) Optional seed.
            :return:
            """
            self.__m_random = Random(seed)  # type: Random

        def bounded(self, lowest, highest=None):
            """
            Generate a random integer between `lowest` and `highest - 1`.
            If `highest` is not provided, generate a random integer between 0 and `lowest - 1`.
            :param lowest: int
            :param highest: (int | None) the Optional highest value.
            :return: int
            """
            return self.__m_random.randint(0, lowest - 1) if highest is None else self.__m_random.randint(
                lowest, highest - 1)

        def generateDouble(self):
            """
            Generate a random double between 0.0 and 1.0.
            :return: float | int
            """
            return self.__m_random.random()

if 'QDeadlineTimer' not in globals():
    from time import time


    class QDeadlineTimer(object):
        """
        QDeadlineTimer class.
        """

        class TimerType(object):
            """
            TimerType enumeration class.
            """
            Precise = 0  # type: int
            Coarse = 1  # type: int
            VeryCoarse = 2  # type: int

        Precise = TimerType.Precise  # type: int
        Coarse = TimerType.Coarse  # type: int
        VeryCoarse = TimerType.VeryCoarse  # type: int

        def __init__(self, deadline=None, type_=TimerType.Coarse):
            """
            Construct a QDeadlineTimer object.
            :param deadline: None (forever), float (seconds since epoch), or int (milliseconds remaining)
            :param type_: (TimerType | int) Precise, Coarse, VeryCoarse
            :return:
            """
            self._type = type_  # type: int
            if deadline is None:
                # Forever case.
                self._deadline = float('inf')  # type: float
            elif isinstance(deadline, (int, float)):
                if deadline < 0:
                    # Negative values are treated as milliseconds remaining.
                    self._deadline = time() * 1000 + deadline  # type: float
                else:
                    # Positive values are treated as absolute time since epoch in seconds.
                    self._deadline = deadline * 1000  # type: float # convert to ms.
            else:
                raise TypeError("deadline must be None, int, or float")

        @classmethod
        def current(cls, type_=TimerType.Coarse):
            """
            Create a QDeadlineTimer that expires immediately.
            :param type_: int | TimerType
            :return: QDeadlineTimer
            """
            return cls(0, type_)

        @classmethod
        def addNSecs(cls, deadline, nsecs):
            """
            Add nanoseconds to a deadline and return a new QDeadlineTimer.
            :param deadline: QDeadlineTimer
            :param nsecs: int
            :return: QDeadlineTimer
            """
            if not isinstance(deadline, QDeadlineTimer):
                raise TypeError("deadline must be a QDeadlineTimer")
            return cls(deadline._deadline + (nsecs / 1000000.0), deadline._type)

        def deadline(self):
            """
            Return the absolute time in milliseconds since epoch.
            :return: float | int
            """
            return self._deadline

        def deadlineNSecs(self):
            """
            Return the absolute time in nanoseconds since epoch.
            :return: float | int
            """
            return self._deadline * 1000000

        def hasExpired(self):
            """
            Check if the deadline has passed.
            :return: bool
            """
            return self.remainingTime() <= 0

        def isForever(self):
            """
            Check if the deadline is forever.
            :return: bool
            """
            return self._deadline == float('inf')

        def remainingTime(self):
            """
            Return remaining time in milliseconds.
            :return: float | int
            """
            if self.isForever():
                return float('inf')
            remaining = self._deadline - (time() * 1000)  # type: float
            return max(0, remaining) if remaining > 0 else 0

        def remainingTimeNSecs(self):
            """
            Return remaining time in nanoseconds.
            :return: float | int
            """
            return self.remainingTime() * 1000000

        def setDeadline(self, deadline, type_=None):
            """
            Set a new deadline.
            :param deadline: float | int
            :param type_: int | TimerType | None
            :return:
            """
            if type_ is not None:
                self._type = type_  # type: int
            self._deadline = deadline * 1000  # type: float # Convert to ms.

        def setPreciseDeadline(self, secs, nsecs=0, type_=None):
            """
            Set a precise deadline with seconds and nanoseconds.
            :param secs: float | int
            :param nsecs: float | int
            :param type_: int | TimerType | None
            :return:
            """
            if type_ is not None:
                self._type = type_  # type: int
            self._deadline = secs * 1000 + nsecs / 1000000.0  # type: float

        def setRemainingTime(self, msecs, type_=None):
            """
            Set deadline based on remaining milliseconds.
            :param msecs: float | int
            :param type_: int | TimerType | None
            :return:
            """
            if type_ is not None:
                self._type = type_  # type: int
            if msecs < 0:
                self._deadline = float('inf')  # type: float
            else:
                self._deadline = time() * 1000 + msecs  # type: float

        def setPreciseRemainingTime(self, secs, nsecs=0, type_=None):
            """
            Set deadline based on remaining seconds and nanoseconds.
            :param secs: float | int
            :param nsecs: float | int
            :param type_: int | TimerType | None
            :return:
            """
            if type_ is not None:
                self._type = type_  # type: int
            if secs < 0 and nsecs <= 0:
                self._deadline = float('inf')  # type: float
            else:
                self._deadline = time() * 1000 + secs * 1000 + nsecs / 1000000.0  # type: float

        def timerType(self):
            """
            Get the timer type.
            :return: int | TimerType
            """
            return self._type

        def swap(self, other):
            """
            Swap this deadline timer with another.
            :param other: QDeadlineTimer
            :return:
            """
            if not isinstance(other, QDeadlineTimer):
                raise TypeError("other must be a QDeadlineTimer")
            self._deadline, other._deadline = other._deadline, self._deadline  # type int, int
            self._type, other._type = other._type, self._type  # type int, int

        def __eq__(self, other):
            """
            :param other: QDeadlineTimer
            :return: bool
            """
            return False if not isinstance(other, QDeadlineTimer) else (
                    self._deadline == other._deadline and self._type == other._type)

        def __lt__(self, other):
            """
            :param other: QDeadlineTimer
            :return: bool
            """
            if not isinstance(other, QDeadlineTimer):
                raise TypeError("can only compare with other QDeadlineTimer")
            return self._deadline < other._deadline

        def __le__(self, other):
            """
            :param other: QDeadlineTimer
            :return: bool
            """
            if not isinstance(other, QDeadlineTimer):
                raise TypeError("can only compare with other QDeadlineTimer")
            return self._deadline <= other._deadline

        def __repr__(self):
            """
            :return: str | unicode | QString
            """
            if self.isForever():
                return "QDeadlineTimer(Forever, type={})".format(self._type)
            return "QDeadlineTimer({}ms remaining, type={})".format(self.remainingTime(), self._type)

    # class QDeadlineTimer(QTimer):
    #     """
    #     QDeadlineTimer class.
    #     """
    #
    #     def __init__(self, tryTimeout=0, *args, **kwargs):
    #         """
    #         :param tryTimeout: int
    #         :param args: any
    #         :param kwargs: any
    #         """
    #         super(QDeadlineTimer, self).__init__(*args, **kwargs)
    #         self.__tryTimeOut = tryTimeout  # type: int
    #         self.__endTime = QDateTime.currentDateTime().addMSecs(tryTimeout)  # type: QDateTime
    #         self.start(tryTimeout)
    #
    #     def hasExpired(self):
    #         """
    #         :return: bool
    #         """
    #         return QDateTime.currentDateTime() < self.__endTime
