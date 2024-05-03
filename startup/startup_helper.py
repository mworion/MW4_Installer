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
import os
import subprocess
from startup_logging import log

version = '4.0'


def prt(*args):
    """
    :param args:
    :return:
    """
    print('    ', *args)


def clean_system(python_string: str = 'python') -> None:
    """
    :return:
    """
    prt('Clean system site-packages')
    prt('...takes some time')
    ret = os.popen(f'{python_string} -m pip freeze > clean.txt').read()
    prt(ret)
    ret = os.popen(f'{python_string} -m pip uninstall -y -r clean.txt').read()
    prt(ret)
    prt('Clean finished')
    log.info('Clean system site-packages finished')


def run(command: list[str]) -> bool:
    """
    """
    try:
        process = subprocess.Popen(args=command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        for stdout_line in iter(process.stdout.readline, ""):
            if stdout_line:
                prt(stdout_line)
                log.info(stdout_line.strip('\n'))
        output = process.communicate(timeout=60)[0]

    except subprocess.TimeoutExpired as e:
        log.error(e)
        return False
    except Exception as e:
        log.error(f'Error: {e} happened')
        return False
    else:
        retCode = process.returncode

    success = (process.returncode == 0)
    log.debug(f'Exit code:[{retCode}], message:[{output}], success:[{success}]')
    return success


def install_basic_packages(python_string: str = 'python') -> None:
    """
    :return:
    """
    prt('...adding basic packages')
    command = [python_string, '-m', 'pip', 'install', 'pip', '--upgrade']
    run(command)
    command = [python_string, '-m', 'pip', 'install', 'requests', '--upgrade']
    run(command)
    command = [python_string, '-m', 'pip', 'install', 'wheel', '--upgrade']
    run(command)
    command = [python_string, '-m', 'pip', 'install', 'packaging', '--upgrade']
    run(command)
    command = [python_string, '-m', 'pip', 'list']
    run(command)
    log.info('Basic packages installed')
