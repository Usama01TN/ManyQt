# -*- coding: utf-8 -*-
"""
_fixes is a collection of fixes for PyQt/Pyside bugs.
Fixes should be added here when they are found and fixed upstream.
"""
from warnings import warn
from enum import Enum
from os import name


def qualname(cls_or_func):
    """
    :param cls_or_func: type | Callable[..., Any]
    :return: str | unicode
    """
    if hasattr(cls_or_func, '__qualname__'):
        return cls_or_func.__qualname__
    module_name = cls_or_func.__module__ if hasattr(cls_or_func, '__module__') else cls_or_func.__class__.__module__
    if hasattr(cls_or_func, '__name__'):
        qualname = cls_or_func.__name__  # type: str
    elif hasattr(cls_or_func, 'func_name'):
        qualname = cls_or_func.func_name
    else:
        qualname = cls_or_func.__class__.__name__  # type: str
    if hasattr(cls_or_func, 'im_class'):
        qualname = cls_or_func.im_class.__name__ + '.' + qualname  # type: str
    elif hasattr(cls_or_func, 'im_self') and cls_or_func.im_self is not None:
        qualname = cls_or_func.im_self.__class__.__name__ + '.' + qualname  # type: str
    return module_name + '.' + qualname


def fix_pyqt5_QGraphicsItem_itemChange():
    """
    Attempt to remedy:
    https://www.riverbankcomputing.com/pipermail/pyqt/2016-February/037015.html
    :return:
    """
    # Import QGraphicsObject and QGraphicsItem from PyQt5.QtWidgets
    QtWidgets = __import__('PyQt5.QtWidgets', fromlist=['QGraphicsObject', 'QGraphicsItem'])
    QGraphicsObject = QtWidgets.QGraphicsObject
    QGraphicsItem = QtWidgets.QGraphicsItem

    class Obj(QGraphicsObject):
        """
        Obj class.
        """

        def itemChange(self, change, value):
            """
            :param self: QGraphicsObject
            :param change: QGraphicsItem.GraphicsItemChange | int
            :param value: any
            :return: any
            """
            return QGraphicsObject.itemChange(self, change, value)

    obj = Obj()  # type: Obj
    parent = Obj()  # type: Obj
    obj.setParentItem(parent)

    if obj.parentItem() is None:
        # There was probably already some signal defined using QObject's
        # subclass from QtWidgets.
        # We will monkey patch the QGraphicsItem.itemChange and explicitly
        # cast all input and output QGraphicsItem instances.
        from os.path import dirname
        from sys import path

        if dirname(__file__) not in path:
            path.append(dirname(__file__))

        try:
            from .sip import cast
        except:
            from sip import cast

        QGraphicsItem_itemChange_old = QGraphicsItem.itemChange
        # All the QGraphicsItem.ItemChange flags which accept/return a QGraphicsItem.
        changeset = {
            QGraphicsItem.ItemParentChange,
            QGraphicsItem.ItemParentHasChanged,
            QGraphicsItem.ItemChildAddedChange,
            QGraphicsItem.ItemChildRemovedChange,
        }  # type: set[QGraphicsItem.GraphicsItemChange]

        def QGraphicsItem_itemChange(self, change, value):
            """
            :param self: QGraphicsItem
            :param change: QGraphicsItem.ItemChange | int
            :param value: QGraphicsItem | any
            :return: QGraphicsItem | any
            """
            if change in changeset:
                if isinstance(value, QGraphicsItem):
                    value = cast(value, QGraphicsItem)  # type: QGraphicsItem
                rval = QGraphicsItem_itemChange_old(self, change, value)
                if isinstance(rval, QGraphicsItem):
                    rval = cast(rval, QGraphicsItem)  # type: QGraphicsItem
                return rval
            return QGraphicsItem_itemChange_old(self, change, value)

        QGraphicsItem.itemChange = QGraphicsItem_itemChange
        warn('Monkey patching QGraphicsItem.itemChange', RuntimeWarning)


