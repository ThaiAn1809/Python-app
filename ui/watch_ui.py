# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/watch.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("    background-color: black; /* Black background for the main window */\n"
"    color: white;            /* Default text color as white */\n"
"    border: none;            /* No window border */\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-arrow-left-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 10, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-flag-regular.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 650, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/LOGO.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 650, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-volume-high-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 650, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-arrow-rotate-right-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 650, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-arrow-rotate-left-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(950, 650, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-expand-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(875, 655, 51, 51))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-gauge-high-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(790, 650, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: black;       /* Black background */\n"
"    border: 2px solid transparent; /* Transparent border by default */\n"
"    border-radius: 5px;            /* Rounded corners */\n"
"    padding: 10px;                 /* Default padding */\n"
"    background-repeat: no-repeat; /* No repeating the image */\n"
"    background-position: center;  /* Center the icon */\n"
"    transition: all 0.2s ease;    /* Smooth transition */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;       /* White border on hover */\n"
"    padding: 8px;                  /* Reduced padding to simulate size increase */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;     /* Darker background on press */\n"
"    padding: 6px;                  /* Further reduced padding for pressed state */\n"
"}\n"
"")
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/iconizer-closed-captioning-regular.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 610, 991, 20))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: none;                     /* Remove the groove border */\n"
"    height: 6px;                      /* Groove height */\n"
"    background: #4fa3d9;              /* Groove color (blue-gray) */\n"
"    border-radius: 3px;               /* Rounded groove edges */\n"
"    margin: 0px;                      /* Align properly */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #70d6ff,               /* Light blue at start */\n"
"        stop: 1 #0077cc                /* Darker blue at end */\n"
"    );\n"
"    border: none;                     /* No border for handle */\n"
"    width: 12px;                      /* Handle width */\n"
"    height: 12px;                     /* Handle height */\n"
"    border-radius: 6px;               /* Circular handle */\n"
"    margin: -3px 0;                   /* Align handle perfectly with groove */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #70d6ff,               /* Gradient starts light blue */\n"
"        stop: 1 #0077cc                /* Gradient ends darker blue */\n"
"    );\n"
"    border: none;                     /* No border for filled portion */\n"
"    height: 6px;                      /* Same as groove height */\n"
"    border-radius: 3px;               /* Rounded edges */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #aaaaaa;              /* Unfilled portion color (light gray) */\n"
"    border: none;                     /* No border for unfilled portion */\n"
"    height: 6px;                      /* Same as groove height */\n"
"    border-radius: 3px;               /* Rounded edges */\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 660, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;               /* White text */\n"
"    font-size: 14px;            /* Font size */\n"
"    font-weight: bold;          /* Bold text */\n"
"    text-align: center;         /* Center the text */\n"
"    background-color: transparent; /* No background */\n"
"    padding: 5px;               /* Optional padding for spacing */\n"
"}\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Video name"))
