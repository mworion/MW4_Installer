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
import venv
import platform
from startup_logging import log
from startup_helper import prt, run, version


def findfile(startDir, pattern):
    """
    """
    for root, dirs, files in os.walk(startDir):
        for name in files:
            if name.find(pattern) >= 0:
                return root + os.sep + name

    return None


class Envbuilder(venv.EnvBuilder):
    """
    """
    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        self.context = None
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        """
        :param context:
        :return:
        """
        self.context = context
        binPath = os.path.dirname(findfile(os.getcwd(), 'activate')) + os.pathsep
        os.environ['PATH'] = binPath + os.environ['PATH']


def run_python_in_venv(venv_context, command) -> bool:
    """
    """
    command = [venv_context.env_exe] + command
    return run(command)


def run_bin_in_venv(venv_context, command) -> bool:
    """
    """
    command[0] = str(pathlib.Path(venv_context.bin_path).joinpath(command[0]))
    return run(command)


def venv_create(venv_path, upgrade=False) -> Envbuilder:
    """
    :param venv_path:
    :param upgrade:
    :return:
    """
    prt('-' * 45)
    prt('MountWizzard4')
    prt('-' * 45)
    prt(f'script version   : {version}')
    prt(f'platform         : {platform.system()}')
    prt(f'machine          : {platform.machine()}')
    prt(f'python           : {platform.python_version()}')
    prt('-' * 45)

    if upgrade:
        prt('Update virtual environment')
        Envbuilder(with_pip=True, upgrade=upgrade)

    existInstall = os.path.isdir('venv')
    if existInstall:
        prt('Activate virtual environment')
    else:
        prt('Install and activate virtual environment')

    venv_builder = Envbuilder(with_pip=True)
    venv_builder.create(venv_path)

    log.header('-' * 100)
    log.header(f'script version   : {version}')
    log.header(f'platform         : {platform.system()}')
    log.header(f'sys.executable   : {sys.executable}')
    log.header(f'actual workdir   : {os.getcwd()}')
    log.header(f'machine          : {platform.machine()}')
    log.header(f'cpu              : {platform.processor()}')
    log.header(f'release          : {platform.release()}')
    log.header(f'python           : {platform.python_version()}')
    log.header(f'python runtime   : {platform.architecture()[0]}')
    log.header(f'upgrade venv     : {upgrade}')
    log.header('-' * 100)

    return venv_builder.context
