import sys
from PyQt4 import QtCore, QtGui

# import pyuic generated user interface file
from interface import Ui_MainWindow
from tabela import Tabela
from automato import Automato

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.tabela = Tabela(self.tabela)

	def add_estado(self):
		text = self.campo_estado.text()
		if text == '' or text in self.tabela.y_rotulos:
			return
		self.tabela.add_y_rotulo(text)

	def add_terminal(self):
		text = self.campo_terminal.text()
		if text == '' or text in self.tabela.x_rotulos:
			return
		self.tabela.add_x_rotulo(text)

	def minimizar(self):
		pass
	def determinizar(self):
		pass

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
				a.inserir_transicao(str(atual), str(terminal), final)
		a.inserir_estado_inicial(self.tabela.inicial)
		for final in self.tabela.finais:
			a.inserir_estado_final( final )
		return a			
	def set_final(self):
		self.tabela.set_final()
	def set_initial(self):
		self.tabela.set_initial()

		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyMainWindow()
	myapp.show()
	sys.exit(app.exec_())
