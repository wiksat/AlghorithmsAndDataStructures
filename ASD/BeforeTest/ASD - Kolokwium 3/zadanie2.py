import queue
G1=[[0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,0,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0]
]
s=5
t=2
def funkcja(G1,s,t):
    #1-most,5-prom,8-samolot
    n=len(G1)
    G2=[[0 for _ in range(3*n)] for _ in range(n*3)]
    # for x in G2:
    #     print(x)
    # print()
    for x in range(n):
        for z in range(n):
            if y==0 and G1[x][z]!=1:
                # przyjechano mostem
                G2[x][y][z]=G1[x][z]
            elif y==1 and G1[x][z]!=5:
                # przyjechano promem
                G2[x][y][z]=G1[x][z]
            elif y==2 and G1[x][z]!=8:
                # przyjechano samolotem
                G2[x][y][z]=G1[x][z]

    for x in G2:
        print(x)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    pq = queue.PriorityQueue()
    # def relax(u,v):
    #     nonlocal n, d, parent,pq
    #     if d[v] > d[u] + w(u, v):
    #         d[v] = d[u] + w(u, v)
    #         parent[v] = u
    #         pq.put((d[v], v))
    # def dijkstra():
    #     nonlocal n,d,parent,pq
    #     d[s] = 0
    #     pq.put((d[s], s))
    #     while not pq.empty():
    #         prior, u = pq.get()
    #         for p in G[u]:
    #             relax(u, p[0])

funkcja(G1,s,t)