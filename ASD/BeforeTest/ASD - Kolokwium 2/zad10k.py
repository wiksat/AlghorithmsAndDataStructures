import math

from zad10ktesty import runtests
def rek(N,F):
    if N<=0:
        return 0
    if F[N]!=0:
        return F[N]
    mini=9999999999999
    for q in range(1,int(math.sqrt(N))+1):
        d=rek(N-(q*q),F)+1
        mini=min(mini,d)
    F[N]=mini
    return F[N]

def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    F=[0 for _ in range(N+1)]
    w=rek(N,F)
    print(w)
    a=N
    res=[]
    while a>0:
        mini=999999999999999
        tmp=9999999999999999
        tmp2 = 9999999999999999
        for q in range(1, int(math.sqrt(a)) + 1):
            d = rek(a - (q * q), F)
            if d<mini:
                mini=d
                tmp2=q
                tmp=a - (q * q)
        res.append(tmp2)
        a=tmp
    print(F)
    return res


runtests( dywany )