def fix_pyqt6_qtgui_qaction_menu(namespace):
    """
    Fixes the `setMenu` and `menu` methods for `QAction`.
    This function checks whether the `setMenu` method exists in the given namespace.
    If it does not exist, it defines two new methods: `setMenu` and `menu`. These methods use ctypes to call the underlying C++ functions `_QAction_setMenuObject` and `_QAction_menuObject`, respectively.
    :param namespace: (dict[str | unicode, any]) The namespace dictionary where the `QAction` class is defined.
    :return: None
    """
    if namespace.get('__name__') != 'ManyQt.QtGui':
        return
    from PyQt6.QtGui import QAction
    if hasattr(QAction, "setMenu") and hasattr(QAction, "menu"):
        # Native implementation available: nothing to patch. Return *before* touching any native Qt
        # library with ctypes (loading Qt libraries a second time can crash the process, e.g. on Android).
        return
    try:
        from PyQt6.QtWidgets import QMenu
    except ImportError:
        return  # No QtWidgets then no setMenu.
    from ctypes import c_void_p
    from os.path import dirname
    from sys import path

    if dirname(__file__) not in path:
        path.append(dirname(__file__))

    # NOTE: never fall back to a bare ``from _ctypes import ...``: ``_ctypes`` is also the name of
    # the CPython C extension behind the ``ctypes`` module.
    try:
        from ._ctypes import load_qtlib
    except ImportError:
        from ManyQt._ctypes import load_qtlib

    qtgui = load_qtlib("QtGui")
    if qtgui is None:
        return  # Qt library not found: leave QAction untouched instead of failing the import.
    try:
        if name == "posix":
            _QAction_setMenuObject = qtgui['_ZN7QAction13setMenuObjectEP7QObject']
            _QAction_menuObject = qtgui['_ZNK7QAction10menuObjectEv']
        elif name == "nt":
            _QAction_setMenuObject = qtgui['?setMenuObject@QAction@@AEAAXPEAVQObject@@@Z']
            _QAction_menuObject = qtgui['?menuObject@QAction@@AEBAPEAVQObject@@XZ']
        else:
            return
    except AttributeError:
        return  # Symbols not exported by this Qt build.
    _QAction_menuObject.argtypes = [c_void_p]
    _QAction_menuObject.restype = c_void_p
    _QAction_setMenuObject.argtypes = [c_void_p, c_void_p]
    from PyQt6.sip import isdeleted, unwrapinstance, wrapinstance

    def QAction_setMenu(self, menu):
        """
        :param self: QAction
        :param menu: QMenu
        :return:
        """
        if menu is not None and not isinstance(menu, QMenu):
            raise TypeError()
        if menu is not None and isdeleted(menu):
            raise RuntimeError()
        if isdeleted(self):
            raise RuntimeError()
        self.__QAction_menu = menu
        _QAction_setMenuObject(unwrapinstance(self), unwrapinstance(menu) if menu is not None else 0)

    def QAction_menu(self):
        """
        Returns the menu associated with this action.
        :param self: QAction
        :return: QMenu | None
        """
        if isdeleted(self):
            raise RuntimeError()
        ptr = _QAction_menuObject(unwrapinstance(self))
        if ptr is None:
            return None
        return wrapinstance(ptr, QMenu)

    QAction.setMenu = QAction_setMenu
    QAction.menu = QAction_menu



