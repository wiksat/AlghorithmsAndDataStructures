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
    parent=[None for _ in range(V)]
    d=[10**10 for _ in range(V)]

    for i in range(V):
        for j in range(len(G[i])):
            G[i][j]=(G[i][j][1],G[i][j][0])

    for i in range(V):
        for j in range(V):
            if j==i:
                continue
            G[i].append((A[i]+A[j],j))
    d[s]=0
    kolej=queue.PriorityQueue()
    kolej.put((0,s))
    while not kolej.empty():
        u=kolej.get()
        for v in G[u[1]]:
            # relaksacja
            if d[v[1]]>d[u[1]]+v[0]:
                d[v[1]]=d[u[1]]+v[0]
                parent[v[1]]=u[1]
                kolej.put(v)
    print(d)
    return d[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )