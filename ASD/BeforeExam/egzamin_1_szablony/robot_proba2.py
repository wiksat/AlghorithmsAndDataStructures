from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    n=len(L)
    d=[[[10**10 for _ in range(4)] for _ in range(4)] for _ in range(n)]
    print(d)
    # return 0


runtests( robot )


