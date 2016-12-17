from time import strftime

"""logger.py: A simple logging module"""

__author__ = "Prajesh Ananthan"


def printDebug(text):
    print(strftime('%d/%b/%Y %H:%M:%S DEBUG | {}'.format(text)))


def printInfo(text):
    print(strftime('%d/%b/%Y %H:%M:%S INFO | {}'.format(text)))


def printWarning(text):
    print(strftime('%d/%b/%Y %H:%M:%S WARNING | {}'.format(text)))
