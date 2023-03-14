from egzP9atesty import runtests

def ASD(T, p, Q, n):
    #Tutaj proszę wpisać własną implementację
    def update(index, ile):
        nonlocal T
        index //= 2
        while index != 0:
            tmp = T.get(index)
            T.set(index,tmp+ile)
            index //= 2

    def query(l,r,index,start,end):
        nonlocal T
        if l<=start and end <=r:
            return T.get(index)
        if r<start or end<l:
            return 0
        mid=(start+end)//2
        p1=query(l,r,2*index,start,mid)
        p2=query(l,r,2*index+1,mid+1,end)
        return p1+p2

    def getMid(s, e):
        return s + (e - s) // 2

    def getSumUtil( start, end, l, r, si):
        nonlocal T
        if (l <= start and end <= r):
            print("zwrot",start, end, l, r, si)
            return T.get(si)
        if (start > r or l>end  ):
            return 0
        mid = getMid(start, end)
        return getSumUtil(start, mid, l, r, 2 * si ) + getSumUtil(mid + 1, end, l, r, 2 * si + 1)
    dl=p//2
    dlQ=len(Q)
    suma=0
    for i in range(dlQ):
        if Q[i][0]==0:
            tmp=T.get(Q[i][1]+dl)
            T.set(Q[i][1]+dl,Q[i][2]+tmp)
            update(Q[i][1]+dl,Q[i][2])
        else:
            # print("new")
            suma+=query(Q[i][1], Q[i][2],1,0, int(n/2) - 1)
            # suma+=getSumUtil(0, int(n/2) - 1, Q[i][1], Q[i][2], 1);
    # print(T)
    return suma


#Podpowiedź. Format zadania jest dość nietypowy (także ze względu na sposób działania testów),
#w takiej formie żadne zadanie raczej nie powinno się pojawić na egzaminie. Zadanie ma na celu
#sprawdzenie zrozumienia struktury #### Drzewa Przedziałowego ####

runtests(ASD, all_tests = True)