def fix_pyside6_qtgui_qaction_menu(namespace):
    """
    :param namespace: (dict[str | unicode, any]) The namespace dictionary where the `QAction` class is defined.
    :return: None
    """
    if namespace.get('__name__') != 'ManyQt.QtGui':
        return
    from PySide6.QtGui import QAction
    if hasattr(QAction, "setMenu") and hasattr(QAction, "menu"):
        # PySide6 already provides QAction.setMenu()/menu(). Return *before* touching any native Qt library
        # with ctypes: loading Qt libraries a second time at import time can crash the process later
        # (e.g. on Android/Pydroid when QApplication is created).
        return
    try:
        from PySide6.QtWidgets import QMenu
    except ImportError:
        return  # No QtWidgets then no setMenu.
    from ctypes import c_void_p
    from os.path import dirname
    from sys import path

    if dirname(__file__) not in path:
        path.append(dirname(__file__))

    # NOTE: never fall back to a bare ``from _ctypes import ...``: ``_ctypes`` is also the name of
    # the CPython C extension behind the ``ctypes`` module.
    try:
        from ._ctypes import load_qtlib
    except ImportError:
        from ManyQt._ctypes import load_qtlib

    qtgui = load_qtlib("QtGui")
    if qtgui is None:
        return  # Qt library not found: leave QAction untouched instead of failing the import.
    try:
        if name == "posix":
            _QAction_setMenuObject = qtgui['_ZN7QAction13setMenuObjectEP7QObject']
            _QAction_menuObject = qtgui['_ZNK7QAction10menuObjectEv']
        elif name == "nt":
            _QAction_setMenuObject = qtgui['?setMenuObject@QAction@@AEAAXPEAVQObject@@@Z']
            _QAction_menuObject = qtgui['?menuObject@QAction@@AEBAPEAVQObject@@XZ']
        else:
            return
    except AttributeError:
        return  # Symbols not exported by this Qt build.
    _QAction_menuObject.argtypes = [c_void_p]
    _QAction_menuObject.restype = c_void_p
    _QAction_setMenuObject.argtypes = [c_void_p, c_void_p]
    try:
        from shiboken6 import isValid, getCppPointer, wrapInstance as wrapinstance
    except ImportError:
        from PySide6.shiboken6 import isValid, getCppPointer, wrapInstance as wrapinstance

    def isdeleted(obj):
        """
        :param obj: QObject
        :return: bool
        """
        return not isValid(obj)

    def unwrapinstance(obj):
        """
        :param obj: QObject
        :return: int
        """
        return getCppPointer(obj)[0]

    def QAction_setMenu(self, menu):
        """
        :param self: QAction
        :param menu: QMenu
        :return:
        """
        if menu is not None and not isinstance(menu, QMenu):
            raise TypeError()
        if menu is not None and isdeleted(menu):
            raise RuntimeError()
        if isdeleted(self):
            raise RuntimeError()
        self.__QAction_menu = menu
        _QAction_setMenuObject(unwrapinstance(self), unwrapinstance(menu) if menu is not None else 0)

    def QAction_menu(self):
        """
        Returns the menu associated with this action.
        :param self: QAction
        :return: QMenu | None
        """
        if isdeleted(self):
            raise RuntimeError()
        ptr = _QAction_menuObject(unwrapinstance(self))
        if ptr is None:
            return None
        return wrapinstance(ptr, QMenu)

    QAction.setMenu = QAction_setMenu
    QAction.menu = QAction_menu


def fix_pyqt6_unscoped_enum(namespace):
    """
    Lift all PyQt6 enum members up to class level.
    i.e. Qt.ItemFlags.DisplayRole -> Qt.DisplayRole
    :param namespace: dict[str | unicode | QString, any]
    :return:
    """
    from PyQt6.sip import simplewrapper, wrappertype

    def members(enum):
        """
        :param enum: Enum
        :return: Generator
        """
        return ((name, enum[name]) for name in enum.__members__)

    def lift_enum_namespace(type_, enum):
        """
        :param type_: any
        :param enum: Enum
        :return:
        """
        for name, value in members(enum):
            setattr(type_, name, value)

    def is_unscoped_enum(value):
        """
        :param value: any
        :return: bool
        """
        return isinstance(value, type) and issubclass(value, Enum)

    def can_lift(type_, enum):
        """
        :param type_: any
        :param enum: Enum
        :return: bool
        """
        namespace = type_.__dict__
        return not any(name in namespace and namespace[name] is not value for name, value in members(enum))

    for _, class_ in list(namespace.items()):
        if isinstance(class_, (simplewrapper, wrappertype)):
            for name, value in list(class_.__dict__.items()):
                if is_unscoped_enum(value):
                    if can_lift(class_, value):
                        lift_enum_namespace(class_, value)



