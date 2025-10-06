# coding=utf-8
"""
Calls undefined methods from qt libraries.
"""
from ctypes import c_void_p, c_double, c_bool, c_int, Structure
from sys import path, platform
from os.path import dirname

if dirname(__file__) not in path:
    path.append(dirname(__file__))

try:
    from ._api import USED_API, QT_API_PYQT4, QT_API_PYSIDE, apply_global_fixes
    from .QtGui import QBrush, QImage, QPainter
    from .sip import unwrapinstance
except:
    from _api import USED_API, QT_API_PYQT4, QT_API_PYSIDE, apply_global_fixes
    from QtGui import QBrush, QImage, QPainter
    from sip import unwrapinstance

try:
    try:
        from ._ctypes import load_qtlib
    except:
        from _ctypes import load_qtlib
except:
    try:
        from ManyQt._ctypes import load_qtlib
    except:
        from ManyQt._ctypes import load_qtlib

__qtlib = load_qtlib('QtGui' if USED_API in [QT_API_PYQT4, QT_API_PYSIDE] else 'QtWidgets')
if platform.lower() in ['win32', 'win64', 'windows']:
    __references = {
        "_blurImagePainter": "?qt_blurImage@@YAXPEAVQPainter@@AEAVQImage@@N_N2H@Z",
        "_blurImage": "?qt_blurImage@@YAXAEAVQImage@@N_NH@Z",
        "_halfScaled": "?qt_halfScaled@@YA?AVQImage@@AEBV1@@Z",
        "_qDrawBorderPixmap": "?qDrawBorderPixmap@@YAXPEAVQPainter@@AEBVQRect@@AEBVQMargins@@AEBVQPixmap@@12AEBUQTileRules@@V?$QFlags@W4DrawingHint@QDrawBorderPixmap@@@@@Z",
        "_qDrawPlainRect": "?qDrawPlainRect@@YAXPEAVQPainter@@AEBVQRect@@AEBVQColor@@HPEBVQBrush@@@Z",
        "_qDrawPlainRect2": "?qDrawPlainRect@@YAXPEAVQPainter@@HHHHAEBVQColor@@HPEBVQBrush@@@Z",
        "_qDrawShadeLine": "?qDrawShadeLine@@YAXPEAVQPainter@@AEBVQPoint@@1AEBVQPalette@@_NHH@Z",
        "_qDrawShadeLine2": "?qDrawShadeLine@@YAXPEAVQPainter@@HHHHAEBVQPalette@@_NHH@Z",
        "_qDrawShadePanel": "?qDrawShadePanel@@YAXPEAVQPainter@@AEBVQRect@@AEBVQPalette@@_NHPEBVQBrush@@@Z",
        "_qDrawShadePanel2": "?qDrawShadePanel@@YAXPEAVQPainter@@HHHHAEBVQPalette@@_NHPEBVQBrush@@@Z",
        "_qDrawShadeRect": "?qDrawShadeRect@@YAXPEAVQPainter@@AEBVQRect@@AEBVQPalette@@_NHHPEBVQBrush@@@Z",
        "_qDrawShadeRect2": "?qDrawShadeRect@@YAXPEAVQPainter@@HHHHAEBVQPalette@@_NHHPEBVQBrush@@@Z",
        "_qDrawWinButton": "?qDrawWinButton@@YAXPEAVQPainter@@AEBVQRect@@AEBVQPalette@@_NPEBVQBrush@@@Z",
        "_qDrawWinButton2": "?qDrawWinButton@@YAXPEAVQPainter@@HHHHAEBVQPalette@@_NPEBVQBrush@@@Z",
        "_qDrawWinPanel": "?qDrawWinPanel@@YAXPEAVQPainter@@AEBVQRect@@AEBVQPalette@@_NPEBVQBrush@@@Z",
        "_qDrawWinPanel2": "?qDrawWinPanel@@YAXPEAVQPainter@@HHHHAEBVQPalette@@_NPEBVQBrush@@@Z",
        "_qFadeEffect": "?qFadeEffect@@YAXPEAVQWidget@@H@Z",
        "_qGeomCalc": "?qGeomCalc@@YAXAEAV?$QVector@UQLayoutStruct@@@@HHHHH@Z",
        "_qScrollEffect": "?qScrollEffect@@YAXPEAVQWidget@@IH@Z",
        "_graphicsItemHighlightSelected":
            "?qt_graphicsItem_highlightSelected@@YAXPEAVQGraphicsItem@@PEAVQPainter@@PEBVQStyleOptionGraphicsItem@@@Z"
    }
