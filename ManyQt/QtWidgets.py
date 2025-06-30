# -*- coding: utf-8 -*-
"""
QtWidgets module provides access to all GUI QtWidgets.
"""
from os.path import dirname
from warnings import warn
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes
except:
    from _api import USED_API, QT_API_PYQT6, QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2, \
        QT_API_PYSIDE6, apply_global_fixes

# Names imported from Qt4's QtGui module.
__Qt4_QtGui = [
    'QAbstractButton',
    'QAbstractGraphicsShapeItem',
    'QAbstractItemDelegate',
    'QAbstractItemView',
    'QAbstractScrollArea',
    'QAbstractSlider',
    'QAbstractSpinBox',
    'QAction',
    'QActionGroup',
    'QApplication',
    'QBoxLayout',
    'QButtonGroup',
    'QCalendarWidget',
    'QCheckBox',
    'QColorDialog',
    'QColumnView',
    'QComboBox',
    'QCommandLinkButton',
    'QCommonStyle',
    'QCompleter',
    'QDataWidgetMapper',
    'QDateEdit',
    'QDateTimeEdit',
    'QDesktopWidget',
    'QDial',
    'QDialog',
    'QDialogButtonBox',
    'QDirModel',
    'QDockWidget',
    'QDoubleSpinBox',
    'QErrorMessage',
    'QFileDialog',
    'QFileIconProvider',
    'QFileSystemModel',
    'QFocusFrame',
    'QFontComboBox',
    'QFontDialog',
    'QFormLayout',
    'QFrame',
    'QGesture',
    'QGestureEvent',
    'QGestureRecognizer',
    'QGraphicsAnchor',
    'QGraphicsAnchorLayout',
    'QGraphicsBlurEffect',
    'QGraphicsColorizeEffect',
    'QGraphicsDropShadowEffect',
    'QGraphicsEffect',
    'QGraphicsEllipseItem',
    'QGraphicsGridLayout',
    'QGraphicsItem',
    'QGraphicsItemGroup',
    'QGraphicsLayout',
    'QGraphicsLayoutItem',
    'QGraphicsLineItem',
    'QGraphicsLinearLayout',
    'QGraphicsObject',
    'QGraphicsOpacityEffect',
    'QGraphicsPathItem',
    'QGraphicsPixmapItem',
    'QGraphicsPolygonItem',
    'QGraphicsProxyWidget',
    'QGraphicsRectItem',
    'QGraphicsRotation',
    'QGraphicsScale',
    'QGraphicsScene',
    'QGraphicsSceneContextMenuEvent',
    'QGraphicsSceneDragDropEvent',
    'QGraphicsSceneEvent',
    'QGraphicsSceneHelpEvent',
    'QGraphicsSceneHoverEvent',
    'QGraphicsSceneMouseEvent',
    'QGraphicsSceneMoveEvent',
    'QGraphicsSceneResizeEvent',
    'QGraphicsSceneWheelEvent',
    'QGraphicsSimpleTextItem',
    'QGraphicsTextItem',
    'QGraphicsTransform',
    'QGraphicsView',
    'QGraphicsWidget',
    'QGridLayout',
    'QGroupBox',
    'QHBoxLayout',
    'QHeaderView',
    'QInputDialog',
    'QItemDelegate',
    'QItemEditorCreatorBase',
    'QItemEditorFactory',
    'QKeyEventTransition',
    # 'QKeySequenceEdit',
    'QLCDNumber',
    'QLabel',
    'QLayout',
    'QLayoutItem',
    'QLineEdit',
    'QListView',
    'QListWidget',
    'QListWidgetItem',
    'QMacCocoaViewContainer',
    'QMainWindow',
    'QMdiArea',
    'QMdiSubWindow',
    'QMenu',
    'QMenuBar',
    'QMessageBox',
    'QMouseEventTransition',
    # 'QOpenGLWidget',
    'QPanGesture',
    'QPinchGesture',
    'QPlainTextDocumentLayout',
    'QPlainTextEdit',
    'QProgressBar',
    'QProgressDialog',
    # 'QProxyStyle',
    'QPushButton',
    'QRadioButton',
    'QRubberBand',
    'QScrollArea',
    'QScrollBar',
    # 'QScroller',
    # 'QScrollerProperties',
    'QShortcut',
    'QSizeGrip',
    'QSizePolicy',
    'QSlider',
    'QSpacerItem',
    'QSpinBox',
    'QSplashScreen',
    'QSplitter',
    'QSplitterHandle',
    'QStackedLayout',
    'QStackedWidget',
    'QStatusBar',
    'QStyle',
    'QStyleFactory',
    'QStyleHintReturn',
    'QStyleHintReturnMask',
    'QStyleHintReturnVariant',
    'QStyleOption',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionComplex',
    'QStyleOptionDockWidget',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStylePainter',
    'QStyledItemDelegate',
    'QSwipeGesture',
    'QSystemTrayIcon',
    'QTabBar',
    'QTabWidget',
    'QTableView',
    'QTableWidget',
    'QTableWidgetItem',
    'QTableWidgetSelectionRange',
    'QTapAndHoldGesture',
    'QTapGesture',
    'QTextBrowser',
    'QTextEdit',
    'QTimeEdit',
    'QToolBar',
    'QToolBox',
    'QToolButton',
    'QToolTip',
    'QTreeView',
    'QTreeWidget',
    'QTreeWidgetItem',
    'QTreeWidgetItemIterator',
    'QUndoCommand',
    'QUndoGroup',
    'QUndoStack',
    'QUndoView',
    'QVBoxLayout',
    'QWIDGETSIZE_MAX',
    'QWhatsThis',
    'QWidget',
    'QWidgetAction',
    'QWidgetItem',
    'QWizard',
    'QWizardPage',
    'qApp',
    'qDrawBorderPixmap',
    'qDrawPlainRect',
    'qDrawShadeLine',
    'qDrawShadePanel',
    'qDrawShadeRect',
    'qDrawWinButton',
    'qDrawWinPanel'
]  # type: list[str]

