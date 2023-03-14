from egzP5btesty import runtests 

def koleje ( B ):
    #tutaj proszę wpisać własną implementację
    n=len(B)
    maxW=0
    for i in range(n):
        maxW=max(maxW,B[i][0],B[i][1])
    V=maxW+1
    graf = [[] for _ in range(V)]
    # print(B)
    for i in range(n):
        if B[i][0]>B[i][1]:
            B[i]=(B[i][1],B[i][0])
    # print(B)
    B=sorted(B)
    # print(B)
    temp=B[0]
    new=[]
    new.append(B[0])
    for i in range(1,n):
        if B[i]!=temp:
            temp=B[i]
            new.append(temp)
    # print(new)

    for i in range(len(new)):
        graf[new[i][0]].append(new[i][1])
        graf[new[i][1]].append(new[i][0])
    # for i in graf:
    #     print(i)

    visited=[False for _ in range(V)]
    parent=[None for _ in range(V)]
    low = [float("Inf")] * V
    disc = [float("Inf")] * V
    time=0
    mosty=[]
    def DFSvisit(graf, u):
        nonlocal time
        visited[u]=True
        disc[u]=time
        low[u]=time
        time+=1
        for v in graf[u]:
            if visited[v]==False:
                parent[v]=u
                DFSvisit(graf,v)

                low[u]=min(low[u],low[v]) #dziecko w drzewie DFS
                if low[v] > disc[u]:
                        #znaleziono most u,v
            elif v!=parent[u]:
                low[u] = min(low[u], disc[v]) #krawedz wsteczna

    for i in range(V):
        if visited[i]==False:
            DFSvisit(graf,i)

    return len(mosty)

runtests ( koleje, all_tests=True )