else:
    __references = {
        "_blurImagePainter": "_Z12qt_blurImageP8QPainterR6QImagedbbi",
        "_blurImage": "_Z12qt_blurImageR6QImagedbi",
        "_halfScaled": "_Z13qt_halfScaledRK6QImage",
        "_qDrawBorderPixmap": "_Z17qDrawBorderPixmapP8QPainterRK5QRectRK8QMarginsRK7QPixmapS3_S6_RK10QTileRules6QFlagsIN17QDrawBorderPixmap11DrawingHintEE",
        "_qDrawPlainRect": "_Z14qDrawPlainRectP8QPainterRK5QRectRK6QColoriPK6QBrush",
        "_qDrawPlainRect2": "_Z14qDrawPlainRectP8QPainteriiiiRK6QColoriPK6QBrush",
        "_qDrawShadeLine": "_Z14qDrawShadeLineP8QPainterRK6QPointS3_RK8QPalettebii",
        "_qDrawShadeLine2": "_Z14qDrawShadeLineP8QPainteriiiiRK8QPalettebii",
        "_qDrawShadePanel": "_Z15qDrawShadePanelP8QPainterRK5QRectRK8QPalettebiPK6QBrush",
        "_qDrawShadePanel2": "_Z15qDrawShadePanelP8QPainteriiiiRK8QPalettebiPK6QBrush",
        "_qDrawShadeRect": "_Z14qDrawShadeRectP8QPainterRK5QRectRK8QPalettebiiPK6QBrush",
        "_qDrawShadeRect2": "_Z14qDrawShadeRectP8QPainteriiiiRK8QPalettebiiPK6QBrush",
        "_qDrawWinButton": "_Z14qDrawWinButtonP8QPainterRK5QRectRK8QPalettebPK6QBrush",
        "_qDrawWinButton2": "_Z14qDrawWinButtonP8QPainteriiiiRK8QPalettebPK6QBrush",
        "_qDrawWinPanel": "_Z13qDrawWinPanelP8QPainterRK5QRectRK8QPalettebPK6QBrush",
        "_qDrawWinPanel2": "_Z13qDrawWinPanelP8QPainteriiiiRK8QPalettebPK6QBrush",
        "_qFadeEffect": "_Z11qFadeEffectP7QWidgeti",
        "_qGeomCalc": "_Z9qGeomCalcR7QVectorI13QLayoutStructEiiiii",
        "_qScrollEffect": "_Z13qScrollEffectP7QWidgetji",
        "_graphicsItemHighlightSelected": ""
    }


class QLayoutStruct(Structure):
    """
    QLayoutStruct class.
    """
    # Parameters.
    stretch = c_int(0)  # type: c_int
    sizeHint = c_int(0)  # type: c_int
    maximumSize = c_int(2147483647)  # type: c_int
    minimumSize = c_int(0)  # type: c_int
    spacing = c_int(0)  # type: c_int
    expansive = c_bool(False)  # type: c_bool
    empty = c_bool(True)  # type: c_bool
    # Temporary storage
    done = c_bool(False)  # type: c_bool
    # Result.
    pos = c_int(0)  # type: c_int
    size = c_int(0)  # type: c_int

    def init(self, stretchFactor=0, minSize=0):
        """
        :param stretchFactor: int
        :param minSize: int
        :return:
        """
        self.stretch = c_int(stretchFactor)  # type: c_int
        self.minimumSize = self.sizeHint = c_int(minSize)  # type: c_int
        self.maximumSize = c_int(2147483647)  # type: c_int
        self.expansive = c_bool(False)  # type: c_bool
        self.empty = c_bool(True)  # type: c_bool
        self.spacing = c_int(0)  # type: c_int

    def smartSizeHint(self):
        """
        :return: c_int
        """
        return self.minimumSize if self.stretch > c_int(0) else self.sizeHint

    def effectiveSpacer(self, uniformSpacer):
        """
        :param uniformSpacer: c_int | int
        :return: c_int | int
        """
        assert uniformSpacer >= c_int(0) or self.spacing >= c_int(0)
        return uniformSpacer if uniformSpacer >= c_int(0) else self.spacing