if USED_API in [QT_API_PYQT6, QT_API_PYSIDE6]:
    if USED_API == QT_API_PYQT6:
        from PyQt6.QtGui import QUndoCommand, QUndoStack, QUndoGroup, QAction, QActionGroup, QShortcut
        from PyQt6.QtWidgets import *
    elif USED_API == QT_API_PYSIDE6:
        from PySide6.QtGui import QUndoCommand, QUndoStack, QUndoGroup, QAction, QActionGroup, QShortcut
        from PySide6.QtWidgets import *
    QStyle.State = QStyle.StateFlag
    QStyle.SubControls = QStyle.SubControl
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import PYQT_VERSION as _PYQT_VERSION

    if _PYQT_VERSION < 0x50502:  # ?
        try:
            from . import _fixes
        except:
            import _fixes

        _fixes.fix_pyqt5_QGraphicsItem_itemChange()
        del _fixes

elif USED_API == QT_API_PYQT4:
    from PyQt4 import QtGui as _QtGui

    globals().update({name: getattr(_QtGui, name) for name in __Qt4_QtGui if hasattr(_QtGui, name)})

    # Alias the QStyleOption version classes.
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4
    QStyleOptionViewItem_ = _QtGui.QStyleOptionViewItem
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2
    QStyleOptionToolBox_ = _QtGui.QStyleOptionToolBox
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionDockWidget_ = _QtGui.QStyleOptionDockWidget
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionFrame_ = _QtGui.QStyleOptionFrame
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionProgressBar_ = _QtGui.QStyleOptionProgressBar
    QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
    QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame
    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTabBarBase_ = _QtGui.QStyleOptionTabBarBase
    QStyleOptionTab = _QtGui.QStyleOptionTabV3
    QStyleOptionTab_ = _QtGui.QStyleOptionTab


    # PyQt5's version of QFileDialog's static methods.
    class QFileDialog(_QtGui.QFileDialog):
        """
        QFileDialog class.
        """
        getOpenFileName = _QtGui.QFileDialog.getOpenFileNameAndFilter
        getOpenFileNames = _QtGui.QFileDialog.getOpenFileNamesAndFilter
        getSaveFileName = _QtGui.QFileDialog.getSaveFileNameAndFilter


    # Some extra forward compatibility.
    QHeaderView.setSectionResizeMode = lambda self, *args: self.setResizeMode(*args)
    QHeaderView.sectionResizeMode = lambda self: self.resizeMode()
    QHeaderView.sectionsClickable = lambda self: self.isClickable()
    QHeaderView.setSectionsClickable = lambda self, clickable: self.setClickable(clickable)
    QHeaderView.sectionsMovable = lambda self: self.isMovable()
    QHeaderView.setSectionsMovable = lambda self, movable: self.setMovable(movable)
    from PyQt4 import QtCore as __QtCore

    QWidget = _QtGui.QWidget
    __QPixmap = _QtGui.QPixmap


    def _QWidget_grab(self, rect=__QtCore.QRect(0, 0, -1, -1)):
        """
        :param self: QWidget
        :param rect: QRect
        :return: QPixmap
        """
        return __QPixmap.grabWidget(self) if not rect.isValid() else __QPixmap.grabWidget(self, rect)


    QWidget.grab = _QWidget_grab
    del _QtGui, __QtCore

