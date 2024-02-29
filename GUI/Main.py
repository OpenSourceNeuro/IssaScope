########################################################################
# Libraries import

import sys
import os
import serial
from pypylon import pylon
# Import QT libraries
from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QImage, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from IssaScope import Ui_MainWindow
from Settings import *
from Colours import *
from Arrays import *

# Import GUI page scripts
import Page000, Page101, Camera_Thread


# Setting UART parameters
#ports = Settings.COM()
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    if sys.platform == "linux" or sys.platform == "linux2":
        portList.append(port.systemLocation())
        print(port.systemLocation())
    else:
        portList.append(port.portName())

## ==> GLOBALS
counter = 0
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Custom Navigation bar buttons
        self.icon_expand = QIcon()
        self.icon_expand.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_reduce = QIcon()
        self.icon_reduce.addFile(u":/resources/resources/Reduce.png", QSize(), QIcon.Normal, QIcon.Off)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                p = event.globalPosition()
                self.move(self.pos() + p.toPoint() - self.dragPos)
                self.dragPos = p.toPoint()
                event.accept()

        # Generate LED colours
        Opto_Colours(self)
        White_Colours(self)
        IR_Colours(self)

        # Generate toggle buttons for LEDZap
        ScopeSetup(self)

        Opto_Arrays(self)
        White_Arrays(self)
        IR_Arrays(self)


        # Custom Navigation bar movement
        self.ui.Header_Frame.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        self.ui.FeedLabel = QLabel()
        self.ui.Scope_Camera_Layout.addWidget(self.ui.FeedLabel)


        ########################################################################
        # Set menu/navigation buttons

        # Main Menu Container
        self.icon_DropMenuLeft = QIcon()
        self.icon_DropMenuLeft.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_MenuLeft = QIcon()
        self.icon_MenuLeft.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.Menu_Frame.setMinimumSize(QSize(leftMenu_min, 16777215))
        self.ui.DropMenu_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Menu_Frame, leftMenu_min, leftMenu_max, animation_speed,
                                                                                   self.ui.DropMenu_pushButton, self.icon_MenuLeft, self.icon_DropMenuLeft, True))

        # Left Menu Container
        self.ui.Scope_pushButton.clicked.connect(lambda: Page101.Scope.ShowPage(self))

        ########################################################################
        # Home Page - page000
        # Display Home page on start up
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page)

        self.ui.AppName_pushButton.clicked.connect(lambda: self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page))

        ########################################################################
        # Scope Page - page101

        # Display page101 when LED Zappelin button is clicked
        self.ui.Scope_pushButton.clicked.connect(lambda: Page101.Scope.ShowPage(self))


        #Init Flag and Monitor
        self.ui.Scope_Serial_label.setText('Select a COM port to connect the device')
        self.ui.Scope_ConnectFlag = False
        self.ui.Scope_SerialFlag = False
        self.ui.Scope_StimulusFlag = False
        self.ui.Scope_StartStimulusFlag = False
        self.ui.Scope_PlayingFlag = False
        self.ui.GetWhiteLEDFlag = True
        self.ui.GetIRLEDFlag = True
        self.ui.GetOptoLEDFlag = True
        self.ui.Scope_Display1.clear()
        Page101.Scope_Stimuli.SetGraph(self)
        self.ui.Scope_LED_counter = 0

        self.CameraUSBFlag = True
        self.CameraBaslerFlag = True
        self.ui.Scope_Camera_Stream_pushButton.clicked.connect(lambda: Camera_Thread.CameraClass.Camera(self))

        # Data Recording
        self.ui.Scope_Virtual_FolderName_label = QLabel()
        self.ui.Scope_Virtual_FileName_label = QLabel()
        self.ui.Scope_Virtual_FileFormatName_label = QLabel()
        self.ui.Scope_Virtual_FinalFileName_label = QLabel()
        self.ui.Scope_Recording_BrowseDirectory_pushButton.clicked.connect(lambda:Page101.Scope.BrowseRecordFolder(self))
        self.ui.Scope_Recording_RecordFolder_value.textChanged.connect(lambda: Page101.Scope.RecordFolderText(self))
        self.ui.Scope_Recording_Format_comboBox.currentIndexChanged.connect(lambda: Page101.Scope.VideoFormat(self))
        self.ui.Scope_Camera_Record_pushButton.clicked.connect(lambda: Camera_Thread.CameraClass.Record(self))

        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.Scope_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.Scope_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        #COM port connections
        self.ui.Scope_SelectPortComboBox.currentIndexChanged.connect(lambda: Page101.Scope.ChangePort(self))

        # Start reading serial when connect button is clicked
        self.ui.Scope_ConnectButton.clicked.connect(lambda: Page101.Scope.ConnectSerial(self))

        # Play Stimulus
        self.ui.Scope_Start_pushButton.clicked.connect(lambda: Page101.PlayStimuli(self))

        # Sop Stimulus
        self.ui.Scope_Stop_pushButton.clicked.connect(lambda: Page101.StopStimulus(self))

        # Load Stimulus
        self.ui.Scope_Load_pushButton.clicked.connect(lambda: Page101.LoadStimulus(self))

        # Display Stimulus
        self.ui.Scope_Display_pushButton.clicked.connect(lambda: Page101.Scope_Stimuli.DrawGraph(self))

        # Graph Display page
        self.ui.Scope_Camera_pushButton1.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Display1_page))
        self.ui.Scope_Camera_pushButton2.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Display2_page))

        self.ui.Scope_Display1_pushButton1.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Camera_page))
        self.ui.Scope_Display1_pushButton2.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Display2_page))

        self.ui.Scope_Display2_pushButton1.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Camera_page))
        self.ui.Scope_Display2_pushButton2.clicked.connect(lambda: self.ui.Scope_Display_stackedWidget.setCurrentWidget(self.ui.Scope_Display1_page))



        # LED toggle buttons
        self.ui.Opto1_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateOptoLED(self, 0))
        self.ui.Opto2_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateOptoLED(self, 1))
        self.ui.Opto3_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateOptoLED(self, 2))
        self.ui.Opto4_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateOptoLED(self, 3))

        self.ui.AllWhite_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateAllWhiteLED(self))
        self.ui.White1_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateWhiteLED(self, 0))
        self.ui.White2_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateWhiteLED(self, 1))
        self.ui.White3_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateWhiteLED(self, 2))
        self.ui.White4_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateWhiteLED(self, 3))

        self.ui.AllIR_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateAllIRLED(self))
        self.ui.IR1_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateIRLED(self, 0))
        self.ui.IR2_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateIRLED(self, 1))
        self.ui.IR3_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateIRLED(self, 2))
        self.ui.IR4_toggleButton.toggled.connect(lambda: Page101.Scope.DeactivateIRLED(self, 3))


    ########################################################################
    # Display
    #     self.th = Camera_Thread.Camera(self)
    #     self.th.start()
        self.show()

    @Slot(QImage)
    def setImage(self, image):
        self.ui.Scope_Camera_label.setPixmap(QPixmap.fromImage(image))



    ## APP EVENTS
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(u":/resources/resources/Neuron.png"))
    window = MainWindow()
    sys.exit(app.exec())
########################################################################
## END===>
########