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
