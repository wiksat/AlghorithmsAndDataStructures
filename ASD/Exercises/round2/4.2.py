from queue import *
#macierzowo
inf=10**10
def bfs(G,s):
    V=len(G)
    Q=Queue()
    visited=[0 for _ in range(V)]
    d=[inf for _ in range(V)]
    parent=[None for _ in range(V)]

    d[s]=0
    visited[s]=1
    Q.put(s)
    while not Q.empty():
        s=Q.get()
        for i in range(V):
            if G[s][i]==1:
                if visited[i]==0:
                    Q.put(i)
                    visited[i]=1
                    parent[i]=s
                    d[i]=d[s]+i


def bfsDwudzielność(G, s):
    V = len(G)
    Q = Queue()
    visited = [0 for _ in range(V)]
    color=[0 for _ in range(V)]

    color[s]=1
    visited[s] = 1
    Q.put(s)
    while not Q.empty():
        s = Q.get()
        for i in range(V):
            if G[s][i] == 1:
                if visited[i] == 0:
                    color[i]=3-color[s]
                    Q.put(i)
                    visited[i] = 1
                elif(color[s]==color[i]):
                    return False
    return True
#odtwarzanie ścieżki
def cel(par,w):
    if w!=None:
        cel(par,par[w])
        print(w)
def cel2(parent,w):
    doc=[w]
    x=0
    prev=w
    while x is not None:
        x=parent[prev]
        doc.append(x)
        prev=x
    print(doc.reverse())

def dfs(G,s):
    t = 0
    V=len(G)
    colors=[0 for _ in range(V)]#jakby visited
    d=[0 for _ in range(V)]#początek przetwarzania
    f=[0 for _ in range(V)]#finisz
    par=[None for _ in range(V)]
    def dfsVisit(G,s):
        nonlocal t,colors,d,f,par
        t+=1
        d[s]=t
        colors[s] = 1
        for u in G[s]:
            if colors[u]==0:
                par[u]=s
                dfsVisit(G,u)
        t+=1
        f[s]=t
        colors[s]=2

    lss=0
    for i in range(V):
        if colors[i]==0:
            dfsVisit(G,i)
            lss+=1
    return lss