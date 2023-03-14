from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    n=len(L)
    seconds=[60,40,30]
    moves=[(1,0),(0,1),(-1,0),(0,-1)]
    F=[[[[-1 for _ in range(3)]for _ in range(4)]for _ in range(len(L[0]))]for _ in range(n)]
    kolej=PriorityQueue()
    kolej.put((0,A[0],A[1],0,0))
    while not kolej.empty():
        time,x,y,direction,ile=kolej.get()
        if (x,y)==B:
            return time
        if F[y][x][direction][ile]!=-1 or L[y][x]=="X":
            continue
        F[y][x][direction][ile]=time
        kolej.put((time+45,x,y,(direction+1)%4,0))
        kolej.put((time+45,x,y,(direction+3)%4,0))
        x+=moves[direction][0]
        y+=moves[direction][1]
        kolej.put((time+seconds[ile],x,y,direction,min(ile+1,2)))
    # return 0


runtests( robot )


