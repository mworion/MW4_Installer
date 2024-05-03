############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Python-based Tool for interaction with the 10micron mounts
# GUI with PyQT5 for python3
#
# written in python3, (c) 2019-2024 by mworion
# Licence APL2.0
#
###########################################################
import sys
import platform
import argparse
from startup import main
from startup_logging import setupLogging, addLoggingLevel, log
from startup_helper import install_basic_packages

setupLogging()
addLoggingLevel('HEADER', 55)

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if platform.system() == 'Windows':
    py = 'python'
else:
    py = 'python3'

try:
    import requests
except ImportError:
    log.info('Installing basic packages - requests missing')
    install_basic_packages(python_string=py)
    import requests

try:
    from packaging.utils import Version
except ImportError:
    log.info('Installing basic packages - packaging missing')
    install_basic_packages(python_string=py)
    from packaging.utils import Version


def read_options() -> argparse.Namespace:
    """
    :return:
    """
    parser = argparse.ArgumentParser(
        prog=__name__, description='Installs MountWizzard4 in Python virtual '
                                   'environment in local workdir')
    parser.add_argument(
        '-c', '--clean', default=False, action='store_true', dest='clean',
        help='Cleaning system packages from faulty installs')
    parser.add_argument(
        '-d', '--dpi', default=96, type=float, dest='dpi',
        help='Setting QT font DPI (+dpi = -fontsize, default=96)')
    parser.add_argument(
        '-n', '--no-start', default=False, action='store_true', dest='noStart',
        help='Running script without starting MountWizzard4')
    parser.add_argument(
        '-s', '--scale', default=1, type=float, dest='scale',
        help='Setting Qt DPI scale factor (+scale = +size, default=1)')
    parser.add_argument(
        '-u', '--update', default=False, action='store_true', dest='update',
        help='Update MountWizzard4 to the actual release version')
    parser.add_argument(
        '--update-beta', default=False, action='store_true', dest='updateBeta',
        help='Update MountWizzard4 to the actual beta version')
    parser.add_argument(
        '--update-venv', default=False, action='store_true', dest='venv',
        help='Update the virtual environment directory to use this version of '
             'Python, assuming Python has been upgraded in-place.')
    parser.add_argument(
        '-v', '--version', default='', type=str, dest='version',
        help='Update MountWizzard4 to the named version')

    options = parser.parse_args()
    log.debug(f'Options: {options}')
    return options


# here we start the main application

options = read_options()
exit_code = main(options=options)
sys.exit(exit_code)