elif USED_API == QT_API_PYSIDE:
    from PySide import QtGui as _QtGui

    globals().update({name: getattr(_QtGui, name) for name in __Qt4_QtGui if hasattr(_QtGui, name)})
    # Alias the QStyleOption version classes.
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4
    QStyleOptionViewItem_ = _QtGui.QStyleOptionViewItem
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2
    QStyleOptionToolBox_ = _QtGui.QStyleOptionToolBox
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionDockWidget_ = _QtGui.QStyleOptionDockWidget
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionFrame_ = _QtGui.QStyleOptionFrame
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionProgressBar_ = _QtGui.QStyleOptionProgressBar
    if hasattr(_QtGui, "QStyleOptionTabWidgetFrameV2"):
        QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
        QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame
    else:
        QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrame
        QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame

    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTabBarBase_ = _QtGui.QStyleOptionTabBarBase
    QStyleOptionTab = _QtGui.QStyleOptionTabV3
    QStyleOptionTab_ = _QtGui.QStyleOptionTab
    # Some extra forward compatibility.
    QHeaderView.setSectionResizeMode = lambda self, *args: self.setResizeMode(*args)
    QHeaderView.sectionResizeMode = lambda self: self.resizeMode()
    QHeaderView.sectionsClickable = lambda self: self.isClickable()
    QHeaderView.setSectionsClickable = lambda self, clickable: self.setClickable(clickable)
    QHeaderView.sectionsMovable = lambda self: self.isMovable()
    QHeaderView.setSectionsMovable = lambda self, movable: self.setMovable(movable)

    from PySide import QtCore as __QtCore

    QWidget = _QtGui.QWidget
    __QPixmap = _QtGui.QPixmap


    def _QWidget_grab(self, rect=__QtCore.QRect(0, 0, -1, -1)):
        """
        :param self: QWidget
        :param rect: QRect
        :return: QPixmap
        """
        return __QPixmap.grabWidget(self) if not rect.isValid() else __QPixmap.grabWidget(self, rect)


    QWidget.grab = _QWidget_grab
    del _QtGui, __QtCore

elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtWidgets import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtWidgets import *

try:
    QWIDGETSIZE_MAX  # Missing in older PyQt5, PyQt4
except NameError:
    QWIDGETSIZE_MAX = (1 << 24) - 1  # type: int

if not hasattr(QWidget, "screen"):
    def QWidget_screen(self):
        """
        :param self: QWidget
        :return: QScreen
        """
        screens = QApplication.screens()  # type list[QScreen]
        desktop = __QApplication_desktop()  # type:  QDesktopWidget  # Avoid deprecation warning.
        screenNum = desktop.screenNumber(self)  # type: int
        return screens[screenNum] if 0 <= screenNum < len(screens) else QApplication.primaryScreen()


    QWidget.screen = QWidget_screen
    del QWidget_screen

