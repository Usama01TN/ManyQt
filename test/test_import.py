# -*- coding: utf-8 -*-
"""
Test imports of all modules and submodules.
"""
from subprocess import call, check_output
from sys import executable

apis = {
    'pyqt4': 'PyQt4', 'pyqt5': 'PyQt5', 'pyside': 'PySide', 'pyside2': 'PySide2', 'pyqt6:': "PyQt6"
}  # type: dict[str, str]
submodulesCommon = ['QtCore', 'QtGui', 'QtHelp', 'QtMultimedia', 'QtNetwork', 'QtOpenGL', 'QtPrintSupport', 'QtSql',
                    'QtSvg', 'QtTest', 'QtWidgets', 'QtXml']  # type: list[str]
submodulesQt4 = ['QtXmlPatterns']  # type: list[str]
submodulesQt5 = ['QtMultimediaWidgets', 'QtWebChannel', 'QtWebEngineWidgets', 'QtWebEngineCore', 'QtWebSockets',
                 'QtQml', 'QtXmlPatterns']  # type: list[str]
submodulesQt6 = ['QtSvgWidgets']  # type: list[str]


def getQtVersion(modname):
    """
    :param modname: str | unicode
    :return: bool
    """
    return check_output([executable, '-c', 'import ' + modname + ';from ManyQt.QtCore import QT_VERSION_STR; print(QT_VERSION_STR)'])


def tryImport(modname):
    """
    :param modname: str | unicode
    :return: bool
    """
    return call([executable, '-c', 'import ' + modname]) == 0


def tryImportAnyqt(modname, submodule):
    """
    :param modname: str | unicode
    :param submodule: str | unicode
    :return: bool
    """
    return call([executable, '-c', 'import ' + modname + '; import ManyQt.' + submodule]) == 0


for api in apis:
    modName = apis[api]  # type: str
    if tryImport(modName):
        qtVersion = getQtVersion(modName).decode()  # type: str
        print('-- Found', modName, 'Qt=', qtVersion)
        submodules = list(submodulesCommon)  # type: list[str]
        if qtVersion[0] == '4':
            submodules.extend(submodulesQt4)
        if qtVersion[0] == '5':
            submodules.extend(submodulesQt5)
        if qtVersion[0] == '6':
            submodules.extend(submodulesQt6)
        for submodule in submodules:
            print(submodule, 'Ok' if tryImportAnyqt(modName, submodule) else 'FAIL')
    else:
        print(modName, '-- not found')
