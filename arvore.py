from types import *

class Arvore:
	def __init__(self,valor,esquerda=None,direita=None):
#		 'esquerda',esquerda
		if isinstance(esquerda,str):
			if esquerda[0]=='(':
				indice=[]
				for i in range(len(esquerda)):
					a=esquerda[i]
					if a == '(':
						indice.append(i)
					if a == ')':
						indice.pop()
						if len(indice)==0:
							# 'len',len(esquerda),'i',i
							if len(esquerda)>i+1:
								b=esquerda[i+1]
								if b=='?' or b=='*':
									if len(esquerda)==i+2:
										esquerda=Arvore(b,esquerda[1:i])
									else:
										esquerda=Arvore('.',esquerda[1:i],esquerda[i+2:len(esquerda)])
								elif b=='|':
									if len(esquerda)==i+2:
										esquerda=Arvore('|',esquerda[1:i],Arvore(esquerda[i+2]))
									else:
										esquerda=Arvore('|',esquerda[1:i],esquerda[i+2:len(esquerda)])
								else:
									esquerda=Arvore('.',esquerda[1:i+1],esquerda[i+1:len(esquerda)])
							break
			else:
				if esquerda[1]=='?' or esquerda[1]=='*':
					if len(esquerda)==2:
						esquerda=Arvore(esquerda[1],Arvore(esquerda[0]))
					else:
						esquerda=Arvore('.',esquerda[0:2],esquerda[2:len(esquerda)])
				elif esquerda[1]=='|':
					if len(esquerda)-1>1:
						esquerda=Arvore('|',Arvore(esquerda[0]),esquerda[2:len(esquerda)])
					else:
						esquerda=Arvore('|',Arvore(esquerda[0]),Arvore(esquerda[1]))
				else:
					if len(esquerda)-1>1:
						esquerda=Arvore('.',Arvore(esquerda[0]),esquerda[1:len(esquerda)])
					else:
						esquerda=Arvore('.',Arvore(esquerda[0]),Arvore(esquerda[1]))
		
		if isinstance(direita,str):
			if direita[0]=='(':
#				 'dir[0]=(','len',len(direita)
				indice=[]
				for i in range(len(direita)):
					# 'i',i,'direita[i]',direita[i]
					a=direita[i]
					if a == '(':
						indice.append(i)
					if a == ')':
						indice.pop()
						if len(indice)==0:
							if len(direita)>i:
								b=direita[i+1]
								if b=='?' or b=='*':
									if len(direita)==i+2:
										direita=Arvore(b,direita[1:i])
									else:
										direita=Arvore('.',direita[1:i],direita[i+2:len(direita)])
								elif b=='|':
									direita=Arvore('|',direita[1:i+2],direita[i+2:len(direita)])
								else:
									direita=Arvore('.',direita[1:i+1],direita[i+1:len(direita)])
								break;
			else:
				# 'direita',direita
				if direita[1]=='?' or direita[1]=='*':
					if len(direita)==2:
						direita=Arvore(direita[1],Arvore(direita[0]))
					else:
						if len(direita)-1>1:
				#			 'DIR',direita
							direita=Arvore('.',Arvore(direita[1],Arvore(direita[0])),direita[2:len(direita)])
						else:
							direita=Arvore('.',Arvore(direita[1],Arvore(direita[0])))
				elif direita[1]=='|':
					if len(direita)-1>1:
						direita=Arvore('|',Arvore(direita[0]),direita[2:len(direita)])
					else:
						direita=Arvore('|',Arvore(direita[0]),Arvore(direita[1]))
				else:
					if len(direita)-1>1:
						direita=Arvore('.',Arvore(direita[0]),direita[1:len(direita)])
					else:
						direita=Arvore('.',Arvore(direita[0]),Arvore(direita[1]))
		self.valor=valor
		self.esquerda=esquerda
		self.direita=direita

	#	 '---'*10
	#	 self.valor
	#	 'dir', type(self.direita)
	#	 'esq', type(self.esquerda)
	#	 self.direita
	#	 '---'*10

