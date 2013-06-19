# -*- coding: utf-8 -*- 
import sys
from PyQt4 import QtCore, QtGui
from string import ascii_lowercase
from string import ascii_uppercase
from PyQt4.QtGui import QMessageBox
# import pyuic generated user interface file
from interface import Ui_MainWindow
from tabela import Tabela
from automato import Automato
from gramatica import Gramatica
from pickle import dump, load

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
		a = self.criar_automato()
		if a is None:
			return
		a = a.minimizar()
		self.automato_para_tabela(a)

	def determinizar(self):
		a = self.criar_automato()
		if a is None:
			return
		a = a.determinizar()
		self.automato_para_tabela(a)

	def swap_tables(self):
		t1=self.tabela
		t2=self.tabela2
		t2cc = t2.n_colunas()
		t2rc = t2.n_linhas()
		t2bkp=[]

		for i in range(t2rc):
			t2bkp.append([])
			for j in range(t2cc):
				t2bkp[i].append(t2.item(i,j))
		t2.tabela.setColumnCount(t1.tabela.columnCount())
		t2.tabela.setRowCount(t1.tabela.rowCount())
		

		for i in range(t1.n_linhas()):
			for j in range(t1.n_colunas()):
				t2.set_item(i, j, t1.item( i, j))

		t1.tabela.setColumnCount(t2cc)
		t1.tabela.setRowCount(t2rc)

		for i in range(t2rc):
			for j in range(t2cc):
				t1.set_item(i, j, t2bkp[i][j])
		t1.x_rotulos, t2.x_rotulos = t2.x_rotulos, t1.x_rotulos
		t1.y_rotulos, t2.y_rotulos = t2.y_rotulos, t1.y_rotulos

		t1.inicial,t2.inicial = t2.inicial,t1.inicial
		t1.finais,t2.finais = t2.finais,t1.finais

		self.tabela.refresh()
		self.tabela2.refresh()

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
						if letra not in ['@',',','&']:
							self.msg('Transicao para nao-estado detectada.', atual+' + '+terminal+' = '+final)
							return None
				#Verificar se "final" esta na lista de estados
				for item in final.split(','):
					if item not in a.estados and item != '@':
						self.msg('Transicao para um estado inexistente.', atual+' + '+terminal+' = '+final)
						return None
					a.inserir_transicao(atual, terminal, item)

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

		for e in sorted(automato.transicoes):
			t.add_y_rotulo(e)
		for ter in sorted(automato.alfabeto):
			t.add_x_rotulo(ter)

		for i, e in enumerate(sorted(automato.transicoes)):
			for j, ter in enumerate(sorted(automato.transicoes[e])):
				finais=''
				for k, f in enumerate(automato.transicoes[e][ter]):
					finais = finais + str(f) + ','
				finais = finais.rstrip(',')
				t.set_item(i, j, finais)

		for f in automato.finais:
			t.set_final(t.y_rotulos.index(f))

		for j, estado in enumerate(t.y_rotulos):
			if estado.lstrip('->*') == automato.inicial:
				t.y_rotulos[j] = t.y_rotulos[j].replace('->','')
				t.set_initial(j)
				break

	def gramatica_para_automato(self):
		text = self.textEdit.toPlainText().toAscii()
		text = str(text).splitlines()
		g = Gramatica()
		for line in text:
			g.inserir_producao(str(line))
		a = g.transformar_automato()
		a.imprimir()
		self.automato_para_tabela(a)
	
	def automato_para_gramatica(self):
		a = self.criar_automato()
		g = Gramatica()
		lines = g.transformar_gramatica(a)

		self.textEdit.clear()
		for line in lines:
			self.textEdit.append(line)
	
	def limpar_tabela(self):
		self.tabela.reset()

	def salvar(self, nome='sem_titulo.txt'):
		f = open(nome, 'w')
		if not f:
			return
		a = self.criar_automato()
		dump(a, f)
		f.close()

	def carregar(self, nome='sem_titulo.txt'):
		f = open(nome)
		if not f:
			return
		a = load(f)
		self.automato_para_tabela(a)
		f.close()
	def listar_sentencas(self):
		a = self.criar_automato()
		n = self.spinBox.value()
		lines = a.enumerar_sentencas(n)
		self.textEdit_2.clear()
		for line in lines:
			self.textEdit_2.append(line)
	def reconhecer_sentenca(self):
		s = str(self.textEdit_2.toPlainText().toAscii())
		if len(s.splitlines()) > 1:
			self.msg('Atencao: Apenas a primeira linha do campo eh levada em consideracao.')
			s = s.splitlines()[0]
		a = self.criar_automato()
		if not a:
			return
		if a.reconhecer_sentenca(s):
			self.msg('Sentenca reconhecida.')
		else:
			self.msg('Sentenca nao reconhecida.')
		


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyMainWindow()
	myapp.show()
	sys.exit(app.exec_())
