import sys
import serial
from Main import MainWindow
import resources_rc
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QPropertyAnimation
from PySide6.QtWidgets import QSizeGrip

from py_toggle import PyToggle
import Page101
from Colours import *


def ScopeSetup(self):
    self.ui.BaudRate = 921600
    small_toggle = 30
    large_toggle = 50
    Theme(self)
    self.SerialFlag = False
    self.serial_port = serial.Serial()


    # Opto
    self.ui.Opto1_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.Opto_RGB[0]),
                                          width = large_toggle
                                          )
    self.ui.Opto1_toggleButton_layout.addWidget(self.ui.Opto1_toggleButton)

    self.ui.Opto2_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.Opto_RGB[1]),
                                          width=large_toggle
                                          )
    self.ui.Opto2_toggleButton_layout.addWidget(self.ui.Opto2_toggleButton)

    self.ui.Opto3_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.Opto_RGB[2]),
                                          width=large_toggle
                                          )
    self.ui.Opto3_toggleButton_layout.addWidget(self.ui.Opto3_toggleButton)

    self.ui.Opto4_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.Opto_RGB[3]),
                                          width=large_toggle
                                          )
    self.ui.Opto4_toggleButton_layout.addWidget(self.ui.Opto4_toggleButton)




    # White Illumination
    self.ui.White1_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                           circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                           active_color='#%02x%02x%02x' % tuple(self.ui.White_RGB[0]),
                                           width=small_toggle
                                           )
    self.ui.White1_toggleButton_layout.addWidget(self.ui.White1_toggleButton)

    self.ui.White2_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                           circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                           active_color='#%02x%02x%02x' % tuple(self.ui.White_RGB[1]),
                                           width=small_toggle
                                           )
    self.ui.White2_toggleButton_layout.addWidget(self.ui.White2_toggleButton)

    self.ui.White3_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                           circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                           active_color='#%02x%02x%02x' % tuple(self.ui.White_RGB[2]),
                                           width=small_toggle
                                           )
    self.ui.White3_toggleButton_layout.addWidget(self.ui.White3_toggleButton)

    self.ui.White4_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                           circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                           active_color='#%02x%02x%02x' % tuple(self.ui.White_RGB[3]),
                                           width=small_toggle
                                           )
    self.ui.White4_toggleButton_layout.addWidget(self.ui.White4_toggleButton)

    self.ui.AllWhite_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                           circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                           active_color='#%02x%02x%02x' % tuple(self.ui.White_RGB[4]),
                                           width=small_toggle
                                           )
    self.ui.AllWhite_toggleButton_layout.addWidget(self.ui.AllWhite_toggleButton)




    # IR Illumination
    self.ui.IR1_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                        circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                        active_color='#%02x%02x%02x' % tuple(self.ui.IR_RGB[0]),
                                        width=small_toggle
                                        )
    self.ui.IR1_toggleButton_layout.addWidget(self.ui.IR1_toggleButton)

    self.ui.IR2_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                        circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                        active_color='#%02x%02x%02x' % tuple(self.ui.IR_RGB[1]),
                                        width=small_toggle
                                        )
    self.ui.IR2_toggleButton_layout.addWidget(self.ui.IR2_toggleButton)

    self.ui.IR3_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                        circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                        active_color='#%02x%02x%02x' % tuple(self.ui.IR_RGB[2]),
                                        width=small_toggle
                                        )
    self.ui.IR3_toggleButton_layout.addWidget(self.ui.IR3_toggleButton)

    self.ui.IR4_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                        circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                        active_color='#%02x%02x%02x' % tuple(self.ui.IR_RGB[3]),
                                        width=small_toggle
                                        )
    self.ui.IR4_toggleButton_layout.addWidget(self.ui.IR4_toggleButton)

    self.ui.AllIR_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.IR_RGB[4]),
                                          width=small_toggle
                                          )
    self.ui.AllIR_toggleButton_layout.addWidget(self.ui.AllIR_toggleButton)



    self.ui.Opto1_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateOptoLED(self, 0))
    self.ui.Opto1_Slider.valueChanged.connect(lambda: Page101.Scope.GetOptoLED(self, 0))

    self.ui.Opto2_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateOptoLED(self, 1))
    self.ui.Opto2_Slider.valueChanged.connect(lambda: Page101.Scope.GetOptoLED(self, 1))

    self.ui.Opto3_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateOptoLED(self, 2))
    self.ui.Opto3_Slider.valueChanged.connect(lambda: Page101.Scope.GetOptoLED(self, 2))

    self.ui.Opto4_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateOptoLED(self, 3))
    self.ui.Opto4_Slider.valueChanged.connect(lambda: Page101.Scope.GetOptoLED(self, 3))




    self.ui.AllWhite_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateAllWhiteLED(self))
    self.ui.AllWhite_Slider.valueChanged.connect(lambda: Page101.Scope.GetAllWhiteLED(self))

    self.ui.White1_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateWhiteLED(self, 0))
    self.ui.White1_Slider.valueChanged.connect(lambda: Page101.Scope.GetWhiteLED(self, 0))

    self.ui.White2_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateWhiteLED(self, 1))
    self.ui.White2_Slider.valueChanged.connect(lambda: Page101.Scope.GetWhiteLED(self, 1))

    self.ui.White3_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateWhiteLED(self, 2))
    self.ui.White3_Slider.valueChanged.connect(lambda: Page101.Scope.GetWhiteLED(self, 2))

    self.ui.White4_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateWhiteLED(self, 3))
    self.ui.White4_Slider.valueChanged.connect(lambda: Page101.Scope.GetWhiteLED(self, 3))




    self.ui.AllIR_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateAllIRLED(self))
    self.ui.AllIR_Slider.valueChanged.connect(lambda: Page101.Scope.GetAllIRLED(self))

    self.ui.IR1_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateIRLED(self, 0))
    self.ui.IR1_Slider.valueChanged.connect(lambda: Page101.Scope.GetIRLED(self, 0))

    self.ui.IR2_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateIRLED(self, 1))
    self.ui.IR2_Slider.valueChanged.connect(lambda: Page101.Scope.GetIRLED(self, 1))

    self.ui.IR3_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateIRLED(self, 2))
    self.ui.IR3_Slider.valueChanged.connect(lambda: Page101.Scope.GetIRLED(self, 2))

    self.ui.IR4_toggleButton.toggled.connect(lambda: Page101.Scope.ActivateIRLED(self, 3))
    self.ui.IR4_Slider.valueChanged.connect(lambda: Page101.Scope.GetIRLED(self, 3))






