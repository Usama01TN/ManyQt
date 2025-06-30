.. ManyQt documentation master file, created by
sphinx-quickstart on 2025.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Welcome to ManyQt's documentation!
=================================

ManyQt is a PyQt/PySide compatibility layer intended as a stepping stone to
full Qt's support while still providing support for all PyQtX and PySideX.

The idea is to use use a forward compatible module structure that mimics that
of PyQtX, even when using PySideX

By default PyQt5 is used if available, but that can be changed by a QT_API env
variable (which can take either 'pyqt4' or 'pyqt5', ... values), or setting the
preferred api using the :func:`ManyQt.setpreferredapi`. However if any of the
Qt apis is already imported (listed in `sys.modules`) then it is used instead.

.. note::
   The final choice of api is delayed until the first ManyQt.Qt* module
   is imported


Contents:

.. toctree::
   :maxdepth: 2

   manyqt


Indices and tables:
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
