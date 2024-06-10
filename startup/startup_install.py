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
import glob
import platform
from packaging.utils import Version
from startup_helper import prt
from startup_logging import log
from startup_env import run_python_in_venv
from startup_versions import get_app_version
from startup_wheels import download_and_install_wheels


def install_app(venv_context, version='', is_test=False):
    """
    """
    command = ['-m', 'pip', 'install', 'wheel']
    run_python_in_venv(venv_context, command)
    command = ['-m', 'pip', 'install', 'pip', '-U']
    run_python_in_venv(venv_context, command)

    if is_test:
        prt('Install local package mountwizzard4.tar.gz')
        command = ['-m', 'pip', 'install', 'mountwizzard4.tar.gz']
    else:
        prt(f'Install version {version}')
        command = ['-m', 'pip', 'install', f'mountwizzard4=={version}']

    prt('...this will take some time')
    suc = run_python_in_venv(venv_context, command)
    log.info(f'Installed app with success: {suc}')
    return suc


def check_if_installed(venv_context) -> tuple:
    """
    """
    app_loader_search_path = venv_context.env_dir + '/lib/**/mw4/loader.py'
    solutions = glob.glob(app_loader_search_path, recursive=True)
    is_installed = len(solutions) == 1
    if is_installed:
        loader_path = [solutions[0]]
    else:
        loader_path = ''
    log.info(f'App is installed: {is_installed}, path: {loader_path}')
    return is_installed, loader_path


def install(venv_context, beta: bool = False, version_string: str = '') -> str:
    """
    """
    is_test = os.path.isfile('mountwizzard4.tar.gz')
    version_app = get_app_version(is_test, beta, version_string)
    isV2 = Version('2.999') > version_app > Version('1.999')
    isV3 = Version('3.999') > version_app > Version('2.999')
    isV4 = Version('4.999') > version_app > Version('3.999')

    version_python = Version(platform.python_version())
    compatibleV2 = version_python < Version('3.10')
    compatibleV3 = Version('3.8') <= version_python < Version('3.11')
    compatibleV4 = Version('3.10') <= version_python < Version('3.13')

    if isV2 and not compatibleV2:
        prt('MountWizzard4 v2.x needs python 3.7-3.9')
        log.error('MountWizzard4 v2.x needs python 3.7-3.9')
        return ''

    elif isV3 and not compatibleV3:
        prt('MountWizzard4 v3.x needs python 3.8-3.10')
        log.error('MountWizzard4 v3.x needs python 3.8-3.10')
        return ''

    elif isV4 and not compatibleV4:
        prt('MountWizzard4 v4.x needs python 3.10-3.12')
        log.error('MountWizzard4 v4.x needs python 3.10-3.12')
        return ''

    elif platform.machine() == 'aarch64':
        suc = download_and_install_wheels(venv_context, version=version_app)
        if not suc:
            log.error('Failed to install precompiled wheels')
            return ''
            
    elif platform.machine() == 'armv7':
        log.error('No support for ARM7')
        return ''

    prt('MountWizzard4 installing')
    suc = install_app(venv_context, version=version_app, is_test=is_test)
    if not suc:
        log.error('Failed to install MountWizzard4')
        return ''

    _, loader_path = check_if_installed(venv_context)
    return loader_path