if hasattr(QWidget, "getContentsMargins"):
    def QWidget_getContentsMargins(self):
        """
        :param self: QWidget
        :return: tuple[int, int, int, int]
        """
        warn("QWidget.getContentsMargins is obsolete and is removed in Qt6", DeprecationWarning, stacklevel=2)
        return __QWidget_getContentsMargins(self)


    __QWidget_getContentsMargins = QWidget.getContentsMargins
    QWidget.getContentsMargins = QWidget_getContentsMargins

if hasattr(QLineEdit, "getTextMargins"):
    def __QLineEdit_getTextMargins(self):
        """
        :param self: QLineEdit
        :return: tuple[int, int, int, int]
        """
        warn("QLineEdit.getTextMargins is deprecated and will be removed.", DeprecationWarning, stacklevel=2)
        m = self.textMargins()  # type QMargins
        return m.left(), m.top(), m.right(), m.bottom()


    QLineEdit.getTextMargins = __QLineEdit_getTextMargins
    del __QLineEdit_getTextMargins

if not hasattr(QAbstractItemView, "viewOptions"):
    def __QAbstractItemView_viewOptions(self):
        """
        :param self: QAbstractItemView
        :return: QStyleOptionViewItem
        """
        opt = QStyleOptionViewItem()  # type: QStyleOptionViewItem
        self.initViewItemOption(opt)
        return opt


    QAbstractItemView.viewOptions = __QAbstractItemView_viewOptions
    del __QAbstractItemView_viewOptions
elif not hasattr(QAbstractItemView, "initViewItemOption"):
    def __QAbstractItemView_initViewItemOption(self, option):
        """
        :param self: QAbstractItemView
        :param option: QStyleOptionViewItem
        :return: None
        """
        opt = self.viewOptions()
        option.initFrom(self)
        option.state = opt.state
        option.font = opt.font
        option.decorationSize = opt.decorationSize
        option.decorationPosition = opt.decorationPosition
        option.decorationAlignment = opt.decorationAlignment
        option.displayAlignment = opt.displayAlignment
        option.textElideMode = opt.textElideMode
        option.rect = opt.rect
        option.showDecorationSelected = opt.showDecorationSelected
        option.features = opt.features
        option.locale = opt.locale
        option.widget = opt.widget


    QAbstractItemView.initViewItemOption = __QAbstractItemView_initViewItemOption
    del __QAbstractItemView_initViewItemOption

try:
    from .QtCore import QModelIndex as __QModelIndex
except:
    from QtCore import QModelIndex as __QModelIndex


def __QAbstractItemView_itemDelegate(self, *args):
    """
    :param self: QAbstractItemView
    :param args: any
    :return: QAbstractItemDelegate
    """
    return self.itemDelegateForIndex(*args) if args and isinstance(
        args[0], __QModelIndex) else __QAbstractItemView_itemDelegate_orig(self, *args)


if not hasattr(QAbstractItemView, "itemDelegateForIndex"):
    def __QAbstractItemView_itemDelegateForIndex(self, index):
        """
        :param index: QModelIndex
        :return: QAbstractItemDelegate
        """
        return __QAbstractItemView_itemDelegate_orig(self, index)


    QAbstractItemView.itemDelegateForIndex = __QAbstractItemView_itemDelegateForIndex

__QAbstractItemView_itemDelegate_orig = QAbstractItemView.itemDelegate
QAbstractItemView.itemDelegate = __QAbstractItemView_itemDelegate


if not hasattr(QStyleOption, 'init'):
    def __QStyleOption_init(self, *args, **kwargs):
        """
        :param self: QStyleOption
        :param args: any
        :param kwargs: any
        :return:
        """
        self.initFrom(*args, **kwargs)


    QStyleOption.init = __QStyleOption_init

if not hasattr(QStyleOption, 'initFrom'):
    def __QStyleOption_initFrom(self, *args, **kwargs):
        """
        :param self: QStyleOption
        :param args: any
        :param kwargs: any
        :return:
        """
        self.initFrom(*args, **kwargs)


    QStyleOption.initFrom = __QStyleOption_initFrom