def qt_blurImage(*args, **kwargs):
    """
    :param qp: QPainter
    :param blurImage: QImage
    :param radius: float | int
    :param quality: bool
    :param alphaOnly: bool
    :param transposed: int
    :param args: any
    :param kwargs: any
    :return:
    """
    qp = kwargs.pop('qp', None)
    blurImage = kwargs.pop('blurImage', None)
    radius = kwargs.pop('radius', 0)  # type: float
    quality = kwargs.pop('quality', True)  # type: bool
    alphaOnly = kwargs.pop('alphaOnly', False)  # type: bool
    transposed = kwargs.pop('transposed', 0)  # type: int
    qualityCreated = False  # type: bool
    alphaOnlyCreated = False  # type: bool
    radiusCreated = False  # type: bool
    transposedCreated = False  # type: bool
    for x in args:
        if isinstance(x, QPainter):
            qp = x  # type: QPainter
        elif isinstance(x, QImage):
            blurImage = x  # type: QImage
        elif isinstance(x, bool) and not qualityCreated:
            qualityCreated = True  # type: bool
            quality = x  # type: bool
        elif isinstance(x, bool) and not alphaOnlyCreated:
            alphaOnlyCreated = True  # type: bool
            alphaOnly = x  # type: bool
        elif isinstance(x, (int, float)) and not radiusCreated:
            radiusCreated = True  # type: bool
            radius = x  # type: float
        elif isinstance(x, int) and not transposedCreated:
            transposedCreated = True  # type: bool
            transposed = x  # type: int
    if qp and blurImage:
        _blurImagePainter = __qtlib[__references['_blurImagePainter']]
        if callable(_blurImagePainter):
            if qp:
                qp = c_void_p(unwrapinstance(qp))  # type: c_void_p
            _blurImagePainter(qp, c_void_p(unwrapinstance(blurImage)), c_double(radius), c_bool(quality),
                              c_bool(alphaOnly), c_int(transposed))
    else:
        _blurImage = __qtlib[__references['_blurImage']]
        if callable(_blurImage):
            _blurImage(c_void_p(unwrapinstance(blurImage)), c_double(radius), c_bool(quality), c_int(transposed))


def qt_halfScaled(source):
    """
    :param source: QImage
    :return:
    """
    _halfScaled = __qtlib[__references['_halfScaled']]
    if callable(_halfScaled):
        if source:
            source = c_void_p(unwrapinstance(source))  # type: c_void_p
        _halfScaled(source)


def qScrollEffect(widget, orient, time):
    """
    Scroll widget w in time ms.
    orient may be 1 (vertical), 2 (horizontal) or 3 (diagonal).
    :param widget: QWidget
    :param orient: QEffects.DirFlags | int
    :param time: int
    :return:
    """
    _qScrollEffect = __qtlib[__references['_qScrollEffect']]
    if callable(_qScrollEffect):
        _qScrollEffect(c_void_p(unwrapinstance(widget)), c_int(orient), c_int(time))


def qt_graphicsItemHighlightSelected(item, painter, option):
    """
    Highlights item as selected.
    :param item: QGraphicsItem
    :param painter: QPainter
    :param option: QStyleOptionGraphicsItem
    :return:
    """
    _graphicsItemHighlightSelected = __qtlib[__references['_graphicsItemHighlightSelected']]
    if callable(_graphicsItemHighlightSelected):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _graphicsItemHighlightSelected(c_void_p(unwrapinstance(item)), painter, c_void_p(unwrapinstance(option)))


