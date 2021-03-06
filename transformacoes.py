import copy
import string

class Transformacoes(object):
	def completar(self,obj):
		q=0
		for i in obj.transicoes:
			for j in obj.alfabeto:
				if len(obj.transicoes[i][j])==0:
					obj.transicoes[i][j].append('Qerr')
					q=1
		if q==1:
			x = dict()
			for i in obj.alfabeto:
				x[i]=['Qerr']
			obj.transicoes['Qerr']=x
			obj.estados.append('Qerr')
		return obj

	def determinizar(self,obj):
		self=obj
		det=dict()
		det[self.inicial]=dict()
		for i in self.transicoes[self.inicial]:
			det[self.inicial][i]=self.transicoes[self.inicial][i]
			if len(self.transicoes[self.inicial][i])>1:
				self.transicoes[self.inicial][i].sort()
				s=''
				for j in self.transicoes[self.inicial][i]:
					s=s+j
				det[s]=dict()
				for j in self.alfabeto:
					det[s][j]=[]
			if len(self.transicoes[self.inicial][i])==1:
				for x in self.transicoes[self.inicial][i]:
					if x not in det:
						det[x]=dict()
						for j in self.alfabeto:
							det[x][j]=[]
		d=0
		while d!=det:
			d=copy.deepcopy(det)
			for i in d:
				if len(i)>1:
					for j in i:
						for k in self.transicoes[j]:
							for l in self.transicoes[j][k]:
								if l not in det[i][k]:
									det[i][k].append(l)
					for j in det[i]:
						if len(det[i][j])>1:
							det[i][j].sort()
							s=''
							for k in det[i][j]:
								s=s+k
							if s not in det:
								det[s]=dict()
								for k in self.alfabeto:
									det[s][k]=[]
						else:
							for x in det[i][j]:
								if x not in det:
									det[x]=dict()
									for k in self.alfabeto:
										det[x][k]=[]
				else:
					for j in det[i]:
						if det[i][j] != self.transicoes[i][j]:
							det[i][j]=self.transicoes[i][j]
							if len(det[i][j])>1:
								det[i][j].sort()
								s=''
								for k in det[i][j]:
									s=s+k
								det[s]=dict()
								for k in self.alfabeto:
									det[s][k]=[]
		for i in det:
			for j in det[i]:
				if len(det[i][j])>1:
					s=''
					for k in det[i][j]:
						s=s+k
					det[i][j]=[s]
		self.transicoes = det
		f = []
		for i in self.finais:
			for j in self.transicoes:
				if i in j:
					f.append(j)
		self.finais = f
		e = []
		for i in self.transicoes:
			if i not in e:
				e.append(i)
		self.estados = e
		return self


	def eliminar_inalcancaveis(self,obj):
		self=obj
		a=[]
		c=[self.inicial]
		for i in self.alfabeto:
			for j in self.transicoes[self.inicial][i]:
				a.append(j)
		b=0
		while b!=a:
			b=copy.copy(a)
			for i in b:
				c.append(i)
				for j in self.alfabeto:
					for k in self.transicoes[i][j]:
						if k not in c and k not in a:
							a.append(k)
				a.remove(i)
		copia = copy.deepcopy(self)
		copia.estados = c
		for i in self.transicoes:
			for j in self.transicoes[i]:
				for k in self.transicoes[i][j]:
					if k not in c:
						copia.transicoes[i][j].remove(k)
			if i not in c:
				copia.transicoes.pop(i)			
		copia.finais=[]
		for i in self.finais:
			if i in c and i not in copia.finais:
				copia.finais.append(i)
		return copia

	def eliminar_mortos(self,obj):
		self=obj
		copia = copy.deepcopy(self)
		m=copy.copy(copia.finais)
		n=0
		while n!=m:
			n=copy.copy(m)
			for i in copia.transicoes:
				for j in copia.transicoes[i]:
					for k in copia.transicoes[i][j]:
						if k in m and i not in m:
							m.append(i)
		for i in self.transicoes:
			if i not in m and i in copia.transicoes:
				copia.transicoes.pop(i)
		for i in copia.transicoes:
			for j in copia.transicoes[i]:
				for k in copia.transicoes[i][j]:
					if k not in m:
						copia.transicoes[i][j].remove(k)
		return copia
	
	def formar_classes_de_equivalencia(self,obj):
		f=copy.copy(obj.finais)
		k=[]
		for i in obj.estados:
			if i not in f and i not in k:
				k.append(i)
		if len(k)>0:
			m=[f,k]
		else:
			m=[f]
		n=0
		while n!=m:
			l=[]
			n=copy.copy(m)
			for i in n:
				pivo = i[0]
				for j in i:
					if j!=pivo:
						for k in obj.alfabeto:
							o=obj.transicoes[j][k]
							p=obj.transicoes[pivo][k]
							for h in n:
								if o[0] in h and p[0] not in h:
									if [j] not in l:
										l.append([j])
									x=n.index(i)
									if j in m[x]:
										m[x].remove(j)
									break
			ll=copy.copy(l)
			for i in ll:
				for j in ll:
					if i[0]!=j[0]:
						e=1
						for k in obj.alfabeto:
							o=obj.transicoes[i[0]][k]
							p=obj.transicoes[j[0]][k]
							for h in m:
								if o[0] in h and p[0] not in h:
									e=0
						if e:
							if (i[0] in obj.finais and j[0] in obj.finais) or (i[0] not in obj.finais and j[0] not in obj.finais):
								if i in l:
									l.remove(i)
								if j in l:
									l.remove(j)
								l.append(i+j)
			m=m+l
		e=[]
		f=[]
		ini=''
		for i in m:
			e.append(i[0])
			for j in i:
				if j in obj.finais and i[0] not in f:
					f.append(i[0])
				if j in obj.inicial:
					ini=i[0]
				if j!=i[0]:
					obj.transicoes.pop(j)
			for j in obj.alfabeto:
				for k in m:
					x=i[0]
					if obj.transicoes[x][j][0] in k:
						obj.transicoes[x][j]=[k[0]]
		obj.estados = e
		obj.finais = f
		obj.inicial=ini
		return obj

	def minimizar(self,obj):
		obj=self.eliminar_inalcancaveis(obj)
		obj=self.eliminar_mortos(obj)
		obj=self.completar(obj)
		obj=self.formar_classes_de_equivalencia(obj)
		return obj

	def automato_complementar(self,automato):
		complementar=self.completar(copy.deepcopy(automato))
		complementar.finais=[]
		for i in complementar.estados:
			if i not in automato.finais:
				complementar.finais.append(i)
		return complementar
	
	def automato_interseccao(self,automato1,automato2,uniao):
		complementar1=self.automato_complementar(automato1)
		complementar2=self.automato_complementar(automato2)
		print 'complementar1'
		complementar1.imprimir()
		print 'complementar2'
		complementar2.imprimir()
		indice=0
		uniao.inserir_estado(string.uppercase[indice])
		uniao.inserir_estado_inicial(string.uppercase[indice])
		indice=indice+1
		for i in complementar1.alfabeto:
			uniao.inserir_terminal(i)
		for i in complementar2.alfabeto:
			if i not in uniao.alfabeto:
				uniao.inserir_terminal(i)
		for i in complementar1.estados:
			if i=='Qerr':
				uniao.inserir_estado('#')
				if i in complementar1.finais:
					uniao.inserir_estado_final('#')
			else:
				e=string.uppercase.find(i)+indice
				uniao.inserir_estado(string.uppercase[e])
				print i,'=>',string.uppercase[e]
				if i in complementar1.finais:
					uniao.inserir_estado_final(string.uppercase[e])
		for i in complementar1.estados:
			for j in complementar1.alfabeto:
				for k in complementar1.transicoes[i][j]:
					e=string.uppercase.find(i)+indice
					l=string.uppercase.find(k)+indice
					if i==complementar1.inicial:
						if k!='Qerr':
							uniao.inserir_transicao(uniao.inicial,j,string.uppercase[l])
						else:
							uniao.inserir_transicao(uniao.inicial,j,'#')
						if i in complementar1.finais:
							uniao.inserir_estado_final(uniao.inicial)
					if i!='Qerr':
						if k!='Qerr':
							uniao.inserir_transicao(string.uppercase[e],j,string.uppercase[l])
						else:
							uniao.inserir_transicao(string.uppercase[e],j,'#')

					else:
						uniao.inserir_transicao('#',j,'#')
		m=indice
		for i in uniao.estados:
			j=string.uppercase.find(i)
			if j>m:
				m=j
		m=m+1
		indice=m
		#for i in complementar2.estados:
		#	n=m-string.uppercase.find(i)
		#	if n<indice:
		#		indice=n
		print 'indice',indice+1
		indice=indice+1
		for i in complementar2.estados:
			if i!='Qerr':
				e=string.uppercase.find(i)+indice
				uniao.inserir_estado(string.uppercase[e])
				print i,'=>',string.uppercase[e]
				if i in complementar2.finais:
					uniao.inserir_estado_final(string.uppercase[e])
			else:
				if i not in uniao.estados:
					uniao.inserir_estado('@')
					if i in complementar2.finais:
						uniao.inserir_estado_final('#')
		for i in complementar2.estados:
			for j in complementar2.alfabeto:
				for k in complementar2.transicoes[i][j]:
					e=string.uppercase.find(i)+indice
					l=string.uppercase.find(k)+indice
					if i==complementar2.inicial:
						if k!='Qerr':
							uniao.inserir_transicao(uniao.inicial,j,string.uppercase[l])
						else:
							uniao.inserir_transicao(uniao.inicial,j,'@')
						if i in complementar2.finais:
							if uniao.inicial not in uniao.finais:
								uniao.inserir_estado_final(uniao.inicial)
					if i!='Qerr':
						if k!='Qerr':
							uniao.inserir_transicao(string.uppercase[e],j,string.uppercase[l])
						else:
							uniao.inserir_transicao(string.uppercase[e],j,'@')
					else:
						uniao.inserir_transicao('@',j,'@')
		print 'uniao'
		uniao.imprimir()
		automato=self.determinizar(uniao)
		print 'determinizado'
		automato.imprimir()
		automato=self.minimizar(automato)
		print 'minimizado'
		automato.imprimir()
		automato=self.automato_complementar(automato)
		print 'final'
		automato.imprimir()
		return automato

	def automatos_equivalentes(self,automato1,automato2,obj):
		complementar1=self.automato_complementar(copy.deepcopy(automato1))
		complementar2=self.automato_complementar(copy.deepcopy(automato2))
		interseccao1=self.automato_interseccao(copy.deepcopy(automato1),complementar2,copy.deepcopy(obj))
		interseccao2=self.automato_interseccao(copy.deepcopy(automato2),complementar1,copy.deepcopy(obj))
		if len(interseccao1.finais)==0 and len(interseccao2.finais)==0:
			return True
		return False