if hasattr(QApplication, "desktop"):
    def QApplication_desktop():
        """
        :return: QDesktopWidget
        """
        warn("QApplication.desktop is obsolete and is removed in Qt6", DeprecationWarning, stacklevel=2)
        return __QApplication_desktop()


    __QApplication_desktop = QApplication.desktop
    QApplication.desktop = staticmethod(QApplication_desktop)
    del QApplication_desktop

if not hasattr(QPlainTextEdit, "setTabStopDistance"):
    def __QPlainTextEdit_setTabStopDistance(self, width):
        """
        :param width: width: float | int
        :return:
        """
        self.setTabStopWidth(int(width))


    def __QPlainTextEdit_tabStopDistance(self):
        """
        :return: float | int
        """
        return float(self.tabStopWidth())


    QPlainTextEdit.setTabStopDistance = __QPlainTextEdit_setTabStopDistance
    QPlainTextEdit.tabStopDistance = __QPlainTextEdit_tabStopDistance

if not hasattr(QTextEdit, "setTabStopDistance"):
    def __QTextEdit_setTabStopDistance(self, width):
        """
        :param self: QTextEdit
        :param width: width: float | int
        :return:
        """
        self.setTabStopWidth(int(width))


    def __QTextEdit_tabStopDistance(self):
        """
        :param self: QTextEdit
        :return: float | int
        """
        return float(self.tabStopWidth())


    QTextEdit.setTabStopDistance = __QTextEdit_setTabStopDistance
    QTextEdit.tabStopDistance = __QTextEdit_tabStopDistance

try:
    from .QtCore import Signal, Slot
except:
    from QtCore import Signal, Slot

if not hasattr(QButtonGroup, "idClicked"):
    class QButtonGroup(QButtonGroup):
        """
        QButtonGroup class.
        """
        idClicked = Signal(int)  # type: Signal
        idPressed = Signal(int)  # type: Signal
        idReleased = Signal(int)  # type: Signal
        idToggled = Signal(int, bool)  # type: Signal

        def __init__(self, *args, **kwargs):
            """
            :param args: any
            :param kwargs: any
            """
            buttonClicked = kwargs.pop("buttonClicked", None)
            buttonPressed = kwargs.pop("buttonPressed", None)
            buttonReleased = kwargs.pop("buttonReleased", None)
            buttonToggled = kwargs.pop("buttonToggled", None)
            super(QButtonGroup, self).__init__(*args, **kwargs)
            self.buttonClicked.connect(self.__button_clicked)
            self.buttonPressed.connect(self.__button_pressed)
            self.buttonReleased.connect(self.__button_released)
            self.buttonToggled.connect(self.__button_toggled)
            if buttonClicked is not None:
                self.buttonClicked.connect(buttonClicked)
            if buttonPressed is not None:
                self.buttonPressed.connect(buttonPressed)
            if buttonReleased is not None:
                self.buttonReleased.connect(buttonReleased)
            if buttonToggled is not None:
                self.buttonToggled.connect(buttonToggled)

        @Slot(QAbstractButton)
        def __button_clicked(self, button):
            """
            :param button: QAbstractButton
            :return:
            """
            self.idClicked.emit(self.id(button))

        @Slot(QAbstractButton)
        def __button_pressed(self, button):
            """
            :param button: QAbstractButton
            :return:
            """
            self.idPressed.emit(self.id(button))

        @Slot(QAbstractButton)
        def __button_released(self, button):
            """
            :param button: QAbstractButton
            :return:
            """
            self.idReleased.emit(self.id(button))

        @Slot(QAbstractButton, bool)
        def __button_toggled(self, button, checked):
            """
            :param button: QAbstractButton
            :param checked: bool
            :return:
            """
            self.idToggled.emit(self.id(button), checked)

