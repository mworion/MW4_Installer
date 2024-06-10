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
import logging
from logging.handlers import RotatingFileHandler
import time
import datetime


log = logging.getLogger()
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


class LoggerWriter:
    """
    """
    def __init__(self, level, mode, std):
        """
        :param level:
        :param mode:
        :param std:
        """
        self.level = level
        self.mode = mode
        self.standard = std

    def write(self, message):
        """
        :param message:
        :return:
        """
        first = True
        for line in message.rstrip().splitlines():
            if first:
                self.level(f'[{self.mode}] ' + line.strip())
                first = False
            else:
                self.level(' ' * 9 + line.strip())

    def flush(self):
        pass


def add_logging_level(level_name, level_num, method_name=None):
    """    
    :param level_name:
    :param level_num:
    :param method_name:
    :return: 
    """
    if not method_name:
        method_name = level_name.lower()
    if hasattr(logging, level_name):
        return
    if hasattr(logging, method_name):
        return
    if hasattr(logging.getLoggerClass(), method_name):
        return

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, logForLevel)


def setup_logging() -> None:
    """
    setup_logging defines the logger and formats and disables unnecessary
    library logging

    :return: true for test purpose
    """
    if not os.path.isdir('./log'):
        os.mkdir('./log')

    logging.Formatter.converter = time.gmtime
    timeTag = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    logFile = f'./log/mw4-{timeTag}.log'
    logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=100 * 1024 * 1024,
                                     backupCount=100, encoding=None, delay=False)
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s.%(msecs)03d]'
                               '[%(levelname)1.1s]'
                               '[%(filename)15.15s]'
                               '[%(lineno)4s]'
                               ' %(message)s',
                        handlers=[logHandler],
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    # transfer all sys outputs to logging
    sys.stderr = LoggerWriter(logging.getLogger().error, 'STDERR', sys.stderr)
