# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(559, 804)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border-color: rgb(170, 170, 255);")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_import = QPushButton(self.groupBox)
        self.pb_import.setObjectName(u"pb_import")

        self.gridLayout_2.addWidget(self.pb_import, 0, 0, 1, 1)

        self.lb_len = QLabel(self.groupBox)
        self.lb_len.setObjectName(u"lb_len")

        self.gridLayout_2.addWidget(self.lb_len, 5, 0, 1, 1)

        self.lb_size = QLabel(self.groupBox)
        self.lb_size.setObjectName(u"lb_size")

        self.gridLayout_2.addWidget(self.lb_size, 3, 0, 1, 1)

        self.lb_file = QLabel(self.groupBox)
        self.lb_file.setObjectName(u"lb_file")

        self.gridLayout_2.addWidget(self.lb_file, 2, 0, 1, 1)

        self.lb_codec = QLabel(self.groupBox)
        self.lb_codec.setObjectName(u"lb_codec")

        self.gridLayout_2.addWidget(self.lb_codec, 4, 0, 1, 1)

        self.list_file = QListWidget(self.groupBox)
        self.list_file.setObjectName(u"list_file")
        self.list_file.setDragEnabled(True)

        self.gridLayout_2.addWidget(self.list_file, 1, 0, 1, 1)

        self.gridLayout_2.setRowMinimumHeight(1, 2)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_1920 = QRadioButton(self.groupBox_2)
        self.radio_1920.setObjectName(u"radio_1920")

        self.horizontalLayout.addWidget(self.radio_1920)

        self.radio_3840 = QRadioButton(self.groupBox_2)
        self.radio_3840.setObjectName(u"radio_3840")

        self.horizontalLayout.addWidget(self.radio_3840)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.pb_size = QPushButton(self.groupBox_2)
        self.pb_size.setObjectName(u"pb_size")

        self.gridLayout_3.addWidget(self.pb_size, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_avc = QRadioButton(self.groupBox_3)
        self.radio_avc.setObjectName(u"radio_avc")

        self.verticalLayout.addWidget(self.radio_avc)

        self.pb_codec = QPushButton(self.groupBox_3)
        self.pb_codec.setObjectName(u"pb_codec")

        self.verticalLayout.addWidget(self.pb_codec)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.line_start = QLineEdit(self.groupBox_4)
        self.line_start.setObjectName(u"line_start")

        self.horizontalLayout_2.addWidget(self.line_start)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.line_end = QLineEdit(self.groupBox_4)
        self.line_end.setObjectName(u"line_end")

        self.horizontalLayout_2.addWidget(self.line_end)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pb_time = QPushButton(self.groupBox_4)
        self.pb_time.setObjectName(u"pb_time")

        self.verticalLayout_3.addWidget(self.pb_time)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 5)

        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pb_frame = QPushButton(self.groupBox_5)
        self.pb_frame.setObjectName(u"pb_frame")

        self.verticalLayout_4.addWidget(self.pb_frame)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.lb_done = QLabel(self.centralwidget)
        self.lb_done.setObjectName(u"lb_done")

        self.gridLayout_8.addWidget(self.lb_done, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Video File", None))
        self.pb_import.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.lb_len.setText(QCoreApplication.translate("MainWindow", u"length : ", None))
        self.lb_size.setText(QCoreApplication.translate("MainWindow", u"Size : ", None))
        self.lb_file.setText(QCoreApplication.translate("MainWindow", u"File : ", None))
        self.lb_codec.setText(QCoreApplication.translate("MainWindow", u"Codec : ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.radio_1920.setText(QCoreApplication.translate("MainWindow", u"1920*1080", None))
        self.radio_3840.setText(QCoreApplication.translate("MainWindow", u"3840*2160", None))
        self.pb_size.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Codec", None))
        self.radio_avc.setText(QCoreApplication.translate("MainWindow", u"convert AVC", None))
        self.pb_codec.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Time cut", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"start:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"end:", None))
        self.pb_time.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Show Frame number ", None))
        self.pb_frame.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.lb_done.setText("")
    # retranslateUi

