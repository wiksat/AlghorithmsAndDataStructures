from queue import PriorityQueue
from math import inf

def dijkstra(G,v,s,D,T):

    n = len(G)
    d = [[inf]*D for _ in range(n)]
    d[v][0] = 0
    p = [[-1]*D for _ in range(n)]
    K = PriorityQueue()
    K.put((0, v, 0)) # krotka - (dotychczaswoy koszt, wierzchołek, ile l benzyny mam dojezdzajac do wierzchołka)
    while not K.empty():
        u=K.get()
        if u[1]==s:
            return u[0]
        i=0
        while i+u[2]<=D:
            for x in G[u[1]]:
                if x[1]<=i+u[2] and d[x[0]][i+u[2]-x[1]]>u[0]+T[u[1]]*i:
                    d[x[0]][i + u[2] - x[1]] = u[0] + T[u[1]] * i
                    p[x[0]][i + u[2] - x[1]] = u[1]
                    K.put((d[x[0]][i + u[2] - x[1]],x[0],i+u[2]-x[1]))
            i+=1
    return d

A = [
    [(1,3),(4,2),(3,3)],    # 0
    [(0,3),(3,4),(2,5)],    # 1
    [(1,5),(3,2),(7,1)],    # 2
    [(0,3),(1,4),(2,2),(6,4)],  # 3
    [(0,2),(5,3)],      # 4
    [(4,3),(6,4),(8,3)]   ,  # 5
    [(5,4),(3,4),(8,2),(7,3)],  # 6
    [(2,1),(6,3),(8,1)], # 7
    [(5,3),(6,2),(7,1)]

]
T = [1,3,2,2,2,2,4,4,3]
print(dijkstra(A,0,8,5,T))