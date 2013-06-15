from automato import *

class Gramatica(object):
	def __init__(self):
		self.producoes = []
		#producoes=['S->aA|bB|&','A->a']
	
	def inserir_producao(self,novo):
		self.producoes.append(novo)

	def transformar_automato(self):
		automato = Automato()
		automato.inserir_estado('@')
		automato.inserir_estado_final('@')
		ini = self.producoes[0].split('->')
		automato.inserir_estado_inicial(ini[0])
		for i in self.producoes:
			prod = i.split('->')
			pred = prod[1].split('|')
			automato.inserir_estado(prod[0])
			for j in pred:
				if len(j)==1:
					if j=='&':
						if prod[0]==automato.inicial:
							automato.inserir_estado_final(prod[0])
					else:
						automato.inserir_terminal(j)
						automato.inserir_transicao(prod[0],j,'@')
				else:
					automato.inserir_terminal(j[0])
					automato.inserir_estado(j[1])
					automato.inserir_transicao(prod[0],j[0],j[1])
		return automato
	
	def transformar_gramatica(self,automato):
		self.producoes=[]
		for i in automato.estados:
			if i != automato.inicial:
				s=i+'->'
				for j in automato.alfabeto:
					if len(automato.transicoes[i][j])>0:
						if automato.transicoes[i][j][0] in automato.finais:
							s=s+j+' | '
						s=s+j+automato.transicoes[i][j][0]
						if len(automato.transicoes[i][j])>1:
							for k in range(1,len(automato.transicoes[i][j])):
								if automato.transicoes[i][j][k] in automato.finais:
									s=s+' | '+j
								s=s+' | '+j+automato.transicoes[i][j][k]
						s=s+' | '
				if s[len(s)-2]=='|':
					s=s[0:len(s)-2]
				self.inserir_producao(s)
			else:
				if i in automato.finais:
					s=i+'\'-> & | '
					for j in automato.alfabeto:
						if len(automato.transicoes[i][j])>0:
							if automato.transicoes[i][j][0] in automato.finais:
								s=s+j+' | '
							s=s+j+automato.transicoes[i][j][0]
							if len(automato.transicoes[i][j])>1:
								for k in range(1,len(automato.transicoes[i][j])):
									if automato.transicoes[i][j][k] in automato.finais:
										s=s+' | '+j
									s=s+' | '+j+automato.transicoes[i][j][k]
							s=s+' | '
					if s[len(s)-2]=='|':
						s=s[0:len(s)-2]
					self.inserir_producao(s)
				x=i+'->'
				for j in automato.alfabeto:
					if automato.transicoes[i][j]>0:
						if automato.transicoes[i][j][0] in automato.finais:
							x=x+j+' | '
						x=x+j+automato.transicoes[i][j][0]
						if len(automato.transicoes[i][j])>1:
							for k in range(1,len(automato.transicoes[i][j])):
								if automato.transicoes[i][j][k] in automato.finais:
									x=x+' | '+j
								x=x+' | '+j+automato.transicoes[i][j][k]
						x=x+' | '
				if x[len(x)-2]=='|':
					x=x[0:len(x)-2]
				self.inserir_producao(x)
		return self


	def imprimir(self):
		for i in self.producoes:
			print i

if __name__ == "__main__":
	g=Gramatica()
	g.inserir_producao('S->aA|bB|&')
	g.inserir_producao('A->aS|a')
	g.inserir_producao('B->bS|b')
	a=g.transformar_automato()
	print 'minimizado'
	a.minimizar()
	b=Gramatica()
	b.inserir_producao('S->aS|a')
	c=b.transformar_automato()
	c.imprimir()
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
	print 'gramatica d'
	g.transformar_gramatica(r)
	g.imprimir()
	
