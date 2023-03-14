from queue import PriorityQueue
from math import inf

def islands(G,v,t):
    n=len(G)
    d=[[inf,inf,inf] for _ in range(n)]
    d[v][0],d[v][1],d[v][2]=0,0,0
    kolej=PriorityQueue()
    kolej.put((0,v,0))
    kolej.put((0, v, 1))
    kolej.put((0, v, 2))
    while not kolej.empty():
        u=kolej.get()
        if u[1]==t:
            return u[0]
        for v in range(n):
            if G[u[1]][v]!=0 and G[u[1]][v]!=u[2]:
                if G[u[1]][v]==1:
                    wartosc=1
                    indeks=0
                elif G[u[1]][v]==5:
                    wartosc=5
                    indeks=1
                else:
                    wartosc=8
                    indeks=2
                if d[v][indeks]>u[0]+wartosc:
                    d[v][indeks] = u[0] + wartosc
                    kolej.put((d[v][indeks],v,wartosc))
    return None
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
print(islands(G1,5,2))