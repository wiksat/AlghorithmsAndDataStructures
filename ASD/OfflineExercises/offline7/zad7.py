"""
WIKTOR SATORA
Algorytm poszukuje rekurencyjnie cyklu hamiltona począwszy od zerowego wierzchołka.
Przy każdym wywołaniu rekurencji sprawdzamy którą bramą weszliśmy i wychodzimy tą drugą.
Sprawdzamy możliwość odwiedzenia wierzchołków używając tablicy visited oraz gdy nie znajdziemy cyklu,
cofamy visited.
Złożoność obliczeniowa to prawdopodobnie O(v!)
"""
from zad7testy import runtests

def droga( G ):
    # tu prosze wpisac wlasna implementacje
    n=len(G)
    visited=[False for _ in range(n)]
    tab=[]
    # counter=0
    def rek(v,tab,counter,poczatek,prev,visited):
        nonlocal n,G
        counter+=1
        visited[v]=True
        tab.append(v)
        if poczatek==1:
            for i in G[v][0]:
                zm = rek(i, tab, counter, 0, v, visited)
                if zm[0]:
                    return zm
        elif prev in G[v][0]:
            for i in G[v][1]:
                if i==0 and counter==n:
                    return True,tab
                if visited[i]==False:
                    zm=rek(i,tab,counter,0,v,visited)
                    if zm[0]:
                        return zm
        elif prev in G[v][1]:
            for i in G[v][0]:
                if i==0 and counter==n:
                    return True,tab
                if visited[i]==False:
                    zm=rek(i,tab,counter,0,v,visited)
                    if zm[0]:
                        return zm
        counter-=1
        tab.pop()
        visited[v]=False
        return False,[]
    w=rek(0,tab,0,1,None,visited)
    if w[0]==True:
        return w[1]
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )