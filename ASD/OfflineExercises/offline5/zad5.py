#WIKTOR SATORA
#Zadanie opiera się na algorytmie zachłannym, który wpisuje do kolejki priorytetowej możliwe zasięgi, a
#następnie wybiera największy z niech. O tyle dopisuje kolejne wartości (usuwa wykorzystany),
#a następnie znowy wybiera największy i tak w kółko, złożoność będzie O(n*log(n))
from zad5testy import runtests
from queue import PriorityQueue
def plan(T):
    kolejka=PriorityQueue()
    n=len(T)
    ile=0
    w=T[0]
    respond=[0]
    ind=0
    while ind<n-2:
        e=ind
        # while i<e+w+1:
        for i in range(1+e,e+w+1):
            if ind==n-2:
                return sorted(respond)
            kolejka.put((-T[i],ind+1))
            ind+=1
            i+=1
        ile+=1
        new=kolejka.get()
        w=-new[0]
        respond.append(new[1])
    return sorted(respond)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
