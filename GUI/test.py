import sys
import cv2

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

# https://ru.stackoverflow.com/a/1150993/396441

class thread1(QThread):
    changepixmap = Signal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        self.cap1 = cv2.VideoCapture(0)
        self.cap1.set(3, 480)
        self.cap1.set(4, 640)
        self.cap1.set(5, 30)
        while True:
            ret1, image1 = self.cap1.read()
            if ret1:
                im1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = im1.shape
                step1 = channel1 * width1
                qimg1 = QImage(im1.data, width1, height1, step1, QImage.Format_RGB888)
                self.changepixmap.emit(qimg1)


class thread2(QThread):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.active = True

    def run(self):
        if self.active:
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out1 = cv2.VideoWriter('output.avi', self.fourcc, 30, (640, 480))
            self.cap1 = cv2.VideoCapture(0)
            self.cap1.set(3, 480)
            self.cap1.set(4, 640)
            self.cap1.set(5, 30)
            while self.active:
                ret1, image1 = self.cap1.read()
                if ret1:
                    self.out1.write(image1)
                self.msleep(10)

    def stop(self):
        self.out1.release()


class mainwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(660, 520)
        self.control_bt = QPushButton('start')
        self.control_bt.clicked.connect(self.controltimer)
        self.image_label = QLabel()
        self.savetimer = QTimer()
        self.th1 = thread1(self)
        self.th1.changepixmap.connect(self.setimage)
        self.th1.start()

        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.image_label)
        vlayout.addWidget(self.control_bt)

    @Slot(QImage)
    def setimage(self, qimg1):
        self.image_label.setPixmap(QPixmap.fromImage(qimg1))

    def controltimer(self):
        if not self.savetimer.isActive():
            # write video
            self.savetimer.start()
            self.th2 = thread2(self)
            self.th2.active = True
            self.th2.start()
            # update control_bt text
            self.control_bt.setText("stop")
        else:
            # stop writing
            self.savetimer.stop()
            self.th2.active = false
            self.th2.stop()
            self.th2.terminate()
            # update control_bt text
            self.control_bt.settext("start")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = mainwindow()
    mainwindow.show()
    sys.exit(app.exec())