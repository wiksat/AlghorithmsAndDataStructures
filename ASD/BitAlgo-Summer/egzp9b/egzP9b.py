from egzP9btesty import runtests

def DFS(graf,V):
	odwiedzanie=[]
	time=0
	def DFSvisit(graf, u):
		nonlocal time,odwiedzanie
		time+=1
		d=len(graf[u])
		for v in range(d):
			if graf[u][v][1]:
				graf[u][v][1] = False
				DFSvisit(graf, graf[u][v][0])
		odwiedzanie.append(u)
	DFSvisit(graf,0)
	odwiedzanie.reverse()
	return odwiedzanie


def dyrektor( G, R ):
	#Tutaj proszę wpisać własną implementację
	V=len(G)
	for i in range(V):
		for j in range(len(G[i])):
			G[i][j] = [G[i][j], True,j]
	for i in G:
		i.sort()
	for i in R:
		i.sort()
	for i in range(V):
		wsk=0
		flag=True
		for j in range(len(G[i])):
			if len(R[i])>0 and flag and G[i][j][0]==R[i][wsk]:
				G[i][j]=[G[i][j][0],False,G[i][j][2]]
				wsk+=1
				if wsk>=len(R[i]):
					flag=False
			else:
				G[i][j] = [G[i][j][0], True,G[i][j][2]]
	for i in G:
		i=sorted(i,key=lambda x:x[2])
	return DFS(G,V)

runtests(dyrektor, all_tests=True)
