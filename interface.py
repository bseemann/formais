# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Sun Jun 16 23:04:21 2013
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
        MainWindow.resize(831, 604)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabela = QtGui.QTableWidget(self.centralwidget)
        self.tabela.setGeometry(QtCore.QRect(70, 60, 321, 221))
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
        self.botao_determinizar.setGeometry(QtCore.QRect(70, 290, 94, 27))
        self.botao_determinizar.setObjectName(_fromUtf8("botao_determinizar"))
        self.botao_minimizar = QtGui.QPushButton(self.centralwidget)
        self.botao_minimizar.setGeometry(QtCore.QRect(170, 290, 94, 27))
        self.botao_minimizar.setObjectName(_fromUtf8("botao_minimizar"))
        self.botao_inicial = QtGui.QPushButton(self.centralwidget)
        self.botao_inicial.setGeometry(QtCore.QRect(70, 320, 94, 27))
        self.botao_inicial.setObjectName(_fromUtf8("botao_inicial"))
        self.botao_final = QtGui.QPushButton(self.centralwidget)
        self.botao_final.setGeometry(QtCore.QRect(170, 320, 94, 27))
        self.botao_final.setObjectName(_fromUtf8("botao_final"))
        self.tabela2 = QtGui.QTableWidget(self.centralwidget)
        self.tabela2.setGeometry(QtCore.QRect(460, 60, 321, 221))
        self.tabela2.setObjectName(_fromUtf8("tabela2"))
        self.tabela2.setColumnCount(0)
        self.tabela2.setRowCount(0)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 40, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 140, 41, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 350, 621, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 380, 281, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 480, 181, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 510, 181, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 25))
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
        QtCore.QObject.connect(self.botao_inicial, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.set_initial)
        QtCore.QObject.connect(self.botao_final, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.set_final)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.gramatica_para_automato)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.swap_tables)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_estado.setText(QtGui.QApplication.translate("MainWindow", "+Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_terminal.setText(QtGui.QApplication.translate("MainWindow", "+Terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_determinizar.setText(QtGui.QApplication.translate("MainWindow", "Determinizar", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_minimizar.setText(QtGui.QApplication.translate("MainWindow", "Minimizar", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_inicial.setText(QtGui.QApplication.translate("MainWindow", "Definir Inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_final.setText(QtGui.QApplication.translate("MainWindow", "Definir Final", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Automato Resultante", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "←→", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Gramática para Automato", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Automato para Gramática", None, QtGui.QApplication.UnicodeUTF8))