animation_speed = 500
leftMenu_min = 40
leftMenu_max = 180
centerMenu_min = 0
centerMenu_max = 200
rightMenu_min = 0
rightMenu_max = 200
rightSubMenu_min = 40
rightSubMenu_max = 200

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

        def maximize_restore(self):
            global GLOBAL_STATE
            status = GLOBAL_STATE

            # IF NOT MAXIMIZED
            if status == 0:
                self.showMaximized()
                self.ui.Expand_pushButton.setIcon(self.icon_reduce)

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1
                self.ui.Expand_pushButton.setToolTip("Restore")

            else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.ui.Expand_pushButton.setIcon(self.icon_expand)
                self.resize(self.width() + 1, self.height() + 1)
                self.ui.Expand_pushButton.setToolTip("Maximize")

        ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
        def returnStatus():
            return GLOBAL_STATE


        ## ==> UI DEFINITIONS
        def uiDefinitions(self):

            # REMOVE TITLE BAR
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # MAXIMIZE / RESTORE
            self.ui.Expand_pushButton.clicked.connect(lambda: UIFunctions.maximize_restore(self))

            # MINIMIZE
            self.ui.Reduce_pushButton.clicked.connect(lambda: self.showMinimized())

            # CLOSE
            self.ui.Exit_pushButton.clicked.connect(lambda: self.close())

            ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.SizeGrip_Frame)
            self.sizegrip.setToolTip("Resize Window")



        def toggleMenu(self, menu, standard, maxWidth, duration, pushButton, icon_min, icon_max, enable):
                if enable:
                        #Get width
                        width = menu.width()

                        #Extend
                        if width == standard:
                                widthExtended = maxWidth
                                pushButton.setIcon(icon_max)
                        #Retract
                        else:
                                widthExtended = standard
                                pushButton.setIcon(icon_min)

                        #Animation
                        self.animation = QPropertyAnimation(menu, b"minimumWidth")
                        self.animation.setDuration(duration)
                        self.animation.setStartValue(width)
                        self.animation.setEndValue(widthExtended)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()

        def expandMenu(self, menu, standard, maxWidth, duration, enable):
                if enable:
                        width = menu.width()
                        if width == standard:
                            #Animation
                            self.animation = QPropertyAnimation(menu, b"minimumWidth")
                            self.animation.setDuration(duration)
                            self.animation.setStartValue(standard)
                            self.animation.setEndValue(maxWidth)
                            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                            self.animation.start()

        def collapseMenu(self, menu, standard, maxWidth, duration, enable):
                if enable:
                        width = menu.width()
                        if width == maxWidth:
                            #Animation
                            self.animation = QPropertyAnimation(menu, b"minimumWidth")
                            self.animation.setDuration(duration)
                            self.animation.setStartValue(maxWidth)
                            self.animation.setEndValue(standard)
                            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                            self.animation.start()


