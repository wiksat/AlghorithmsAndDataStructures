from egzP8btesty import runtests

def minDistance(d,visited,n):
    min=float('inf')
    min_index = 0
    for u in range(n):
        if d[u]<min and visited[u]==False:
            min=d[u]
            min_index=u
    return min_index

def dijkstra(n,graf,P,i):
    s=P[i-1]
    t=P[i]
    d = [float('inf') for _ in range(n)]
    d[s]=0
    visited=[False]*n
    for cout in range(n):
        x=minDistance(d,visited,n)
        visited[x]=True
        for y in range(n):
            if graf[x][y]>0 and visited[y]==False and d[y]>d[x]+graf[x][y]:
                d[y] = d[x] + graf[x][y]

    return d[t]
def robot( G, P ):
    #Tutaj proszę wpisać własną implementację
    n=len(G)
    np=len(P)
    graf=[[10**10 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            graf[i][G[i][j][0]]=G[i][j][1]
    suma=0
    i=1
    while i<np:
        suma+=dijkstra(n,graf,P,i)
        i+=1
    return suma
    
runtests(robot, all_tests = True)
