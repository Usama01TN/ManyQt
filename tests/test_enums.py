# -*- coding: utf-8 -*-
"""
Test enumerations.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .ManyQt.QtCore import Qt
except:
    from ManyQt.QtCore import Qt


def testCommonEnums():
    """
    :return:
    """
    Qt.DisplayRole
    Qt.EditRole
    Qt.DecorationRole
    Qt.UserRole
