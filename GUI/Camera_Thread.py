import sys
import cv2
from pypylon import pylon
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import time


class CameraClass():

    def Camera(self):
        self.CameraSelect = self.ui.Scope_CameraSelectPortComboBox.currentIndex()
        self.CameraStateFlag = True

        if self.CameraSelect == 0:
            self.ui.Scope_Serial_label.setText('Nope! Select a camera first')


        if self.CameraSelect == 1 and self.CameraUSBFlag == False:
            self.CameraUSBFlag = True
            self.CameraStateFlag = False
            self.threadUSB.stop()
            self.ui.Scope_Camera_Stream_pushButton.setText("Start Camera")
            self.ui.Scope_Camera_Stream_pushButton.setStyleSheet("color: rgb(147,161,161);\n" "background-color: rgb(0, 43, 54);")

        if self.CameraStateFlag == True:
            if self.CameraSelect == 1 and self.CameraUSBFlag == True:
                self.threadUSB = CameraUSB()
                self.CameraUSBFlag = False
                self.threadUSB.start()
                self.threadUSB.ImageUpdate.connect(self.setImage)
                self.ui.Scope_Camera_Stream_pushButton.setText("Stop Camera")
                self.ui.Scope_Camera_Stream_pushButton.setStyleSheet("color: rgb(147,161,161);\n" "background-color: rgb(220, 50, 47);")


        if self.CameraSelect == 2 and self.CameraBaslerFlag == False:
            self.CameraBaslerFlag = True
            self.CameraStateFlag = False
            self.threadBasler.stop()
            self.ui.Scope_Camera_Stream_pushButton.setText("Start Camera")
            self.ui.Scope_Camera_Stream_pushButton.setStyleSheet("color: rgb(147,161,161);\n" "background-color: rgb(0, 43, 54);")

        if self.CameraStateFlag == True:
            if self.CameraSelect == 2 and self.CameraBaslerFlag == True:
                self.threadBasler = CameraBasler()
                self.CameraBaslerFlag = False
                self.threadBasler.start()
                self.threadBasler.ImageUpdate.connect(self.setImage)
                self.ui.Scope_Camera_Stream_pushButton.setText("Stop Camera")
                self.ui.Scope_Camera_Stream_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n" "background-color: rgb(50, 220, 47);")

    def Record(self):
        self.RecordFolder = self.ui.Scope_Virtual_FolderName_label
        self.RecordFile = self.ui.Scope_Virtual_FileFormatName_label

        if self.ui.Scope_Camera_Record_pushButton.isChecked():
            self.ui.Scope_Camera_Record_pushButton.setText("Stop Recording")
            self.ui.Scope_Camera_Record_pushButton.setStyleSheet("color: rgb(220, 50, 47);\n" "background-color: rgb(147,161,161);")

        else:
            self.ui.Scope_Camera_Record_pushButton.setText("Record")
            self.ui.Scope_Camera_Record_pushButton.setStyleSheet("color: rgb(147,161,161);\n" "background-color: rgb(220, 50, 47);")

class CameraUSB(QThread):
    ImageUpdate = Signal(QImage)
    ThreadActive = False

    def run(self):
        CameraUSB.ThreadActive = True
        Camera = cv2.VideoCapture(0)
        while True:
            ret, frame = Camera.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                ScaledImage = ConvertToQtFormat.scaled(850,650, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledImage)
            if (self.ThreadActive==False):
                break
        Camera.release()
    def stop(self):
        CameraUSB.ThreadActive = False

    def record(self):
        pass

class CameraBasler(QThread):
    ImageUpdate = Signal(QImage)
    ThreadActive = False
    def run(self):
        CameraBasler.ThreadActive = True
        Camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        # Grabing Continusely (video) with minimal delay
        Camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        while Camera.IsGrabbing():
            grabResult = Camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
                Image = converter.Convert(grabResult)
                Img = Image.GetArray()
                ConvertToQtFormat = QImage(Img, Img.shape[1], Img.shape[0], QImage.Format_RGB888)
                ScaledImage = ConvertToQtFormat.scaled(850, 650, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledImage)
            if (self.ThreadActive == False):
                break
                grabResult.Release()

    def stop(self):
        CameraBasler.ThreadActive = False


