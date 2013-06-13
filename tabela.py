
class Tabela:
	def __init__(self, t):
		self.tabela = t
		self.x_rotulos = []
		self.y_rotulos = []
		self.inicial = ''
		self.finais = []
	
	def add_x_rotulo(self, l):
		self.tabela.insertColumn(self.tabela.columnCount())
		self.x_rotulos.append(str(l))
		self.tabela.setHorizontalHeaderLabels(self.x_rotulos)
	def add_y_rotulo(self, l):
		self.tabela.insertRow(self.tabela.rowCount())
		self.y_rotulos.append(str(l))
		self.tabela.setVerticalHeaderLabels(self.y_rotulos)
	def n_linhas(self):
		return self.tabela.rowCount()
	def get_linha(self, i):
		nc = self.tabela.columnCount()
		line=[]
		for j in range(nc):
			line.append( str(self.tabela.item(i,j).text()) )
		return line
	def set_final(self):
		i = self.tabela.currentColumn()
		self.y_rotulos[i] = '*'+self.y_rotulos[i]
		self.tabela.setVerticalHeaderLabels(self.y_rotulos)
		self.finais.append(self.y_rotulos[i])
	def set_initial(self):
		i = self.tabela.currentColumn()
		self.y_rotulos[i] = '->'+self.y_rotulos[i]
		self.tabela.setVerticalHeaderLabels(self.y_rotulos)
		self.inicial = self.y_rotulos[i]
	def reset(self):
		self.tabela.clear()
		self.tabela.clearContents()
		self.tabela.setRowCount(0)
		self.tabela.setColumnCount(0)
