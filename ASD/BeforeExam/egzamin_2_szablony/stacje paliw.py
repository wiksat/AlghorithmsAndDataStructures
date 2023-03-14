G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
from math import inf
from queue import PriorityQueue
def jak_dojade(G, P, d, a ,b):
    n = len(G)
    distance = [[inf] * d for _ in range(n)]
    parent=[[-1]*d for _ in range(n)]
    kolej=PriorityQueue()
    for i in range(d):
        distance[a][i]=0
    kolej.put((0,a,0))
    # kolej.put((0, a, d))
    while not kolej.empty():
        u=kolej.get()
        if u[1]==b:
            trasa=[]
            trasa.append(b)
            rodzic=parent[u[1]][u[2]]
            while rodzic[0]!=a:
                trasa.append(rodzic[0])
                if rodzic[1]==d:
                    max=0
                    for i in range(d):
                        if distance[rodzic[0]][i]<distance[rodzic[0]][max]:
                            max=i
                    rodzic=parent[rodzic[0]][max]
                else:
                    rodzic=parent[rodzic[0]][rodzic[1]]
            trasa.append(a)
            return trasa[::-1]
        for x in range(n):
            if G[u[1]][x] > 0:
                if u[1] in P:
                    if distance[x][d-G[u[1]][x]]>G[u[1]][x]+u[0]:
                        distance[x][u[2] - G[u[1]][x]] = G[u[1]][x] + u[0]
                        parent[x][u[2] - G[u[1]][x]] = (u[1], u[2])
                        kolej.put((distance[x][d - G[u[1]][x]], x, d - G[u[1]][x]))
                if distance[x][u[2] - G[u[1]][x]] > G[u[1]][x] + u[0]:
                    distance[x][u[2] - G[u[1]][x]] = G[u[1]][x] + u[0]
                    parent[x][u[2]-G[u[1]][x]]=(u[1],u[2])
                    kolej.put((distance[x][u[2] - G[u[1]][x]], x, u[2] - G[u[1]][x]))
        # for x in range(n):
        #     if G[u[1]][x]>0 and G[u[1]][x]<=u[2]:
        #         if distance[x][u[2]-G[u[1]][x]]>G[u[1]][x] + u[0]:#sprawdzic u[0]
        #             distance[x][u[2]-G[u[1]][x]]=G[u[1]][x]+u[0]
        #             parent[x][u[2]-G[u[1]][x]]=(u[1],u[2])
        #             if x in P:
        #                 kolej.put((distance[x][u[2] - G[u[1]][x]], x, d))
        #                 kolej.put((distance[x][u[2] - G[u[1]][x]], x, u[2] - G[u[1]][x]))
        #             else:
        #                 kolej.put((distance[x][u[2] - G[u[1]][x]], x, u[2] - G[u[1]][x]))


    return None
print(jak_dojade(G, P, 6, 0, 2))