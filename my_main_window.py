# -*- coding: utf-8 -*- 
import sys
from PyQt4 import QtCore, QtGui
from string import ascii_lowercase
from string import ascii_uppercase
from PyQt4.QtGui import QTableWidgetItem
from PyQt4.QtGui import QMessageBox
# import pyuic generated user interface file
from interface import Ui_MainWindow
from tabela import Tabela
from automato import Automato

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.tabela = Tabela(self.tabela)
		self.tabela2 = Tabela(self.tabela2)

	def add_estado(self):
		text = str(self.campo_estado.text())
		if text == '' or text in self.tabela.y_rotulos:
			return
		for t in text:
			if t not in ascii_uppercase:
				return
		self.tabela.add_y_rotulo(text)

	def add_terminal(self):
		text = str(self.campo_terminal.text())
		if text == '' or text in self.tabela.x_rotulos:
			return
		for t in text:
			if t not in ascii_lowercase:
				return
		self.tabela.add_x_rotulo(text)

	def minimizar(self):
		pass
	def determinizar(self):
		a = self.criar_automato()
		if a is None:
			return
		a = a.determinizar()
		self.automato_para_tabela(a)

	def msg(self, mensagem, informative=''):
		dialog = QMessageBox()
		dialog.setText(mensagem)
		if informative != '':
			dialog.setInformativeText(informative)
		dialog.exec_()

	def criar_automato(self):
		a = Automato()
		for terminal in self.tabela.x_rotulos:
			a.inserir_terminal(terminal)
		for estado in self.tabela.y_rotulos:
			a.inserir_estado(estado.lstrip('->*'))

		for i in range(self.tabela.n_linhas()):
			line = self.tabela.get_linha(i)
			atual = self.tabela.y_rotulos[i].lstrip('->*')
			for j in range(len(line)):
				terminal = self.tabela.x_rotulos[j]
				final = line[j]
				if final == '' or final == '-':
					continue
				for letra in final:
					if letra not in ascii_uppercase:
						self.msg('Transicao para nao-estado detectada.', atual+' + '+terminal+' = '+final)
						return None
				#Verificar se "final" esta na lista de estados
				for estado in self.tabela.y_rotulos:
					if estado.lstrip('*->') == final:
						break
				else:
					self.msg('Transicao para um estado inexistente.', atual+' + '+terminal+' = '+final)
					return None

				a.inserir_transicao(atual, terminal, final)
		a.inserir_estado_inicial(self.tabela.inicial)
		for final in self.tabela.finais:
			a.inserir_estado_final( final )
		if self.tabela.finais == []:
			self.msg('O automato deve ter ao menos um estado final.')
			return None
		if self.tabela.inicial == '':
			self.msg('O automato deve ter um estado inicial.')
			return None				
		return a			
	def set_final(self,i=-1):
		self.tabela.set_final(i)
	def set_initial(self,i=-1):
		self.tabela.set_initial(i)
	
	def automato_para_tabela(self, automato):
		t=self.tabela2
		t.reset()
		for e in automato.estados:
			t.add_y_rotulo(e)
		for ter in automato.alfabeto:
			t.add_x_rotulo(ter)

		for f in automato.finais:
			t.set_final(t.y_rotulos.index(f))

		for j, estado in enumerate(t.y_rotulos):
			if estado.lstrip('->*') == automato.inicial:
				t.set_initial(j)

		for i, e in enumerate(automato.transicoes):
			for j, ter in enumerate(automato.transicoes[e]):
				finais=''
				for k, f in enumerate(automato.transicoes[e][ter]):
					finais = finais + str(f) + ','
				finais = finais.rstrip(',')
				t.tabela.setItem(i, j, QTableWidgetItem(finais))



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyMainWindow()
	myapp.show()
	sys.exit(app.exec_())