def fix_pyside6_unscoped_enum(namespace):
    """
    Lift all PyQt6 enum members up to class level.
    i.e. Qt.ItemFlags.DisplayRole -> Qt.DisplayRole
    :param namespace: dict[str | unicode | QString, any]
    :return:
    """
    def members(enum):
        """
        :param type_: any
        :param enum: Enum
        :return: Generator
        """
        return ((name, enum[name]) for name in enum.__members__)

    def is_pyside6_type(value):
        """
        Only PySide6 (Shiboken) wrapper classes are touched. The namespace also contains plain Python objects
        (e.g. ``re.IGNORECASE``), and setting attributes on those fails or corrupts them.
        :param value: any
        :return: bool
        """
        return (isinstance(value, type) and type(value).__module__ == 'Shiboken'
                and str(getattr(value, '__module__', '')).startswith('PySide6.'))

    def lift_enum_namespace(type_, enum):
        """
        :param type_: any
        :param enum: Enum
        :return:
        """
        for name, value in members(enum):
            # PySide6 >= 6.4 already resolves "Qt.AlignLeft"-style names itself (forgiveness mode). Never
            # shadow an attribute that is already reachable (own, inherited, or provided by PySide6).
            if hasattr(type_, name):
                continue
            try:
                setattr(type_, name, value)
            except (AttributeError, TypeError):
                pass

    def is_unscoped_enum(value):
        """
        :param value: any
        :return: bool
        """
        return isinstance(value, type) and issubclass(value, Enum)

    def can_lift(type_, enum):
        """
        :param type_: any
        :param enum: Enum
        :return: bool
        """
        namespace = type_.__dict__
        return not any(name in namespace and namespace[name] is not value for name, value in members(enum))

    for _, class_ in list(namespace.items()):
        if is_pyside6_type(class_):
            for name, value in list(class_.__dict__.items()):
                if is_unscoped_enum(value):
                    if can_lift(class_, value):
                        lift_enum_namespace(class_, value)

def fix_pyqt5_missing_enum_members(namespace):
    """
    :param namespace: dict[str | unicode | QString, any]
    :return:
    """
    from os.path import dirname
    from enum import Enum
    from sys import path

    if dirname(__file__) not in path:
        path.append(dirname(__file__))

    try:
        from .sip import simplewrapper, wrappertype
    except:
        from sip import simplewrapper, wrappertype

    def is_pyqt_enum_type(value):
        """
        :param value: any
        :return: bool
        """
        return (isinstance(value, type)
                and issubclass(value, int)
                and value is not int
                and ("." in qualname(value))
                and not issubclass(value, Enum))

    for _, class_ in list(namespace.items()):
        if isinstance(class_, (simplewrapper, wrappertype)):
            enumTypes = {}
            for name_, value in list(class_.__dict__.items()):
                if is_pyqt_enum_type(value):
                    enumTypes[qualname(value)] = value
            types_ = tuple(enumTypes.values())
            for name_, value in list(class_.__dict__.items()):
                if type(value) in types_:
                    type_ = enumTypes[qualname(type(value))]
                    if hasattr(type_, name_) and (
                            getattr(type_, name_) != value and not 'QKeySequence.StandardKey' in (
                            qualname(type_))):
                        warn("{} {} is already present and is not {}".format(type_, name_, value), RuntimeWarning)
                    elif not hasattr(type_, name_):
                        setattr(type_, name_, value)


def fix_pyside_QActionEvent_action(namespace):
    """
    Fixes the `action` and `before` methods for `QActionEvent` in PySide2.
    This function adds the `action` and `before` methods to the `QActionEvent` class if they are not already present.
    It uses ctypes to access the underlying C++ structures and shiboken2 to wrap the C++ pointers.
    :param namespace: (dict[str | unicode, any]) The namespace dictionary where the `QActionEvent` class is defined.
    :return: None
    """
    if namespace.get('__name__') != 'ManyQt.QtGui':
        return
    __QActionEvent = namespace.get('QActionEvent')
    if __QActionEvent is None or (hasattr(__QActionEvent, 'action') and hasattr(__QActionEvent, 'before')):
        return  # Nothing to fix (and no need to import QtWidgets from inside the QtGui import).
    from ctypes import Structure, c_void_p, c_ushort
    try:
        from PySide2.shiboken2 import wrapInstance, getCppPointer  # PySide2 < 5.12.0
    except:
        try:
            from shiboken2 import wrapInstance, getCppPointer
        except:
            from shiboken2.Shiboken import wrapInstance, getCppPointer

    from os.path import dirname
    from sys import path

    if dirname(__file__) not in path:
        path.append(dirname(__file__))

    try:
        from .QtGui import QActionEvent
        from .QtWidgets import QAction
    except:
        from QtGui import QActionEvent
        from QtWidgets import QAction

    class _QActionEvent(Structure):
        """
        _QActionEvent structure class.
        """
        _fields_ = [
            ("vtable", c_void_p),
            # QEvent
            ("d", c_void_p),  # private data ptr
            ("t", c_ushort),  # type
            ("_flags", c_ushort),  # various flags
            # QActionEvent
            ("act", c_void_p),  # QAction *act
            ("bef", c_void_p),  # QAction *bef
        ]

        def action(self):
            """
            :return: QAction
            """
            return from_address(self.act, QAction)

        def before(self):
            """
            :return: QAction
            """
            return from_address(self.bef, QAction)

        @classmethod
        def from_event(cls, event):
            """
            :param event: QActionEvent
            :return: QActionEvent
            """
            p, = getCppPointer(event)
            return cls.from_address(p)

    def from_address(address, type_):
        """
        :param address: int
        :param type_: any
        :return: QAction | None
        """
        return wrapInstance(address, type_) if address else None

    def action(self):
        """
        Returns the action associated with this event.
        :param self: QActionEvent
        :return: QAction
        """
        ev = _QActionEvent.from_event(self)
        return ev.action()

    def before(self):
        """
        Returns the action that precedes the current action in the application's action list.
        :param self: QActionEvent
        :return: QAction
        """
        ev = _QActionEvent.from_event(self)
        return ev.before()

    if not hasattr(QActionEvent, 'action'):
        QActionEvent.action = action
    if not hasattr(QActionEvent, 'before'):
        QActionEvent.before = before


