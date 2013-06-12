import copy
from transformacoes import *

class Automato(object):
	def __init__(self):
		self.estados = []
		self.alfabeto = []
		self.transicoes = dict()
		self.finais = []
		self.inicial = ''
		#esquema das transicoes:
		#estado atual = (terminal=(estados alcancaveis))
		#transicoes=('S'=('a'=['A','B'],b=[]),'A'=('a'=['A'],'b'=['S']))

	def inserir_estado(self,novo):
		self.estados.append(novo)
		x = dict()
		for i in self.alfabeto:
			x[i]=[]
		self.transicoes[novo] = x
	
	def inserir_terminal(self,novo):
		self.alfabeto.append(novo)
		for i in self.transicoes:
			self.transicoes[i][novo]=[]

	def inserir_transicao(self,estado_atual,terminal,estado_final):
		self.transicoes[estado_atual][terminal].append(estado_final)
	
	#def completar(self):
	#	q=0
	#	for i in self.transicoes:
	#		for j in self.alfabeto:
	#			if len(self.transicoes[i][j])==0:
	#				self.transicoes[i][j].append('Qerr')
	#				q=1
	#	if q==1:
	#		x = dict()
	#		for i in self.alfabeto:
	#			x[i]=['Qerr']
	#		self.transicoes['Qerr']=x
	
	def inserir_estado_inicial(self,inicial):
		if len(self.inicial)==0:
			self.inicial=inicial
		else:
			print 'Estado inicial ja definido'
	
	def inserir_estado_final(self,final):
		self.finais.append(final)
	
#	def determinizar(self):
#		det=dict()
#		det[self.inicial]=dict()
#		for i in self.transicoes[self.inicial]:
#			det[self.inicial][i]=self.transicoes[self.inicial][i]
#			if len(self.transicoes[self.inicial][i])>1:
#				self.transicoes[self.inicial][i].sort()
#				s=''
#				for j in self.transicoes[self.inicial][i]:
#					s=s+j
#				det[s]=dict()
#				for j in self.alfabeto:
#					det[s][j]=[]
#			if len(self.transicoes[self.inicial][i])==1:
#				for x in self.transicoes[self.inicial][i]:
#					if x not in det:
#						det[x]=dict()
#						for j in self.alfabeto:
#							det[x][j]=[]
#		d=0
#		while d!=det:
#			d=copy.deepcopy(det)
#			for i in d:
#				if len(i)>1:
#					for j in i:
#						for k in self.transicoes[j]:
#							for l in self.transicoes[j][k]:
#								if l not in det[i][k]:
#									det[i][k].append(l)
#					for j in det[i]:
#						if len(det[i][j])>1:
#							det[i][j].sort()
#							s=''
#							for k in det[i][j]:
#								s=s+k
#							if s not in det:
#								det[s]=dict()
#								for k in self.alfabeto:
#									det[s][k]=[]
#						else:
#							for x in det[i][j]:
#								if x not in det:
#									det[x]=dict()
#									for k in self.alfabeto:
#										det[x][k]=[]
#				else:
#					for j in det[i]:
#						if det[i][j] != self.transicoes[i][j]:
#							det[i][j]=self.transicoes[i][j]
#							if len(det[i][j])>1:
#								det[i][j].sort()
#								s=''
#								for k in det[i][j]:
#									s=s+k
#								det[s]=dict()
#								for k in self.alfabeto:
#									det[s][k]=[]
#		for i in det:
#			for j in det[i]:
#				if len(det[i][j])>1:
#					s=''
#					for k in det[i][j]:
#						s=s+k
#					det[i][j]=[s]
#		self.transicoes = det
#		f = []
#		for i in self.finais:
#			for j in self.transicoes:
#				if i in j:
#					f.append(j)
#		self.finais = f
#
	def determinizar(self):
		t=Transformacoes()
		self=t.determinizar(self)

#	def eliminar_inalcancaveis(self):
#		t=Transformacoes()
#		self=t.eliminar_inalcancaveis(self)
#		a=[]
#		c=[self.inicial]
#		for i in self.alfabeto:
#			for j in self.transicoes[self.inicial][i]:
#				a.append(j)
#		for i in a:
#			c.append(i)
#			for j in self.alfabeto:
#				for k in self.transicoes[i][j]:
#					if k not in c and k not in a:
#						a.append(k)
#			a.remove(i)
#		copia = copy.deepcopy(self)
#		copia.estados = c
#		copia.alfabeto=[]
#		for i in c:
#			for j in self.alfabeto:
#				for k in self.transicoes[i][j]:
#					if k in c and j not in copia.alfabeto:
#						copia.alfabeto.append(j)
#		for i in self.transicoes:
#			for j in self.transicoes[i]:
#				for k in self.transicoes[i][j]:
#					if k not in c:
#						copia.transicoes[i][j].remove(k)
#			if i not in c:
#				copia.transicoes.pop(i)			
#		copia.finais=[]
#		for i in self.finais:
#			if i in c:
#				copia.finais.append(i)
#		print "Sem inalcancaveis"
#		copia.imprimir()
#		return copia

