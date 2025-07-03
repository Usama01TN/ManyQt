# 📚 ManyQt

**ManyQt** is a lightweight abstraction layer that enables developers to write applications with a single API targeting PyQt and PySide. It supports multiple Qt versions and bindings—**PyQt4, PyQt5, PySide, PySide2, PyQt6, and PySide6**—under a **Qt5-style layout**, where `QtGui` and `QtWidgets` are separated.

*(Inspired from [QtPy](https://github.com/spyder-ide/qtpy) and [AnyQt](https://github.com/ales-erjavec/anyqt).)*

---

## 🛠️ Installation:

### From PyPI (recommended):
```bash
pip install ManyQt
```

### From GitHub (latest development version):
```bash
pip install git+https://github.com/Usama01TN/manyqt.git
```
or for a specific branch:
```bash
pip install git+https://github.com/Usama01TN/manyqt.git@branch-name
```

Note: ManyQt itself has no dependencies, but you must have at least one Qt binding installed (PyQt or PySide variant). To install a Qt binding alongside ManyQt:

```bash
pip install ManyQt pyqt5  # or pyqt6, pyside2, pyside6, etc...
```

---

## 🚀 Purpose & Benefits:

ManyQt simplifies cross-version and cross-binding development:

- Write your code using **standard Qt API patterns**.
- Import from `manyqt` instead of `PyQtX` or `PySideX`.
- Seamlessly **port between** Qt4, Qt5, and Qt6.
- Resolve incompatibilities automatically.
- Incrementally migrate large codebases—**module by module**.

---

## 🧰 Requirements:

To use **ManyQt**, you must have one of the following libraries installed:

- `PyQt4`
- `PyQt5`
- `PyQt6`
- `PySide`
- `PySide2`
- `PySide6`

If multiple packages are available, **`PyQt5` is selected by default** unless overridden by an environment variable.

---

## ⚙️ Selecting the Backend:

The active Qt binding can be set using the `QT_API` environment variable:

| Value     | Selects |
|-----------|---------|
| `pyqt4`   | PyQt4   |
| `pyqt5`   | PyQt5   |
| `pyqt6`   | PyQt6   |
| `pyside`  | PySide  |
| `pyside2` | PySide2 |
| `pyside6` | PySide6 |

Alternatively, you may also configure the API **programmatically**—as long as no other Qt libraries have been imported yet.

---

## 🧩 Features at a Glance:

### 🧭 Unified Namespace:

Provides a consistent, Qt5-compatible module layout with some minor renaming for portability.

### 🧪 Environment & Code-Based Selection:

Specify your preferred binding via:

- `QT_API` environment variable.
- Python code (early in execution).

### 🛡️ Safe Import Hook (Optional):

Includes an import guard that:

- Detects and blocks mixed Qt binding imports.
- Emulates Qt4-style imports via **Qt5-compatible monkey patching**.

### 📋 Simple Usage:

```python
from os import environ
environ["QT_API"] = "pyqt5"  # or "pyqt4", "pyside", "pyside2", "pyqt6", "pyside6", to force a specific backend.
from ManyQt.QtWidgets import *
from ManyQt.QtCore import *
from ManyQt.QtGui import *
```
