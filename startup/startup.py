############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Installer for MountWizzard4
#
# a Python-based Tool for interaction with the
# 10micron mounts GUI with PyQT5/6
#
# written in python3, (c) 2019-2024 by mworion
# Licence APL2.0
#
###########################################################
import os
import sys
import pathlib
import platform
import argparse
from startup_helper import prt, clean_system
from startup_env import run_python_in_venv, venv_create
from startup_versions import version_script_online, version_script_local
from startup_install import install, check_if_installed


def check_base_compatibility() -> bool:
    """
    """
    compatible = True
    if not hasattr(sys, 'base_prefix'):
        compatible = False
    if platform.machine() in ['armv7l']:
        compatible = False
    return compatible


def checking_app_start() -> bool:
    """
    """
    prt()
    if version_script_online() > version_script_local():
        prt('-' * 45)
        prt('Newer version of startup script available')
        prt('-' * 45)

    if not check_base_compatibility():
        prt('-' * 45)
        prt('Startup - no compatible virtual environment')
        prt('- needs python 3.7-3.9 for MW4 version 2.x')
        prt('- needs python 3.8-3.10 for MW4 version 3.x')
        prt('- needs python 3.9-3.12 for MW4 version 4.x')
        prt('- no support for ARM7')
        prt(f'You are running {platform.python_version()}')
        prt('...closing startup script')
        prt('-' * 45)
        prt()
        return False
    return True


def main(options: argparse.Namespace) -> int:
    """
    """
    if not checking_app_start():
        return 1

    if platform.system() == 'Windows':
        os.environ['QT_SCALE_FACTOR'] = f'{options.scale:2.1f}'
        os.environ['QT_FONT_DPI'] = f'{options.dpi:2.0f}'

    if options.clean:
        clean_system()

    venv_path = pathlib.Path.cwd().joinpath('venv')
    venv_context = venv_create(venv_path, upgrade=options.venv)

    is_installed, loader_path = check_if_installed(venv_context)

    if not is_installed or options.update:
        loader_path = install(venv_context, beta=options.updateBeta,
                              version_string=options.version)

    if not options.noStart and loader_path:
        prt('MountWizzard4 starting')
        suc = run_python_in_venv(venv_context, loader_path)
        if not suc:
            prt('...failed to start MountWizzard4')
            prt()
            return 1
        prt('...closing MountWizzard4')
        prt()
        return 0
    elif not loader_path:
        prt('Install failed')
        prt()
        return 1
