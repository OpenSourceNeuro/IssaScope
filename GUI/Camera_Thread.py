import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import cv2

class Worker1(QThread):
    ImageUpdate = Signal(QImage)

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                self.Image =  cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.FlippedImage = cv2.flip(self.Image, 1)
                ConvertToQtFormat = QImage(self.FlippedImage.data, self.FlippedImage.shape[1], self.FlippedImage.shape[0], QImage.Format_RGB888)
                self.Pic = ConvertToQtFormat.scaled(640,480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(self.Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()

class Camera():
    def __init__(self):
        super(MainWindow, self).__init__()

    def ImageUpdateSlot(self, Image):
        self.ui.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker.stop()

    def ConnectCamera(self):
        self.CameraSelect = self.ui.Scope_SelectPortComboBox.currentIndex()
        print(self.CameraSelect)
        if self.CameraSelect == 0:

            self.Worker = Worker1()

            self.Worker.start()
            self.Worker.ImageUpdate.connect(Camera.ImageUpdateSlot())
            self.setLayout(self.ui.Scope_Camera_Layout)

