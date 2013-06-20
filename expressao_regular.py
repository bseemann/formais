from automato import *
from transformacoes import *
from arvore import *
import string

class Expressao_Regular(object):
	# ((ab)*|a?ba*)?ab
	def construir_arvore(self,expressao):
		#print '\n\nExpressao: ',expressao
		#print '-----------construindo arvore-------------'
		if expressao[0]=='(':
			indice=[]
			for i in range(len(expressao)):
				a=expressao[i]
				if a == '(':
					indice.append(i)
				if a == ')':
					indice.pop()
					if len(indice)==0:
						if len(expressao)>i:
							b=expressao[i+1]
							if b=='?' or b=='*':
								#print 'i',i,'len',len(expressao)
								if len(expressao)==i+2:
									arvore=Arvore(b,expressao[1:i])
								else:
									arvore=Arvore('.',expressao[1:i],expressao[i+2:len(expressao)])
							elif b=='|':
								arvore=Arvore('|',expressao[0:i],expressao[i+2:len(expressao)])
							else:
								arvore=Arvore('.',expressao[0:i+1],expressao[i+1:len(expressao)])
		else:
			if expressao[1]=='?' or expressao[1]=='*':
				if len(expressao)==2:
					arvore=Arvore(b,Arvore(expressao[0]))
				else:
					arvore=Arvore('.',expressao[0:2],expressao[2:len(expressao)])
			elif expressao[1]=='|':
				arvore=Arvore('|',Arvore(expressao[0]),expressao[2:len(expressao)])
			else:
				#print 'exp[0]',expressao[0],'exp[1:len]',expressao[1:len(expressao)]
				arvore=Arvore('.',Arvore(expressao[0]),expressao[1:len(expressao)])
		return arvore

	def di_simone(self,expressao):
		arvore = self.construir_arvore(expressao)
		print 'ARE YOU MAD?'

	def thompson_modificado(self,expressao):
		a=expressao[0]
		automato=Automato()
		estado=''
		indice=0
		tamanho=len(expressao)
		percorrido=0
		if len(expressao)==3:
			a=expressao[0]
			b=expressao[1]
			c=expressao[2]
			automato.inserir_estado(string.uppercase[indice])
			automato.inserir_estado_inicial(string.uppercase[indice])
			indice=indice+1
			percorrido=1
			if b=='|':
				automato.inserir_estado(string.uppercase[indice])
				automato.inserir_terminal(a)
				automato.inserir_terminal(c)
				automato.inserir_transicao(automato.inicial,a,string.uppercase[indice])
				automato.inserir_transicao(automato.inicial,c,string.uppercase[indice])
				automato.inserir_estado_final(string.uppercase[indice])
				return automato
			if b=='?' or b=='*':
				subautomato=self.thompson_modificado(a+b)
				for i in subautomato.alfabeto:
					if i not in automato.alfabeto:
						automato.inserir_terminal(i)
				for i in subautomato.estados:
					if i!=subautomato.inicial:
						j=string.uppercase.find(i)+percorrido
						automato.inserir_estado(string.uppercase[j])
				for i in subautomato.transicoes:
					for j in subautomato.alfabeto:
						for k in subautomato.transicoes[i][j]:
							l=string.uppercase.find(k)+percorrido
							if i==subautomato.inicial:
								if k==subautomato.inicial:
									automato.inserir_transicao(automato.inicial,j,automato.inicial)
								else:
									automato.inserir_transicao(automato.inicial,j,string.uppercase[l])
							else:
								e=string.uppercase.find(i)+percorrido
								automato.inserir_transicao(string.uppercase[e],j,string.uppercase[l])
				m=percorrido
				for i in automato.estados:
					j=string.uppercase.find(i)
					if j>m:
						m=j
				automato.inserir_terminal(c)
				automato.inserir_estado(string.uppercase[m+1])
				automato.inserir_estado_final(string.uppercase[m+1])
				for i in subautomato.finais:
					automato.inserir_transicao(i,c,string.uppercase[m+1])
				return automato
			if b in string.lowercase:
				if c=='*' or c=='?':
					subautomato=self.thompson_modificado(b+c)
					for i in subautomato.alfabeto:
						if i not in automato.alfabeto:
							automato.inserir_terminal(i)
					for i in subautomato.estados:
						j=string.uppercase.find(i)+percorrido
						automato.inserir_estado(string.uppercase[j])
					e=string.uppercase.find(subautomato.inicial)+percorrido
					automato.inserir_terminal(a)
					automato.inserir_transicao(automato.inicial,a,string.uppercase[e])
					for i in subautomato.transicoes:
						for j in subautomato.alfabeto:
							for k in subautomato.transicoes[i][j]:
								l=string.uppercase.find(k)+percorrido
								e=string.uppercase.find(i)+percorrido
								automato.inserir_transicao(string.uppercase[e],j,string.uppercase[l])
					for i in subautomato.finais:
						e=string.uppercase.find(i)+percorrido
						automato.inserir_estado_final(string.uppercase[e])
					return automato
				if c in string.lowercase:
					automato.inserir_estado(string.uppercase[indice])
					automato.inserir_estado(string.uppercase[indice+1])
					automato.inserir_estado(string.uppercase[indice+2])
					automato.inserir_terminal(a)
					automato.inserir_terminal(b)
					automato.inserir_terminal(c)
					automato.inserir_transicao(automato.inicial,a,string.uppercase[indice])
					automato.inserir_transicao(string.uppercase[indice],b,string.uppercase[indice+1])
					automato.inserir_transicao(string.uppercase[indice+1],c,string.uppercase[indice+2])
					automato.inserir_estado_final(string.uppercase[indice+2])
					return automato

		if len(expressao)==2:
			a=expressao[0]
			b=expressao[1]
			automato.inserir_estado(string.uppercase[indice])
			automato.inserir_estado_inicial(string.uppercase[indice])
			indice=indice+1
			if b in string.lowercase:
				automato.inserir_estado(string.uppercase[indice])
				automato.inserir_estado(string.uppercase[indice+1])
				automato.inserir_terminal(a)
				automato.inserir_terminal(b)
				automato.inserir_transicao(automato.inicial,a,string.uppercase[indice])
				automato.inserir_transicao(string.uppercase[indice],b,string.uppercase[indice+1])
				automato.inserir_estado_final(string.uppercase[indice+1])
				return automato
			elif b=='?':
				automato.inserir_estado(string.uppercase[indice])
				automato.inserir_terminal(a)
				automato.inserir_transicao(automato.inicial,a,string.uppercase[indice])
				automato.inserir_estado_final(string.uppercase[indice])
				automato.inserir_estado_final(automato.inicial)
				return automato
			elif b=='*':
				automato.inserir_terminal(a)
				automato.inserir_transicao(automato.inicial,a,automato.inicial)
				automato.inserir_estado_final(automato.inicial)
				return automato
		if len(expressao)==1:
			for i in range(2):
				estado=string.uppercase[i]
				automato.inserir_estado(estado)
			automato.inserir_terminal(expressao[0])
			automato.inserir_estado_inicial(string.uppercase[indice])
			automato.inserir_estado_final(string.uppercase[indice+1])
			automato.inserir_transicao(automato.inicial,expressao[0],automato.finais[0])
			return automato
	
	def imprimir_arvore(self,arvore):
		if arvore==None:return
		self.imprimir_arvore(arvore.esquerda)
		print arvore.valor,
		self.imprimir_arvore(arvore.direita)


