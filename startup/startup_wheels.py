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
import sys
from packaging.utils import Version
from startup_logging import log
from startup_helper import prt
from startup_env import run_python_in_venv


def download_and_install_wheels(venv_context, version: Version) -> bool:
    """
    """
    preRepo = 'https://github.com/mworion/InstallerMW4'
    preSource = '/raw/main/wheels/'
    postRepo = ''
    wheels = {
        '2.0.0': {
            '3.8': [
                'sep-1.2.0-cp38-cp38-linux_aarch64.whl',
                'sgp4-2.20-cp38-cp38-linux_aarch64.whl',
                'pyerfa-2.0.0-cp38-cp38-linux_aarch64.whl',
                'astropy-4.3.1-cp38-cp38-linux_aarch64.whl',
                'PyQt5_sip-12.8.1-cp38-cp38-linux_aarch64.whl',
                'PyQt5-5.15.4-cp36.cp37.cp38.cp39-abi3-manylinux2014_aarch64.whl',
            ],
            '3.9': [
                'sep-1.2.0-cp39-cp39-linux_aarch64.whl',
                'sgp4-2.20-cp39-cp39-linux_aarch64.whl',
                'pyerfa-2.0.0-cp39-cp39-linux_aarch64.whl',
                'astropy-4.3.1-cp39-cp39-linux_aarch64.whl',
                'PyQt5_sip-12.8.1-cp39-cp39-linux_aarch64.whl',
                'PyQt5-5.15.4-cp36.cp37.cp38.cp39-abi3-manylinux2014_aarch64.whl',
            ],
            '3.10': [
                'sep-1.2.0-cp310-cp310-linux_aarch64.whl',
                'sgp4-2.20-cp310-cp310-linux_aarch64.whl',
                'pyerfa-2.0.0-cp310-cp310-linux_aarch64.whl',
                'astropy-4.3.1-cp310-cp310-linux_aarch64.whl',
                'PyQt5_sip-12.8.1-cp310-cp310-linux_aarch64.whl',
                'PyQt5-5.15.4-cp36.cp37.cp38.cp39-abi3-manylinux2014_aarch64.whl',
            ],
        },
        '3.0.0': {
            '3.8': [
                'PyQt5_sip-12.11.1-cp38-cp38-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.9': [
                'PyQt5_sip-12.11.1-cp39-cp39-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.10': [
                'PyQt5_sip-12.11.1-cp310-cp310-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
        },
        '4.0.0': {
            '3.9': [
                'PyQt5_sip-13.6.0-cp39-cp39-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.10': [
                'PyQt5_sip-13.6.0-cp310-cp310-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.11': [
                'PyQt5_sip-13.6.0-cp311-cp311-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.12': [
                'PyQt5_sip-13.6.0-cp312-cp312-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
        },
    }
    log.info(f'Got version {version}')
    prt(f'Install precompiled packages for {version}')

    if version < Version('2.0.0'):
        log.info('No actual supported version')
        prt('...no supported version')
        return False
    elif version < Version('3.0.0'):
        versionKey = '2.0.0'
        log.info('Path version 2.x.y')
    elif version < Version('4.0.0'):
        versionKey = '3.0.0'
        log.info('Path version 3.x.y')
    else:
        versionKey = '4.0.0'
        log.info('Path version 4.x.y')

    ver = f'{sys.version_info[0]}.{sys.version_info[1]}'
    for item in wheels[versionKey][ver]:
        prt(f'...{item.split("-")[0]}-{item.split("-")[1]}')
        command = ['-m', 'pip', 'install', preRepo + preSource + item + postRepo]
        suc = run_python_in_venv(venv_context, command)
        if not suc:
            prt('...error install precompiled packages')
            return False
    prt('Precompiled packages ready')
    return True