def fix_pyside6_QActionEvent_action(namespace):
    """
    Fixes the `action` and `before` methods for `QActionEvent` in PySide2.
    This function adds the `action` and `before` methods to the `QActionEvent` class if they are not already present.
    It uses ctypes to access the underlying C++ structures and shiboken2 to wrap the C++ pointers.
    :param namespace: (dict[str | unicode, any]) The namespace dictionary where the `QActionEvent` class is defined.
    :return: None
    """
    if namespace.get('__name__') != 'ManyQt.QtGui':
        return
    QActionEvent = namespace.get('QActionEvent')
    QAction = namespace.get('QAction')  # In Qt6 QAction lives in QtGui (no circular QtWidgets import needed).
    if QActionEvent is None or QAction is None:
        return
    if hasattr(QActionEvent, 'action') and hasattr(QActionEvent, 'before'):
        return  # PySide6 provides both natively: nothing to fix.
    from ctypes import Structure, c_void_p, c_ushort
    try:
        from shiboken6 import wrapInstance, getCppPointer
    except ImportError:
        try:
            from PySide6.shiboken6 import wrapInstance, getCppPointer
        except ImportError:
            from shiboken6.Shiboken import wrapInstance, getCppPointer

    class _QActionEvent(Structure):
        """
        _QActionEvent structure class.
        """
        _fields_ = [
            ('vtable', c_void_p),
            # QEvent
            ('d', c_void_p),  # private data ptr
            ('t', c_ushort),  # type
            ('_flags', c_ushort),  # various flags
            # QActionEvent
            ('act', c_void_p),  # QAction *act
            ('bef', c_void_p),  # QAction *bef
        ]

        def action(self):
            """
            :return: QAction
            """
            return from_address(self.act, QAction)

        def before(self):
            """
            :return: QAction
            """
            return from_address(self.bef, QAction)

        @classmethod
        def from_event(cls, event):
            """
            :param event: QActionEvent
            :return: QActionEvent
            """
            p, = getCppPointer(event)
            return cls.from_address(p)

    def from_address(address, type_):
        """
        :param address: int
        :param type_: any
        :return: QAction | None
        """
        return wrapInstance(address, type_) if address else None

    def action(self):
        """
        Returns the action associated with this event.
        :param self: QActionEvent
        :return: QAction
        """
        ev = _QActionEvent.from_event(self)
        return ev.action()

    def before(self):
        """
        Returns the action that precedes the current action in the application's action list.
        :param self: QActionEvent
        :return: QAction
        """
        ev = _QActionEvent.from_event(self)
        return ev.before()

    if not hasattr(QActionEvent, 'action'):
        QActionEvent.action = action
    if not hasattr(QActionEvent, 'before'):
        QActionEvent.before = before


