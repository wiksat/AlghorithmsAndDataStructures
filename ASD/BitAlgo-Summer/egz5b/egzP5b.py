from egzP5btesty import runtests
time=0
# po prostu znalezienie które wierzchołki są punktami artykulacji
def DFSvisit(graf, art, low, disc, parent,visited, u):
    global time
    children = 0
    visited[u]=True

    disc[u] = time
    low[u] = time
    time += 1
    for v in graf[u]:
        if visited[v]==False:
            children += 1
            parent[v]=u
            DFSvisit(graf, art, low, disc, parent,visited, v)
            low[u] = min(low[u], low[v])
            if low[v] >= disc[u]:
                art[u] = True
            # if parent[u] is None and children > 1:
            #     art[u] = True
            # if parent[u] is not None and low[v] >= disc[u]:
            #     art[u] = True
        elif v!=parent[u]:
        # else:
            low[u] = min(low[u], disc[v])
    return children
def koleje ( B ):
    #tutaj proszę wpisać własną implementację
    n=len(B)
    maxW=0
    for i in range(n):
        maxW=max(maxW,B[i][0],B[i][1])
    V=maxW+1
    graf = [[] for _ in range(V)]

    for i in range(n):
        if B[i][0]>B[i][1]:
            B[i]=(B[i][1],B[i][0])
    B=sorted(B)
    temp=B[0]
    new=[]
    new.append(B[0])
    for i in range(1,n):
        if B[i]!=temp:
            temp=B[i]
            new.append(temp)

    for i in range(len(new)):
        graf[new[i][0]].append(new[i][1])
        graf[new[i][1]].append(new[i][0])

    visited = [False for _ in range(V)]
    art=[False for _ in range(V)]
    parent=[None for _ in range(V)]
    low = [None] * V
    disc = [None] * V


    for i in range(V):
        if visited[i]==False:
            if DFSvisit(graf,art,low,disc,parent,visited,i)>1:
                art[i]=True
            else:
                art[i]=False
    points=0
    for i in range(V):
        if art[i]==True:
            points+=1

    return points

runtests ( koleje, all_tests=True )