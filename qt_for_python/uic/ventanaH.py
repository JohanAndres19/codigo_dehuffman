# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\ciencias 2.2\Codigo de huffman\ventanaH.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qt_for_python.rcc.source import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 482)
        MainWindow.setStyleSheet("*{\n"
                                 "\n"
                                 "     background-image: url(:/Imagenes/imagenes/456.jpg);\n"
                                 "     font-family:     Comic Sans MS;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "   background:#2d89ef;\n"
                                 "   color: white;\n"
                                 "   border: 2px solid;\n"
                                 "   border-radius:15px;\n"
                                 "   font-size:15px;        \n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "  background:white;    \n"
                                 "  border: 2px solid;\n"
                                 "  border-radius:15px;    \n"
                                 "  font-size:13px;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#contenedor{\n"
                                 "    border:transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView {\n"
                                 "    color: white;\n"
                                 "    font-size:15px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView{\n"
                                 "  qproperty-defaultAlignment: AlignHCenter;\n"
                                 "  background: rgb(59, 89, 213);\n"
                                 " font-weight: bold;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit{\n"
                                 "    color:white;\n"
                                 "    font-size:13px;\n"
                                 "    font-weight: bold;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.boton_encriptar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_encriptar.setGeometry(QtCore.QRect(320, 40, 81, 31))
        self.boton_encriptar.setObjectName("boton_encriptar")
        self.text_ingresar = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar.setGeometry(QtCore.QRect(20, 40, 271, 31))
        self.text_ingresar.setObjectName("text_ingresar")
        self.contenedor = QtWidgets.QWidget(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(20, 90, 631, 271))
        self.contenedor.setObjectName("contenedor")
        self.tableWidget = QtWidgets.QTableWidget(self.contenedor)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.boton_mostrar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_mostrar.setGeometry(QtCore.QRect(430, 40, 121, 31))
        self.boton_mostrar.setObjectName("boton_mostrar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 440, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 370, 631, 61))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_encriptar.setText(_translate("MainWindow", "Encriptar"))
        self.boton_mostrar.setText(_translate("MainWindow", "Mostrar Arbol"))
        self.pushButton.setText(_translate(
            "MainWindow", "Valor de los simbolos"))
