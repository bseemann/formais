
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
	def set_final(self, i=-1):
		if i == -1:
			i = self.tabela.currentRow()
		if self.y_rotulos[i].find('*') != -1:
			self.finais.remove(self.y_rotulos[i].lstrip('->*'))
			self.y_rotulos[i] = self.y_rotulos[i].replace('*', '')
			self.tabela.setVerticalHeaderLabels(self.y_rotulos)
			return
		self.finais.append(self.y_rotulos[i].lstrip('->'))
		self.y_rotulos[i] = '*'+self.y_rotulos[i]
		self.tabela.setVerticalHeaderLabels(self.y_rotulos)
	def set_initial(self, i=-1):
		if i == -1:
			i = self.tabela.currentRow()
		if self.y_rotulos[i].find('->') != -1:
			self.y_rotulos[i] = self.y_rotulos[i].replace('->', '')
			self.inicial = ''
			self.tabela.setVerticalHeaderLabels(self.y_rotulos)
			return

		for j, estado in enumerate(self.y_rotulos):
			if estado.find('->') != -1:
				self.y_rotulos[j] = estado.replace('->', '')

		self.inicial = self.y_rotulos[i].lstrip('*')
		self.y_rotulos[i] = '->'+self.y_rotulos[i]
		self.tabela.setVerticalHeaderLabels(self.y_rotulos)
	def reset(self):
		self.tabela.clear()
		self.tabela.clearContents()
		self.tabela.setRowCount(0)
		self.tabela.setColumnCount(0)
