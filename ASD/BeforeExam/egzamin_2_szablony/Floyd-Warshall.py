INF=float('inf')
G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
nV = 4
distance = list(map(lambda i: list(map(lambda j: j, i)), G))
print(distance)
for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
print(distance)


# skrót
def Floyd_Warshall(G):
    n = len(G)
    for t in range(n): # na wykladzie (1,n+) inna numeracja wierzchołkow
        for u in range(n):
            for w in range(n):
                G[u][w] = min(G[u][w], G[u][t] + G[t][w])