#	def eliminar_mortos(self):
#		t=Transformacoes()
#		self=t.eliminar_mortos(self)
#		print 'self'
#		self.imprimir()
#		m=copia.finais
#		n=[]
#		while n!=m:
#			n=m
#			for i in copia.transicoes:
#				for j in copia.transicoes[i]:
#					for k in copia.transicoes[i][j]:
#						if k in m and i not in m:
#							m.append(i)
#		for i in self.transicoes:
#			if i not in m and i in copia.transicoes:
#				copia.transicoes.pop(i)
#		for i in copia.transicoes:
#			for j in copia.transicoes[i]:
#				for k in copia.transicoes[i][j]:
#					if k not in m:
#						copia.transicoes[i][j].remove(k)
#		print "Sem mortos"
#		copia.imprimir()
#		return copia

	def minimizar(self):
		t=Transformacoes()
		self=t.minimizar(self)
		print "\nNovo"
		self.imprimir()

	def imprimir(self):
		for i in self.alfabeto:
			print "\t",i,
		print ""
		for i in self.transicoes:
			s=''
			if i in self.finais:
				s='*'
			if i in self.inicial:
				s=s+'->'
			print s,i,"\t",
			for j in self.alfabeto:
				for k in self.transicoes[i][j]:
					print k,
				print "\t",
			print ""

if __name__ == "__main__":


	a=Automato()
	a.inserir_estado('S')
	a.inserir_estado('A')
	a.inserir_estado('B')
	a.inserir_estado('C')
	a.inserir_estado('D')
	a.inserir_estado('F')
	a.inserir_terminal('a')
	a.inserir_terminal('b')
	a.inserir_transicao('S','a','B')
	a.inserir_transicao('S','a','D')
	a.inserir_transicao('S','a','F')
	a.inserir_transicao('S','b','A')
	a.inserir_transicao('S','b','C')
	a.inserir_transicao('S','b','F')
	a.inserir_transicao('A','a','B')
	a.inserir_transicao('A','a','F')
	a.inserir_transicao('A','b','A')
	a.inserir_transicao('B','a','A')
	a.inserir_transicao('B','b','B')
	a.inserir_transicao('B','b','F')
	a.inserir_transicao('C','a','D')
	a.inserir_transicao('C','b','C')
	a.inserir_transicao('C','b','F')
	a.inserir_transicao('D','a','C')
	a.inserir_transicao('D','a','F')
	a.inserir_transicao('D','b','D')
	a.inserir_estado_inicial('S')
	a.inserir_estado_final('F')
	#a.imprimir()
	#print 'Inalcancaveis'
	#b = a.eliminar_inalcancaveis()
	#print 'Estados'
	#print b.estados
	b=Automato()
	b.inserir_estado('S')
	b.inserir_estado('A')
	b.inserir_estado('B')
	b.inserir_estado('C')
	b.inserir_terminal('a')
	b.inserir_terminal('b')
	b.inserir_transicao('S','a','S')
	b.inserir_transicao('S','a','A')
	b.inserir_transicao('S','b','S')
	b.inserir_transicao('A','b','B')
	b.inserir_transicao('B','b','C')
	b.inserir_estado_inicial('S')
	b.inserir_estado_final('C')
	b.determinizar()
#	print 'Automato B'
#	b.imprimir()
	a.determinizar()
#	print '\nAutomato A'
#	a.imprimir()
	c=Automato()
	c.inserir_estado('S')
	c.inserir_estado('A')
	c.inserir_estado('B')
	c.inserir_estado('C')
	c.inserir_estado('D')
	c.inserir_terminal('a')
	c.inserir_terminal('b')
	c.inserir_transicao('S','a','A')
	c.inserir_transicao('S','a','C')
	c.inserir_transicao('S','a','D')
	c.inserir_transicao('S','b','A')
	c.inserir_transicao('S','b','B')
	c.inserir_transicao('S','b','C')
	c.inserir_transicao('A','b','A')
	c.inserir_transicao('A','b','B')
	c.inserir_transicao('B','a','A')
	c.inserir_transicao('B','b','B')
	c.inserir_transicao('C','a','C')
	c.inserir_transicao('C','a','D')
	c.inserir_transicao('D','a','D')
	c.inserir_transicao('D','b','C')
	c.inserir_estado_inicial('S')
	c.inserir_estado_final('A')
	c.inserir_estado_final('B')
	c.inserir_estado_final('C')
	c.inserir_estado_final('D')
#	print '\n\nAutomato C Nao deterministico'
#	c.imprimir()
	c.determinizar()
#	print '\n\nAutomato C Deterministico'
#	c.imprimir()
	a.minimizar()
	b.minimizar()

