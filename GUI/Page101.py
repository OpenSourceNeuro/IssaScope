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
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Scope_Page)

    ############################################################################################################################


    # Serial Port Functions
    def ChangePort(self):
        self.COM = self.ui.Scope_SelectPortComboBox.currentText()
        self.BaudRate = self.ui.BaudRate
        self.serial_port = serial.Serial(self.COM, self.BaudRate)
        if self.serial_port.is_open:
            self.ui.Scope_ConnectButton.setEnabled(True)
            self.ui.Scope_SerialFlag = True
            self.serial_port.close()
            self.ui.Scope_Serial_label.setText('COM port ' + str(self.COM) + ' selected. Now click on the "Connect" button')
        else:
            self.ui.Scope_Serial_label.setText('Nope! try another COM port')

    def ConnectSerial(self):
        if self.ui.Scope_SerialFlag == True:
            self.ui.Scope_ConnectFlag = False
            self.COM = self.ui.Scope_SelectPortComboBox.currentText()
            self.BaudRate = self.ui.BaudRate
            self.serial_port = serial.Serial(port=self.COM, baudrate=self.BaudRate)
            self.ui.Scope_ConnectButton.setText("Connected")
            self.ui.Scope_Serial_label.setText('Device connected')
            self.ui.Scope_ConnectButton.setStyleSheet("color: rgb" + str(tuple(self.ui.DarkSolarized[3])) + ";\n"
                                                       "background-color: rgb" + str(tuple(self.ui.DarkSolarized[11])) + ";\n"
                                                       "border: 1px solid rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                       "border-radius: 10px;"
                                                       )
            self.ui.Scope_SerialFlag = False

        else:
            self.ui.Scope_Serial_label.setText('Select a COM port first, preferably the one to which the device is connected')

        if self.ui.Scope_ConnectFlag == True:
            self.serial_port.close()
            self.ui.Scope_ConnectFlag = False
            self.ui.Scope_SerialFlag = True
            self.ui.Scope_ConnectButton.setText("Disconnected")
            self.ui.Scope_Serial_label.setText('Device disconnected')

            self.ui.Scope_ConnectButton.setStyleSheet("color: rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                       "background-color: rgb" + str(tuple(self.ui.DarkSolarized[2])) + ";\n"
                                                       "border: 1px solid rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                       "border-radius: 10px;"
                                                       )


    ############################################################################################################################
    # Optogenetics LEDs

    def ActivateOptoLED(self,i):
        if self.ui.Opto_LED_toggleButton[i].isChecked():
            self.ui.Opto_LED_Slider[i].setEnabled(True)
            self.Opto_LED_Val = self.ui.Opto_LED_Slider[i].value()
            self.ui.Opto_LED_Value[i].setText(str(self.Opto_LED_Val) +' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('O' + str(i + 1) + (' ') + str(self.Opto_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')
        else:
            self.ui.Opto_LED_Slider[i].setEnabled(False)
            self.ui.Opto_LED_Value[i].setText('')
            if self.serial_port.is_open:
                pass
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

    def GetOptoLED(self,i):
        if self.ui.GetOptoLEDFlag == True:
            self.Opto_LED_Val = self.ui.Opto_LED_Slider[i].value()
            self.ui.Opto_LED_Value[i].setText(str(self.Opto_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('O' + str(i + 1) + (' ') + str(self.Opto_LED_Val) + '\n').encode('utf-8'))
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

    def DeactivateOptoLED(self,i):
        if self.ui.Opto_LED_toggleButton[i].isChecked() == False:
            self.ui.Opto_LED_Slider[i].setValue(0)
            self.ui.Opto_LED_Value[i].setText('Off')

    def TestOptoLED(self, i):
        self.LED_Val = self.ui.Opto_LED_Slider[i].value()
        if self.serial_port.is_open:
            self.serial_port.write(str('T' + str(i + 1) + (' ') + str(self.LED_Val) + '\n').encode('utf-8'))
            time.sleep(0.01)
        else:
            self.ui.Scope_Serial_label.setText('Device is not connected: LEDs will not light up')

    ############################################################################################################################
    # White LED Illumination

    def ActivateAllWhiteLED(self):
        if self.ui.AllWhite_toggleButton.isChecked():
            self.AllWhite_Val = self.ui.AllWhite_Slider.value()
            for i in range (self.ui.White_nLED + 1):
                self.ui.White_LED_toggleButton[i].setChecked(True)
                self.ui.White_LED_Slider[i].setEnabled(True)
                self.ui.White_LED_Slider[i].setValue(self.AllWhite_Val)
                self.ui.White_LED_Value[i].setText(str(self.AllWhite_Val) + ' %')

                if self.serial_port.is_open:
                    self.serial_port.write(str('W' + str(i + 1) + (' ') + str(self.AllWhite_Val) + '\n').encode('utf-8'))
                    time.sleep(0.01)
                else:
                    self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')
        else:
            for i in range (self.ui.White_nLED + 1):
                self.ui.White_LED_toggleButton[i].setChecked(False)
                self.ui.White_LED_Slider[i].setEnabled(False)
                self.ui.White_LED_Value[i].setText('')

            if self.serial_port.is_open:
                pass
            else:
                self.ui.Scope_Serial_label.setText(
                    'Device is not connected: LED value change will not be applied')

    def ActivateWhiteLED(self,i):
        if self.ui.White_LED_toggleButton[i].isChecked():
            self.ui.White_LED_Slider[i].setEnabled(True)
            self.White_LED_Val = self.ui.White_LED_Slider[i].value()
            self.ui.White_LED_Value[i].setText(str(self.White_LED_Val) +' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('W' + str(i + 1) + (' ') + str(self.White_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')
        else:
            self.ui.White_LED_Slider[i].setEnabled(False)
            self.ui.White_LED_Value[i].setText('')
            if self.serial_port.is_open:
                pass
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')


    def GetAllWhiteLED(self):
        self.ui.GetWhiteLEDFlag = False
        self.AllWhite_LED_Val = self.ui.AllWhite_Slider.value()
        for i in range(self.ui.White_nLED + 1):
            self.ui.White_LED_Slider[i].setValue(self.AllWhite_LED_Val)
            self.ui.White_LED_Value[i].setText(str(self.AllWhite_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('W' + str(i + 1) + (' ') + str(self.AllWhite_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

        self.ui.GetWhiteLEDFlag = True


    def GetWhiteLED(self,i):
        if self.ui.GetWhiteLEDFlag == True:
            self.White_LED_Val = self.ui.White_LED_Slider[i].value()
            self.ui.White_LED_Value[i].setText(str(self.White_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('W' + str(i + 1) + (' ') + str(self.White_LED_Val) + '\n').encode('utf-8'))
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')


    def DeactivateWhiteLED(self,i):
        if self.ui.White_LED_toggleButton[i].isChecked() == False:
            self.ui.White_LED_Slider[i].setValue(0)
            self.ui.White_LED_Value[i].setText('Off')


    def DeactivateAllWhiteLED(self):
        if self.ui.AllWhite_toggleButton.isChecked() == False:
            for i in range(self.ui.White_nLED + 1):
                self.ui.White_LED_Slider[i].setValue(0)
                self.ui.White_LED_Value[i].setText('Off')


    ############################################################################################################################
    # IR LED Illumination

    def ActivateAllIRLED(self):
        if self.ui.AllIR_toggleButton.isChecked():
            self.AllIR_Val = self.ui.AllIR_Slider.value()
            for i in range(self.ui.IR_nLED + 1):
                self.ui.IR_LED_toggleButton[i].setChecked(True)
                self.ui.IR_LED_Slider[i].setEnabled(True)
                self.ui.IR_LED_Slider[i].setValue(self.AllIR_Val)
                self.ui.IR_LED_Value[i].setText(str(self.AllIR_Val) + ' %')

                if self.serial_port.is_open:
                    self.serial_port.write(str('R' + str(i + 1) + (' ') + str(self.AllWhite_Val) + '\n').encode('utf-8'))
                    time.sleep(0.01)
                else:
                    self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')
        else:
            for i in range(self.ui.IR_nLED + 1):
                self.ui.IR_LED_toggleButton[i].setChecked(False)
                self.ui.IR_LED_Slider[i].setEnabled(False)
                self.ui.IR_LED_Value[i].setText('')

            if self.serial_port.is_open:
                pass
            else:
                self.ui.Scope_Serial_label.setText(
                    'Device is not connected: LED value change will not be applied')

    def ActivateIRLED(self, i):
        if self.ui.IR_LED_toggleButton[i].isChecked():
            self.ui.IR_LED_Slider[i].setEnabled(True)
            self.IR_LED_Val = self.ui.IR_LED_Slider[i].value()
            self.ui.IR_LED_Value[i].setText(str(self.IR_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('R' + str(i + 1) + (' ') + str(self.IR_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')
        else:
            self.ui.IR_LED_Slider[i].setEnabled(False)
            self.ui.IR_LED_Value[i].setText('')
            if self.serial_port.is_open:
                pass
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

    def GetAllIRLED(self):
        self.ui.GetIRLEDFlag = False
        self.AllIR_LED_Val = self.ui.AllIR_Slider.value()
        for i in range(self.ui.IR_nLED + 1):
            self.ui.IR_LED_Slider[i].setValue(self.AllIR_LED_Val)
            self.ui.IR_LED_Value[i].setText(str(self.AllIR_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('R' + str(i + 1) + (' ') + str(self.AllIR_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

        self.ui.GetIRLEDFlag = True

    def GetIRLED(self, i):
        if self.ui.GetIRLEDFlag == True:
            self.IR_LED_Val = self.ui.IR_LED_Slider[i].value()
            self.ui.IR_LED_Value[i].setText(str(self.IR_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('R' + str(i + 1) + (' ') + str(self.IR_LED_Val) + '\n').encode('utf-8'))
            else:
                self.ui.Scope_Serial_label.setText('Device is not connected: LED value change will not be applied')

    def DeactivateIRLED(self, i):
        if self.ui.IR_LED_toggleButton[i].isChecked() == False:
            self.ui.IR_LED_Slider[i].setValue(0)
            self.ui.IR_LED_Value[i].setText('Off')

    def DeactivateAllIRLED(self):
        if self.ui.AllIR_toggleButton.isChecked() == False:
            for i in range(self.ui.IR_nLED + 1):
                self.ui.IR_LED_Slider[i].setValue(0)
                self.ui.IR_LED_Value[i].setText('Off')






def PlayStimuli(self):
    self.currentLoop = 1
    self.Stim = []
    self.Data = 0

    def ReadStimulus(self):
        if self.ui.Scope_StimulusFlag == True:
            FileName = self.ui.Scope_Stimulus_Label.text()

            Df = pd.read_csv(FileName)
            for i in range (self.ui.Scope_nLED):
                self.ui.Scope_Df[i] = Df[self.ui.Scope_Dataframe[i]]
                self.Stim.append(self.ui.Scope_Df[i])

            self.df_StimRes = Df["Resolution"]
            self.df_nEntries = Df["nEntries"]
            self.df_Trigger = Df["Trigger"]
            self.df_PreAdapt = Df["PreAdaptation"]

            self.Stim.append(self.df_StimRes)
            self.Stim.append(self.df_nEntries)
            self.Stim.append(self.df_Trigger)
            self.Stim.append(self.df_PreAdapt)

            return self.Stim

        else:
            self.ui.Scope_Serial_label.setText('Load a stimulus to play first')

    self.Stim = ReadStimulus(self)


    def SetTriggerMode(self):
        self.TriggerMode = int(self.Stim[14][0])

        if self.TriggerMode == 0:
            self.serial_port.write(str('M ' + str(self.TriggerMode) + '\n').encode('utf-8'))

        elif self.TriggerMode > 0:
            self.serial_port.write(str('M ' + str(self.TriggerMode) + '\n').encode('utf-8'))


    def SetTrigger(self):
        self.TriggerMode = int(self.Stim[14][0])

        if self.TriggerMode > 0:
            self.TriggerString = ""
            for i in range(self.TriggerMode):
                self.TriggerString += ' ' + str(int(self.Stim[14][i+1]))
            self.serial_port.write(str('T' + self.TriggerString + '\n').encode('utf-8'))
        elif self.TriggerMode == 0:
            pass




    def SetStimulus(self):
        self.serial_port.write(str('S ' + str(self.Stim[12][0]) + ' '
                                   + str(self.Stim[13][0]) + ' '
                                   + str(self.Stim[15][0]) + ' '
                                   + '\n').encode('utf-8'))

        for i in range (self.ui.Opto_nLED):
            Scope.GetOptoLED(self,i)

    def SetNumberofLoop(self):
        self.ui.NumberofLoop = int(self.ui.Scope_NumbeofLoop.text())

    if self.ui.Scope_StimulusFlag:
        SetTriggerMode(self)
        SetTrigger(self)
        SetStimulus(self)
        SetNumberofLoop(self)
        self.ui.Scope_PlayingFlag = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: PlayStimulus(self))
        self.timer.start()



    def PlayStimulus(self):
        if self.ui.Scope_StimulusFlag == True:
            if self.ui.Scope_PlayingFlag == True:
                self.ui.Scope_PlayingFlag = False
                self.ui.Scope_StartStimulusFlag = True
                self.ui.Scope_Serial_label.setText("Playing Stimulus: Loop 0")
                self.ui.Scope_Start_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                              "background-color: rgb(220, 50, 47);")
        else:
            self.ui.Scope_Serial_label.setText('Load a stimulus to play first')


        if self.ui.Scope_StartStimulusFlag == True:
            self.serial_port.write(str('P ' + str(self.Stim[0][int(self.Data)]) + ' '
                                       + str(self.Stim[1][int(self.Data)]) + ' '
                                       + str(self.Stim[2][int(self.Data)]) + ' '
                                       + str(self.Stim[3][int(self.Data)]) + ' '
                                       + '\n').encode('utf-8'))

            self.Data = ReadSerial(self)

            if int(self.Data) == 1:
                self.ui.Scope_Serial_label.setText("Playing Stimulus: Loop " + str(self.currentLoop))
                self.currentLoop = self.currentLoop + 1

            if self.ui.NumberofLoop > 0:
                if self.currentLoop == self.ui.NumberofLoop + 2:
                    StopStimulus(self)





    # Read Serial and return data
    def ReadSerial(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8')
        return self.rx_serial



def LoadStimulus(self):
    self.ui.Scope_StimulusFlag = True
    self.FileName, _ = QFileDialog.getOpenFileName(self,
                                           caption='Select a stimulus',
                                           dir="./Stimuli",
                                           filter='csv files (*.csv)'
                                           )
    self.ui.Scope_Stimulus_Label.setText(self.FileName)



def StopStimulus(self):
    if self.ui.Scope_StartStimulusFlag == True:
        self.ui.Scope_StartStimulusFlag = False
        self.ui.Scope_Start_pushButton.setStyleSheet("color: rgb(147, 161, 161);\n"
                                                    "background-color: rgb(7, 54, 66);")

        self.serial_port.write(('O ' + '\n').encode('utf-8'))
        self.ui.Scope_Serial_label.setText('Stimulus stopped')

    else:
        self.ui.Scope_Serial_label.setText('No stimulus to stop at the moment')


class Scope_Stimuli():


    def SetGraph(self):
        Theme(self)

        self.ui.Scope_Display1.showGrid(x=True,y=True)
        self.ui.Scope_Display1.setRange(yRange=[0,100])
        self.ui.Scope_Display1.setBackground(self.ui.DarkSolarized[0])
        self.ui.Scope_Display1.setLabel('left', 'Stimulus Intensity', 'a.u.')
        self.ui.Scope_Display1.setLabel('bottom', 'time', 'ms')

        self.ui.Scope_Display2.showGrid(x=True, y=True)
        self.ui.Scope_Display2.setRange(yRange=[0, 100])
        self.ui.Scope_Display2.setBackground(self.ui.DarkSolarized[0])
        self.ui.Scope_Display2.setLabel('left', 'Stimulus Intensity', 'a.u.')
        self.ui.Scope_Display2.setLabel('bottom', 'time', 'ms')


    def DrawGraph(self):
        self.ui.Scope_Display1.clear()

        Scope_Stimuli.Brush(self)

        self.FileName = self.ui.Scope_Stimulus_Label.text()
        self.Df = pd.read_csv(self.FileName)
        self.Resolution = self.Df["Resolution"][0] / 1000
        self.nEntries = self.Df["nEntries"][0]
        self.xStim = np.linspace(0,int(self.nEntries)*int(self.Resolution),int(self.nEntries))


        for i in range(self.ui.Opto_nLED):
            if self.ui.Opto_LED_toggleButton[i].isChecked():
                self.yStim = self.Df[self.ui.Scope_Dataframe[i]]
                self.ui.Scope_Display1.plot(self.xStim,self.yStim,fillLevel=-0.3,brush=self.ui.Opto_Brush[i])



        self.ui.Scope_LED_counter = 0
        self.ui.Scope_LED_Index = []
        for i in range(self.ui.Opto_nLED):
            if self.ui.Opto_LED_toggleButton[i].isChecked():
                self.ui.Scope_LED_counter += 1
                self.ui.Scope_LED_Index.append(i)

        def clearLayout(layout):
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        clearLayout(self.ui.Scope_Display2_Layout)

        for i in range(self.ui.Scope_LED_counter):
            self.ui.Scope_Graph = pg.PlotWidget()
            self.ui.Scope_Graph.showGrid(x=True, y=True)
            self.ui.Scope_Graph.setRange(yRange=[0, 100])
            self.ui.Scope_Graph.setBackground(self.ui.DarkSolarized[0])
            self.Scope_Curve = pg.PlotCurveItem()
            self.ui.Scope_Graph.addItem(self.Scope_Curve)
            self.ui.Scope_Display2_Layout.addWidget(self.ui.Scope_Graph)
            self.yStim = self.Df[self.ui.Scope_Dataframe[self.ui.Scope_LED_Index[i]]]
            self.ui.Scope_Graph.plot(self.xStim, self.yStim, fillLevel=-0.3, brush=self.ui.Opto_Brush[self.ui.Scope_LED_Index[i]])


    def Brush(self):
        for i in range (self.ui.Opto_nLED):
            self.transparency = self.ui.Opto_LED_Slider[i].value()
            self.ui.Opto_Brush[i][0] = self.ui.Opto_RGB[i][0]
            self.ui.Opto_Brush[i][1] = self.ui.Opto_RGB[i][1]
            self.ui.Opto_Brush[i][2] = self.ui.Opto_RGB[i][2]
            self.ui.Opto_Brush[i][3] = self.transparency*2


