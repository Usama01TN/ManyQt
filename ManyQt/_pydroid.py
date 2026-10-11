# -*- coding: utf-8 -*-
"""
Pydroid 3 (Android) support.

Pydroid 3 chooses how to start a script *before* running it, by searching the script text:
PySide6 (Qt) mode is only enabled when the script contains ``import PySide6``, ``from PySide6`` or the special
comment ``#Pydroid run qt``. A script that only imports ``ManyQt`` is therefore started in *terminal* mode, where
there is no Android Qt window/surface, and creating ``QApplication``/``QGuiApplication`` crashes the interpreter with
``Segmentation fault``. A library cannot switch the mode itself (the choice is made before Python starts), so this
module only detects the situation and prints a clear message *before* the crash happens.

Set the environment variable ``MANYQT_NO_PYDROID_CHECK=1`` to disable the check.
"""
from os.path import isfile, basename
from os import environ, sep
import sys
import io

# Exact markers Pydroid 3 looks for (PyQt5 ones are used by Pydroid 3 releases older than 7.0).
_PYDROID_QT_MARKERS = (
    "#Pydroid run qt",
    "import PySide6",
    "from PySide6",
    "import PyQt5",
    "from PyQt5",
)  # type: tuple[str, ...]

_MESSAGE = """
=============================================================================
ManyQt: Pydroid 3 detected, but the script
    {script}
does not contain "#Pydroid run qt" (nor "import PySide6" / "from PySide6").
Pydroid 3 therefore started it in TERMINAL mode, where Qt has no window to
draw on: creating QApplication or QGuiApplication will crash with
"Segmentation fault".

FIX: add this line at the very top of your main script, then run it again:

#Pydroid run qt

(Set MANYQT_NO_PYDROID_CHECK=1 to silence this message.)
=============================================================================
"""  # type: str

_checked = False  # type: bool


def is_android():
    """
    :return: bool
    """
    return hasattr(sys, "getandroidapilevel") or "ANDROID_ROOT" in environ or "ANDROID_DATA" in environ


def is_pydroid():
    """
    :return: bool
    """
    if not is_android():
        return False
    candidates = [sys.prefix, sys.exec_prefix, sys.executable or "", environ.get("HOME", ""),
                  environ.get("PYTHONHOME", "")]  # type: list[str]
    return any("pydroid" in str(candidate).lower() for candidate in candidates)


def _is_pydroid_launcher(filename):
    """
    Pydroid's own launcher (.../accomp_files/iiec_run/iiec_run.py), never the user's script.
    :param filename: str | unicode
    :return: bool
    """
    return basename(filename).startswith("iiec_run") or (sep + "accomp_files" + sep) in filename


def _candidate_scripts():
    """
    Pydroid 3 does not run the user's file directly: its launcher calls ``start(fakepyfile, mainpyfile)`` which
    does ``exec(open(mainpyfile).read(), __main__.__dict__)``. So ``__main__.__file__`` is not reliable; the paths
    are read from the launcher's frames (the import of ManyQt happens inside that ``exec``), with
    ``__main__.__file__`` and ``sys.argv[0]`` as fallbacks.
    :return: list[str | unicode]
    """
    found = []  # type: list[str]

    def add(filename):
        """
        :param filename: any
        :return: None
        """
        if isinstance(filename, str) and filename.endswith((".py", ".pyw")) and filename not in found:
            found.append(filename)

    frame = sys._getframe(0) if hasattr(sys, "_getframe") else None
    while frame is not None:
        try:
            frameLocals = frame.f_locals
            add(frameLocals.get("mainpyfile"))
            add(frameLocals.get("fakepyfile"))
        except Exception:
            pass
        frame = frame.f_back
    add(getattr(sys.modules.get("__main__"), "__file__", None))
    if sys.argv:
        add(sys.argv[0])
    return [filename for filename in found if not _is_pydroid_launcher(filename) and isfile(filename)]


def check_pydroid_run_mode():
    """
    Print an explanation when running under Pydroid 3 in terminal mode, where QApplication would segfault.
    Never raises.
    :return: bool (True when the warning was printed)
    """
    global _checked
    if _checked:
        return False
    _checked = True
    try:
        if environ.get("MANYQT_NO_PYDROID_CHECK", "").strip() not in ("", "0"):
            return False
        if not is_pydroid():
            return False
        scripts = _candidate_scripts()  # type: list[str]
        if not scripts:
            return False  # Interactive interpreter, unknown launcher, ...: cannot tell, stay silent.
        for script in scripts:
            with io.open(script, "r", encoding="utf-8", errors="replace") as f:
                source = f.read()  # type: str
            if any(marker in source for marker in _PYDROID_QT_MARKERS):
                return False
        sys.stderr.write(_MESSAGE.format(script=scripts[0]))
        sys.stderr.flush()
        return True
    except Exception:
        return False
