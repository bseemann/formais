from automato import *
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


	def imprimir_arvore(self,arvore):
		if arvore==None:return
		self.imprimir_arvore(arvore.esquerda)
		print arvore.valor,
		self.imprimir_arvore(arvore.direita)


if __name__ == "__main__":
	e=Expressao_Regular()
	a=e.di_simone('ab*')
	e.imprimir_arvore(a)
	a=e.di_simone('ab*a*')
	e.imprimir_arvore(a)
	a=e.di_simone('(ab)*')
	e.imprimir_arvore(a)
	a=e.di_simone('ab*(ab)*')
	e.imprimir_arvore(a)




