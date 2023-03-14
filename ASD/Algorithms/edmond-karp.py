import bisect
import collections
def dfs_visit(G,visited,parent,source):
    for i in range(len(G[source])):
        if visited==False and G[source][i]>0:
            parent[i] = source
            dfs_visit(G, visited, parent, i)
def dfs(G,source,sink,parent):
    visited=[False]*len(G)
    dfs_visit(G, visited, parent, source)
    return visited[sink]
def bfs(G,source,sink,parent):
    visited = [False] * len(G)
    queue = collections.deque()
    queue.append(source)
    visited[source]=True
    while queue:
        q=queue.popleft()
        for ind in range(len(G[q])):
            if (visited[ind] == False) and G[q][ind]>0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = q
    return visited[sink]


def edmond_karp(G,source,sink):
    parent=[None for _ in range(len(G))]
    max_flow=0
    while bfs(G,source,sink,parent):
        p=sink
        path_flow = float("Inf")
        while p!=source:
            path_flow=min(path_flow,G[parent[p]][p])
            p=parent[p]
        max_flow+=path_flow
        p=sink
        while p!=source:
            e=parent[p]
            G[e][p]-=path_flow
            G[p][e]+=path_flow
            p=parent[p]
    return max_flow