"""
WIKTOR SATORA
Wybieram wszystkie możliwe pary wierzchołków (dwa fory) i tworze do nich krawędzie do superwierzchołka, który będzie tym ostatnim, do którego będzie zmierzał algorytm.
Później algorytmem Edmonda-Karpa przy wykorzystaniu algortmu BFS, korzystając z grafu w postaci macierzowej, oraz reprezentacji sąsiadów w postaci listowej wyznaczam
max przepływ, który porównuje z globalnym
Złożoność obliczeniowa to O(V^2*V*E^2)
"""
from zad9testy import runtests
import queue

def maxflow(G, s):
    # tu prosze wpisac wlasna implementacje
    maxi = 0
    kolej = queue.Queue()
    for i in G:
        maxi = max(maxi, i[0], i[1])
    t = maxi + 1
    globalmax = 0
    count = 0
    suma=0
    for i in G:
        if i[0]==s:
            suma+=i[2]
    for x in range(t):
        for y in range(x, t):
            if x != s and y != s and x != y:
                tab_sasiad = [[] for _ in range(t + 1)]
                for i in G:
                    tab_sasiad[i[0]].append(i[1])
                count += 1
                macierz = [[0 for _ in range(maxi + 2)] for _ in range(maxi + 2)]
                for i in G:
                    macierz[i[0]][i[1]] += i[2]
                macierz[x][maxi + 1] = 10**10
                macierz[y][maxi + 1] = 10**10
                tab_sasiad[x].append(maxi + 1)
                tab_sasiad[y].append(maxi + 1)
                f = 0
                while True:
                    parent = [-1 for _ in range(t + 1)]
                    flow = [float('inf') for _ in range(t + 1)]
                    parent[s] = -5
                    while not kolej.empty():
                        kolej.get()
                    kolej.put(s)
                    flag = 0
                    while not kolej.empty():
                        d = kolej.get()
                        for i in tab_sasiad[d]:
                            cp = macierz[d][i]
                            if cp <= 0:
                                continue
                            if parent[i] != -1: #taki visited
                                continue
                            parent[i] = d
                            flow[i] = min(flow[d], cp)
                            if i == t:
                                f += flow[t]
                                while s != i:
                                    d = parent[i]
                                    macierz[d][i] -= flow[t]
                                    if macierz[d][i]==0:
                                        tab_sasiad[d].pop(tab_sasiad[d].index(i))
                                    per=macierz[i][d]
                                    macierz[i][d] += flow[t]
                                    if per==0:
                                        tab_sasiad[i].append(d)
                                    i = d
                                flag = 1
                                break
                            kolej.put(i)
                        if flag == 1:
                            break
                    else:
                        break
                globalmax = max(globalmax, f)
                if globalmax==suma:
                    return globalmax
    return globalmax


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)