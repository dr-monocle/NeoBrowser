# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class Ui_Browser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        MainWindow.resize(800, 575)
        MainWindow.setMinimumSize(QtCore.QSize(0, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.title_frame.setStyleSheet("QFrame#title_frame {\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(144, 144, 144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #E8960C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #FF8000;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.title_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_bar = QtWidgets.QHBoxLayout()
        self.title_bar.setObjectName("title_bar")
        self.label = QtWidgets.QLabel(self.title_frame)
        self.label.setMinimumSize(QtCore.QSize(15, 15))
        self.label.setMaximumSize(QtCore.QSize(15, 15))
        self.label.setStyleSheet("background-color: #E85A0C;\n"
"border-radius: 7px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.title_bar.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.title_frame)
        self.label_4.setMinimumSize(QtCore.QSize(15, 15))
        self.label_4.setMaximumSize(QtCore.QSize(15, 15))
        self.label_4.setStyleSheet("background-color: #FF8000;\n"
"border: 4px solid rgba(0,0,0,0);\n"
"border-radius: 7px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.title_bar.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.title_frame)
        self.label_3.setMinimumSize(QtCore.QSize(15, 15))
        self.label_3.setMaximumSize(QtCore.QSize(15, 15))
        self.label_3.setStyleSheet("background-color: #E8960C;\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-radius: 7px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.title_bar.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.title_frame)
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("padding-left: 2px;\n"
"color: #E8960C;")
        self.label_2.setObjectName("label_2")
        self.title_bar.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(self.title_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_bar.addWidget(self.frame)
        self.btn_minimize = QtWidgets.QPushButton(self.title_frame)
        self.btn_minimize.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setObjectName("btn_minimize")
        self.title_bar.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.title_frame)
        self.btn_maximize.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_maximize.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_maximize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_maximize.setObjectName("btn_maximize")
        self.title_bar.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.title_frame)
        self.btn_close.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_close.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setObjectName("btn_close")
        self.title_bar.addWidget(self.btn_close)
        self.verticalLayout_2.addLayout(self.title_bar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_previous = QtWidgets.QPushButton(self.title_frame)
        self.btn_previous.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_previous.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_previous.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout_2.addWidget(self.btn_previous)
        self.btn_next = QtWidgets.QPushButton(self.title_frame)
        self.btn_next.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_next.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.btn_reload = QtWidgets.QPushButton(self.title_frame)
        self.btn_reload.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_reload.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_reload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reload.setObjectName("btn_reload")
        self.horizontalLayout_2.addWidget(self.btn_reload)
        self.btn_minimize_3 = QtWidgets.QPushButton(self.title_frame)
        self.btn_minimize_3.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_minimize_3.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_minimize_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize_3.setObjectName("btn_minimize_3")
        self.horizontalLayout_2.addWidget(self.btn_minimize_3)
        self.lineEdit = QtWidgets.QLineEdit(self.title_frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("background-color: rgb(31,31,31);\n"
"border-radius: 5px;\n"
"color: rgb(184, 184, 184);\n"
"padding-left: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btn_minimize_2 = QtWidgets.QPushButton(self.title_frame)
        self.btn_minimize_2.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_minimize_2.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_minimize_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize_2.setObjectName("btn_minimize_2")
        self.horizontalLayout_2.addWidget(self.btn_minimize_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.title_frame)
        self.content_frame = QtWidgets.QFrame(self.centralwidget)
        self.content_frame.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.content_frame)
        self.tabWidget.setStyleSheet("QTabWidget::scroller {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    background: #35363A;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #35363A;\n"
"    color: #fff;\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    border-right: 1px solid #C7CBCF;\n"
"    border-left: 1px solid #C7CBCF;\n"
"    background: #202124;\n"
"    color: #BEC2C7;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #2F3034;\n"
"    color: #BEC2C7;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 24ex;\n"
"    margin-right: -1px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    background: rgba(0,0,0,0);\n"
"    image: url(:/img/img/cross.png);\n"
"    subcontrol-position: left;\n"
"    border-radius: 7px;\n"
"    padding: 2px;\n"
" }\n"
"\n"
"QTabBar::close-button:hover {\n"
"    background: #505053;\n"
"cursor: pointing-hand\n"
"}")
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.content_frame)
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setMinimumSize(QtCore.QSize(0, 35))
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.bottom_frame.setStyleSheet("background-color: rgb(45,45,45); border-bottom-left-radius: 20px; border-bottom-right-radius: 20px")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout.setContentsMargins(9, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.bottom_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.resize_frame = QtWidgets.QFrame(self.bottom_frame)
        self.resize_frame.setMinimumSize(QtCore.QSize(25, 25))
        self.resize_frame.setMaximumSize(QtCore.QSize(25, 25))
        self.resize_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resize_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resize_frame.setObjectName("resize_frame")
        self.horizontalLayout.addWidget(self.resize_frame)
        self.verticalLayout.addWidget(self.bottom_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Neo Browser"))
        self.label_2.setText(_translate("MainWindow", "<b>NEO</b> BROWSER"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_minimize.setText(_translate("MainWindow", "-"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_maximize.setText(_translate("MainWindow", ""))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_close.setText(_translate("MainWindow", "X"))
        self.btn_previous.setToolTip(_translate("MainWindow", "Go to previous page"))
        self.btn_previous.setText(_translate("MainWindow", "⬅"))
        self.btn_next.setToolTip(_translate("MainWindow", "Go to next page"))
        self.btn_next.setText(_translate("MainWindow", "➡"))
        self.btn_reload.setToolTip(_translate("MainWindow", "Reload page"))
        self.btn_reload.setText(_translate("MainWindow", "⟲"))
        self.btn_minimize_3.setToolTip(_translate("MainWindow", "Open start page"))
        self.btn_minimize_3.setText(_translate("MainWindow", "⌂"))
        self.btn_minimize_2.setToolTip(_translate("MainWindow", "Options"))
        self.btn_minimize_2.setText(_translate("MainWindow", "⚙"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
import components.file_rc