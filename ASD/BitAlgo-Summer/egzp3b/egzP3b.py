from egzP3btesty import runtests 
from queue import PriorityQueue
class Node:
    def __init__(self,value):
        self.parent=self
        self.value=value
        self.rank=0
def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent
def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację
    V=len(G)
    tab=[]
    wszystkie=0
    for a in range(V):
        krawWW=len(G[a])
        for b in range(krawWW):
            if G[a][b][0]>a:
                tab.append((-G[a][b][1],a,G[a][b][0]))
                wszystkie+=G[a][b][1]
    tab=sorted(tab)

    # print(tab)
    # print(tab)
    len_tab = len(tab)
    adresy = [Node(a) for a in range(V)]
    new=[]
    suma=0
    for z in range(len_tab):
        if find(adresy[tab[z][1]]) is find(adresy[tab[z][2]]):
            continue
        union(adresy[tab[z][1]], adresy[tab[z][2]])
        new.append((-tab[z][0],tab[z][1],tab[z][2]))
        suma-=tab[z][0]
    for i in range(len_tab):
        tab[i]=(-tab[i][0],tab[i][1],tab[i][2])
    # print(tab)
    # print(new)
    for i in tab:
        if i not in new:
            # print(i)
            suma+=i[0]
            break
    # print(new)
    return wszystkie-suma

runtests ( lufthansa, all_tests=True )