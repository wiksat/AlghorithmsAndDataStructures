"""
WIKTOR SATORA
Najpierw program do grafu G dodaje możliwości dostania się szybowcem (dodaje krawędzie z wagami do tablicy)
Następnie jest uruchamiany zwykły algorytm Dijkstry
Zwracana jest wartość z tablicy t-ego miejsca tablicy d.
Złożoność oblicznieowa O(n^2)
"""
import queue
from kol3btesty import runtests

def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    V=len(G)
    visited=[False for _ in range(V)]
    d=[10**10 for _ in range(V)]
    graf=[[0 for _ in range(V)] for _ in range(V)]

    for i in range(V):
        for j in range(len(G[i])):
            graf[i][G[i][j][0]]=G[i][j][1]

    for i in range(V):
        for j in range(V):
            if j==i:
                continue
            if graf[i][j]>0 and A[i]+A[j]<graf[i][j] :
                graf[i][j]=A[i]+A[j]
            if graf[i][j]==0:
                graf[i][j] = A[i] + A[j]
    d[s]=0
    for i in range(V):
        mini=10**10
        # x=0
        for u in range(V):
            if d[u]<mini and visited[u]==False:
                mini=d[u]
                x=u
        visited[x]=True
        for y in range(V):
            if graf[x][y]>0 and visited[y]==False and d[y]>d[x]+graf[x][y]:
                d[y]=d[x]+graf[x][y]
    return d[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )