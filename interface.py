# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Wed Jun 12 16:45:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(868, 521)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabela = QtGui.QTableWidget(self.centralwidget)
        self.tabela.setGeometry(QtCore.QRect(70, 60, 281, 201))
        self.tabela.setObjectName(_fromUtf8("tabela"))
        self.tabela.setColumnCount(0)
        self.tabela.setRowCount(0)
        self.campo_estado = QtGui.QLineEdit(self.centralwidget)
        self.campo_estado.setGeometry(QtCore.QRect(10, 60, 41, 31))
        self.campo_estado.setObjectName(_fromUtf8("campo_estado"))
        self.campo_terminal = QtGui.QLineEdit(self.centralwidget)
        self.campo_terminal.setGeometry(QtCore.QRect(70, 20, 41, 31))
        self.campo_terminal.setObjectName(_fromUtf8("campo_terminal"))
        self.botao_estado = QtGui.QPushButton(self.centralwidget)
        self.botao_estado.setGeometry(QtCore.QRect(0, 90, 61, 31))
        self.botao_estado.setObjectName(_fromUtf8("botao_estado"))
        self.botao_terminal = QtGui.QPushButton(self.centralwidget)
        self.botao_terminal.setGeometry(QtCore.QRect(110, 20, 94, 27))
        self.botao_terminal.setObjectName(_fromUtf8("botao_terminal"))
        self.botao_determinizar = QtGui.QPushButton(self.centralwidget)
        self.botao_determinizar.setGeometry(QtCore.QRect(70, 270, 94, 27))
        self.botao_determinizar.setObjectName(_fromUtf8("botao_determinizar"))
        self.botao_minimizar = QtGui.QPushButton(self.centralwidget)
        self.botao_minimizar.setGeometry(QtCore.QRect(170, 270, 94, 27))
        self.botao_minimizar.setObjectName(_fromUtf8("botao_minimizar"))
        self.botao_criar_automato = QtGui.QPushButton(self.centralwidget)
        self.botao_criar_automato.setGeometry(QtCore.QRect(490, 50, 94, 27))
        self.botao_criar_automato.setObjectName(_fromUtf8("botao_criar_automato"))
        self.botao_inicial = QtGui.QPushButton(self.centralwidget)
        self.botao_inicial.setGeometry(QtCore.QRect(70, 300, 94, 27))
        self.botao_inicial.setObjectName(_fromUtf8("botao_inicial"))
        self.botao_final = QtGui.QPushButton(self.centralwidget)
        self.botao_final.setGeometry(QtCore.QRect(170, 300, 94, 27))
        self.botao_final.setObjectName(_fromUtf8("botao_final"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.botao_estado, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.add_estado)
        QtCore.QObject.connect(self.botao_terminal, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.add_terminal)
        QtCore.QObject.connect(self.botao_determinizar, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.determinizar)
        QtCore.QObject.connect(self.botao_minimizar, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.minimizar)
        QtCore.QObject.connect(self.botao_criar_automato, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.criar_automato)
        QtCore.QObject.connect(self.botao_inicial, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.set_initial)
        QtCore.QObject.connect(self.botao_final, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.set_final)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_estado.setText(QtGui.QApplication.translate("MainWindow", "+Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_terminal.setText(QtGui.QApplication.translate("MainWindow", "+Terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_determinizar.setText(QtGui.QApplication.translate("MainWindow", "Determinizar", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_minimizar.setText(QtGui.QApplication.translate("MainWindow", "Minimizar", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_criar_automato.setText(QtGui.QApplication.translate("MainWindow", "criar_automato", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_inicial.setText(QtGui.QApplication.translate("MainWindow", "Definir Inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_final.setText(QtGui.QApplication.translate("MainWindow", "Definir Final", None, QtGui.QApplication.UnicodeUTF8))

