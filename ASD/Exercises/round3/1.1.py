import queue

"""
implementacja listowa grafu
(wierzchołek sąsiad,waga)
"""
def relax(u,v,d,parent,pq):
    if d[v]>d[u]+w(u,v):
        d[v]=d[u]+w(u,v)
        parent[v]=u
        pq.put((d[v],v))
def dijkstra(G,s):
    V=len(G)
    d=[float('inf') for _ in range(V)]
    parent=[None for _ in range(V)]
    d[s]=0
    pq=queue.PriorityQueue()
    pq.put((d[s],s))
    while not pq.empty():
        prior,u=pq.get()
        for p in G[u]:
            relax(u,p[0],d,parent,pq)