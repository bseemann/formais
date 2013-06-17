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
		if novo not in self.estados:
			self.estados.append(novo)
			x = dict()
			for i in self.alfabeto:
				x[i]=[]
			self.transicoes[novo] = x
	
	def inserir_terminal(self,novo):
		if novo not in self.alfabeto:
			self.alfabeto.append(novo)
			for i in self.transicoes:
				self.transicoes[i][novo]=[]

	def inserir_transicao(self,estado_atual,terminal,estado_final):
		self.transicoes[estado_atual][terminal].append(estado_final)
	
	def inserir_estado_inicial(self,inicial):
		if len(self.inicial)==0:
			self.inicial=inicial
		else:
			print 'Estado inicial ja definido'
	
	def inserir_estado_final(self,final):
		self.finais.append(final)

	def verificar_determinismo(self):
		for i in self.transicoes:
			for j in self.transicoes[i]:
				if len(self.transicoes[i][j])>1:
					return 0
		return 1

	def determinizar(self):
		t=Transformacoes()
		cop=t.determinizar(self)
		cop.imprimir()
		return cop

	def minimizar(self):
		t=Transformacoes()
		if not self.verificar_determinismo():
			copia=t.determinizar(self)
			copia=t.minimizar(copia)
		else:
			copia=t.minimizar(self)
		copia.imprimir()
		return copia
	
	def reconhecer_sentenca(self,sentenca):
		formas_sentenciais=[]
		sentencas=[]
		for i in self.transicoes[self.inicial][sentenca[0]]:
			s=sentenca[0]+i
			if s not in formas_sentenciais:
				formas_sentenciais.append(s)
		for n in range(len(sentenca)-1):
			m=copy.copy(formas_sentenciais)
			formas_sentenciais=[]
			for i in m:
				nt=i[n+1:len(i)]
				for j in self.transicoes[nt][sentenca[n+1]]:
					if j!='Qerr':
						s=i[0:n+1]+sentenca[n+1]+j
						if s not in formas_sentenciais:
							formas_sentenciais.append(s)
						if j in self.finais:
							if s[0:len(s)-len(j)] not in sentencas:
								sentencas.append(s[0:len(s)-len(j)])
		if sentenca in sentencas:
			return 'Pertence'
		return 'Nao pertence'


	def enumerar_sentencas(self,tamanho):
		formas_sentenciais=[]
		sentencas=[]
		for i in self.alfabeto:
			for j in self.transicoes[self.inicial][i]:
				formas_sentenciais.append(i+j)
				if j in self.finais:
					sentencas.append(i)
		for n in range(tamanho-1):
			m=copy.copy(formas_sentenciais)
			formas_sentenciais=[]
			for i in m:
				nt=i[n+1:len(i)]
				pred=i[0:n+1]
				for j in self.alfabeto:
					for k in self.transicoes[nt][j]:
						if k != 'Qerr':
							s=pred+j+k
							if s not in formas_sentenciais:
								formas_sentenciais.append(s)
							if k in self.finais:
								if s[:len(s)-len(k)] not in sentencas:
									sentencas.append(s[:len(s)-len(k)])
		return sentencas

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
	a.minimizar()
	b.minimizar()
	d=Automato()
	d.inserir_estado('S')
	d.inserir_estado('A')
	d.inserir_estado('B')
	d.inserir_estado('C')
	d.inserir_estado('D')
	d.inserir_terminal('a')
	d.inserir_terminal('b')
	d.inserir_transicao('S','a','B')
	d.inserir_transicao('S','a','C')
	d.inserir_transicao('S','b','A')
	d.inserir_transicao('S','b','D')
	d.inserir_transicao('A','a','B')
	d.inserir_transicao('A','b','A')
	d.inserir_transicao('B','a','A')
	d.inserir_transicao('B','b','B')
	d.inserir_transicao('C','a','C')
	d.inserir_transicao('C','b','D')
	d.inserir_transicao('D','a','D')
	d.inserir_transicao('D','b','C')
	d.inserir_estado_inicial('S')
	d.inserir_estado_final('S')
	d.inserir_estado_final('C')
	d.inserir_estado_final('D')
	print 'automato d'
	r=d.minimizar()
	print 'automato c'
	c.minimizar()
	#c.determinizar() 
	print 'automato 4c'
	e=Automato()
	e.inserir_estado('S')
	e.inserir_estado('A')
	e.inserir_estado('B')
	e.inserir_estado('C')
	e.inserir_estado('D')
	e.inserir_estado('E')
	e.inserir_terminal('a')
	e.inserir_terminal('b')
	e.inserir_transicao('S','a','A')
	e.inserir_transicao('S','b','B')
	e.inserir_transicao('A','a','S')
	e.inserir_transicao('A','b','C')
	e.inserir_transicao('A','b','E')
	e.inserir_transicao('B','a','A')
	e.inserir_transicao('B','a','C')
	e.inserir_transicao('C','a','B')
	e.inserir_transicao('D','a','E')
	e.inserir_transicao('E','a','S')
	e.inserir_transicao('E','a','D')
	e.inserir_estado_inicial('S')
	e.inserir_estado_final('S')
	e.inserir_estado_final('B')
	e.inserir_estado_final('D')
	e.minimizar()
	f=Automato()
	f.inserir_estado('S')
	f.inserir_estado('A')
	f.inserir_estado('B')
	f.inserir_estado('F')
	f.inserir_terminal('a')
	f.inserir_terminal('b')
	f.inserir_terminal('c')
	f.inserir_transicao('S','a','A')
	f.inserir_transicao('S','b','B')
	f.inserir_transicao('S','c','F')
	f.inserir_transicao('A','a','S')
	f.inserir_transicao('A','a','F')
	f.inserir_transicao('B','b','S')
	f.inserir_transicao('B','b','F')
	f.inserir_estado_inicial('S')
	f.inserir_estado_final('F')
	print 'S->aA|bB|c; A->aS|a; B->bS|b'
	g=f.minimizar()
	print g.reconhecer_sentenca('aabbc')
	print g.reconhecer_sentenca('aabbaabbaaaacaa')
