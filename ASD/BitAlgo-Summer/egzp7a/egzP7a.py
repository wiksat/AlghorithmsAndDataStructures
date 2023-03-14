from egzP7atesty import runtests 
import collections

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]
def dfs_visit(graph,visited,parent,u):
    visited[u]=True
    for v in range(len(graph)):
        if not visited[v] and graph[u][v]!=0:
            parent[v]=u
            dfs_visit(graph,visited,parent,v)
def dfs(graph,s,t,parent):
    visited=[False for _ in range(len(graph))]
    dfs_visit(graph,visited,parent,s)
    return visited[t]
def edmonds_karp(graph, source, sink,n):
    parent = [-1] * len(graph)
    max_flow = 0
    while dfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
def akademik( T ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    graf=[[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    licz=0
    for y in range(n):
        for x in range(3):
            if x==0 and T[y][x] is None and T[y][x+1] is None and T[y][x+2] is None:
                licz+=1
            if T[y][x] is not None:
                graf[y][T[y][x]+n]=1
    for y in range(n):
        graf[2*n][y]=1
        graf[n+y][2*n+1]=1
    maxp=edmonds_karp(graf,2*n,2*n+1,n)
    print(licz)

    return n-maxp-licz

runtests ( akademik )