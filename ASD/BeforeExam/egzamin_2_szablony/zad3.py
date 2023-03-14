from zad3testy import runtests


def lamps( n,T ):
    """tu prosze wpisac wlasna implementacje"""
    lampki=[0]*n
    maxblue=0
    blue = 0
    for i in range(len(T)):
        for j in range(T[i][0],T[i][1]+1):
            if lampki[j]==0:
                lampki[j]=1
            elif lampki[j]==1:
                lampki[j]=2
                blue+=1
            elif lampki[j]==2:
                lampki[j]=0
                blue-=1

        maxblue=max(maxblue,blue)
    return maxblue

    
runtests( lamps )


