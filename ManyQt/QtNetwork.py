# -*- coding: utf-8 -*-
"""
QtNetwork is a module that provides access to network-related classes and functions.
"""
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

# Names imported from Qt4' QtNetwork module.
__Qt4_QtNetwork = [
    'QAbstractNetworkCache',
    'QAbstractSocket',
    'QAuthenticator',
    # 'QDnsDomainNameRecord',
    # 'QDnsHostAddressRecord',
    # 'QDnsLookup',
    # 'QDnsMailExchangeRecord',
    # 'QDnsServiceRecord',
    # 'QDnsTextRecord',
    'QHostAddress',
    'QHostInfo',
    'QHttpMultiPart',
    'QHttpPart',
    'QLocalServer',
    'QLocalSocket',
    'QNetworkAccessManager',
    'QNetworkAddressEntry',
    'QNetworkCacheMetaData',
    'QNetworkConfiguration',
    'QNetworkConfigurationManager',
    'QNetworkCookie',
    'QNetworkCookieJar',
    'QNetworkDiskCache',
    'QNetworkInterface',
    'QNetworkProxy',
    'QNetworkProxyFactory',
    'QNetworkProxyQuery',
    'QNetworkReply',
    'QNetworkRequest',
    'QNetworkSession',
    'QSsl',
    'QSslCertificate',
    # 'QSslCertificateExtension',
    'QSslCipher',
    'QSslConfiguration',
    # 'QSslEllipticCurve',
    'QSslError',
    'QSslKey',
    # 'QSslPreSharedKeyAuthenticator',
    'QSslSocket',
    'QTcpServer',
    'QTcpSocket',
    'QUdpSocket',
]  # type: list[str]
if USED_API == QT_API_PYQT6:
    from PyQt6.QtNetwork import *
elif USED_API == QT_API_PYQT5:
    from PyQt5.QtNetwork import *
elif USED_API == QT_API_PYQT4:
    from PyQt4.QtNetwork import *
elif USED_API == QT_API_PYSIDE:
    from PySide.QtNetwork import *
elif USED_API == QT_API_PYSIDE2:
    from PySide2.QtNetwork import *
elif USED_API == QT_API_PYSIDE6:
    from PySide6.QtNetwork import *
else:
    raise ImportError("No module named 'QtNetwork' in the selected Qt api ({})".format(USED_API))

apply_global_fixes(globals())
