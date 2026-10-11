#Pydroid run qt
# ManyQt crash check for Pydroid 3.
# Run it from Pydroid. If it crashes, open 'manyqt_crash_log.txt' (path is printed at the start):
# it contains the exact Python line where the native crash happened.
from os.path import abspath, dirname, join, isfile
from sys import version, stdout, path, modules
from os import W_OK, access, getcwd
from time import time

try:
    from faulthandler import enable
except:
    enable = None

try:
    _here = dirname(abspath(__file__))
    if not access(_here, W_OK):
        raise OSError
except Exception:
    _here = getcwd()
LOG_PATH = join(_here, 'manyqt_crash_log.txt')
_log = open(LOG_PATH, 'w')


def step(message):
    line = '[%7.3fs] %s' % (time() - _t0, message)
    print(line)
    stdout.flush()
    _log.write(line + '\n')
    _log.flush()


_t0 = time()
if enable:
    enable(file=_log, all_threads=True)  # a segfault writes its Python traceback into the log
print('log file:', LOG_PATH)
step('python %s' % version.split()[0])

import ManyQt

step('ManyQt %s from %s' % (ManyQt.__version__, dirname(ManyQt.__file__)))
fixed = isfile(join(dirname(ManyQt.__file__), '_native_helpers.py'))
step('fixed ManyQt installed: %s' % fixed)
if not fixed:
    step('!!! the OLD ManyQt is still installed: reinstall the fixed one (pip install --force-reinstall .)')
step('available bindings on disk: %s' % ManyQt.availableapi())

import ManyQt.QtCore as QtCore

step('selected binding: %s | Qt %s' % (ManyQt.USED_API, QtCore.QT_VERSION_STR))
step('ManyQt folder on sys.path (should be False): %s' % (dirname(ManyQt.__file__) in path))
step('ctypes imported (should be False): %s' % ('ctypes' in modules))

import ManyQt.QtGui
step('ManyQt.QtGui imported')
from ManyQt.QtWidgets import QApplication, QLabel
step('ManyQt.QtWidgets imported')

app = QApplication([])  # type: QApplication
step('QApplication created')
label = QLabel('ManyQt works on this device')  # type: QLabel
label.show()
step('QLabel shown, closing in 3 s')
QtCore.QTimer.singleShot(3000, app.quit)
app.exec_()
step('SUCCESS: event loop finished normally')
