import sys
import threading
import time
import os
import cv2
from pypylon import pylon
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *



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
        self.Timer = QTimer()

        if self.CameraSelect == 0:
            self.ui.Scope_Serial_label.setText('Nope! Select a camera first')
            return

        if self.CameraSelect == 1:
            self.threadCamera = CameraUSB()

        if self.CameraSelect == 2:
            self.threadCamera = CameraBasler()




        FolderName = self.ui.Scope_Virtual_FolderName_label.text()
        Format = self.ui.Scope_Recording_Format_comboBox.currentText()
        FileName = self.ui.Scope_Recording_RecordFolder_value.text() + Format
        self.threadCamera.RecordFolder = FolderName
        self.threadCamera.RecordFile = str(FileName) + str(Format)

        if Format == '.avi':
            Codec = 'XVID'
            self.threadCamera.RecordCodec = Codec


        if FolderName == "" or FileName == "" or Format == 0:
            self.ui.Scope_Serial_label.setText('Nope! Select a directory, a video format and enter a file name before recording')

        else:

            if self.ui.Scope_Camera_Record_pushButton.isChecked():
                self.ui.Scope_Camera_Record_pushButton.setText("Stop Recording")
                self.ui.Scope_Camera_Record_pushButton.setStyleSheet("color: rgb(220, 50, 47);\n" "background-color: rgb(147,161,161);")
                #self.Timer.start()
                self.threadCamera.Record_Settings(FolderName,FileName,Codec)
                self.threadCamera.Record_Start()

            else:
                self.ui.Scope_Camera_Record_pushButton.setText("Record")
                self.ui.Scope_Camera_Record_pushButton.setStyleSheet("color: rgb(147,161,161);\n" "background-color: rgb(220, 50, 47);")
                #self.Timer.stop()
                self.threadCamera.Record_Stop()






class CameraUSB(QThread):
    ImageUpdate = Signal(QImage)
    ThreadActive = False
    RecordActive = False
    RecordThreadFlag = True
    ReleaseThreadFlag = False
    RecordFolder = 'Folder'
    RecordFile = 'File'
    RecordCodec = 'Codec'

    def run(self):
        CameraUSB.ThreadActive = True
        Camera = cv2.VideoCapture(0)

        while True:
            ret, frame = Camera.read()

            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)


                if self.RecordActive == True:
                    if self.RecordThreadFlag == True:
                        self.RecordThreadFlag = False
                        self.ReleaseThreadFlag = True
                        self.fourcc = cv2.VideoWriter_fourcc(*str(self.RecordCodec))
                        self.Video_Output = cv2.VideoWriter(os.path.join(self.RecordFolder, self.RecordFile), self.fourcc, 30, (Image.shape[1], Image.shape[0]))

                    self.Video_Output.write(frame)

                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                ScaledImage = ConvertToQtFormat.scaled(850,650, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledImage)

                if self.RecordActive == False and self.ReleaseThreadFlag == True:
                    self.ReleaseThreadFlag = False
                    self.Video_Output.release()

            if self.ThreadActive==False:
                break

        Camera.release()

    def stop(self):
        CameraUSB.ThreadActive = False

    def Record_Settings(self, Folder, File, Codec):
        CameraUSB.RecordFolder = Folder
        CameraUSB.RecordFile = File
        CameraUSB.RecordCodec = Codec
    def Record_Start(self):
        CameraUSB.RecordActive = True
    def Record_Stop(self):
        CameraUSB.RecordActive = False



class CameraBasler(QThread):
    ImageUpdate = Signal(QImage)
    ThreadActive = False
    RecordActive = False
    RecordThreadFlag = True
    ReleaseThreadFlag = False
    RecordFolder = 'Folder'
    RecordFile = 'File'
    RecordCodec = 'Codec'

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

                if self.RecordActive == True:
                    if self.RecordThreadFlag == True:
                        self.RecordThreadFlag = False
                        self.ReleaseThreadFlag = True
                        self.fourcc = cv2.VideoWriter_fourcc(*str(self.RecordCodec))
                        self.Video_Output = cv2.VideoWriter(os.path.join(self.RecordFolder, self.RecordFile), self.fourcc, 30, (Image.shape[1], Image.shape[0]))

                    self.Video_Output.write(Img)

                ConvertToQtFormat = QImage(Img, Img.shape[1], Img.shape[0], QImage.Format_RGB888)
                ScaledImage = ConvertToQtFormat.scaled(850, 650, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledImage)

                if self.RecordActive == False and self.ReleaseThreadFlag == True:
                    self.ReleaseThreadFlag = False
                    self.Video_Output.release()


            if (self.ThreadActive == False):
                break

                grabResult.Release()

    def stop(self):
        CameraBasler.ThreadActive = False

    def Record_Settings(self, Folder, File, Codec):
        CameraUSB.RecordFolder = Folder
        CameraUSB.RecordFile = File
        CameraUSB.RecordCodec = Codec
    def Record_Start(self):
        CameraUSB.RecordActive = True
    def Record_Stop(self):
        CameraUSB.RecordActive = False



# class Camera_Record(QThread):
#     def __init__(self, *args, **kwargs):
#         super().__init__()
#         self.active = True
#         self.frames_queue = []
#         self.lock = threading.Lock()
#
#     def run(self):
#         self.fourcc = cv2.VideoWriter_fourcc(self.RecordCodec)
#         self.output = cv2.VideoWriter(self.RecordFolder, self.RecordFile, self.fourcc, 30)
#         while True:
#             if self.frames_queue:
#                 with self.lock:
#                     Frame = self.frames_queue.pop(0)
#             while self.active:
#                 self.output.write(Frame)
#
#     def add_frame(self, frame):
#         with self.lock:
#             self.frames_queue.append(frame)
#
#
#     def stop(self):
#         #        if self.active == False:
#         self.output.release()