if __name__ == "__main__":
	e=Expressao_Regular()
#	a=e.di_simone('ab*')
#	e.imprimir_arvore(a)
#	a=e.di_simone('ab*a*')
#	e.imprimir_arvore(a)
#	a=e.di_simone('(ab)*')
#	e.imprimir_arvore(a)
#	a=e.di_simone('ab*(ab)*')
#	e.imprimir_arvore(a)
	a=e.thompson_modificado('abb')
#	a.imprimir()
	t=Transformacoes()
	a=Automato()
	a.inserir_estado('A')
	a.inserir_estado('B')
	a.inserir_terminal('a')
	a.inserir_terminal('b')
	a.inserir_transicao('A','a','A')
	a.inserir_transicao('A','b','B')
	a.inserir_transicao('B','a','B')
	a.inserir_transicao('B','b','A')
	a.inserir_estado_inicial('A')
	a.inserir_estado_final('A')
	b=Automato()
	b.inserir_estado('A')
	b.inserir_estado('B')
	b.inserir_terminal('a')
	b.inserir_terminal('b')
	b.inserir_transicao('A','a','A')
	b.inserir_transicao('A','b','A')
	b.inserir_transicao('B','a','B')
	b.inserir_transicao('B','b','A')
	b.inserir_estado_inicial('A')
	b.inserir_estado_final('A')
	c=Automato()
	a=e.thompson_modificado('abb')
	b=e.thompson_modificado('abb')
	print 'a'
	a.imprimir()
	print 'b'
	b.imprimir()
	if t.automatos_equivalentes(a,b,c):
		print 'Equivalentes'
	

