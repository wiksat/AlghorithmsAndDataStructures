import math
from zad8testy import runtests
from queue import PriorityQueue

def highway( A ):
    n=len(A)
    roznica=10**10
    kolej=PriorityQueue()
    macierz=[[float('inf') for _ in range(n)] for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    tab=[]
    for a in range(n):
        for b in range(n):
            if a != b:
                wynik = math.ceil(math.sqrt((A[a][0] - A[b][0]) ** 2 + (A[a][1] - A[b][1]) ** 2))
                macierz[a][b]=wynik
    visited[0]=True
    v=0
    # for i in macierz:
    #     print(i)
    for i in range(n-1):
        for x in range(n):
            if macierz[v][x]!=float('inf'):
                if visited[x]== False:
                    kolej.put((macierz[v][x],v,x))
        while True:
            d=kolej.get()
            # print(d)
            if visited[d[2]]==False:
                break
        tab.append(d)
        visited[d[2]]=True
        parent[d[2]]=d[1]
        v=d[2]
    # print("---------")
    print(tab)
    # print(visited)
    # print(parent)
    # print("reszta kolejki")
    # while not kolej.empty():
    #     d=kolej.get()
    #     print(d)
    return roznica

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = False )