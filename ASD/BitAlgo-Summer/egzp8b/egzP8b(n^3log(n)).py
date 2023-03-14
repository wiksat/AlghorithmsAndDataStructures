from egzP8btesty import runtests
import queue

def dijkstra(n,G,P,i):
    s=P[i-1]
    t=P[i]
    parent = [None for _ in range(n)]
    d = [10 ** 10 for _ in range(n)]
    d[s] = 0
    kolej = queue.PriorityQueue()
    kolej.put((0, s))
    while not kolej.empty():
        u = kolej.get()
        for v in G[u[1]]:
            # if v in P and P.index(v)>i:
            if v==P[i]:
                pass
            if d[v[1]] > d[u[1]] + v[0]:
                d[v[1]] = d[u[1]] + v[0]
                parent[v[1]] = u[1]
                kolej.put(v)
    return d[t]
def robot( G, P ):
    #Tutaj proszę wpisać własną implementację
    n=len(G)
    np=len(P)
    for i in range(n):
        for j in range(len(G[i])):
            G[i][j]=(G[i][j][1],G[i][j][0])
    suma=0
    i=1
    while i<np:
        suma+=dijkstra(n,G,P,i)
        i+=1
    return suma
    
runtests(robot, all_tests = True)