def fix_pyside_exec(namespace):
    """
    Fix exec method on dialogs and menus.
    :param namespace: dict[str | unicode, any]
    :return:
    """
    if namespace.get('__name__') == 'ManyQt.QtWidgets':
        from PySide2.QtWidgets import QApplication, QDialog, QMenu
        if 'exec' not in QApplication.__dict__:
            setattr(QApplication, 'exec', QApplication.exec_)
        if not hasattr(QDialog, 'exec'):
            setattr(QDialog, 'exec', QDialog.exec_)
        if not hasattr(QMenu, 'exec'):
            setattr(QMenu, 'exec', QMenu.exec_)
        if 'exec_' not in QApplication.__dict__:
            setattr(QApplication, 'exec_', getattr(QApplication, 'exec'))
        if not hasattr(QDialog, 'exec_'):
            setattr(QDialog, 'exec_', getattr(QDialog, 'exec'))
        if not hasattr(QMenu, 'exec_'):
            setattr(QMenu, 'exec_', getattr(QMenu, 'exec'))
    if namespace.get('__name__') == 'ManyQt.QtGui':
        from PySide2.QtGui import QGuiApplication, QDrag
        if "exec" not in QGuiApplication.__dict__:
            setattr(QGuiApplication, 'exec', QGuiApplication.exec_)
        if not hasattr(QDrag, 'exec'):
            setattr(QDrag, 'exec', QDrag.exec_)
        if 'exec_' not in QGuiApplication.__dict__:
            setattr(QGuiApplication, 'exec_', getattr(QGuiApplication, 'exec'))
        if not hasattr(QDrag, 'exec_'):
            setattr(QDrag, 'exec_', getattr(QDrag, 'exec'))
    elif namespace.get('__name__') == 'ManyQt.QtCore':
        from PySide2.QtCore import QCoreApplication, QEventLoop, QThread
        if not hasattr(QCoreApplication, 'exec'):
            setattr(QCoreApplication, 'exec', QCoreApplication.exec_)
        if not hasattr(QEventLoop, 'exec'):
            setattr(QEventLoop, 'exec', QEventLoop.exec_)
        if not hasattr(QThread, 'exec'):
            setattr(QThread, 'exec', QThread.exec_)
        if not hasattr(QCoreApplication, 'exec_'):
            setattr(QCoreApplication, 'exec_', getattr(QCoreApplication, 'exec'))
        if not hasattr(QEventLoop, 'exec_'):
            setattr(QEventLoop, 'exec_', getattr(QEventLoop, 'exec'))
        if not hasattr(QThread, 'exec_'):
            setattr(QThread, 'exec_', getattr(QThread, 'exec'))
    elif namespace.get('__name__') == 'ManyQt.QtPrintSupport':
        from PySide2.QtPrintSupport import QPageSetupDialog, QPrintDialog
        if 'exec' not in QPageSetupDialog.__dict__:
            setattr(QPageSetupDialog, 'exec', QPageSetupDialog.exec_)
        if 'exec' not in QPrintDialog.__dict__:
            setattr(QPrintDialog, 'exec', QPrintDialog.exec_)
        if 'exec_' not in QPageSetupDialog.__dict__:
            setattr(QPageSetupDialog, 'exec_', getattr(QPageSetupDialog, 'exec'))
        if "exec_" not in QPrintDialog.__dict__:
            setattr(QPrintDialog, 'exec_', getattr(QPrintDialog, 'exec'))


def fix_qstandarditem_insert_row(namespace):
    """
    :param namespace: dict[str | unicode, any]
    :return:
    """
    if namespace.get("__name__") == "ManyQt.QtGui":
        QStandardItem = namespace["QStandardItem"]
        __QStandardItem_insertRow = QStandardItem.insertRow

        def QStandardItem_insertRow(self, row, items):
            """
            Inserts rows into the model at position row.
            :param self: QStandardItem
            :param row: int
            :param items: list[QStandardItem] | QStandardItem
            """
            if isinstance(items, QStandardItem):
                # PYSIDE-237
                __QStandardItem_insertRow(self, row, [items])
            else:
                __QStandardItem_insertRow(self, row, items)

        QStandardItem.insertRow = QStandardItem_insertRow



