from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QFileDialog, QWidget
from PySide6.QtCore import QIODevice, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QCoreApplication, QFileInfo
import pyqtgraph as pg
import Camera_Thread

import cv2
from pypylon import pylon

from Settings import *
from Colours import *
from Arrays import *
from py_toggle import PyToggle

import serial
import os
import time
import numpy as np
import pandas as pd
from sys import platform

portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        if platform == "linux" or platform == "linux2":
            portList.append(port.systemLocation())
        else:
            portList.append(port.portName())


class Scope():

    def ShowPage(self):
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Scope2_Page)

    ############################################################################################################################
