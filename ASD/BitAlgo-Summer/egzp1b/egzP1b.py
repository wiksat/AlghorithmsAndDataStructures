from egzP1btesty import runtests 
from math import inf
from queue import PriorityQueue
def turysta( G, D, L ):
    #tutaj proszę wpisać własną implementację
    maxW=0
    for x,y,z in G:
        maxW=max(maxW,x,y)
    n=maxW+1
    graf=[[] for _ in range(n)]
    for x,y,z in G:
        graf[x].append((y,z))
        graf[y].append((x,z))

    distance = [[inf] * 5 for _ in range(n)]

    kolej = PriorityQueue()
    distance[D][4]=0
    kolej.put((0,D,4))
    while not kolej.empty():
        odl,wierzch,ile=kolej.get()
        if ile!=0:
            for v in graf[wierzch]:
                if ile-1>=0 and distance[v[0]][ile-1]>odl+v[1]:
                    distance[v[0]][ile-1]=odl+v[1]
                    kolej.put((distance[v[0]][ile- 1], v[0], ile - 1))

    return distance[L][0]

runtests ( turysta )