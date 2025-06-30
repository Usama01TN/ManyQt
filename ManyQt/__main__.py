# -*- coding: utf-8 -*-
"""
Dev CLI entry point for ManyQt, a compat layer for the Python Qt bindings.
"""
from os.path import dirname
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from . import cli
except:
    import cli


def main():
    """
    :return: None
    """
    return cli.main()


if __name__ == "__main__":
    main()
