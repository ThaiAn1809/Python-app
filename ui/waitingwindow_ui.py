# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/waitingwindow.ui'
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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/ThaiAn/Python-app/ui/../img/LOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(670, 30, 191, 51))
        self.comboBox.setStyleSheet("    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparent-like background */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparent-like background */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 971, 341))
        self.label_2.setStyleSheet("    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparent-like background */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 120, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 160, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 200, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 240, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 290, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 330, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Geist Semibold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    background-color: rgb(255, 0, 0); /* Transparent-like background */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 18px \"Geist Semibold\"; /* Font family and size */")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 330, 411, 51))
        self.lineEdit.setStyleSheet("    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparent-like background */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(500, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(650, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(800, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(950, 500, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"    border: 1px solid #cccccc; /* Light gray border */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 15px; /* Padding to create space around the text */\n"
"    color: white; /* Text color */\n"
"    font: 15px \"Segoe UI\"; /* Font family and size */")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(190, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(490, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(640, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(340, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(940, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(790, 500, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Geist SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("\n"
"    color: white; /* Text color */\n"
"    font: \"Geist Semibold\"; /* Font family and size */")
        self.label_24.setObjectName("label_24")
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
        self.comboBox.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vitnamese"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.label_3.setText(_translate("MainWindow", "Unlimited movies,"))
        self.label_4.setText(_translate("MainWindow", "TV shows, and"))
        self.label_5.setText(_translate("MainWindow", "more"))
        self.label_7.setText(_translate("MainWindow", "Starts at 70,000 ₫. Cancel anytime."))
        self.label_9.setText(_translate("MainWindow", "Ready to watch? Enter your email to create or restart your membership"))
        self.pushButton_2.setText(_translate("MainWindow", "Get started"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Email address"))
        self.label_6.setText(_translate("MainWindow", "Trending Now"))
        self.label_16.setText(_translate("MainWindow", "1"))
        self.label_17.setText(_translate("MainWindow", "2"))
        self.label_18.setText(_translate("MainWindow", "4"))
        self.label_21.setText(_translate("MainWindow", "5"))
        self.label_22.setText(_translate("MainWindow", "3"))
        self.label_23.setText(_translate("MainWindow", "7"))
        self.label_24.setText(_translate("MainWindow", "6"))
