"""
algorytm kruskala
implementacja listy krawędzi
(waga,1wierzchołek,2wierzchołek)
"""
def find(x):
    if find(x)!=x:
        x=find(x.parent)
    return x
def union(u,v):
    """"""
def makeset(x):
    """"""
def kruskal(G):
    G=sorted(G,key=lambda x: x[0])
    E=len(G)
    """zakładamy że wierzchołki są ponumerowane """
    v=0
    for i in range(E):
        if G[i][2]>v:
            v=G[i][2]
    D=[None for _ in range(v)]
    for u in range(v):
        D[u]=Node(u)
    MST=[]
    for e in range(G):
        if find(D[G[e][1]])!=find(D[G[e][2]]):
            union(D[G[e][1]],D[G[e][2]])
            MST.append(G[e])
    return MTS
