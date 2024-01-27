# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IssaScope.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 760)
        MainWindow.setMinimumSize(QSize(20, 20))
        MainWindow.setStyleSheet(u"/* --- General Settings --- */\n"
"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin:0;\n"
"	color: rgb(147,161,161);    \n"
"}\n"
"#centralwidget{\n"
"	background-color:  rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"/* --- Top Frame --- */\n"
"\n"
"#TopMainFrame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#AppName_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"/* --- Bottom Frame --- */\n"
"\n"
"#BottomMainFrame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"/* --- Menu Frame --- */\n"
"\n"
"#Menu_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Menu_Frame QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 5px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Menu_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#HideSubMenu_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
""
                        "/* --- Scope --- */\n"
"\n"
"#Scope_frame Line{\n"
" border: 1px solid rgb(147,161,161);\n"
"}\n"
"#Scope_Frame QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"#Scope_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#Scope_Display_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#Scope_Display_stackedWidget QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopMainFrame = QFrame(self.centralwidget)
        self.TopMainFrame.setObjectName(u"TopMainFrame")
        self.TopMainFrame.setMinimumSize(QSize(0, 40))
        self.TopMainFrame.setMaximumSize(QSize(16777215, 40))
        self.TopMainFrame.setFrameShape(QFrame.StyledPanel)
        self.TopMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TopMainFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Header_Frame = QFrame(self.TopMainFrame)
        self.Header_Frame.setObjectName(u"Header_Frame")
        self.Header_Frame.setFrameShape(QFrame.StyledPanel)
        self.Header_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header_Frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.AppName_Frame = QFrame(self.Header_Frame)
        self.AppName_Frame.setObjectName(u"AppName_Frame")
        self.AppName_Frame.setFrameShape(QFrame.StyledPanel)
        self.AppName_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.AppName_Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.AppName_pushButton = QPushButton(self.AppName_Frame)
        self.AppName_pushButton.setObjectName(u"AppName_pushButton")
        font = QFont()
        font.setPointSize(16)
        self.AppName_pushButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.AppName_pushButton)


        self.horizontalLayout.addWidget(self.AppName_Frame, 0, Qt.AlignLeft)

        self.AppButton_Frame = QFrame(self.Header_Frame)
        self.AppButton_Frame.setObjectName(u"AppButton_Frame")
        self.AppButton_Frame.setFrameShape(QFrame.StyledPanel)
        self.AppButton_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.AppButton_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Reduce_pushButton = QPushButton(self.AppButton_Frame)
        self.Reduce_pushButton.setObjectName(u"Reduce_pushButton")
        icon = QIcon()
        icon.addFile(u":/resources/resources/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reduce_pushButton.setIcon(icon)
        self.Reduce_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Reduce_pushButton)

        self.Expand_pushButton = QPushButton(self.AppButton_Frame)
        self.Expand_pushButton.setObjectName(u"Expand_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Expand_pushButton.setIcon(icon1)
        self.Expand_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Expand_pushButton)

        self.Exit_pushButton = QPushButton(self.AppButton_Frame)
        self.Exit_pushButton.setObjectName(u"Exit_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit_pushButton.setIcon(icon2)
        self.Exit_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Exit_pushButton)


        self.horizontalLayout.addWidget(self.AppButton_Frame, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.Header_Frame)


        self.verticalLayout.addWidget(self.TopMainFrame)

        self.CenterMainFrame = QFrame(self.centralwidget)
        self.CenterMainFrame.setObjectName(u"CenterMainFrame")
        self.CenterMainFrame.setFrameShape(QFrame.StyledPanel)
        self.CenterMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CenterMainFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Menu_Frame = QFrame(self.CenterMainFrame)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setMaximumSize(QSize(40, 16777215))
        self.Menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Menu_Frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 15)
        self.DropMenu_Frame = QFrame(self.Menu_Frame)
        self.DropMenu_Frame.setObjectName(u"DropMenu_Frame")
        self.DropMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.DropMenu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.DropMenu_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.DropMenu_pushButton = QPushButton(self.DropMenu_Frame)
        self.DropMenu_pushButton.setObjectName(u"DropMenu_pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.DropMenu_pushButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DropMenu_pushButton.setIcon(icon3)
        self.DropMenu_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.DropMenu_pushButton)


        self.verticalLayout_2.addWidget(self.DropMenu_Frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Menus_Frame = QFrame(self.Menu_Frame)
        self.Menus_Frame.setObjectName(u"Menus_Frame")
        self.Menus_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menus_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Menus_Frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Scope_pushButton = QPushButton(self.Menus_Frame)
        self.Scope_pushButton.setObjectName(u"Scope_pushButton")
        self.Scope_pushButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/resources/resources/LEDZap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Scope_pushButton.setIcon(icon4)
        self.Scope_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.Scope_pushButton)


        self.verticalLayout_2.addWidget(self.Menus_Frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.Options_Frame = QFrame(self.Menu_Frame)
        self.Options_Frame.setObjectName(u"Options_Frame")
        self.Options_Frame.setFrameShape(QFrame.StyledPanel)
        self.Options_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Options_Frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Settings_pushButton = QPushButton(self.Options_Frame)
        self.Settings_pushButton.setObjectName(u"Settings_pushButton")
        self.Settings_pushButton.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/resources/resources/Settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings_pushButton.setIcon(icon5)
        self.Settings_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Settings_pushButton)

        self.About_pushButton = QPushButton(self.Options_Frame)
        self.About_pushButton.setObjectName(u"About_pushButton")
        self.About_pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About_pushButton.setIcon(icon6)
        self.About_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.About_pushButton)

        self.Help_pushButton = QPushButton(self.Options_Frame)
        self.Help_pushButton.setObjectName(u"Help_pushButton")
        self.Help_pushButton.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Help_pushButton.setIcon(icon7)
        self.Help_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Help_pushButton)

        self.GitHub_pushButton = QPushButton(self.Options_Frame)
        self.GitHub_pushButton.setObjectName(u"GitHub_pushButton")
        self.GitHub_pushButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHub_pushButton.setIcon(icon8)
        self.GitHub_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.GitHub_pushButton)


        self.verticalLayout_2.addWidget(self.Options_Frame)


        self.horizontalLayout_10.addWidget(self.Menu_Frame)

        self.SubMenu_Frame = QFrame(self.CenterMainFrame)
        self.SubMenu_Frame.setObjectName(u"SubMenu_Frame")
        self.SubMenu_Frame.setMinimumSize(QSize(200, 0))
        self.SubMenu_Frame.setMaximumSize(QSize(200, 16777215))
        self.SubMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.SubMenu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.SubMenu_Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.HideSubMenu_Frame = QFrame(self.SubMenu_Frame)
        self.HideSubMenu_Frame.setObjectName(u"HideSubMenu_Frame")
        self.HideSubMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.HideSubMenu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.HideSubMenu_Frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HideSubFrame_pushButton = QPushButton(self.HideSubMenu_Frame)
        self.HideSubFrame_pushButton.setObjectName(u"HideSubFrame_pushButton")
        self.HideSubFrame_pushButton.setMinimumSize(QSize(0, 30))
        self.HideSubFrame_pushButton.setFont(font1)
        self.HideSubFrame_pushButton.setLayoutDirection(Qt.RightToLeft)
        icon9 = QIcon()
        icon9.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HideSubFrame_pushButton.setIcon(icon9)
        self.HideSubFrame_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.HideSubFrame_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.HideSubMenu_Frame)

        self.stackedWidget = QStackedWidget(self.SubMenu_Frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(200, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_10.addWidget(self.SubMenu_Frame)

        self.MainContent_Frame = QFrame(self.CenterMainFrame)
        self.MainContent_Frame.setObjectName(u"MainContent_Frame")
        self.MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.MainContent_Frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Main_stackedWidget = QStackedWidget(self.MainContent_Frame)
        self.Main_stackedWidget.setObjectName(u"Main_stackedWidget")
        self.Main_stackedWidget.setFont(font1)
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.verticalLayout_36 = QVBoxLayout(self.Home_Page)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Home_Header_Frame = QFrame(self.Home_Page)
        self.Home_Header_Frame.setObjectName(u"Home_Header_Frame")
        self.Home_Header_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Header_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.Home_Header_Frame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 0, 10, 0)
        self.Home_Logo_frame = QFrame(self.Home_Header_Frame)
        self.Home_Logo_frame.setObjectName(u"Home_Logo_frame")
        self.Home_Logo_frame.setMinimumSize(QSize(200, 125))
        self.Home_Logo_frame.setMaximumSize(QSize(200, 125))
        self.Home_Logo_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.Home_Logo_frame)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.Home_Logo = QLabel(self.Home_Logo_frame)
        self.Home_Logo.setObjectName(u"Home_Logo")
        self.Home_Logo.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.Home_Logo.setScaledContents(True)

        self.horizontalLayout_113.addWidget(self.Home_Logo)


        self.horizontalLayout_35.addWidget(self.Home_Logo_frame)

        self.Home_Title_frame = QFrame(self.Home_Header_Frame)
        self.Home_Title_frame.setObjectName(u"Home_Title_frame")
        self.Home_Title_frame.setMinimumSize(QSize(0, 200))
        self.Home_Title_frame.setMaximumSize(QSize(16777215, 200))
        self.Home_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.Home_Title_frame)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.Home_Title = QLabel(self.Home_Title_frame)
        self.Home_Title.setObjectName(u"Home_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home_Title.sizePolicy().hasHeightForWidth())
        self.Home_Title.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(False)
        self.Home_Title.setFont(font2)
        self.Home_Title.setStyleSheet(u"")

        self.horizontalLayout_114.addWidget(self.Home_Title)


        self.horizontalLayout_35.addWidget(self.Home_Title_frame)


        self.verticalLayout_36.addWidget(self.Home_Header_Frame, 0, Qt.AlignTop)

        self.Home_Main_Frame = QFrame(self.Home_Page)
        self.Home_Main_Frame.setObjectName(u"Home_Main_Frame")
        self.Home_Main_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.Home_Main_Frame)
        self.horizontalLayout_115.setSpacing(10)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(10, 0, 10, 10)
        self.Home_Main_Text_frame = QFrame(self.Home_Main_Frame)
        self.Home_Main_Text_frame.setObjectName(u"Home_Main_Text_frame")
        self.Home_Main_Text_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.Home_Main_Text_frame)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Text = QLabel(self.Home_Main_Text_frame)
        self.Home_Main_Text.setObjectName(u"Home_Main_Text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Home_Main_Text.sizePolicy().hasHeightForWidth())
        self.Home_Main_Text.setSizePolicy(sizePolicy1)
        self.Home_Main_Text.setAlignment(Qt.AlignCenter)
        self.Home_Main_Text.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.Home_Main_Text, 0, Qt.AlignBottom)


        self.horizontalLayout_115.addWidget(self.Home_Main_Text_frame)

        self.Home_Main_Illustration_frame = QFrame(self.Home_Main_Frame)
        self.Home_Main_Illustration_frame.setObjectName(u"Home_Main_Illustration_frame")
        self.Home_Main_Illustration_frame.setMinimumSize(QSize(500, 0))
        self.Home_Main_Illustration_frame.setMaximumSize(QSize(500, 16777215))
        self.Home_Main_Illustration_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.Home_Main_Illustration_frame)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 50)
        self.Home_Main_Illustration_Title_frame = QFrame(self.Home_Main_Illustration_frame)
        self.Home_Main_Illustration_Title_frame.setObjectName(u"Home_Main_Illustration_Title_frame")
        self.Home_Main_Illustration_Title_frame.setMinimumSize(QSize(500, 40))
        self.Home_Main_Illustration_Title_frame.setMaximumSize(QSize(500, 40))
        self.Home_Main_Illustration_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_Title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.Home_Main_Illustration_Title_frame)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Illustration_Title = QLabel(self.Home_Main_Illustration_Title_frame)
        self.Home_Main_Illustration_Title.setObjectName(u"Home_Main_Illustration_Title")
        self.Home_Main_Illustration_Title.setMinimumSize(QSize(0, 40))
        self.Home_Main_Illustration_Title.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(True)
        self.Home_Main_Illustration_Title.setFont(font3)

        self.verticalLayout_40.addWidget(self.Home_Main_Illustration_Title, 0, Qt.AlignHCenter)


        self.verticalLayout_39.addWidget(self.Home_Main_Illustration_Title_frame, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.Home_Main_Illustration_Image_frame = QFrame(self.Home_Main_Illustration_frame)
        self.Home_Main_Illustration_Image_frame.setObjectName(u"Home_Main_Illustration_Image_frame")
        self.Home_Main_Illustration_Image_frame.setMaximumSize(QSize(500, 350))
        self.Home_Main_Illustration_Image_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_Image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.Home_Main_Illustration_Image_frame)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Illustration_Image = QLabel(self.Home_Main_Illustration_Image_frame)
        self.Home_Main_Illustration_Image.setObjectName(u"Home_Main_Illustration_Image")
        self.Home_Main_Illustration_Image.setMaximumSize(QSize(500, 350))
        self.Home_Main_Illustration_Image.setStyleSheet(u"")
        self.Home_Main_Illustration_Image.setFrameShape(QFrame.NoFrame)
        self.Home_Main_Illustration_Image.setFrameShadow(QFrame.Plain)
        self.Home_Main_Illustration_Image.setLineWidth(1)
        self.Home_Main_Illustration_Image.setPixmap(QPixmap(u":/resources/resources/DarkSideOfTheRetina.png"))
        self.Home_Main_Illustration_Image.setScaledContents(True)

        self.horizontalLayout_116.addWidget(self.Home_Main_Illustration_Image)


        self.verticalLayout_39.addWidget(self.Home_Main_Illustration_Image_frame)


        self.horizontalLayout_115.addWidget(self.Home_Main_Illustration_frame)


        self.verticalLayout_36.addWidget(self.Home_Main_Frame)

        self.Main_stackedWidget.addWidget(self.Home_Page)
        self.Scope_Page = QWidget()
        self.Scope_Page.setObjectName(u"Scope_Page")
        self.verticalLayout_7 = QVBoxLayout(self.Scope_Page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Scope_Frame = QFrame(self.Scope_Page)
        self.Scope_Frame.setObjectName(u"Scope_Frame")
        self.Scope_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Scope_Frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Scope_MainContent_Frame = QFrame(self.Scope_Frame)
        self.Scope_MainContent_Frame.setObjectName(u"Scope_MainContent_Frame")
        self.Scope_MainContent_Frame.setMinimumSize(QSize(0, 0))
        self.Scope_MainContent_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Scope_MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Scope_MainContent_Frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Scope_Connection_Frame = QFrame(self.Scope_MainContent_Frame)
        self.Scope_Connection_Frame.setObjectName(u"Scope_Connection_Frame")
        self.Scope_Connection_Frame.setMinimumSize(QSize(0, 0))
        self.Scope_Connection_Frame.setMaximumSize(QSize(16777215, 50))
        self.Scope_Connection_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Connection_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Scope_Connection_Frame)
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.Scope_Connection_Frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_6)

        self.Scope_PortConnect_Frame = QFrame(self.Scope_Connection_Frame)
        self.Scope_PortConnect_Frame.setObjectName(u"Scope_PortConnect_Frame")
        self.Scope_PortConnect_Frame.setMinimumSize(QSize(0, 50))
        self.Scope_PortConnect_Frame.setMaximumSize(QSize(16777215, 50))
        self.Scope_PortConnect_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_PortConnect_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Scope_PortConnect_Frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.Scope_SelectPortLabel = QLabel(self.Scope_PortConnect_Frame)
        self.Scope_SelectPortLabel.setObjectName(u"Scope_SelectPortLabel")
        self.Scope_SelectPortLabel.setFont(font1)

        self.horizontalLayout_14.addWidget(self.Scope_SelectPortLabel, 0, Qt.AlignHCenter)

        self.Scope_SelectPortComboBox = QComboBox(self.Scope_PortConnect_Frame)
        self.Scope_SelectPortComboBox.addItem("")
        self.Scope_SelectPortComboBox.setObjectName(u"Scope_SelectPortComboBox")

        self.horizontalLayout_14.addWidget(self.Scope_SelectPortComboBox)

        self.Scope_ConnectButton = QPushButton(self.Scope_PortConnect_Frame)
        self.Scope_ConnectButton.setObjectName(u"Scope_ConnectButton")
        self.Scope_ConnectButton.setEnabled(True)
        self.Scope_ConnectButton.setFont(font1)
        self.Scope_ConnectButton.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.Scope_ConnectButton)


        self.horizontalLayout_19.addWidget(self.Scope_PortConnect_Frame)

        self.line_5 = QFrame(self.Scope_Connection_Frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_5)

        self.Scope_CameraConnect_Frame = QFrame(self.Scope_Connection_Frame)
        self.Scope_CameraConnect_Frame.setObjectName(u"Scope_CameraConnect_Frame")
        self.Scope_CameraConnect_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_CameraConnect_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.Scope_CameraConnect_Frame)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.Scope_CameraSelectPortLabel = QLabel(self.Scope_CameraConnect_Frame)
        self.Scope_CameraSelectPortLabel.setObjectName(u"Scope_CameraSelectPortLabel")
        self.Scope_CameraSelectPortLabel.setFont(font1)

        self.horizontalLayout_33.addWidget(self.Scope_CameraSelectPortLabel)

        self.Scope_CameraSelectPortComboBox = QComboBox(self.Scope_CameraConnect_Frame)
        self.Scope_CameraSelectPortComboBox.addItem("")
        self.Scope_CameraSelectPortComboBox.addItem("")
        self.Scope_CameraSelectPortComboBox.addItem("")
        self.Scope_CameraSelectPortComboBox.setObjectName(u"Scope_CameraSelectPortComboBox")

        self.horizontalLayout_33.addWidget(self.Scope_CameraSelectPortComboBox)


        self.horizontalLayout_19.addWidget(self.Scope_CameraConnect_Frame)


        self.verticalLayout_8.addWidget(self.Scope_Connection_Frame)

        self.Scope_Display_Frame = QFrame(self.Scope_MainContent_Frame)
        self.Scope_Display_Frame.setObjectName(u"Scope_Display_Frame")
        self.Scope_Display_Frame.setMinimumSize(QSize(0, 100))
        self.Scope_Display_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Display_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Scope_Display_Frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.Scope_Display_stackedWidget = QStackedWidget(self.Scope_Display_Frame)
        self.Scope_Display_stackedWidget.setObjectName(u"Scope_Display_stackedWidget")
        self.Scope_Camera_page = QWidget()
        self.Scope_Camera_page.setObjectName(u"Scope_Camera_page")
        self.verticalLayout_15 = QVBoxLayout(self.Scope_Camera_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Scope_Camera_pushButton_frame = QFrame(self.Scope_Camera_page)
        self.Scope_Camera_pushButton_frame.setObjectName(u"Scope_Camera_pushButton_frame")
        self.Scope_Camera_pushButton_frame.setMinimumSize(QSize(0, 20))
        self.Scope_Camera_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.Scope_Camera_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Camera_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.Scope_Camera_pushButton_frame)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 5, 0)
        self.Scope_Camera_pushButton1 = QPushButton(self.Scope_Camera_pushButton_frame)
        self.Scope_Camera_pushButton1.setObjectName(u"Scope_Camera_pushButton1")
        self.Scope_Camera_pushButton1.setMinimumSize(QSize(175, 0))
        self.Scope_Camera_pushButton1.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_31.addWidget(self.Scope_Camera_pushButton1)

        self.Scope_Camera_pushButton2 = QPushButton(self.Scope_Camera_pushButton_frame)
        self.Scope_Camera_pushButton2.setObjectName(u"Scope_Camera_pushButton2")
        self.Scope_Camera_pushButton2.setMinimumSize(QSize(175, 0))
        self.Scope_Camera_pushButton2.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_31.addWidget(self.Scope_Camera_pushButton2)


        self.verticalLayout_15.addWidget(self.Scope_Camera_pushButton_frame, 0, Qt.AlignRight)

        self.Scope_Camera = QFrame(self.Scope_Camera_page)
        self.Scope_Camera.setObjectName(u"Scope_Camera")
        self.Scope_Camera.setFrameShape(QFrame.StyledPanel)
        self.Scope_Camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Scope_Camera)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Scope_Camera_Widget = QWidget(self.Scope_Camera)
        self.Scope_Camera_Widget.setObjectName(u"Scope_Camera_Widget")
        self.Scope_Camera_Layout = QVBoxLayout(self.Scope_Camera_Widget)
        self.Scope_Camera_Layout.setSpacing(0)
        self.Scope_Camera_Layout.setObjectName(u"Scope_Camera_Layout")
        self.Scope_Camera_Layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.Scope_Camera_Widget)


        self.verticalLayout_15.addWidget(self.Scope_Camera)

        self.Scope_Display_stackedWidget.addWidget(self.Scope_Camera_page)
        self.Scope_Display1_page = QWidget()
        self.Scope_Display1_page.setObjectName(u"Scope_Display1_page")
        self.verticalLayout_17 = QVBoxLayout(self.Scope_Display1_page)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Scope_Display1_pushButton_frame = QFrame(self.Scope_Display1_page)
        self.Scope_Display1_pushButton_frame.setObjectName(u"Scope_Display1_pushButton_frame")
        self.Scope_Display1_pushButton_frame.setMinimumSize(QSize(0, 20))
        self.Scope_Display1_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.Scope_Display1_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Display1_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.Scope_Display1_pushButton_frame)
        self.horizontalLayout_73.setSpacing(10)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 5, 0)
        self.Scope_Display1_pushButton1 = QPushButton(self.Scope_Display1_pushButton_frame)
        self.Scope_Display1_pushButton1.setObjectName(u"Scope_Display1_pushButton1")
        self.Scope_Display1_pushButton1.setMinimumSize(QSize(175, 0))
        self.Scope_Display1_pushButton1.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_73.addWidget(self.Scope_Display1_pushButton1)

        self.Scope_Display1_pushButton2 = QPushButton(self.Scope_Display1_pushButton_frame)
        self.Scope_Display1_pushButton2.setObjectName(u"Scope_Display1_pushButton2")
        self.Scope_Display1_pushButton2.setMinimumSize(QSize(175, 0))
        self.Scope_Display1_pushButton2.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_73.addWidget(self.Scope_Display1_pushButton2)


        self.verticalLayout_17.addWidget(self.Scope_Display1_pushButton_frame, 0, Qt.AlignRight)

        self.Scope_Display1 = PlotWidget(self.Scope_Display1_page)
        self.Scope_Display1.setObjectName(u"Scope_Display1")
        self.Scope_Display1.setMinimumSize(QSize(0, 0))
        self.LEDZap_Display1_Layout = QVBoxLayout(self.Scope_Display1)
        self.LEDZap_Display1_Layout.setSpacing(0)
        self.LEDZap_Display1_Layout.setObjectName(u"LEDZap_Display1_Layout")
        self.LEDZap_Display1_Layout.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_17.addWidget(self.Scope_Display1)

        self.Scope_Display_stackedWidget.addWidget(self.Scope_Display1_page)
        self.Scope_Display2_page = QWidget()
        self.Scope_Display2_page.setObjectName(u"Scope_Display2_page")
        self.verticalLayout_18 = QVBoxLayout(self.Scope_Display2_page)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Scope_Display2_pushButton_frame = QFrame(self.Scope_Display2_page)
        self.Scope_Display2_pushButton_frame.setObjectName(u"Scope_Display2_pushButton_frame")
        self.Scope_Display2_pushButton_frame.setMinimumSize(QSize(0, 20))
        self.Scope_Display2_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.Scope_Display2_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Display2_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.Scope_Display2_pushButton_frame)
        self.horizontalLayout_74.setSpacing(10)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 5, 0)
        self.Scope_Display2_pushButton1 = QPushButton(self.Scope_Display2_pushButton_frame)
        self.Scope_Display2_pushButton1.setObjectName(u"Scope_Display2_pushButton1")
        self.Scope_Display2_pushButton1.setMinimumSize(QSize(175, 0))
        self.Scope_Display2_pushButton1.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_74.addWidget(self.Scope_Display2_pushButton1)

        self.Scope_Display2_pushButton2 = QPushButton(self.Scope_Display2_pushButton_frame)
        self.Scope_Display2_pushButton2.setObjectName(u"Scope_Display2_pushButton2")
        self.Scope_Display2_pushButton2.setMinimumSize(QSize(175, 0))
        self.Scope_Display2_pushButton2.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_74.addWidget(self.Scope_Display2_pushButton2)


        self.verticalLayout_18.addWidget(self.Scope_Display2_pushButton_frame, 0, Qt.AlignRight)

        self.Scope_Display2 = PlotWidget(self.Scope_Display2_page)
        self.Scope_Display2.setObjectName(u"Scope_Display2")
        self.Scope_Display2.setMinimumSize(QSize(0, 0))
        self.LEDZap_Display1_Layout_2 = QVBoxLayout(self.Scope_Display2)
        self.LEDZap_Display1_Layout_2.setSpacing(0)
        self.LEDZap_Display1_Layout_2.setObjectName(u"LEDZap_Display1_Layout_2")
        self.LEDZap_Display1_Layout_2.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_18.addWidget(self.Scope_Display2)

        self.Scope_Display_stackedWidget.addWidget(self.Scope_Display2_page)

        self.verticalLayout_25.addWidget(self.Scope_Display_stackedWidget)


        self.verticalLayout_8.addWidget(self.Scope_Display_Frame)

        self.Scope_Serial_Frame = QFrame(self.Scope_MainContent_Frame)
        self.Scope_Serial_Frame.setObjectName(u"Scope_Serial_Frame")
        self.Scope_Serial_Frame.setMinimumSize(QSize(0, 60))
        self.Scope_Serial_Frame.setMaximumSize(QSize(16777215, 60))
        self.Scope_Serial_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Serial_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Scope_Serial_Frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Scope_Serial = QWidget(self.Scope_Serial_Frame)
        self.Scope_Serial.setObjectName(u"Scope_Serial")
        self.Scope_Serial.setMinimumSize(QSize(0, 0))
        self.Scope_Serial.setMaximumSize(QSize(16777215, 16777215))
        self.Scope_Serial.setStyleSheet(u"background-color: rgb(0,12,15);")
        self.verticalLayout_27 = QVBoxLayout(self.Scope_Serial)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 0, 10, 0)
        self.Scope_Serial_label = QLabel(self.Scope_Serial)
        self.Scope_Serial_label.setObjectName(u"Scope_Serial_label")
        self.Scope_Serial_label.setFont(font1)
        self.Scope_Serial_label.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.Scope_Serial_label)


        self.verticalLayout_26.addWidget(self.Scope_Serial)


        self.verticalLayout_8.addWidget(self.Scope_Serial_Frame, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.Scope_MainContent_Frame)

        self.line_2 = QFrame(self.Scope_Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_2)

        self.Scope_Stimulus_frame = QFrame(self.Scope_Frame)
        self.Scope_Stimulus_frame.setObjectName(u"Scope_Stimulus_frame")
        self.Scope_Stimulus_frame.setMaximumSize(QSize(400, 16777215))
        self.Scope_Stimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Scope_Stimulus_frame)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Scope_StimulusControl_frame = QFrame(self.Scope_Stimulus_frame)
        self.Scope_StimulusControl_frame.setObjectName(u"Scope_StimulusControl_frame")
        self.Scope_StimulusControl_frame.setMinimumSize(QSize(0, 0))
        self.Scope_StimulusControl_frame.setMaximumSize(QSize(16777215, 125))
        self.Scope_StimulusControl_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_StimulusControl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Scope_StimulusControl_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 5, 0)
        self.Scope_Load_frame = QFrame(self.Scope_StimulusControl_frame)
        self.Scope_Load_frame.setObjectName(u"Scope_Load_frame")
        self.Scope_Load_frame.setFont(font1)
        self.Scope_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.Scope_Load_frame)
        self.horizontalLayout_59.setSpacing(10)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.Scope_Load_pushButton_frame = QFrame(self.Scope_Load_frame)
        self.Scope_Load_pushButton_frame.setObjectName(u"Scope_Load_pushButton_frame")
        self.Scope_Load_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_Load_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Load_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.Scope_Load_pushButton_frame)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.Scope_Load_pushButton = QPushButton(self.Scope_Load_pushButton_frame)
        self.Scope_Load_pushButton.setObjectName(u"Scope_Load_pushButton")
        self.Scope_Load_pushButton.setMinimumSize(QSize(100, 0))
        self.Scope_Load_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Scope_Load_pushButton.setFont(font1)
        self.Scope_Load_pushButton.setCheckable(True)

        self.horizontalLayout_80.addWidget(self.Scope_Load_pushButton)


        self.horizontalLayout_59.addWidget(self.Scope_Load_pushButton_frame)

        self.Scope_Stimulus_Label_frame = QFrame(self.Scope_Load_frame)
        self.Scope_Stimulus_Label_frame.setObjectName(u"Scope_Stimulus_Label_frame")
        self.Scope_Stimulus_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stimulus_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.Scope_Stimulus_Label_frame)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.Scope_Stimulus_Label = QLabel(self.Scope_Stimulus_Label_frame)
        self.Scope_Stimulus_Label.setObjectName(u"Scope_Stimulus_Label")
        self.Scope_Stimulus_Label.setMinimumSize(QSize(0, 25))
        self.Scope_Stimulus_Label.setMaximumSize(QSize(275, 25))
        font4 = QFont()
        font4.setPointSize(8)
        self.Scope_Stimulus_Label.setFont(font4)
        self.Scope_Stimulus_Label.setScaledContents(True)
        self.Scope_Stimulus_Label.setWordWrap(True)

        self.horizontalLayout_79.addWidget(self.Scope_Stimulus_Label)


        self.horizontalLayout_59.addWidget(self.Scope_Stimulus_Label_frame)


        self.verticalLayout_16.addWidget(self.Scope_Load_frame)

        self.Scope_StimulusMain_frame = QFrame(self.Scope_StimulusControl_frame)
        self.Scope_StimulusMain_frame.setObjectName(u"Scope_StimulusMain_frame")
        self.Scope_StimulusMain_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_StimulusMain_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.Scope_StimulusMain_frame)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.Scope_Stimulus_Right_frame = QFrame(self.Scope_StimulusMain_frame)
        self.Scope_Stimulus_Right_frame.setObjectName(u"Scope_Stimulus_Right_frame")
        self.Scope_Stimulus_Right_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stimulus_Right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.Scope_Stimulus_Right_frame)
        self.verticalLayout_97.setSpacing(20)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.Scope_Stimulus_Play_frame = QFrame(self.Scope_Stimulus_Right_frame)
        self.Scope_Stimulus_Play_frame.setObjectName(u"Scope_Stimulus_Play_frame")
        self.Scope_Stimulus_Play_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stimulus_Play_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.Scope_Stimulus_Play_frame)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Scope_Stimulus_Left_frame = QFrame(self.Scope_Stimulus_Play_frame)
        self.Scope_Stimulus_Left_frame.setObjectName(u"Scope_Stimulus_Left_frame")
        self.Scope_Stimulus_Left_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stimulus_Left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.Scope_Stimulus_Left_frame)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.Scope_Display_pushButton_frame = QFrame(self.Scope_Stimulus_Left_frame)
        self.Scope_Display_pushButton_frame.setObjectName(u"Scope_Display_pushButton_frame")
        self.Scope_Display_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Scope_Display_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_Display_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Display_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.Scope_Display_pushButton_frame)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Scope_Display_pushButton = QPushButton(self.Scope_Display_pushButton_frame)
        self.Scope_Display_pushButton.setObjectName(u"Scope_Display_pushButton")
        self.Scope_Display_pushButton.setMinimumSize(QSize(100, 0))
        self.Scope_Display_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Scope_Display_pushButton.setFont(font1)
        self.Scope_Display_pushButton.setCheckable(True)

        self.horizontalLayout_83.addWidget(self.Scope_Display_pushButton)


        self.verticalLayout_96.addWidget(self.Scope_Display_pushButton_frame)


        self.horizontalLayout_46.addWidget(self.Scope_Stimulus_Left_frame)

        self.Scope_Start_pushButton_frame = QFrame(self.Scope_Stimulus_Play_frame)
        self.Scope_Start_pushButton_frame.setObjectName(u"Scope_Start_pushButton_frame")
        self.Scope_Start_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Scope_Start_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_Start_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Start_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.Scope_Start_pushButton_frame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Scope_Start_pushButton = QPushButton(self.Scope_Start_pushButton_frame)
        self.Scope_Start_pushButton.setObjectName(u"Scope_Start_pushButton")
        self.Scope_Start_pushButton.setMinimumSize(QSize(125, 0))
        self.Scope_Start_pushButton.setMaximumSize(QSize(125, 16777215))
        self.Scope_Start_pushButton.setFont(font1)
        self.Scope_Start_pushButton.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.Scope_Start_pushButton)


        self.horizontalLayout_46.addWidget(self.Scope_Start_pushButton_frame)

        self.Scope_Stop_pushButton_frame = QFrame(self.Scope_Stimulus_Play_frame)
        self.Scope_Stop_pushButton_frame.setObjectName(u"Scope_Stop_pushButton_frame")
        self.Scope_Stop_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Scope_Stop_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_Stop_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Stop_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.Scope_Stop_pushButton_frame)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Scope_Stop_pushButton = QPushButton(self.Scope_Stop_pushButton_frame)
        self.Scope_Stop_pushButton.setObjectName(u"Scope_Stop_pushButton")
        self.Scope_Stop_pushButton.setMinimumSize(QSize(125, 0))
        self.Scope_Stop_pushButton.setMaximumSize(QSize(125, 16777215))
        self.Scope_Stop_pushButton.setFont(font1)
        self.Scope_Stop_pushButton.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.Scope_Stop_pushButton)


        self.horizontalLayout_46.addWidget(self.Scope_Stop_pushButton_frame)


        self.verticalLayout_97.addWidget(self.Scope_Stimulus_Play_frame)

        self.Scope_NumbeofLoop_frame = QFrame(self.Scope_Stimulus_Right_frame)
        self.Scope_NumbeofLoop_frame.setObjectName(u"Scope_NumbeofLoop_frame")
        self.Scope_NumbeofLoop_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_NumbeofLoop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.Scope_NumbeofLoop_frame)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.Scope_NumbeofLoop_Label_frame = QFrame(self.Scope_NumbeofLoop_frame)
        self.Scope_NumbeofLoop_Label_frame.setObjectName(u"Scope_NumbeofLoop_Label_frame")
        self.Scope_NumbeofLoop_Label_frame.setMinimumSize(QSize(125, 0))
        self.Scope_NumbeofLoop_Label_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_NumbeofLoop_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_NumbeofLoop_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.Scope_NumbeofLoop_Label_frame)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.Scope_NumbeofLoop_Label = QLabel(self.Scope_NumbeofLoop_Label_frame)
        self.Scope_NumbeofLoop_Label.setObjectName(u"Scope_NumbeofLoop_Label")
        self.Scope_NumbeofLoop_Label.setMaximumSize(QSize(1752, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        self.Scope_NumbeofLoop_Label.setFont(font5)

        self.horizontalLayout_142.addWidget(self.Scope_NumbeofLoop_Label, 0, Qt.AlignRight)


        self.horizontalLayout_140.addWidget(self.Scope_NumbeofLoop_Label_frame, 0, Qt.AlignHCenter)

        self.Scope_NumbeofLoop_lineEdit_frame = QFrame(self.Scope_NumbeofLoop_frame)
        self.Scope_NumbeofLoop_lineEdit_frame.setObjectName(u"Scope_NumbeofLoop_lineEdit_frame")
        self.Scope_NumbeofLoop_lineEdit_frame.setMinimumSize(QSize(125, 0))
        self.Scope_NumbeofLoop_lineEdit_frame.setMaximumSize(QSize(125, 16777215))
        self.Scope_NumbeofLoop_lineEdit_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_NumbeofLoop_lineEdit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.Scope_NumbeofLoop_lineEdit_frame)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.Scope_NumbeofLoop = QLineEdit(self.Scope_NumbeofLoop_lineEdit_frame)
        self.Scope_NumbeofLoop.setObjectName(u"Scope_NumbeofLoop")
        self.Scope_NumbeofLoop.setMinimumSize(QSize(100, 0))
        self.Scope_NumbeofLoop.setMaximumSize(QSize(100, 16777215))
        self.Scope_NumbeofLoop.setFont(font1)
        self.Scope_NumbeofLoop.setStyleSheet(u" border: 1px solid rgb(147,161,161);\n"
"background-color: rgb(7, 54, 66);")
        self.Scope_NumbeofLoop.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_143.addWidget(self.Scope_NumbeofLoop)


        self.horizontalLayout_140.addWidget(self.Scope_NumbeofLoop_lineEdit_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_97.addWidget(self.Scope_NumbeofLoop_frame)


        self.horizontalLayout_141.addWidget(self.Scope_Stimulus_Right_frame)


        self.verticalLayout_16.addWidget(self.Scope_StimulusMain_frame)


        self.verticalLayout_9.addWidget(self.Scope_StimulusControl_frame)

        self.line = QFrame(self.Scope_Stimulus_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.Scope_Opto_frame = QFrame(self.Scope_Stimulus_frame)
        self.Scope_Opto_frame.setObjectName(u"Scope_Opto_frame")
        self.Scope_Opto_frame.setMinimumSize(QSize(0, 0))
        self.Scope_Opto_frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Opto_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Scope_Opto_frame)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 5)
        self.Opto_Label = QLabel(self.Scope_Opto_frame)
        self.Opto_Label.setObjectName(u"Opto_Label")
        self.Opto_Label.setMinimumSize(QSize(0, 0))
        self.Opto_Label.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.Opto_Label.setFont(font6)

        self.verticalLayout_11.addWidget(self.Opto_Label, 0, Qt.AlignHCenter)

        self.Opto1_frame = QFrame(self.Scope_Opto_frame)
        self.Opto1_frame.setObjectName(u"Opto1_frame")
        self.Opto1_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto1_frame.setFrameShadow(QFrame.Raised)
        self.aa = QHBoxLayout(self.Opto1_frame)
        self.aa.setSpacing(5)
        self.aa.setObjectName(u"aa")
        self.aa.setContentsMargins(0, 0, 0, 0)
        self.Opto1_Display_frame = QFrame(self.Opto1_frame)
        self.Opto1_Display_frame.setObjectName(u"Opto1_Display_frame")
        self.Opto1_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Opto1_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto1_Display_frame.setFrameShadow(QFrame.Raised)
        self.Opto1_toggleButton_layout = QHBoxLayout(self.Opto1_Display_frame)
        self.Opto1_toggleButton_layout.setSpacing(0)
        self.Opto1_toggleButton_layout.setObjectName(u"Opto1_toggleButton_layout")
        self.Opto1_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Opto1_Display_label = QLabel(self.Opto1_Display_frame)
        self.Opto1_Display_label.setObjectName(u"Opto1_Display_label")
        self.Opto1_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Opto1_toggleButton_layout.addWidget(self.Opto1_Display_label)


        self.aa.addWidget(self.Opto1_Display_frame)

        self.Opto1_Slider_frame = QFrame(self.Opto1_frame)
        self.Opto1_Slider_frame.setObjectName(u"Opto1_Slider_frame")
        self.Opto1_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Opto1_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto1_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Opto1_Slider_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Opto1_Slider = QSlider(self.Opto1_Slider_frame)
        self.Opto1_Slider.setObjectName(u"Opto1_Slider")
        self.Opto1_Slider.setMaximum(1000)
        self.Opto1_Slider.setSingleStep(1)
        self.Opto1_Slider.setPageStep(25)
        self.Opto1_Slider.setSliderPosition(0)
        self.Opto1_Slider.setOrientation(Qt.Horizontal)
        self.Opto1_Slider.setTickPosition(QSlider.TicksBelow)
        self.Opto1_Slider.setTickInterval(100)

        self.verticalLayout_12.addWidget(self.Opto1_Slider)


        self.aa.addWidget(self.Opto1_Slider_frame)

        self.Opto1_Light_frame = QFrame(self.Opto1_frame)
        self.Opto1_Light_frame.setObjectName(u"Opto1_Light_frame")
        self.Opto1_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Opto1_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto1_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.Opto1_Light_frame)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.Opto1_Value = QLabel(self.Opto1_Light_frame)
        self.Opto1_Value.setObjectName(u"Opto1_Value")
        self.Opto1_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.Opto1_Value)


        self.aa.addWidget(self.Opto1_Light_frame)


        self.verticalLayout_11.addWidget(self.Opto1_frame)

        self.Opto2_frame = QFrame(self.Scope_Opto_frame)
        self.Opto2_frame.setObjectName(u"Opto2_frame")
        self.Opto2_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto2_frame.setFrameShadow(QFrame.Raised)
        self.aa_2 = QHBoxLayout(self.Opto2_frame)
        self.aa_2.setSpacing(5)
        self.aa_2.setObjectName(u"aa_2")
        self.aa_2.setContentsMargins(0, 0, 0, 0)
        self.Opto2_Display_frame = QFrame(self.Opto2_frame)
        self.Opto2_Display_frame.setObjectName(u"Opto2_Display_frame")
        self.Opto2_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Opto2_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto2_Display_frame.setFrameShadow(QFrame.Raised)
        self.Opto2_toggleButton_layout = QHBoxLayout(self.Opto2_Display_frame)
        self.Opto2_toggleButton_layout.setSpacing(0)
        self.Opto2_toggleButton_layout.setObjectName(u"Opto2_toggleButton_layout")
        self.Opto2_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Opto2_Display_label = QLabel(self.Opto2_Display_frame)
        self.Opto2_Display_label.setObjectName(u"Opto2_Display_label")
        self.Opto2_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.Opto2_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Opto2_toggleButton_layout.addWidget(self.Opto2_Display_label)


        self.aa_2.addWidget(self.Opto2_Display_frame)

        self.Opto2_Slider_frame = QFrame(self.Opto2_frame)
        self.Opto2_Slider_frame.setObjectName(u"Opto2_Slider_frame")
        self.Opto2_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Opto2_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto2_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Opto2_Slider_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Opto2_Slider = QSlider(self.Opto2_Slider_frame)
        self.Opto2_Slider.setObjectName(u"Opto2_Slider")
        self.Opto2_Slider.setMaximumSize(QSize(16777215, 16777215))
        self.Opto2_Slider.setMaximum(1000)
        self.Opto2_Slider.setSingleStep(1)
        self.Opto2_Slider.setPageStep(25)
        self.Opto2_Slider.setSliderPosition(0)
        self.Opto2_Slider.setOrientation(Qt.Horizontal)
        self.Opto2_Slider.setTickPosition(QSlider.TicksBelow)
        self.Opto2_Slider.setTickInterval(100)

        self.horizontalLayout_20.addWidget(self.Opto2_Slider)


        self.aa_2.addWidget(self.Opto2_Slider_frame)

        self.Opto2_Light_frame = QFrame(self.Opto2_frame)
        self.Opto2_Light_frame.setObjectName(u"Opto2_Light_frame")
        self.Opto2_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Opto2_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto2_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.Opto2_Light_frame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.Opto2_Value = QLabel(self.Opto2_Light_frame)
        self.Opto2_Value.setObjectName(u"Opto2_Value")
        self.Opto2_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.Opto2_Value)


        self.aa_2.addWidget(self.Opto2_Light_frame)


        self.verticalLayout_11.addWidget(self.Opto2_frame)

        self.Opto3_frame = QFrame(self.Scope_Opto_frame)
        self.Opto3_frame.setObjectName(u"Opto3_frame")
        self.Opto3_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto3_frame.setFrameShadow(QFrame.Raised)
        self.aa_3 = QHBoxLayout(self.Opto3_frame)
        self.aa_3.setSpacing(5)
        self.aa_3.setObjectName(u"aa_3")
        self.aa_3.setContentsMargins(0, 0, 0, 0)
        self.Opto3_Display_frame = QFrame(self.Opto3_frame)
        self.Opto3_Display_frame.setObjectName(u"Opto3_Display_frame")
        self.Opto3_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Opto3_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto3_Display_frame.setFrameShadow(QFrame.Raised)
        self.Opto3_toggleButton_layout = QHBoxLayout(self.Opto3_Display_frame)
        self.Opto3_toggleButton_layout.setSpacing(0)
        self.Opto3_toggleButton_layout.setObjectName(u"Opto3_toggleButton_layout")
        self.Opto3_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Opto3_Display_label = QLabel(self.Opto3_Display_frame)
        self.Opto3_Display_label.setObjectName(u"Opto3_Display_label")
        self.Opto3_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.Opto3_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Opto3_toggleButton_layout.addWidget(self.Opto3_Display_label)


        self.aa_3.addWidget(self.Opto3_Display_frame)

        self.Opto3_Slider_frame = QFrame(self.Opto3_frame)
        self.Opto3_Slider_frame.setObjectName(u"Opto3_Slider_frame")
        self.Opto3_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Opto3_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto3_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.Opto3_Slider_frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Opto3_Slider = QSlider(self.Opto3_Slider_frame)
        self.Opto3_Slider.setObjectName(u"Opto3_Slider")
        self.Opto3_Slider.setMaximum(1000)
        self.Opto3_Slider.setSingleStep(1)
        self.Opto3_Slider.setPageStep(25)
        self.Opto3_Slider.setSliderPosition(0)
        self.Opto3_Slider.setOrientation(Qt.Horizontal)
        self.Opto3_Slider.setTickPosition(QSlider.TicksBelow)
        self.Opto3_Slider.setTickInterval(100)

        self.horizontalLayout_21.addWidget(self.Opto3_Slider)


        self.aa_3.addWidget(self.Opto3_Slider_frame)

        self.Opto3_Light_frame = QFrame(self.Opto3_frame)
        self.Opto3_Light_frame.setObjectName(u"Opto3_Light_frame")
        self.Opto3_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Opto3_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto3_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.Opto3_Light_frame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.Opto3_Value = QLabel(self.Opto3_Light_frame)
        self.Opto3_Value.setObjectName(u"Opto3_Value")
        self.Opto3_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.Opto3_Value)


        self.aa_3.addWidget(self.Opto3_Light_frame)


        self.verticalLayout_11.addWidget(self.Opto3_frame)

        self.Opto4_frame = QFrame(self.Scope_Opto_frame)
        self.Opto4_frame.setObjectName(u"Opto4_frame")
        self.Opto4_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto4_frame.setFrameShadow(QFrame.Raised)
        self.aa_4 = QHBoxLayout(self.Opto4_frame)
        self.aa_4.setSpacing(5)
        self.aa_4.setObjectName(u"aa_4")
        self.aa_4.setContentsMargins(0, 0, 0, 0)
        self.Opto4_Display_frame = QFrame(self.Opto4_frame)
        self.Opto4_Display_frame.setObjectName(u"Opto4_Display_frame")
        self.Opto4_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Opto4_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto4_Display_frame.setFrameShadow(QFrame.Raised)
        self.Opto4_toggleButton_layout = QHBoxLayout(self.Opto4_Display_frame)
        self.Opto4_toggleButton_layout.setSpacing(0)
        self.Opto4_toggleButton_layout.setObjectName(u"Opto4_toggleButton_layout")
        self.Opto4_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Opto4_Display_label = QLabel(self.Opto4_Display_frame)
        self.Opto4_Display_label.setObjectName(u"Opto4_Display_label")
        self.Opto4_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Opto4_toggleButton_layout.addWidget(self.Opto4_Display_label)


        self.aa_4.addWidget(self.Opto4_Display_frame)

        self.Opto4_Slider_frame = QFrame(self.Opto4_frame)
        self.Opto4_Slider_frame.setObjectName(u"Opto4_Slider_frame")
        self.Opto4_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Opto4_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto4_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.Opto4_Slider_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Opto4_Slider = QSlider(self.Opto4_Slider_frame)
        self.Opto4_Slider.setObjectName(u"Opto4_Slider")
        self.Opto4_Slider.setMaximum(1000)
        self.Opto4_Slider.setPageStep(25)
        self.Opto4_Slider.setSliderPosition(0)
        self.Opto4_Slider.setOrientation(Qt.Horizontal)
        self.Opto4_Slider.setTickPosition(QSlider.TicksBelow)
        self.Opto4_Slider.setTickInterval(100)

        self.horizontalLayout_22.addWidget(self.Opto4_Slider)


        self.aa_4.addWidget(self.Opto4_Slider_frame)

        self.Opto4_Light_frame = QFrame(self.Opto4_frame)
        self.Opto4_Light_frame.setObjectName(u"Opto4_Light_frame")
        self.Opto4_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Opto4_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Opto4_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.Opto4_Light_frame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.Opto4_Value = QLabel(self.Opto4_Light_frame)
        self.Opto4_Value.setObjectName(u"Opto4_Value")
        self.Opto4_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.Opto4_Value)


        self.aa_4.addWidget(self.Opto4_Light_frame)


        self.verticalLayout_11.addWidget(self.Opto4_frame)


        self.verticalLayout_9.addWidget(self.Scope_Opto_frame)

        self.line_3 = QFrame(self.Scope_Stimulus_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.Scope_Illumination_Frame = QFrame(self.Scope_Stimulus_frame)
        self.Scope_Illumination_Frame.setObjectName(u"Scope_Illumination_Frame")
        self.Scope_Illumination_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_Illumination_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Scope_Illumination_Frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.Illuminatio_Label = QLabel(self.Scope_Illumination_Frame)
        self.Illuminatio_Label.setObjectName(u"Illuminatio_Label")
        self.Illuminatio_Label.setMaximumSize(QSize(16777215, 20))
        self.Illuminatio_Label.setFont(font6)

        self.verticalLayout_10.addWidget(self.Illuminatio_Label, 0, Qt.AlignHCenter)

        self.Scope_LED_Illumiation_Frame = QFrame(self.Scope_Illumination_Frame)
        self.Scope_LED_Illumiation_Frame.setObjectName(u"Scope_LED_Illumiation_Frame")
        self.Scope_LED_Illumiation_Frame.setFrameShape(QFrame.StyledPanel)
        self.Scope_LED_Illumiation_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.Scope_LED_Illumiation_Frame)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.White_LED_Frame = QFrame(self.Scope_LED_Illumiation_Frame)
        self.White_LED_Frame.setObjectName(u"White_LED_Frame")
        self.White_LED_Frame.setMinimumSize(QSize(0, 0))
        self.White_LED_Frame.setFrameShape(QFrame.StyledPanel)
        self.White_LED_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.White_LED_Frame)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.White_Light_Label = QLabel(self.White_LED_Frame)
        self.White_Light_Label.setObjectName(u"White_Light_Label")
        self.White_Light_Label.setFont(font5)

        self.verticalLayout_13.addWidget(self.White_Light_Label, 0, Qt.AlignHCenter)

        self.White_All_LED_Frame = QFrame(self.White_LED_Frame)
        self.White_All_LED_Frame.setObjectName(u"White_All_LED_Frame")
        self.White_All_LED_Frame.setFrameShape(QFrame.StyledPanel)
        self.White_All_LED_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.White_All_LED_Frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.AllWhite_frame = QFrame(self.White_All_LED_Frame)
        self.AllWhite_frame.setObjectName(u"AllWhite_frame")
        self.AllWhite_frame.setFrameShape(QFrame.StyledPanel)
        self.AllWhite_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.AllWhite_frame)
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.AllWhite_Display_frame = QFrame(self.AllWhite_frame)
        self.AllWhite_Display_frame.setObjectName(u"AllWhite_Display_frame")
        self.AllWhite_Display_frame.setMinimumSize(QSize(50, 0))
        self.AllWhite_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.AllWhite_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.AllWhite_Display_frame.setFrameShadow(QFrame.Raised)
        self.AllWhite_toggleButton_layout = QHBoxLayout(self.AllWhite_Display_frame)
        self.AllWhite_toggleButton_layout.setSpacing(0)
        self.AllWhite_toggleButton_layout.setObjectName(u"AllWhite_toggleButton_layout")
        self.AllWhite_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.AllWhite_label = QLabel(self.AllWhite_Display_frame)
        self.AllWhite_label.setObjectName(u"AllWhite_label")
        self.AllWhite_label.setMaximumSize(QSize(125, 16777215))
        self.AllWhite_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.AllWhite_toggleButton_layout.addWidget(self.AllWhite_label)


        self.horizontalLayout_32.addWidget(self.AllWhite_Display_frame)

        self.AllWhite_Slider_frame = QFrame(self.AllWhite_frame)
        self.AllWhite_Slider_frame.setObjectName(u"AllWhite_Slider_frame")
        self.AllWhite_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.AllWhite_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.AllWhite_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.AllWhite_Slider_frame)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.AllWhite_Slider = QSlider(self.AllWhite_Slider_frame)
        self.AllWhite_Slider.setObjectName(u"AllWhite_Slider")
        self.AllWhite_Slider.setMaximum(100)
        self.AllWhite_Slider.setSliderPosition(0)
        self.AllWhite_Slider.setOrientation(Qt.Horizontal)
        self.AllWhite_Slider.setTickPosition(QSlider.TicksBelow)
        self.AllWhite_Slider.setTickInterval(10)

        self.horizontalLayout_34.addWidget(self.AllWhite_Slider)


        self.horizontalLayout_32.addWidget(self.AllWhite_Slider_frame)

        self.AllWhite_value_frame = QFrame(self.AllWhite_frame)
        self.AllWhite_value_frame.setObjectName(u"AllWhite_value_frame")
        self.AllWhite_value_frame.setMinimumSize(QSize(30, 0))
        self.AllWhite_value_frame.setMaximumSize(QSize(30, 16777215))
        self.AllWhite_value_frame.setFrameShape(QFrame.StyledPanel)
        self.AllWhite_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.AllWhite_value_frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.AllWhite_Value = QLabel(self.AllWhite_value_frame)
        self.AllWhite_Value.setObjectName(u"AllWhite_Value")
        self.AllWhite_Value.setMaximumSize(QSize(16777215, 16777215))
        self.AllWhite_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.AllWhite_Value)


        self.horizontalLayout_32.addWidget(self.AllWhite_value_frame)


        self.horizontalLayout_25.addWidget(self.AllWhite_frame)


        self.verticalLayout_13.addWidget(self.White_All_LED_Frame)

        self.White1_Frame = QFrame(self.White_LED_Frame)
        self.White1_Frame.setObjectName(u"White1_Frame")
        self.White1_Frame.setFrameShape(QFrame.StyledPanel)
        self.White1_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.White1_Frame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.White1_frame = QFrame(self.White1_Frame)
        self.White1_frame.setObjectName(u"White1_frame")
        self.White1_frame.setFrameShape(QFrame.StyledPanel)
        self.White1_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.White1_frame)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.White1_Display_frame = QFrame(self.White1_frame)
        self.White1_Display_frame.setObjectName(u"White1_Display_frame")
        self.White1_Display_frame.setMinimumSize(QSize(50, 0))
        self.White1_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.White1_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.White1_Display_frame.setFrameShadow(QFrame.Raised)
        self.White1_toggleButton_layout = QHBoxLayout(self.White1_Display_frame)
        self.White1_toggleButton_layout.setSpacing(0)
        self.White1_toggleButton_layout.setObjectName(u"White1_toggleButton_layout")
        self.White1_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.White1_label = QLabel(self.White1_Display_frame)
        self.White1_label.setObjectName(u"White1_label")
        self.White1_label.setMaximumSize(QSize(125, 16777215))
        self.White1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.White1_toggleButton_layout.addWidget(self.White1_label)


        self.horizontalLayout_38.addWidget(self.White1_Display_frame)

        self.White1_Slider_frame = QFrame(self.White1_frame)
        self.White1_Slider_frame.setObjectName(u"White1_Slider_frame")
        self.White1_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.White1_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.White1_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.White1_Slider_frame)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.White1_Slider = QSlider(self.White1_Slider_frame)
        self.White1_Slider.setObjectName(u"White1_Slider")
        self.White1_Slider.setMaximum(100)
        self.White1_Slider.setSliderPosition(0)
        self.White1_Slider.setOrientation(Qt.Horizontal)
        self.White1_Slider.setTickPosition(QSlider.TicksBelow)
        self.White1_Slider.setTickInterval(10)

        self.horizontalLayout_39.addWidget(self.White1_Slider)


        self.horizontalLayout_38.addWidget(self.White1_Slider_frame)

        self.White1_value_frame = QFrame(self.White1_frame)
        self.White1_value_frame.setObjectName(u"White1_value_frame")
        self.White1_value_frame.setMinimumSize(QSize(30, 0))
        self.White1_value_frame.setMaximumSize(QSize(30, 16777215))
        self.White1_value_frame.setFrameShape(QFrame.StyledPanel)
        self.White1_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.White1_value_frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.White1_Value = QLabel(self.White1_value_frame)
        self.White1_Value.setObjectName(u"White1_Value")
        self.White1_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.White1_Value)


        self.horizontalLayout_38.addWidget(self.White1_value_frame)


        self.horizontalLayout_45.addWidget(self.White1_frame)


        self.verticalLayout_13.addWidget(self.White1_Frame)

        self.White2_Frame = QFrame(self.White_LED_Frame)
        self.White2_Frame.setObjectName(u"White2_Frame")
        self.White2_Frame.setFrameShape(QFrame.StyledPanel)
        self.White2_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.White2_Frame)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.White2_frame = QFrame(self.White2_Frame)
        self.White2_frame.setObjectName(u"White2_frame")
        self.White2_frame.setFrameShape(QFrame.StyledPanel)
        self.White2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.White2_frame)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.White2_Display_frame = QFrame(self.White2_frame)
        self.White2_Display_frame.setObjectName(u"White2_Display_frame")
        self.White2_Display_frame.setMinimumSize(QSize(50, 0))
        self.White2_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.White2_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.White2_Display_frame.setFrameShadow(QFrame.Raised)
        self.White2_toggleButton_layout = QHBoxLayout(self.White2_Display_frame)
        self.White2_toggleButton_layout.setSpacing(0)
        self.White2_toggleButton_layout.setObjectName(u"White2_toggleButton_layout")
        self.White2_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.White2_label = QLabel(self.White2_Display_frame)
        self.White2_label.setObjectName(u"White2_label")
        self.White2_label.setMaximumSize(QSize(125, 16777215))
        self.White2_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.White2_toggleButton_layout.addWidget(self.White2_label)


        self.horizontalLayout_40.addWidget(self.White2_Display_frame)

        self.White2_Slider_frame = QFrame(self.White2_frame)
        self.White2_Slider_frame.setObjectName(u"White2_Slider_frame")
        self.White2_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.White2_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.White2_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.White2_Slider_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.White2_Slider = QSlider(self.White2_Slider_frame)
        self.White2_Slider.setObjectName(u"White2_Slider")
        self.White2_Slider.setMaximum(100)
        self.White2_Slider.setSliderPosition(0)
        self.White2_Slider.setOrientation(Qt.Horizontal)
        self.White2_Slider.setTickPosition(QSlider.TicksBelow)
        self.White2_Slider.setTickInterval(10)

        self.horizontalLayout_41.addWidget(self.White2_Slider)


        self.horizontalLayout_40.addWidget(self.White2_Slider_frame)

        self.White2_value_frame = QFrame(self.White2_frame)
        self.White2_value_frame.setObjectName(u"White2_value_frame")
        self.White2_value_frame.setMinimumSize(QSize(30, 0))
        self.White2_value_frame.setMaximumSize(QSize(30, 16777215))
        self.White2_value_frame.setFrameShape(QFrame.StyledPanel)
        self.White2_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.White2_value_frame)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.White2_Value = QLabel(self.White2_value_frame)
        self.White2_Value.setObjectName(u"White2_Value")
        self.White2_Value.setMinimumSize(QSize(0, 0))
        self.White2_Value.setMaximumSize(QSize(16777215, 16777215))
        self.White2_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.White2_Value)


        self.horizontalLayout_40.addWidget(self.White2_value_frame)


        self.horizontalLayout_51.addWidget(self.White2_frame)


        self.verticalLayout_13.addWidget(self.White2_Frame)

        self.White3_Frame = QFrame(self.White_LED_Frame)
        self.White3_Frame.setObjectName(u"White3_Frame")
        self.White3_Frame.setFrameShape(QFrame.StyledPanel)
        self.White3_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.White3_Frame)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.White3_frame = QFrame(self.White3_Frame)
        self.White3_frame.setObjectName(u"White3_frame")
        self.White3_frame.setFrameShape(QFrame.StyledPanel)
        self.White3_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.White3_frame)
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.White3_Display_frame = QFrame(self.White3_frame)
        self.White3_Display_frame.setObjectName(u"White3_Display_frame")
        self.White3_Display_frame.setMinimumSize(QSize(50, 0))
        self.White3_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.White3_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.White3_Display_frame.setFrameShadow(QFrame.Raised)
        self.White3_toggleButton_layout = QHBoxLayout(self.White3_Display_frame)
        self.White3_toggleButton_layout.setSpacing(0)
        self.White3_toggleButton_layout.setObjectName(u"White3_toggleButton_layout")
        self.White3_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.White3_label = QLabel(self.White3_Display_frame)
        self.White3_label.setObjectName(u"White3_label")
        self.White3_label.setMaximumSize(QSize(125, 16777215))
        self.White3_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.White3_toggleButton_layout.addWidget(self.White3_label)


        self.horizontalLayout_36.addWidget(self.White3_Display_frame)

        self.White3_Slider_frame = QFrame(self.White3_frame)
        self.White3_Slider_frame.setObjectName(u"White3_Slider_frame")
        self.White3_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.White3_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.White3_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.White3_Slider_frame)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.White3_Slider = QSlider(self.White3_Slider_frame)
        self.White3_Slider.setObjectName(u"White3_Slider")
        self.White3_Slider.setMaximum(100)
        self.White3_Slider.setSliderPosition(0)
        self.White3_Slider.setOrientation(Qt.Horizontal)
        self.White3_Slider.setTickPosition(QSlider.TicksBelow)
        self.White3_Slider.setTickInterval(10)

        self.horizontalLayout_37.addWidget(self.White3_Slider)


        self.horizontalLayout_36.addWidget(self.White3_Slider_frame)

        self.White3_value_frame = QFrame(self.White3_frame)
        self.White3_value_frame.setObjectName(u"White3_value_frame")
        self.White3_value_frame.setMinimumSize(QSize(30, 0))
        self.White3_value_frame.setMaximumSize(QSize(30, 16777215))
        self.White3_value_frame.setFrameShape(QFrame.StyledPanel)
        self.White3_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.White3_value_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.White3_Value = QLabel(self.White3_value_frame)
        self.White3_Value.setObjectName(u"White3_Value")
        self.White3_Value.setMinimumSize(QSize(0, 0))
        self.White3_Value.setMaximumSize(QSize(16777215, 16777215))
        self.White3_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.White3_Value)


        self.horizontalLayout_36.addWidget(self.White3_value_frame)


        self.horizontalLayout_27.addWidget(self.White3_frame)


        self.verticalLayout_13.addWidget(self.White3_Frame)

        self.White4_Frame = QFrame(self.White_LED_Frame)
        self.White4_Frame.setObjectName(u"White4_Frame")
        self.White4_Frame.setFrameShape(QFrame.StyledPanel)
        self.White4_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.White4_Frame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.White4_frame = QFrame(self.White4_Frame)
        self.White4_frame.setObjectName(u"White4_frame")
        self.White4_frame.setFrameShape(QFrame.StyledPanel)
        self.White4_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.White4_frame)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.White4_Display_frame = QFrame(self.White4_frame)
        self.White4_Display_frame.setObjectName(u"White4_Display_frame")
        self.White4_Display_frame.setMinimumSize(QSize(50, 0))
        self.White4_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.White4_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.White4_Display_frame.setFrameShadow(QFrame.Raised)
        self.White4_toggleButton_layout = QHBoxLayout(self.White4_Display_frame)
        self.White4_toggleButton_layout.setSpacing(0)
        self.White4_toggleButton_layout.setObjectName(u"White4_toggleButton_layout")
        self.White4_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.White4_label = QLabel(self.White4_Display_frame)
        self.White4_label.setObjectName(u"White4_label")
        self.White4_label.setMaximumSize(QSize(125, 16777215))
        self.White4_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.White4_toggleButton_layout.addWidget(self.White4_label)


        self.horizontalLayout_42.addWidget(self.White4_Display_frame)

        self.White4_Slider_frame = QFrame(self.White4_frame)
        self.White4_Slider_frame.setObjectName(u"White4_Slider_frame")
        self.White4_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.White4_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.White4_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.White4_Slider_frame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.White4_Slider = QSlider(self.White4_Slider_frame)
        self.White4_Slider.setObjectName(u"White4_Slider")
        self.White4_Slider.setMaximum(100)
        self.White4_Slider.setSliderPosition(0)
        self.White4_Slider.setOrientation(Qt.Horizontal)
        self.White4_Slider.setTickPosition(QSlider.TicksBelow)
        self.White4_Slider.setTickInterval(10)

        self.horizontalLayout_43.addWidget(self.White4_Slider)


        self.horizontalLayout_42.addWidget(self.White4_Slider_frame)

        self.White4_value_frame = QFrame(self.White4_frame)
        self.White4_value_frame.setObjectName(u"White4_value_frame")
        self.White4_value_frame.setMinimumSize(QSize(30, 0))
        self.White4_value_frame.setMaximumSize(QSize(30, 16777215))
        self.White4_value_frame.setFrameShape(QFrame.StyledPanel)
        self.White4_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.White4_value_frame)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.White4_Value = QLabel(self.White4_value_frame)
        self.White4_Value.setObjectName(u"White4_Value")
        self.White4_Value.setMinimumSize(QSize(0, 0))
        self.White4_Value.setMaximumSize(QSize(16777215, 16777215))
        self.White4_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.White4_Value)


        self.horizontalLayout_42.addWidget(self.White4_value_frame)


        self.horizontalLayout_44.addWidget(self.White4_frame)


        self.verticalLayout_13.addWidget(self.White4_Frame)


        self.horizontalLayout_23.addWidget(self.White_LED_Frame)

        self.line_4 = QFrame(self.Scope_LED_Illumiation_Frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_23.addWidget(self.line_4)

        self.IR_LED_frame = QFrame(self.Scope_LED_Illumiation_Frame)
        self.IR_LED_frame.setObjectName(u"IR_LED_frame")
        self.IR_LED_frame.setFrameShape(QFrame.StyledPanel)
        self.IR_LED_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.IR_LED_frame)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.IR_Light_Label = QLabel(self.IR_LED_frame)
        self.IR_Light_Label.setObjectName(u"IR_Light_Label")
        self.IR_Light_Label.setFont(font5)

        self.verticalLayout_14.addWidget(self.IR_Light_Label, 0, Qt.AlignHCenter)

        self.AllIR_LED_Frame = QFrame(self.IR_LED_frame)
        self.AllIR_LED_Frame.setObjectName(u"AllIR_LED_Frame")
        self.AllIR_LED_Frame.setFrameShape(QFrame.StyledPanel)
        self.AllIR_LED_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.AllIR_LED_Frame)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.AllIR_frame = QFrame(self.AllIR_LED_Frame)
        self.AllIR_frame.setObjectName(u"AllIR_frame")
        self.AllIR_frame.setFrameShape(QFrame.StyledPanel)
        self.AllIR_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.AllIR_frame)
        self.horizontalLayout_58.setSpacing(5)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.AllIR_Display_frame = QFrame(self.AllIR_frame)
        self.AllIR_Display_frame.setObjectName(u"AllIR_Display_frame")
        self.AllIR_Display_frame.setMinimumSize(QSize(50, 0))
        self.AllIR_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.AllIR_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.AllIR_Display_frame.setFrameShadow(QFrame.Raised)
        self.AllIR_toggleButton_layout = QHBoxLayout(self.AllIR_Display_frame)
        self.AllIR_toggleButton_layout.setSpacing(0)
        self.AllIR_toggleButton_layout.setObjectName(u"AllIR_toggleButton_layout")
        self.AllIR_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.AllIR_label = QLabel(self.AllIR_Display_frame)
        self.AllIR_label.setObjectName(u"AllIR_label")
        self.AllIR_label.setMinimumSize(QSize(0, 0))
        self.AllIR_label.setMaximumSize(QSize(125, 16777215))
        self.AllIR_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.AllIR_toggleButton_layout.addWidget(self.AllIR_label)


        self.horizontalLayout_58.addWidget(self.AllIR_Display_frame)

        self.AllIR_Slider_frame = QFrame(self.AllIR_frame)
        self.AllIR_Slider_frame.setObjectName(u"AllIR_Slider_frame")
        self.AllIR_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.AllIR_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.AllIR_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.AllIR_Slider_frame)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.AllIR_Slider = QSlider(self.AllIR_Slider_frame)
        self.AllIR_Slider.setObjectName(u"AllIR_Slider")
        self.AllIR_Slider.setMaximum(100)
        self.AllIR_Slider.setSliderPosition(0)
        self.AllIR_Slider.setOrientation(Qt.Horizontal)
        self.AllIR_Slider.setTickPosition(QSlider.TicksBelow)
        self.AllIR_Slider.setTickInterval(10)

        self.horizontalLayout_60.addWidget(self.AllIR_Slider)


        self.horizontalLayout_58.addWidget(self.AllIR_Slider_frame)

        self.AllIR_value_frame = QFrame(self.AllIR_frame)
        self.AllIR_value_frame.setObjectName(u"AllIR_value_frame")
        self.AllIR_value_frame.setMinimumSize(QSize(30, 0))
        self.AllIR_value_frame.setMaximumSize(QSize(30, 16777215))
        self.AllIR_value_frame.setFrameShape(QFrame.StyledPanel)
        self.AllIR_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.AllIR_value_frame)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.AllIR_Value = QLabel(self.AllIR_value_frame)
        self.AllIR_Value.setObjectName(u"AllIR_Value")
        self.AllIR_Value.setMinimumSize(QSize(0, 0))
        self.AllIR_Value.setMaximumSize(QSize(16777215, 16777215))
        self.AllIR_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.AllIR_Value)


        self.horizontalLayout_58.addWidget(self.AllIR_value_frame)


        self.horizontalLayout_72.addWidget(self.AllIR_frame)


        self.verticalLayout_14.addWidget(self.AllIR_LED_Frame)

        self.IR1_Frame = QFrame(self.IR_LED_frame)
        self.IR1_Frame.setObjectName(u"IR1_Frame")
        self.IR1_Frame.setFrameShape(QFrame.StyledPanel)
        self.IR1_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.IR1_Frame)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.IR1_frame = QFrame(self.IR1_Frame)
        self.IR1_frame.setObjectName(u"IR1_frame")
        self.IR1_frame.setFrameShape(QFrame.StyledPanel)
        self.IR1_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.IR1_frame)
        self.horizontalLayout_62.setSpacing(5)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.IR1_Display_frame = QFrame(self.IR1_frame)
        self.IR1_Display_frame.setObjectName(u"IR1_Display_frame")
        self.IR1_Display_frame.setMinimumSize(QSize(50, 0))
        self.IR1_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.IR1_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.IR1_Display_frame.setFrameShadow(QFrame.Raised)
        self.IR1_toggleButton_layout = QHBoxLayout(self.IR1_Display_frame)
        self.IR1_toggleButton_layout.setSpacing(0)
        self.IR1_toggleButton_layout.setObjectName(u"IR1_toggleButton_layout")
        self.IR1_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.IR1_label = QLabel(self.IR1_Display_frame)
        self.IR1_label.setObjectName(u"IR1_label")
        self.IR1_label.setMinimumSize(QSize(0, 0))
        self.IR1_label.setMaximumSize(QSize(125, 16777215))
        self.IR1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.IR1_toggleButton_layout.addWidget(self.IR1_label)


        self.horizontalLayout_62.addWidget(self.IR1_Display_frame)

        self.IR1_Slider_frame = QFrame(self.IR1_frame)
        self.IR1_Slider_frame.setObjectName(u"IR1_Slider_frame")
        self.IR1_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.IR1_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.IR1_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.IR1_Slider_frame)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.IR1_Slider = QSlider(self.IR1_Slider_frame)
        self.IR1_Slider.setObjectName(u"IR1_Slider")
        self.IR1_Slider.setMaximum(100)
        self.IR1_Slider.setSliderPosition(0)
        self.IR1_Slider.setOrientation(Qt.Horizontal)
        self.IR1_Slider.setTickPosition(QSlider.TicksBelow)
        self.IR1_Slider.setTickInterval(10)

        self.horizontalLayout_63.addWidget(self.IR1_Slider)


        self.horizontalLayout_62.addWidget(self.IR1_Slider_frame)

        self.IR1_value_frame = QFrame(self.IR1_frame)
        self.IR1_value_frame.setObjectName(u"IR1_value_frame")
        self.IR1_value_frame.setMinimumSize(QSize(30, 0))
        self.IR1_value_frame.setMaximumSize(QSize(30, 16777215))
        self.IR1_value_frame.setFrameShape(QFrame.StyledPanel)
        self.IR1_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.IR1_value_frame)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.IR1_Value = QLabel(self.IR1_value_frame)
        self.IR1_Value.setObjectName(u"IR1_Value")
        self.IR1_Value.setMinimumSize(QSize(0, 0))
        self.IR1_Value.setMaximumSize(QSize(16777215, 16777215))
        self.IR1_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.IR1_Value)


        self.horizontalLayout_62.addWidget(self.IR1_value_frame)


        self.horizontalLayout_71.addWidget(self.IR1_frame)


        self.verticalLayout_14.addWidget(self.IR1_Frame)

        self.IR2_Frame = QFrame(self.IR_LED_frame)
        self.IR2_Frame.setObjectName(u"IR2_Frame")
        self.IR2_Frame.setFrameShape(QFrame.StyledPanel)
        self.IR2_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.IR2_Frame)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.IR2_frame = QFrame(self.IR2_Frame)
        self.IR2_frame.setObjectName(u"IR2_frame")
        self.IR2_frame.setFrameShape(QFrame.StyledPanel)
        self.IR2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.IR2_frame)
        self.horizontalLayout_65.setSpacing(5)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.IR2_Display_frame = QFrame(self.IR2_frame)
        self.IR2_Display_frame.setObjectName(u"IR2_Display_frame")
        self.IR2_Display_frame.setMinimumSize(QSize(50, 0))
        self.IR2_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.IR2_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.IR2_Display_frame.setFrameShadow(QFrame.Raised)
        self.IR2_toggleButton_layout = QHBoxLayout(self.IR2_Display_frame)
        self.IR2_toggleButton_layout.setSpacing(0)
        self.IR2_toggleButton_layout.setObjectName(u"IR2_toggleButton_layout")
        self.IR2_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.IR2_label = QLabel(self.IR2_Display_frame)
        self.IR2_label.setObjectName(u"IR2_label")
        self.IR2_label.setMinimumSize(QSize(0, 0))
        self.IR2_label.setMaximumSize(QSize(125, 16777215))
        self.IR2_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.IR2_toggleButton_layout.addWidget(self.IR2_label)


        self.horizontalLayout_65.addWidget(self.IR2_Display_frame)

        self.IR2_Slider_frame = QFrame(self.IR2_frame)
        self.IR2_Slider_frame.setObjectName(u"IR2_Slider_frame")
        self.IR2_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.IR2_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.IR2_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.IR2_Slider_frame)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.IR2_Slider = QSlider(self.IR2_Slider_frame)
        self.IR2_Slider.setObjectName(u"IR2_Slider")
        self.IR2_Slider.setMaximum(100)
        self.IR2_Slider.setSliderPosition(0)
        self.IR2_Slider.setOrientation(Qt.Horizontal)
        self.IR2_Slider.setTickPosition(QSlider.TicksBelow)
        self.IR2_Slider.setTickInterval(10)

        self.horizontalLayout_66.addWidget(self.IR2_Slider)


        self.horizontalLayout_65.addWidget(self.IR2_Slider_frame)

        self.IR2_value_frame = QFrame(self.IR2_frame)
        self.IR2_value_frame.setObjectName(u"IR2_value_frame")
        self.IR2_value_frame.setMinimumSize(QSize(30, 0))
        self.IR2_value_frame.setMaximumSize(QSize(30, 16777215))
        self.IR2_value_frame.setFrameShape(QFrame.StyledPanel)
        self.IR2_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.IR2_value_frame)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.IR2_Value = QLabel(self.IR2_value_frame)
        self.IR2_Value.setObjectName(u"IR2_Value")
        self.IR2_Value.setMinimumSize(QSize(0, 0))
        self.IR2_Value.setMaximumSize(QSize(16777215, 16777215))
        self.IR2_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.IR2_Value)


        self.horizontalLayout_65.addWidget(self.IR2_value_frame)


        self.horizontalLayout_70.addWidget(self.IR2_frame)


        self.verticalLayout_14.addWidget(self.IR2_Frame)

        self.IR3_Frame = QFrame(self.IR_LED_frame)
        self.IR3_Frame.setObjectName(u"IR3_Frame")
        self.IR3_Frame.setFrameShape(QFrame.StyledPanel)
        self.IR3_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.IR3_Frame)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.IR3_frame = QFrame(self.IR3_Frame)
        self.IR3_frame.setObjectName(u"IR3_frame")
        self.IR3_frame.setFrameShape(QFrame.StyledPanel)
        self.IR3_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.IR3_frame)
        self.horizontalLayout_55.setSpacing(5)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.IR3_Display_frame = QFrame(self.IR3_frame)
        self.IR3_Display_frame.setObjectName(u"IR3_Display_frame")
        self.IR3_Display_frame.setMinimumSize(QSize(50, 0))
        self.IR3_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.IR3_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.IR3_Display_frame.setFrameShadow(QFrame.Raised)
        self.IR3_toggleButton_layout = QHBoxLayout(self.IR3_Display_frame)
        self.IR3_toggleButton_layout.setSpacing(0)
        self.IR3_toggleButton_layout.setObjectName(u"IR3_toggleButton_layout")
        self.IR3_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.IR3_label = QLabel(self.IR3_Display_frame)
        self.IR3_label.setObjectName(u"IR3_label")
        self.IR3_label.setMinimumSize(QSize(0, 0))
        self.IR3_label.setMaximumSize(QSize(125, 16777215))
        self.IR3_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.IR3_toggleButton_layout.addWidget(self.IR3_label)


        self.horizontalLayout_55.addWidget(self.IR3_Display_frame)

        self.IR3_Slider_frame = QFrame(self.IR3_frame)
        self.IR3_Slider_frame.setObjectName(u"IR3_Slider_frame")
        self.IR3_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.IR3_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.IR3_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.IR3_Slider_frame)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.IR3_Slider = QSlider(self.IR3_Slider_frame)
        self.IR3_Slider.setObjectName(u"IR3_Slider")
        self.IR3_Slider.setMaximum(100)
        self.IR3_Slider.setSliderPosition(0)
        self.IR3_Slider.setOrientation(Qt.Horizontal)
        self.IR3_Slider.setTickPosition(QSlider.TicksBelow)
        self.IR3_Slider.setTickInterval(10)

        self.horizontalLayout_56.addWidget(self.IR3_Slider)


        self.horizontalLayout_55.addWidget(self.IR3_Slider_frame)

        self.IR3_value_frame = QFrame(self.IR3_frame)
        self.IR3_value_frame.setObjectName(u"IR3_value_frame")
        self.IR3_value_frame.setMinimumSize(QSize(30, 0))
        self.IR3_value_frame.setMaximumSize(QSize(30, 16777215))
        self.IR3_value_frame.setFrameShape(QFrame.StyledPanel)
        self.IR3_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.IR3_value_frame)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.IR3_Value = QLabel(self.IR3_value_frame)
        self.IR3_Value.setObjectName(u"IR3_Value")
        self.IR3_Value.setMinimumSize(QSize(0, 0))
        self.IR3_Value.setMaximumSize(QSize(16777215, 16777215))
        self.IR3_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.IR3_Value)


        self.horizontalLayout_55.addWidget(self.IR3_value_frame)


        self.horizontalLayout_69.addWidget(self.IR3_frame)


        self.verticalLayout_14.addWidget(self.IR3_Frame)

        self.IR4_Frame = QFrame(self.IR_LED_frame)
        self.IR4_Frame.setObjectName(u"IR4_Frame")
        self.IR4_Frame.setFrameShape(QFrame.StyledPanel)
        self.IR4_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.IR4_Frame)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.IR4_frame = QFrame(self.IR4_Frame)
        self.IR4_frame.setObjectName(u"IR4_frame")
        self.IR4_frame.setFrameShape(QFrame.StyledPanel)
        self.IR4_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.IR4_frame)
        self.horizontalLayout_52.setSpacing(5)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.IR4_Display_frame = QFrame(self.IR4_frame)
        self.IR4_Display_frame.setObjectName(u"IR4_Display_frame")
        self.IR4_Display_frame.setMinimumSize(QSize(50, 0))
        self.IR4_Display_frame.setMaximumSize(QSize(50, 16777215))
        self.IR4_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.IR4_Display_frame.setFrameShadow(QFrame.Raised)
        self.IR4_toggleButton_layout = QHBoxLayout(self.IR4_Display_frame)
        self.IR4_toggleButton_layout.setSpacing(0)
        self.IR4_toggleButton_layout.setObjectName(u"IR4_toggleButton_layout")
        self.IR4_toggleButton_layout.setContentsMargins(0, 0, 0, 0)
        self.IR4_label = QLabel(self.IR4_Display_frame)
        self.IR4_label.setObjectName(u"IR4_label")
        self.IR4_label.setMinimumSize(QSize(0, 0))
        self.IR4_label.setMaximumSize(QSize(125, 16777215))
        self.IR4_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.IR4_toggleButton_layout.addWidget(self.IR4_label)


        self.horizontalLayout_52.addWidget(self.IR4_Display_frame)

        self.IR4_Slider_frame = QFrame(self.IR4_frame)
        self.IR4_Slider_frame.setObjectName(u"IR4_Slider_frame")
        self.IR4_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.IR4_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.IR4_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.IR4_Slider_frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.IR4_Slider = QSlider(self.IR4_Slider_frame)
        self.IR4_Slider.setObjectName(u"IR4_Slider")
        self.IR4_Slider.setMaximum(100)
        self.IR4_Slider.setSliderPosition(0)
        self.IR4_Slider.setOrientation(Qt.Horizontal)
        self.IR4_Slider.setTickPosition(QSlider.TicksBelow)
        self.IR4_Slider.setTickInterval(10)

        self.horizontalLayout_53.addWidget(self.IR4_Slider)


        self.horizontalLayout_52.addWidget(self.IR4_Slider_frame)

        self.IR4_value_frame = QFrame(self.IR4_frame)
        self.IR4_value_frame.setObjectName(u"IR4_value_frame")
        self.IR4_value_frame.setMinimumSize(QSize(30, 0))
        self.IR4_value_frame.setMaximumSize(QSize(30, 16777215))
        self.IR4_value_frame.setFrameShape(QFrame.StyledPanel)
        self.IR4_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.IR4_value_frame)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.IR4_Value = QLabel(self.IR4_value_frame)
        self.IR4_Value.setObjectName(u"IR4_Value")
        self.IR4_Value.setMinimumSize(QSize(0, 0))
        self.IR4_Value.setMaximumSize(QSize(16777215, 16777215))
        self.IR4_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.IR4_Value)


        self.horizontalLayout_52.addWidget(self.IR4_value_frame)


        self.horizontalLayout_68.addWidget(self.IR4_frame)


        self.verticalLayout_14.addWidget(self.IR4_Frame)


        self.horizontalLayout_23.addWidget(self.IR_LED_frame)


        self.verticalLayout_10.addWidget(self.Scope_LED_Illumiation_Frame)


        self.verticalLayout_9.addWidget(self.Scope_Illumination_Frame)


        self.horizontalLayout_13.addWidget(self.Scope_Stimulus_frame)


        self.verticalLayout_7.addWidget(self.Scope_Frame)

        self.Main_stackedWidget.addWidget(self.Scope_Page)
        self.About_Page = QWidget()
        self.About_Page.setObjectName(u"About_Page")
        self.horizontalLayout_15 = QHBoxLayout(self.About_Page)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.About_Page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label)

        self.Main_stackedWidget.addWidget(self.About_Page)
        self.GitHub_Page = QWidget()
        self.GitHub_Page.setObjectName(u"GitHub_Page")
        self.horizontalLayout_16 = QHBoxLayout(self.GitHub_Page)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.GitHub_Page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.Main_stackedWidget.addWidget(self.GitHub_Page)
        self.Help_Page = QWidget()
        self.Help_Page.setObjectName(u"Help_Page")
        self.horizontalLayout_17 = QHBoxLayout(self.Help_Page)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.Help_Page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_3)

        self.Main_stackedWidget.addWidget(self.Help_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.horizontalLayout_18 = QHBoxLayout(self.Settings_Page)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.Settings_Page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.Main_stackedWidget.addWidget(self.Settings_Page)

        self.horizontalLayout_12.addWidget(self.Main_stackedWidget)


        self.horizontalLayout_10.addWidget(self.MainContent_Frame)


        self.verticalLayout.addWidget(self.CenterMainFrame)

        self.BottomMainFrame = QFrame(self.centralwidget)
        self.BottomMainFrame.setObjectName(u"BottomMainFrame")
        self.BottomMainFrame.setMinimumSize(QSize(0, 30))
        self.BottomMainFrame.setMaximumSize(QSize(16777215, 30))
        self.BottomMainFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BottomMainFrame)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Footer_Frame = QFrame(self.BottomMainFrame)
        self.Footer_Frame.setObjectName(u"Footer_Frame")
        self.Footer_Frame.setMinimumSize(QSize(0, 30))
        self.Footer_Frame.setMaximumSize(QSize(16777215, 50))
        self.Footer_Frame.setFrameShape(QFrame.StyledPanel)
        self.Footer_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Footer_Frame)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.License_Frame = QFrame(self.Footer_Frame)
        self.License_Frame.setObjectName(u"License_Frame")
        self.License_Frame.setFrameShape(QFrame.StyledPanel)
        self.License_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.License_Frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.License_Label = QLabel(self.License_Frame)
        self.License_Label.setObjectName(u"License_Label")

        self.horizontalLayout_8.addWidget(self.License_Label)


        self.horizontalLayout_6.addWidget(self.License_Frame)

        self.Logo_Frame = QFrame(self.Footer_Frame)
        self.Logo_Frame.setObjectName(u"Logo_Frame")
        self.Logo_Frame.setFrameShape(QFrame.StyledPanel)
        self.Logo_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Logo_Frame)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.Logo_Frame, 0, Qt.AlignRight)

        self.OSN_Logo = QLabel(self.Footer_Frame)
        self.OSN_Logo.setObjectName(u"OSN_Logo")
        self.OSN_Logo.setMinimumSize(QSize(60, 30))
        self.OSN_Logo.setMaximumSize(QSize(60, 30))
        self.OSN_Logo.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.OSN_Logo.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.OSN_Logo)

        self.SizeGrip_Frame = QFrame(self.Footer_Frame)
        self.SizeGrip_Frame.setObjectName(u"SizeGrip_Frame")
        self.SizeGrip_Frame.setMinimumSize(QSize(20, 20))
        self.SizeGrip_Frame.setMaximumSize(QSize(20, 20))
        self.SizeGrip_Frame.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.SizeGrip_Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.SizeGrip_Label = QLabel(self.SizeGrip_Frame)
        self.SizeGrip_Label.setObjectName(u"SizeGrip_Label")
        self.SizeGrip_Label.setPixmap(QPixmap(u":/resources/resources/SizeGrip.png"))
        self.SizeGrip_Label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.SizeGrip_Label)


        self.horizontalLayout_6.addWidget(self.SizeGrip_Frame)


        self.horizontalLayout_5.addWidget(self.Footer_Frame)


        self.verticalLayout.addWidget(self.BottomMainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.Main_stackedWidget.setCurrentIndex(1)
        self.Scope_CameraSelectPortComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AppName_pushButton.setText(QCoreApplication.translate("MainWindow", u"IssaScope v1.0", None))
        self.Reduce_pushButton.setText("")
        self.Expand_pushButton.setText("")
        self.Exit_pushButton.setText("")
        self.DropMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Menus", None))
        self.Scope_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin'", None))
        self.Settings_pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.About_pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Help_pushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.GitHub_pushButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.HideSubFrame_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Sub-Menus", None))
        self.Home_Logo.setText("")
        self.Home_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#93a1a1;\">IssaScope </span><span style=\" font-size:16pt; color:#93a1a1;\">v1.0</span></p><p align=\"center\"><span style=\" font-size:16pt;\">An open source ethoscope for optogenetics stimulation</span></p><p align=\"right\"><span style=\" font-size:8pt; font-weight:700;\">Conceived and developed by M.J.Y. Zimmermann</span></p></body></html>", None))
        self.Home_Main_Text.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">This project is licensed under the </span><span style=\" font-size:12pt; font-weight:700; color:#268bd2;\">GNU General Public License v3.0</span></p>\n"
"<"
                        "p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">The hardware is licensed under the </span><span style=\" font-size:12pt; font-weight:700; color:#268bd2;\">CERN OHL v1.2</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700; color:#268bd2;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">https://github.com/OpenSourceNeuro/LED-Zappelin_V2</span></p></body></html>", None))
        self.Home_Main_Illustration_Title.setText(QCoreApplication.translate("MainWindow", u"Studying the Dark Side of the Retina", None))
        self.Home_Main_Illustration_Image.setText("")
        self.Scope_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.Scope_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.Scope_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.Scope_CameraSelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Camera:", None))
        self.Scope_CameraSelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))
        self.Scope_CameraSelectPortComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Basler Camera", None))
        self.Scope_CameraSelectPortComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"USB Camera", None))

        self.Scope_CameraSelectPortComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Select a COM port:", None))
        self.Scope_Camera_pushButton1.setText(QCoreApplication.translate("MainWindow", u"Single stimulus display", None))
        self.Scope_Camera_pushButton2.setText(QCoreApplication.translate("MainWindow", u"Multiple  stimulus display", None))
        self.Scope_Display1_pushButton1.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.Scope_Display1_pushButton2.setText(QCoreApplication.translate("MainWindow", u"Multiple stimulus display", None))
        self.Scope_Display2_pushButton1.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.Scope_Display2_pushButton2.setText(QCoreApplication.translate("MainWindow", u"Single stimulus display", None))
        self.Scope_Serial_label.setText("")
        self.Scope_Load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Scope_Stimulus_Label.setText(QCoreApplication.translate("MainWindow", u"Load a stimulus", None))
        self.Scope_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.Scope_Start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Scope_Stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Scope_NumbeofLoop_Label.setText(QCoreApplication.translate("MainWindow", u"Number of Loop :", None))
        self.Scope_NumbeofLoop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Opto_Label.setText(QCoreApplication.translate("MainWindow", u"Optogenetics", None))
        self.Opto1_Display_label.setText(QCoreApplication.translate("MainWindow", u"Opto 1", None))
        self.Opto1_Value.setText("")
        self.Opto2_Display_label.setText(QCoreApplication.translate("MainWindow", u"Opto 2", None))
        self.Opto2_Value.setText("")
        self.Opto3_Display_label.setText(QCoreApplication.translate("MainWindow", u"Opto 3", None))
        self.Opto3_Value.setText("")
        self.Opto4_Display_label.setText(QCoreApplication.translate("MainWindow", u"Opto 4", None))
        self.Opto4_Value.setText("")
        self.Illuminatio_Label.setText(QCoreApplication.translate("MainWindow", u"Illumination", None))
        self.White_Light_Label.setText(QCoreApplication.translate("MainWindow", u"White light", None))
        self.AllWhite_label.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.AllWhite_Value.setText("")
        self.White1_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.White1_Value.setText("")
        self.White2_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.White2_Value.setText("")
        self.White3_label.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.White3_Value.setText("")
        self.White4_label.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.White4_Value.setText("")
        self.IR_Light_Label.setText(QCoreApplication.translate("MainWindow", u"Infra-red light", None))
        self.AllIR_label.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.AllIR_Value.setText("")
        self.IR1_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.IR1_Value.setText("")
        self.IR2_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.IR2_Value.setText("")
        self.IR3_label.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.IR3_Value.setText("")
        self.IR4_label.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.IR4_Value.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.License_Label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.OSN_Logo.setText("")
        self.SizeGrip_Label.setText("")
    # retranslateUi

