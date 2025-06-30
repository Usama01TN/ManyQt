# -*- coding: utf-8 -*-
"""
Provide a CLI to allow configuring developer settings, including mypy.
"""
# Standard library imports.
from argparse import RawTextHelpFormatter, ArgumentParser
from textwrap import dedent
from json import dumps


def printVersion():
    """
    Print the current version of the package.
    :return:
    """
    from os.path import dirname
    from sys import path

    path.append(dirname(__file__))
    path.append(dirname(dirname(__file__)))

    try:
        from .ManyQt import __version__
    except:
        from ManyQt import __version__

    print("ManyQt version", __version__)


def getApiStatus():
    """
    Get the status of each Qt API usage.
    :return: dict[str | unicode, bool]
    """
    from os.path import dirname
    from sys import path

    path.append(dirname(__file__))
    path.append(dirname(dirname(__file__)))

    try:
        from .ManyQt import USED_API, availableapi
    except:
        from ManyQt import USED_API, availableapi

    return {name: name == USED_API for name in availableapi()}


def generateMypyArgs():
    """
    Generate a string with always-true/false args to pass to mypy.
    :return: str | unicode
    """
    options = {False: "--always-false", True: "--always-true"}  # type: dict[bool, str]
    apisActive = getApiStatus()
    return " ".join("{}={}".format(options[is_active], name.upper()) for name, is_active in apisActive.items())


def generatePyrightConfigJson():
    """
    Generate Pyright config to be used in `pyrightconfig.json`.
    :return: str | unicode
    """
    apisActive = getApiStatus()
    return dumps({"defineConstant": {name.upper(): is_active for name, is_active in apisActive.items()}})


def generatePyrightConfigToml():
    """
    Generate a Pyright config to be used in `pyproject.toml`.
    :return: str | unicode
    """
    apisActive = getApiStatus()  # type: dict[str, bool]
    return "[tool.pyright.defineConstant]\n" + "\n".join(
        "{} = {}".format(name.upper(), str(is_active).lower()) for name, is_active in apisActive.items())


def printMypyArgs():
    """
    Print the generated mypy args to stdout.
    :return:
    """
    print(generateMypyArgs())


def printPyrightConfigJson():
    """
    Print the generated Pyright JSON config to stdout.
    :return:
    """
    print(generatePyrightConfigJson())


def printPyrightConfigToml():
    """
    Print the generated Pyright TOML config to stdout.
    :return:
    """
    print(generatePyrightConfigToml())


def printPyrightConfigs():
    """
    Print the generated Pyright configs to stdout.
    :return:
    """
    print("pyrightconfig.json:")
    printPyrightConfigJson()
    print()
    print("pyproject.toml:")
    printPyrightConfigToml()


def generateArgParser():
    """
    Generate the argument parser for the dev CLI for ManyQt.
    :return: ArgumentParser
    """
    parser = ArgumentParser(description="Features to support development with ManyQt.")  # type: ArgumentParser
    parser.set_defaults(func=parser.print_help)
    parser.add_argument("--version", action="store_const", dest="func", const=printVersion,
                        help="If passed, will print the version and exit")
    cliSubparsers = parser.add_subparsers(title="Subcommands", help="Subcommand to run", metavar="Subcommand")
    # Parser for the MyPy args subcommand
    mypyArgsParser = cliSubparsers.add_parser(
        name="mypy-args",
        help="Generate command line arguments for using mypy with ManyQt.",
        formatter_class=RawTextHelpFormatter,
        description=dedent(
            """
            Generate command line arguments for using mypy with ManyQt.

            This will generate strings similar to the following
            which help guide mypy through which library ManyQt would have used
            so that mypy can get the proper underlying type hints.

                --always-false=PYQT5 --always-false=PYQT6 --always-true=PYSIDE2 --always-false=PYSIDE6

            It can be used as follows on Bash or a similar shell:

                mypy --package mypackage $(manyqt mypy-args)
            """,
        ),
    )
    mypyArgsParser.set_defaults(func=printMypyArgs)
    # Parser for the Pyright config subcommand.
    pyrightConfigParser = cliSubparsers.add_parser(
        name="pyright-config",
        help="Generate Pyright config for using Pyright with ManyQt.",
        formatter_class=RawTextHelpFormatter,
        description=dedent(
            """
            Generate Pyright config for using Pyright with ManyQt.

            This will generate config sections to be included in a Pyright
            config file (either `pyrightconfig.json` or `pyproject.toml`)
            which help guide Pyright through which library ManyQt would have used
            so that Pyright can get the proper underlying type hints.

            """,
        ),
    )
    pyrightConfigParser.set_defaults(func=printPyrightConfigs)
    return parser


def main(args=None):
    """
    Run the development CLI for ManyQt.
    :param args: str | unicode | None
    :return:
    """
    parser = generateArgParser()  # type: generateArgParser
    parsedArgs = parser.parse_args(args=args)
    reservedParams = {"func"}
    parsedArgs.func(**{key: value for key, value in vars(parsedArgs).items() if key not in reservedParams})