if not hasattr(QComboBox, "textActivated"):
    class QComboBox(QComboBox):
        """
        QComboBox class.
        """
        textActivated = Signal(str)  # type: Signal
        textHighlighted = Signal(str)  # type: Signal

        def __init__(self, *args, **kwargs):
            """
            :param args: any
            :param kwargs: any
            """
            activated = kwargs.pop("activated", None)
            highlighted = kwargs.pop("highlighted", None)
            super(QComboBox, self).__init__(*args, **kwargs)
            self.activated[int].connect(self.__activated)
            self.highlighted[int].connect(self.__highlighted)
            if activated is not None:
                self.activated.connect(activated)
            if highlighted is not None:
                self.highlighted.connect(highlighted)

        @Slot(int)
        def __activated(self, index):
            """
            :param index: int
            :return:
            """
            self.textActivated.emit(self.itemText(index))

        @Slot(int)
        def __highlighted(self, index):
            """
            :param index: int
            :return:
            """
            self.textHighlighted.emit(self.itemText(index))

try:
    QProxyStyle
except:
    class QProxyStyle(QCommonStyle):
        """
        QProxyStyle class.
        """

        def __init__(self, style=None, *args, **kwargs):
            """
            :param style: QProxyStyle | QCommonStyle | QStyle
            :param args: any
            :param kwargs: any
            """
            if isinstance(self, QProxyStyle):
                super(QProxyStyle, self).__init__(style, *args, **kwargs)
            elif isinstance(self, QCommonStyle):
                super(QProxyStyle, self).__init__(*args, **kwargs)
            elif isinstance(self, QStyle):
                super(QProxyStyle, self).__init__(*args, **kwargs)
            self.__style = style  # type: QStyle
            if hasattr(self, 'setBaseStyle'):
                self.setBaseStyle(style if style else self.styleBase())

        def unpolish(self, *__args):
            """
            :param __args: QWidget | QApplication | any
            :return: None
            """
            return self.baseStyle().unpolish(*__args) if self.baseStyle() else super(
                QProxyStyle, self).unpolish(*__args)

        def subElementRect(self, subElement, option, widget=None):
            """
            :param subElement: QStyle.SubElement | int
            :param option: QStyleOption
            :param widget: QWidget | None
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().subElementRect(subElement, option, widget)
            return super(QProxyStyle, self).subElementRect(subElement, option, widget)

        def subControlRect(self, cc, opt, subControl, widget=None):
            """
            :param cc: QStyle.ComplexControl | int
            :param opt: QStyleOptionComplex
            :param subControl: QStyle.SubControl | int
            :param widget: QWidget | None
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().subControlRect(cc, opt, subControl, widget)
            return super(QProxyStyle, self).subControlRect(cc, opt, subControl, widget)

        def styleHint(self, hint, option=None, widget=None, returnData=None):
            """
            :param hint: QStyle.StyleHint | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :param returnData: QStyleHintReturn | None
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().styleHint(hint, option, widget, returnData)
            return super(QProxyStyle, self).styleHint(hint, option, widget, returnData)

        def standardPixmap(self, standardPixmap, option=None, widget=None):
            """
            :param standardPixmap: QStyle.StandardPixmap | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :return: QPixmap
            """
            if self.baseStyle():
                return self.baseStyle().standardPixmap(standardPixmap, option, widget)
            return super(QProxyStyle, self).standardPixmap(standardPixmap, option, widget)

        def standardPalette(self):
            """
            :return: QPalette
            """
            return self.baseStyle().standardPalette() if self.baseStyle() else super(
                QProxyStyle, self).standardPalette()

        def standardIcon(self, standardIcon, option=None, widget=None):
            """
            :param standardIcon: QStyle.StandardPixmap | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :return: QIcon
            """
            if self.baseStyle():
                return self.baseStyle().standardIcon(standardIcon, option, widget)
            return super(QProxyStyle, self).standardIcon(standardIcon, option, widget)

        def sliderValueFromPosition(self, minimum, maximum, position, span, upsideDown=False):
            """
            :param minimum: int
            :param maximum: int
            :param position: int
            :param span: int
            :param upsideDown: bool
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().sliderValueFromPosition(minimum, maximum, position, span, upsideDown)
            return super(QProxyStyle, self).sliderValueFromPosition(minimum, maximum, position, span, upsideDown)

        def sliderPositionFromValue(self, minimum, maximum, logicalValue, span, upsideDown=False):
            """
            :param minimum: int
            :param maximum: int
            :param logicalValue: int
            :param span: int
            :param upsideDown: bool
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().sliderPositionFromValue(minimum, maximum, logicalValue, span, upsideDown)
            return super(QProxyStyle, self).sliderPositionFromValue(minimum, maximum, logicalValue, span, upsideDown)

        def generatedIconPixmap(self, iconMode, pixmap, opt):
            """
            :param iconMode: QIcon.Mode | int
            :param pixmap: QPixmap
            :param opt: QStyleOption
            :return: QPixmap
            """
            if self.baseStyle():
                return self.baseStyle().generatedIconPixmap(iconMode, pixmap, opt)
            return super(QProxyStyle, self).generatedIconPixmap(iconMode, pixmap, opt)

        def hitTestComplexControl(self, control, option, pos, widget=None):
            """
            :param control: QStyle.ComplexControl | int
            :param option: QStyleOptionComplex
            :param pos: QPoint
            :param widget: QWidget | None
            :return: QStyle.SubControl | int
            """
            if self.baseStyle():
                return self.baseStyle().hitTestComplexControl(control, option, pos, widget)
            return super(QProxyStyle, self).hitTestComplexControl(control, option, pos, widget)

        def pixelMetric(self, metric, option=None, widget=None):
            """
            :param metric: QStyle.PixelMetric | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().pixelMetric(metric, option, widget)
            return super(QProxyStyle, self).pixelMetric(metric, option, widget)

        def itemPixmapRect(self, rect, p_int, pixmap):
            """
            :param rect: QRect
            :param p_int: int
            :param pixmap: QPixmap
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().itemPixmapRect(rect, p_int, pixmap)
            return super(QProxyStyle, self).itemPixmapRect(rect, p_int, pixmap)

        def itemTextRect(self, fontMetrics, rect, flags, enabled, text):
            """
            :param fontMetrics: QFontMetrics
            :param rect: QRect
            :param flags: int
            :param enabled: bool
            :param text: str | unicode | QString
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().itemTextRect(fontMetrics, rect, flags, enabled, text)
            return super(QProxyStyle, self).itemTextRect(fontMetrics, rect, flags, enabled, text)

        def layoutSpacing(self, control1, control2, orientation, option=None, widget=None):
            """
            :param control1: QSizePolicy.ControlType | int
            :param control2: QSizePolicy.ControlType | int
            :param orientation: Qt.Orientation | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().layoutSpacing(control1, control2, orientation, option, widget)
            return super(QProxyStyle, self).layoutSpacing(control1, control2, orientation, option, widget)

        def proxy(self):
            """
            :return: QStyle
            """
            return self.baseStyle().proxy() if self.baseStyle() else super(QProxyStyle, self).proxy()

        def visualAlignment(self, direction, alignment):
            """
            :param direction: Qt.LayoutDirection | int
            :param alignment: Qt.Alignment | Qt.AlignmentFlag | int
            :return: Qt.Alignment | int
            """
            if self.baseStyle():
                return self.baseStyle().visualAlignment(direction, alignment)
            return super(QProxyStyle, self).visualAlignment(direction, alignment)

        def visualPos(self, direction, rect, point):
            """
            :param direction: Qt.LayoutDirection | int
            :param rect: QRect
            :param point: QPoint
            :return: QPoint
            """
            if self.baseStyle():
                return self.baseStyle().visualPos(direction, rect, point)
            return super(QProxyStyle, self).visualPos(direction, rect, point)

        def visualRect(self, direction, boundingRect, logicalRect):
            """
            :param direction: Qt.LayoutDirection | int
            :param boundingRect: QRect
            :param logicalRect: QRect
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().visualRect(direction, boundingRect, logicalRect)
            return super(QProxyStyle, self).visualRect(direction, boundingRect, logicalRect)

        def combinedLayoutSpacing(self, controls1, controls2, orientation, option=None, widget=None):
            """
            :param controls1: QSizePolicy.ControlTypes | int
            :param controls2: QSizePolicy.ControlTypes | int
            :param orientation: Qt.Orientation | int
            :param option: QStyleOption | None
            :param widget: QWidget | None
            :return: int
            """
            if self.baseStyle():
                return self.baseStyle().combinedLayoutSpacing(controls1, controls2, orientation, option, widget)
            return super(QProxyStyle, self).combinedLayoutSpacing(controls1, controls2, orientation, option, widget)

        def alignedRect(self, direction, alignment, size, rectangle):
            """
            :param direction: Qt.LayoutDirection | int
            :param alignment: Qt.Alignment | Qt.AlignmentFlag | int
            :param size: QSize
            :param rectangle: QRect
            :return: QRect
            """
            if self.baseStyle():
                return self.baseStyle().alignedRect(direction, alignment, size, rectangle)
            return super(QProxyStyle, self).alignedRect(direction, alignment, size, rectangle)

        def drawComplexControl(self, control, option, painter, widget=None):
            """
            :param control: QStyle.ComplexControl | int
            :param option: QStyleOptionComplex
            :param painter: QPainter
            :param widget: QWidget | None
            :return: None
            """
            if self.baseStyle():
                return self.baseStyle().drawComplexControl(control, option, painter, widget)
            return super(QProxyStyle, self).drawComplexControl(control, option, painter, widget)

        def drawControl(self, element, opt, p, widget=None):
            """
            :param element: QStyle.ControlElement | int
            :param opt: QStyleOption
            :param p: QPainter
            :param widget: QWidget | None
            :return: None
            """
            if self.baseStyle():
                return self.baseStyle().drawControl(element, opt, p, widget)
            return super(QProxyStyle, self).drawControl(element, opt, p, widget)

        def drawPrimitive(self, pe, opt, p, widget=None):
            """
            :param pe: QStyle.PrimitiveElement | int
            :param opt: QStyleOption
            :param p: QPainter
            :param widget: QWidget | None
            :return: None
            """
            return self.baseStyle().drawPrimitive(pe, opt, p, widget) if self.baseStyle() else super(
                QProxyStyle, self).drawPrimitive(pe, opt, p, widget)

        def drawItemPixmap(self, painter, rect, p_int, pixmap):
            """
            :param painter: QPainter
            :param rect: QRect
            :param p_int: int
            :param pixmap: QPixmap
            :return: None
            """
            if self.baseStyle():
                return self.baseStyle().drawItemPixmap(painter, rect, p_int, pixmap)
            return super(QProxyStyle, self).drawItemPixmap(painter, rect, p_int, pixmap)

        def drawItemText(self, painter, rect, flags, palette, enabled, text, textRole=None):
            """
            :param painter: QPainter
            :param rect: QRect
            :param flags: int
            :param palette: QPalette
            :param enabled: bool
            :param text: str | unicode | QString
            :param textRole: QPalette.ColorRole | None
            :return: None
            """
            if self.baseStyle():
                return self.baseStyle().drawItemText(painter, rect, flags, palette, enabled, text, textRole)
            return super(QProxyStyle, self).drawItemText(painter, rect, flags, palette, enabled, text, textRole)

        def styleBase(self, style=None):
            """
            :param style: QStyle
            :return: QStyle
            """
            if style:
                self.__style = style  # type: QStyle
                return style
            elif self.__style:
                return self.__style
            return QStyleFactory.create("Fusion")

        def baseStyle(self):
            """
            :return: QStyle
            """
            return self.styleBase()

        def polish(self, paletteApp):
            """
            :param paletteApp: QWidget | QPalette | QPalette
            :return: QPalette | None
            """
            return self.baseStyle().polish(paletteApp) if self.baseStyle() else super(
                QProxyStyle, self).polish(paletteApp)

if not hasattr(QWidget, 'devicePixelRatioF'):
    QWidget.devicePixelRatioF = lambda self, x: float(self.devicePixelRatio(x))
del Signal, Slot
apply_global_fixes(globals())