def qGeomCalc(chain, start, count, pos, space, spacer):
    """
    This is the main workhorse of the QGridLayout. It portions out available space to the chain's children.
    The calculation is done in fixed point: "fixed" variables are scaled by a factor of 256.
    If the layout runs "backwards" (i.e. RightToLeft or Up) the layout is computed mirror-reversed,
    and it's the caller's responsibility do reverse the values before use.
    chain contains input and output parameters describing the geometry.
    count is the count of items in the chain; pos and space give the interval (relative to parentWidget topLeft).
    :param chain: List(QLayoutStruct) | list | QVector(QLayoutStruct)
    :param start: int
    :param count: int
    :param pos: int
    :param space: int
    :param spacer: int
    :return:
    """
    _qGeomCalc = __qtlib[__references['_qGeomCalc']]
    if callable(_qGeomCalc):
        _qGeomCalc(chain, c_int(start), c_int(count), c_int(pos), c_int(space), c_int(spacer))


def qFadeEffect(widget, time=-1):
    """
    Fade in widget in time ms.
    :param widget: QWidget
    :param time: int
    :return:
    """
    _qFadeEffect = __qtlib[__references['_qFadeEffect']]
    if callable(_qFadeEffect):
        if widget:
            widget = c_void_p(unwrapinstance(widget))  # type: c_void_p
        _qFadeEffect(widget, c_int(time))


def qDrawBorderPixmap(painter, target, margins, pixmap, *args):
    """
    The qDrawBorderPixmap function is for drawing a pixmap into the margins of a rectangle.
    Draws the given pixmap into the given target rectangle, using the given painter.
    The pixmap will be split into nine segments and drawn according to the margins structure.
    :param painter: QPainter
    :param target: QRect
    :param margins: QMargins
    :param pixmap: QPixmap
    :args: Any
    :return:
    """
    _qDrawBorderPixmap = __qtlib[__references['_qDrawBorderPixmap']]
    if callable(_qDrawBorderPixmap):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawBorderPixmap(painter, c_void_p(unwrapinstance(target)), c_void_p(unwrapinstance(margins)),
                           c_void_p(unwrapinstance(pixmap)), *args)


