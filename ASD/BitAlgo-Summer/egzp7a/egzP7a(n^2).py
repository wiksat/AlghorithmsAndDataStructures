from egzP7atesty import runtests 
import collections

# def bfs(graph, s, t, parent):
#     visited = [False] * len(graph)
#     queue = collections.deque()
#     queue.append(s)
#     visited[s] = True
#     while queue:
#         u = queue.popleft()
#         for ind, val in enumerate(graph[u]):
#             if (visited[ind] == False) and (val > 0):
#                 queue.append(ind)
#                 visited[ind] = True
#                 parent[ind] = u
#     return visited[t]
def dfs_visit(graph,GD,visited,parent,u):
    visited[u]=True
    for v in graph[u]:
        idd = str(u) + "-" + str(v)
        if not visited[v] and GD[idd]!=0:
            parent[v]=u
            dfs_visit(graph,GD,visited,parent,v)
def dfs(graph,GD,s,t,parent):
    visited=[False for _ in range(len(graph))]
    dfs_visit(graph,GD,visited,parent,s)
    return visited[t]
def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    GD={}
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            idd=str(u)+"-"+str(graph[u][v])
            iddBack=str(graph[u][v])+"-"+str(u)
            GD[idd]=1
            if GD.get((iddBack))==None:
                GD[iddBack]=0
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            idd=str(graph[u][v])+"-"+str(u)
            if GD.get((idd)) == 0:
                graph[graph[u][v]].append(u)
    while dfs(graph, GD,source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, GD[str(parent[s])+"-"+str(s)])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            GD[str(u)+"-"+str(v)] -= path_flow
            GD[str(v)+"-"+str(u)] += path_flow
            v = parent[v]
    return max_flow
def akademik( T ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    s=2*n
    t=s+1
    graf=[[] for _ in range(t+1)]
    licz=0
    for y in range(n):
        for x in range(3):
            if x==0 and T[y][x] is None and T[y][x+1] is None and T[y][x+2] is None:
                licz+=1
            if T[y][x] is not None:
                graf[y].append(n+T[y][x])
    for i in range(n):
        graf[s].append(i)
        graf[n+i].append(t)
    maxp=edmonds_karp(graf,s,t)

    return n-maxp-licz

runtests ( akademik )