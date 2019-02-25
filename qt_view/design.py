# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gl_implemet.MOGL import GLWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.openGLWidget = GLWidget(self)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout.addWidget(self.openGLWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная №1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GL_POINT"))
        self.comboBox.setItemText(1, _translate("MainWindow", "GL_LINES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GL_LINE_STRIP"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GL_LINE_LOOP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GL_TRIANGLES"))
        self.comboBox.setItemText(5, _translate("MainWindow", "GL_TRIANGLE_STRIP"))
        self.comboBox.setItemText(6, _translate("MainWindow", "GL_TRIANGLE_FAN"))
        self.comboBox.setItemText(7, _translate("MainWindow", "GL_QUADS"))
        self.comboBox.setItemText(8, _translate("MainWindow", "GL_QUAD_STRIP"))
        self.comboBox.setItemText(9, _translate("MainWindow", "GL_POLYGON"))