def fix_pyside6_exec(namespace=None):
    """
    :param namespace: dict[str | unicode, any]
    :return:
    """
    if not namespace:
        namespace = {}
    if namespace.get('__name__') == 'ManyQt.QtWidgets':
        from PySide6.QtWidgets import QApplication, QDialog, QMenu
        if "exec" not in QApplication.__dict__:
            setattr(QApplication, 'exec', QApplication.exec_)
        if not hasattr(QDialog, 'exec'):
            setattr(QDialog, 'exec', QDialog.exec_)
        if not hasattr(QMenu, 'exec'):
            setattr(QMenu, 'exec', QMenu.exec_)
        if 'exec_' not in QApplication.__dict__:
            setattr(QApplication, 'exec_', getattr(QApplication, 'exec'))
        if not hasattr(QDialog, 'exec_'):
            setattr(QDialog, 'exec_', getattr(QDialog, 'exec'))
        if not hasattr(QMenu, 'exec_'):
            setattr(QMenu, 'exec_', getattr(QMenu, 'exec'))
    if namespace.get('__name__') == 'ManyQt.QtGui':
        from PySide6.QtGui import QGuiApplication, QDrag
        if 'exec' not in QGuiApplication.__dict__:
            setattr(QGuiApplication, 'exec', QGuiApplication.exec_)
        if not hasattr(QDrag, 'exec'):
            setattr(QDrag, 'exec', QDrag.exec_)
        if 'exec_' not in QGuiApplication.__dict__:
            setattr(QGuiApplication, 'exec_', getattr(QGuiApplication, 'exec'))
        if not hasattr(QDrag, 'exec_'):
            setattr(QDrag, 'exec_', getattr(QDrag, 'exec'))
    elif namespace.get('__name__') == 'ManyQt.QtCore':
        from PySide6.QtCore import QCoreApplication, QEventLoop, QThread
        if not hasattr(QCoreApplication, 'exec'):
            setattr(QCoreApplication, 'exec', QCoreApplication.exec_)
        if not hasattr(QEventLoop, 'exec'):
            setattr(QEventLoop, 'exec', QEventLoop.exec_)
        if not hasattr(QThread, "exec"):
            setattr(QThread, 'exec', QThread.exec_)
        if not hasattr(QCoreApplication, 'exec_'):
            setattr(QCoreApplication, 'exec_', getattr(QCoreApplication, 'exec'))
        if not hasattr(QEventLoop, 'exec_'):
            setattr(QEventLoop, 'exec_', getattr(QEventLoop, 'exec'))
        if not hasattr(QThread, 'exec_'):
            setattr(QThread, 'exec_', getattr(QThread, 'exec'))
    elif namespace.get('__name__') == 'ManyQt.QtPrintSupport':
        from PySide6.QtPrintSupport import QPageSetupDialog, QPrintDialog
        if "exec" not in QPageSetupDialog.__dict__:
            setattr(QPageSetupDialog, 'exec', QPageSetupDialog.exec_)
        if "exec" not in QPrintDialog.__dict__:
            setattr(QPrintDialog, 'exec', QPrintDialog.exec_)
        if "exec_" not in QPageSetupDialog.__dict__:
            setattr(QPageSetupDialog, 'exec_', getattr(QPageSetupDialog, 'exec'))
        if "exec_" not in QPrintDialog.__dict__:
            setattr(QPrintDialog, 'exec_', getattr(QPrintDialog, 'exec'))

GLOBAL_FIXES = {
    'pyqt6': [
        fix_pyqt6_unscoped_enum,
        fix_pyqt6_qtgui_qaction_menu,
    ],
    'pyqt5': [
        fix_pyqt5_missing_enum_members,
    ],
    'pyside2': [
        fix_pyside_QActionEvent_action,
        fix_pyside_exec,
        fix_qstandarditem_insert_row,
    ],
    'pyside6': [
        fix_pyside6_QActionEvent_action,
        fix_pyside6_exec,
        fix_qstandarditem_insert_row,
        fix_pyside6_unscoped_enum,
        fix_pyside6_qtgui_qaction_menu,
    ]
}


def global_fixes(namespace):
    """
    :param namespace: dict[str | unicode, any]
    :return:
    """
    from os.path import dirname
    from sys import path

    if dirname(__file__) not in path:
        path.append(dirname(__file__))

    try:
        from ._api import USED_API
    except ImportError:
        from _api import USED_API
    for fixer in GLOBAL_FIXES.get(USED_API, []):
        fixer(namespace)
