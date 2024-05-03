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
from PIL import Image
import glob
import time
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


@task
def version_doc(c):
    printMW('changing the version number to setup.py')

    # getting version of desired package
    with open('setup.py', 'r') as setup:
        text = setup.readlines()

    for line in text:
        if line.strip().startswith('version'):
            _, number, _ = line.split("'")

    # reading configuration file
    with open('./doc/source/conf.py', 'r') as conf:
        text = conf.readlines()
    textNew = list()

    print(f'version is >{number}<')

    # replacing the version number
    for line in text:
        if line.startswith('version'):
            line = f"version = '{number}'\n"
        if line.startswith('release'):
            line = f"release = '{number}'\n"
        textNew.append(line)

    # writing configuration file
    with open('./doc/source/conf.py', 'w+') as conf:
        conf.writelines(textNew)
    printMW('changing the version number to setup.py finished\n')


@task()
def test_mw(c):
    printMW('testing mountwizzard4')
    runMW(c, 'flake8')
    runMW(c, 'pytest tests/unit_tests/zLoader')
    printMW('testing mountwizzard finished\n')


@task(pre=[])
def build_startup(c):
    printMW('...make zip archive')
    zipapp.create_archive('./startup',
                          target='./support/startup.pyz',
                          compressed=True)
    os.chdir('./support')
    with zipfile.ZipFile('startupPackage.zip', 'w') as myzip:
        myzip.write('startup.pyz')
        myzip.write('MountWizzard4.desktop')
        myzip.write('mw4.ico')
        myzip.write('mw4.png')
    os.chdir('../')
    printMW('...copy install script to test dir')
