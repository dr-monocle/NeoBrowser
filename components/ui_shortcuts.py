# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shortcuts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Shortcuts(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        MainWindow.resize(300, 450)
        MainWindow.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow.setMaximumSize(QtCore.QSize(300, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(144, 144, 144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #E8960C;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: rgb(20, 20, 20);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 18px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_5.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.label_5 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setStyleSheet("image: url(:/img/img/logo70x70.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: none;\n"
"color: rgb(107, 107, 107);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.frame_6 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame.setMinimumSize(QtCore.QSize(0, 350))
        self.frame.setStyleSheet("QLabel {\n"
"    color: #FF8000;\n"
"    background-color: rgba(0,0,0,0);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 18))
        self.label.setMaximumSize(QtCore.QSize(16777215, 18))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.btn_addTab = QtWidgets.QPushButton(self.frame)
        self.btn_addTab.setObjectName("btn_addTab")
        self.verticalLayout_5.addWidget(self.btn_addTab)
        self.btn_code = QtWidgets.QPushButton(self.frame)
        self.btn_code.setObjectName("btn_code")
        self.verticalLayout_5.addWidget(self.btn_code)
        self.btn_code_4 = QtWidgets.QPushButton(self.frame)
        self.btn_code_4.setObjectName("btn_code_4")
        self.verticalLayout_5.addWidget(self.btn_code_4)
        self.btn_code_5 = QtWidgets.QPushButton(self.frame)
        self.btn_code_5.setObjectName("btn_code_5")
        self.verticalLayout_5.addWidget(self.btn_code_5)
        self.btn_code_6 = QtWidgets.QPushButton(self.frame)
        self.btn_code_6.setObjectName("btn_code_6")
        self.verticalLayout_5.addWidget(self.btn_code_6)
        self.btn_print = QtWidgets.QPushButton(self.frame)
        self.btn_print.setObjectName("btn_print")
        self.verticalLayout_5.addWidget(self.btn_print)
        self.btn_open = QtWidgets.QPushButton(self.frame)
        self.btn_open.setObjectName("btn_open")
        self.verticalLayout_5.addWidget(self.btn_open)
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_5.addWidget(self.btn_save)
        self.btn_code_3 = QtWidgets.QPushButton(self.frame)
        self.btn_code_3.setObjectName("btn_code_3")
        self.verticalLayout_5.addWidget(self.btn_code_3)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_7 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_7.setStyleSheet("QLabel {\n"
"    color: #FF8000;\n"
"    background-color: rgba(0,0,0,0);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMinimumSize(QtCore.QSize(0, 18))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 18))
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.btn_addTab_2 = QtWidgets.QPushButton(self.frame_7)
        self.btn_addTab_2.setObjectName("btn_addTab_2")
        self.verticalLayout_3.addWidget(self.btn_addTab_2)
        self.btn_addTab_3 = QtWidgets.QPushButton(self.frame_7)
        self.btn_addTab_3.setObjectName("btn_addTab_3")
        self.verticalLayout_3.addWidget(self.btn_addTab_3)
        self.btn_addTab_4 = QtWidgets.QPushButton(self.frame_7)
        self.btn_addTab_4.setObjectName("btn_addTab_4")
        self.verticalLayout_3.addWidget(self.btn_addTab_4)
        self.btn_addTab_5 = QtWidgets.QPushButton(self.frame_7)
        self.btn_addTab_5.setObjectName("btn_addTab_5")
        self.verticalLayout_3.addWidget(self.btn_addTab_5)
        self.btn_addTab_6 = QtWidgets.QPushButton(self.frame_7)
        self.btn_addTab_6.setObjectName("btn_addTab_6")
        self.verticalLayout_3.addWidget(self.btn_addTab_6)
        self.btn_print_2 = QtWidgets.QPushButton(self.frame_7)
        self.btn_print_2.setObjectName("btn_print_2")
        self.verticalLayout_3.addWidget(self.btn_print_2)
        self.btn_open_2 = QtWidgets.QPushButton(self.frame_7)
        self.btn_open_2.setObjectName("btn_open_2")
        self.verticalLayout_3.addWidget(self.btn_open_2)
        self.btn_save_2 = QtWidgets.QPushButton(self.frame_7)
        self.btn_save_2.setObjectName("btn_save_2")
        self.verticalLayout_3.addWidget(self.btn_save_2)
        self.btn_code_2 = QtWidgets.QPushButton(self.frame_7)
        self.btn_code_2.setObjectName("btn_code_2")
        self.verticalLayout_3.addWidget(self.btn_code_2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Neo - Shortcuts"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SHORTCUTS</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "BROWSER"))
        self.btn_addTab.setText(_translate("MainWindow", " Add tab "))
        self.btn_code.setText(_translate("MainWindow", "✖ Close tab"))
        self.btn_code_4.setText(_translate("MainWindow", "⬅ Previous page"))
        self.btn_code_5.setText(_translate("MainWindow", "➡ Next page"))
        self.btn_code_6.setText(_translate("MainWindow", "⟲ Reload page"))
        self.btn_print.setText(_translate("MainWindow", " Print page"))
        self.btn_open.setText(_translate("MainWindow", " Open file"))
        self.btn_save.setText(_translate("MainWindow", " Save page"))
        self.btn_code_3.setText(_translate("MainWindow", " View source code"))
        self.btn_addTab_2.setText(_translate("MainWindow", "Ctrl + T"))
        self.btn_addTab_3.setText(_translate("MainWindow", "Ctrl + W"))
        self.btn_addTab_4.setText(_translate("MainWindow", "Alt + ⬅"))
        self.btn_addTab_5.setText(_translate("MainWindow", "Alt + ➡"))
        self.btn_addTab_6.setText(_translate("MainWindow", "Ctrl + R"))
        self.btn_print_2.setText(_translate("MainWindow", "Ctrl + P"))
        self.btn_open_2.setText(_translate("MainWindow", "Ctrl + O"))
        self.btn_save_2.setText(_translate("MainWindow", "Ctrl + S"))
        self.btn_code_2.setText(_translate("MainWindow", "Ctrl + U"))
import components.file_rc