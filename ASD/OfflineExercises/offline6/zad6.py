from zad6testy import runtests
from queue import *
def bfs(G,s,t):
    n=len(G)
    Q=Queue()
    visited=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s]=0
    visited[s]=True
    Q.put(s)

    while not Q.empty():
        u=Q.get()
        for el in G[u]:
            if visited[el]==False:
                visited[el]=True
                d[el]=d[u]+1
                parent[el] = u
                Q.put(el)
    print(parent)
    res=[t]
    i=t
    # print(parent[i])
    while parent[i] is not None:
        res.append(parent[i])
        i=parent[i]
    res.reverse()
    # print(res)
    return d[t],res

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    V=len(G)
    first,res=bfs(G,s,t)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = False )