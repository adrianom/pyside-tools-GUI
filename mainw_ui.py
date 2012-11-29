# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/DatiVari/Eclipseworkspace/pyside-tools-GUI/src/mainw.ui'
#
# Created: Wed Jul 25 18:15:20 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearbtn = QtGui.QPushButton(self.centralwidget)
        self.clearbtn.setMinimumSize(QtCore.QSize(20, 50))
        self.clearbtn.setObjectName("clearbtn")
        self.horizontalLayout_2.addWidget(self.clearbtn)
        self.removebtn = QtGui.QPushButton(self.centralwidget)
        self.removebtn.setMinimumSize(QtCore.QSize(20, 50))
        self.removebtn.setObjectName("removebtn")
        self.horizontalLayout_2.addWidget(self.removebtn)
        self.addbtn = QtGui.QPushButton(self.centralwidget)
        self.addbtn.setMinimumSize(QtCore.QSize(20, 50))
        self.addbtn.setObjectName("addbtn")
        self.horizontalLayout_2.addWidget(self.addbtn)
        self.gobtn = QtGui.QPushButton(self.centralwidget)
        self.gobtn.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.gobtn.setFont(font)
        self.gobtn.setObjectName("gobtn")
        self.horizontalLayout_2.addWidget(self.gobtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.listlayout = QtGui.QVBoxLayout()
        self.listlayout.setObjectName("listlayout")
        self.gridLayout.addLayout(self.listlayout, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Xcheck = QtGui.QCheckBox(self.groupBox)
        self.Xcheck.setChecked(False)
        self.Xcheck.setObjectName("Xcheck")
        self.gridLayout_2.addWidget(self.Xcheck, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyside-tools-GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.clearbtn.setText(QtGui.QApplication.translate("MainWindow", "Clear list", None, QtGui.QApplication.UnicodeUTF8))
        self.removebtn.setText(QtGui.QApplication.translate("MainWindow", "Remove item", None, QtGui.QApplication.UnicodeUTF8))
        self.addbtn.setText(QtGui.QApplication.translate("MainWindow", "Add (*.ui | *.qrc) files", None, QtGui.QApplication.UnicodeUTF8))
        self.gobtn.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.Xcheck.setText(QtGui.QApplication.translate("MainWindow", "Generate running code (-x) (only *.ui files)", None, QtGui.QApplication.UnicodeUTF8))

