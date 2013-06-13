import sys
from PyQt4 import QtCore, QtGui
from string import ascii_lowercase
from string import ascii_uppercase
from PyQt4.QtGui import QTableWidgetItem
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
		if text not in ascii_uppercase:
			return
		self.tabela.add_y_rotulo(text)
		#t.tabela.setItem(0, 0, QTableWidgetItem('b'))

	def add_terminal(self):
		text = str(self.campo_terminal.text())
		if text == '' or text in self.tabela.x_rotulos:
			return
		if text not in ascii_lowercase:
			return
		self.tabela.add_x_rotulo(text)

	def minimizar(self):
		pass
	def determinizar(self):
		self.automato_para_tabela(self.criar_automato())

	def criar_automato(self):
		a = Automato()
		for terminal in self.tabela.x_rotulos:
			a.inserir_terminal(terminal)
		for estado in self.tabela.y_rotulos:
			a.inserir_estado(estado)

		for i in range(self.tabela.n_linhas()):
			line = self.tabela.get_linha(i)
			atual = self.tabela.y_rotulos[i]
			for j in range(len(line)):
				terminal = self.tabela.x_rotulos[j]
				final = line[j]
				a.inserir_transicao(atual, terminal, final)
		a.inserir_estado_inicial(self.tabela.inicial)
		for final in self.tabela.finais:
			a.inserir_estado_final( final )
		return a			
	def set_final(self):
		self.tabela.set_final()
	def set_initial(self):
		self.tabela.set_initial()
	
	def automato_para_tabela(self, automato):
		t=self.tabela2
		t.reset()
		t.finais = automato.finais
		t.inicial = t.inicial
		for e in automato.estados:
			t.add_y_rotulo(e)
		for ter in automato.alfabeto:
			t.add_x_rotulo(ter)

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
