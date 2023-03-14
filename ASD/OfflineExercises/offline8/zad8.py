"""
WIKTOR SATORA
Algorytm to jest uruchomiony w przybliżeniu E razu algorytm Kruskala. W każdym kolejnym wywołaniu pomniejszam zbiór możliwych krawędzi o tą z najmniejszą wagą,
aby wykusić Kruskalowi wybór innego MST, za każdym razem obliczam różnice maxa i mina, a gdy jest mniejsza od globalnej to aktualizuje
Złożoność to będzie E^2*log(V)
"""
import math
from zad8testy import runtests
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

def highway( A ):
    n=len(A)
    roznica=10**10
    adresy = [Node(a) for a in range(n)]
    tab=[]
    for a in range(n):
        for b in range(a, n):
            if a != b:
                wynik = math.ceil(math.sqrt((A[a][0] - A[b][0]) ** 2 + (A[a][1] - A[b][1]) ** 2))
                tab.append((wynik, a, b))
    tab.sort()
    len_tab=len(tab)
    prev=0
    for x in range(len_tab):
        if x>0:
            if prev==tab[x][0]:
                continue
        prev=tab[x][0]
        for a in range(n):
            adresy[a].parent = adresy[a]
        temp_min=10**10
        temp_max=0
        counter=0
        for z in range(x,len_tab):
            if find(adresy[tab[z][1]]) is find(adresy[tab[z][2]]):
                continue
            counter+=1
            temp_min=min(temp_min,tab[z][0])
            temp_max=max(temp_max,tab[z][0])
            union(adresy[tab[z][1]], adresy[tab[z][2]])
            if (counter > 1 and temp_max - temp_min >= roznica) or counter==n-1:
                break

        if counter==n-1:
            roznica=min(roznica,temp_max-temp_min)

    return roznica

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )