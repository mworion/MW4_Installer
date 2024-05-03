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
# GUI with PyQT5 for python
#
# written in python3, (c) 2019-2024 by mworion
# Licence APL2.0
#
###########################################################
from invoke import task
import os
import zipapp
import zipfile

rn = ''
#
# defining all necessary virtual client login for building over all platforms
#


def runMW(c, param):
    c.run(param)


def printMW(param):
    print(param)


@task()
def test_mw(c):
    printMW('testing mountwizzard4')
    runMW(c, 'flake8')
    runMW(c, 'pytest tests/unit_tests/zLoader')
    printMW('testing mountwizzard finished\n')


@task(pre=[])
def build(c):
    printMW('...make zip archive')
    zipapp.create_archive('./startup',
                          target='./support/startup.pyz',
                          compressed=True)
    zipapp.create_archive('./startup',
                          target='./work/startup.pyz',
                          compressed=True)
    os.chdir('./support')
    with zipfile.ZipFile('startupPackage.zip', 'w') as myzip:
        myzip.write('startup.pyz')
        myzip.write('MountWizzard4.desktop')
        myzip.write('mw4.ico')
        myzip.write('mw4.png')
    os.chdir('../')
    printMW('...copy install script to test dir')