def qDrawPlainRect(painter, rect, lineColor, lineWidth=1, fill=QBrush()):
    """
    This is an overloaded function.
    Draws the plain rectangle specified by rect using the given painter, lineColor and lineWidth.
    The rectangle's interior is filled with the fill brush unless fill is None.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param lineColor: QColor
    :param lineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawPlainRect = __qtlib[__references['_qDrawPlainRect']]
    if callable(_qDrawPlainRect):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawPlainRect(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(lineColor)), c_int(lineWidth),
                        c_void_p(unwrapinstance(fill)))


def qDrawPlainRect2(painter, x, y, width, height, lineColor, lineWidth=1, fill=QBrush()):
    """
    Draws the plain rectangle beginning at (x, y) with the given width and height, using the specified painter,
    lineColor and lineWidth. The rectangle's interior is filled with the fill brush unless fill is None.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param x: int
    :param y: int
    :param width: int
    :param height: int
    :param lineColor: QColor
    :param lineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawPlainRect2 = __qtlib[__references['_qDrawPlainRect2']]
    if callable(_qDrawPlainRect2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawPlainRect2(painter, c_int(x), c_int(y), c_int(width), c_int(height), c_void_p(unwrapinstance(lineColor)),
                         c_int(lineWidth), c_void_p(unwrapinstance(fill)))


def qDrawShadeLine(painter, p1, p2, palette, sunken=True, lineWidth=1, midLineWidth=0):
    """
    This is an overloaded function.
    Draws a horizontal or vertical shaded line between p1 and p2 using the given painter.
    Note that nothing is drawn if the line between the points would be neither horizontal nor vertical.
    The provided palette specifies the shading colors (light, dark and middle colors).
    The given lineWidth specifies the line width for each of the lines; it is not the total line width.
    The given midLineWidth specifies the width of a middle line drawn in the QPalette.mid() color.
    The line appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param p1: QPoint
    :param p2: QPoint
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param midLineWidth: int
    :return:
    """
    _qDrawShadeLine = __qtlib[__references['_qDrawShadeLine']]
    if callable(_qDrawShadeLine):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadeLine(painter, c_void_p(unwrapinstance(p1)), c_void_p(unwrapinstance(p2)),
                        c_void_p(unwrapinstance(palette)), c_bool(sunken), c_int(lineWidth), c_int(midLineWidth))


def qDrawShadeLine2(painter, rect, palette, sunken=True, lineWidth=1, midLineWidth=0):
    """
    Draws a horizontal (y1 == y2) or vertical (x1 == x2) shaded line using the given painter.
    Note that nothing is drawn if y1 != y2 and x1 != x2 (i.e. the line is neither horizontal nor vertical).
    The provided palette specifies the shading colors (light, dark and middle colors).
    The given lineWidth specifies the line width for each of the lines; it is not the total line width.
    The given midLineWidth specifies the width of a middle line drawn in the QPalette.mid() color.
    The line appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param midLineWidth: int
    :return:
    """
    _qDrawShadeLine2 = __qtlib[__references['_qDrawShadeLine2']]
    if callable(_qDrawShadeLine2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadeLine2(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(palette)),
                         c_bool(sunken), c_int(lineWidth), c_int(midLineWidth))


def qDrawShadePanel(painter, rect, palette, sunken=False, lineWidth=1, fill=QBrush()):
    """
    This is an overloaded function.
    Draws the shaded panel at the rectangle specified by rect using the given painter and the given lineWidth.
    The given palette specifies the shading colors (light, dark and middle colors).
    The panel's interior is filled with the fill brush unless fill is None.
    The panel appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawShadePanel = __qtlib[__references['_qDrawShadePanel']]
    if callable(_qDrawShadePanel):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadePanel(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(palette)), c_bool(sunken),
                         c_int(lineWidth), c_void_p(unwrapinstance(fill)))


def qDrawShadePanel2(painter, x, y, width, height, palette, sunken=False, lineWidth=1, fill=QBrush()):
    """
    Draws the shaded panel beginning at (x, y) with the given width and height using the provided painter and
    the given lineWidth.
    The given palette specifies the shading colors (light, dark and middle colors).
    The panel's interior is filled with the fill brush unless fill is None.
    The panel appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param x: int
    :param y: int
    :param width: int
    :param height: int
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawShadePanel2 = __qtlib[__references['_qDrawShadePanel2']]
    if callable(_qDrawShadePanel2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadePanel2(painter, c_int(x), c_int(y), c_int(width), c_int(height), c_void_p(unwrapinstance(palette)),
                          c_bool(sunken), c_int(lineWidth), c_void_p(unwrapinstance(fill)))


def qDrawShadeRect(painter, rect, palette, sunken=False, lineWidth=1, midLineWidth=0, fill=QBrush()):
    """
    This is an overloaded function.
    Draws the shaded panel at the rectangle specified by rect using the given painter and the given lineWidth.
    The given palette specifies the shading colors (light, dark and middle colors).
    The panel's interior is filled with the fill brush unless fill is None.
    The panel appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param midLineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawShadeRect = __qtlib[__references['_qDrawShadeRect']]
    if callable(_qDrawShadeRect):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadeRect(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(palette)), c_bool(sunken),
                        c_int(lineWidth), c_int(midLineWidth), c_void_p(unwrapinstance(fill)))


def qDrawShadeRect2(painter, x, y, width, height, palette, sunken=False, lineWidth=1, midLineWidth=0, fill=QBrush()):
    """
    Draws the shaded rectangle beginning at (x, y) with the given width and height using the provided painter.
    The provide palette specifies the shading colors (light, dark and middle colors.
    The given lineWidth specifies the line width for each of the lines; it is not the total line width.
    The midLineWidth specifies the width of a middle line drawn in the QPalette.mid() color.
    The rectangle's interior is filled with the fill brush unless fill is None.
    The rectangle appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param x: int
    :param y: int
    :param width: int
    :param height: int
    :param palette: QPalette
    :param sunken: bool
    :param lineWidth: int
    :param midLineWidth: int
    :param fill: QBrush
    :return:
    """
    _qDrawShadeRect2 = __qtlib[__references['_qDrawShadeRect2']]
    if callable(_qDrawShadeRect2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawShadeRect2(painter, c_int(x), c_int(y), c_int(width), c_int(height), c_void_p(unwrapinstance(palette)),
                         c_bool(sunken), c_int(lineWidth), c_int(midLineWidth), c_void_p(unwrapinstance(fill)))


def qDrawWinButton(painter, rect, palette, sunken=False, fill=QBrush()):
    """
    This is an overloaded function.
    Draws the Win-style button at the rectangle specified by rect using the given painter with a line width of 2 pixels.
    The button's interior is filled with the fill brush unless fill is None.
    The given palette specifies the shading colors (light, dark and middle colors).
    The button appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style()-> Use the drawing functions in
             QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param palette: QPalette
    :param sunken: bool
    :param fill: QBrush
    :return:
    """
    _qDrawWinButton = __qtlib[__references['_qDrawWinButton']]
    if callable(_qDrawWinButton):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawWinButton(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(palette)), c_bool(sunken),
                        c_void_p(unwrapinstance(fill)))


def qDrawWinButton2(painter, x, y, width, height, palette, sunken=False, fill=QBrush()):
    """
    Draws the Windows-style button specified by the given point (x, y},
    width and height using the provided painter with a line width of 2 pixels.
    The button's interior is filled with the fill brush unless fill is None.
    The given palette specifies the shading colors (light, dark and middle colors).
    The button appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style()-> Use the drawing functions in
             QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param x: int
    :param y: int
    :param width: int
    :param height: int
    :param palette: QPalette
    :param sunken: bool
    :param fill: QBrush
    :return:
    """
    _qDrawWinButton2 = __qtlib[__references['_qDrawWinButton2']]
    if callable(_qDrawWinButton2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawWinButton2(painter, c_int(x), c_int(y), c_int(width), c_int(height), c_void_p(unwrapinstance(palette)),
                         c_bool(sunken), c_void_p(unwrapinstance(fill)))


def qDrawWinPanel(painter, rect, palette, sunken=False, fill=QBrush()):
    """
    This is an overloaded function.
    Draws the Win-style panel at the rectangle specified by rect using the given painter with a line width of 2 pixels.
    The button's interior is filled with the fill brush unless fill is None.
    The given palette specifies the shading colors. The panel appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param rect: QRect
    :param palette: QPalette
    :param sunken: bool
    :param fill: QBrush
    :return:
    """
    _qDrawWinPanel = __qtlib[__references['_qDrawWinPanel']]
    if callable(_qDrawWinPanel):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawWinPanel(painter, c_void_p(unwrapinstance(rect)), c_void_p(unwrapinstance(palette)), c_bool(sunken),
                       c_void_p(unwrapinstance(fill)))


def qDrawWinPanel2(painter, x, y, width, height, palette, sunken=False, fill=QBrush()):
    """
    Draws the Windows-style panel specified by the given point(x, y),
    width and height using the provided painter with a line width of 2 pixels.
    The button's interior is filled with the fill brush unless fill is None.
    The given palette specifies the shading colors. The panel appears sunken if sunken is true, otherwise raised.
    Warning: This function does not look at QWidget.style() or QApplication.style().
             Use the drawing functions in QStyle to make widgets that follow the current GUI style.
    :param painter: QPainter
    :param x: int
    :param y: int
    :param width: int
    :param height: int
    :param palette: QPalette
    :param sunken: bool
    :param fill: QBrush
    :return:
    """
    _qDrawWinPanel2 = __qtlib[__references['_qDrawWinPanel2']]
    if callable(_qDrawWinPanel2):
        if painter:
            painter = c_void_p(unwrapinstance(painter))  # type: c_void_p
        _qDrawWinPanel2(painter, c_int(x), c_int(y), c_int(width), c_int(height), c_void_p(unwrapinstance(palette)),
                        c_bool(sunken), c_void_p(unwrapinstance(fill)))

apply_global_fixes(globals())
