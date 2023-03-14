"""
WIKTOR SATORA
Najpierw sortuję tablicę w kolejności,
później uruchamiam funkcję rekurencyjną zwracającą minimalną ilość przesiadek,
gdy Marian przejechał minimalną ilość punktów kontrolnych
w zależności od parametów (i,o,z), i-kolejny punkt,
o-osoba kierunjąca, z-zapas do zmiany

"""

from kol2atesty import runtests

def drivers( P, B ):
    n = len(P)
    counter=1
    for i in P:
        if i[1]==True:
            counter+=1
    # print(counter)
    W=[]
    for i in range(n):
        W.append((P[i][0],P[i][1],i))
    W.sort()
    # print(W)
    przesiadkowe=[]
    for i in range(n):
        if W[i][1]==True:
            przesiadkowe.append(W[i])
    # print(przesiadkowe)
    c=[]
    c.append(0)
    t_sum=0
    for i in W:
        if i[1]==True:
            c.append(t_sum)
        else: t_sum+=1
    c.append(t_sum)
    # print(c)
    F=[[-1 for _ in range(2)] for _ in range(counter+1)]
    F[0][0]=99999999999999999
    F[0][1] = 0
    def rek(i,o):
        nonlocal P,B,W,F
        if i<0:
            return 0
        if F[i][o]!=-1:
            return F[i][o]
        d=0
        if i==1:
            if o==0:
                d = rek(i - 1, 1)
            if o==1:
                d = rek(i - 1, 0)+c[i]-c[i-1]
        if i==2:
            if o==0:
                d = min(rek(i - 1, 1), rek(i - 2, 1))
            if o==1:
                d = min(rek(i - 1, 0)+c[i]-c[i-1], rek(i - 2, 1)+c[i]-c[i-2])
        if i>2:
            if o==0:
                d = min(rek(i - 1, 1), rek(i - 2, 1), rek(i - 3, 1))
            if o==1:
                d = min(rek(i - 1, 0)+c[i]-c[i-1], rek(i - 2, 0)+c[i]-c[i-2], rek(i - 3, 0)+c[i]-c[i-3])
        F[i][o]=d
        return F[i][o]
    w1=rek(counter,1)
    print(F)
    w2=rek(counter,0)
    print(F)
    # w=min(w1,w2)
    if w1<w2:
        osoba=1
    else:
        osoba=0
    # print(przesiadkowe)
    i=counter
    res=[]
    while i>0:
        if osoba==0:
            d=99999999999999999999999
            t=0
            if rek(i - 1, 1)<d:
                d=rek(i - 1, 1)
                t=1
            if i>=2 and rek(i - 2, 1)<d:
                d = rek(i - 2, 1)
                t=2
            if i>2 and rek(i - 3, 1)<d:
                d = rek(i - 3, 1)
                t=3
            osoba=1
            if i - t - 1 < 0:
                break
            res.append(przesiadkowe[i-t-1][2])
            i=i-t
        if osoba==1:
            # d = min(rek(i - 1, 0) + c[i] - c[i - 1], rek(i - 2, 0) + c[i] - c[i - 2], rek(i - 3, 0) + c[i] - c[i - 3])
            d = 99999999999999999999999
            t = 0
            if rek(i - 1, 0)+ c[i] - c[i - 1]<d:
                d=rek(i - 1, 0)+ c[i] - c[i - 1]
                t=1
            if i>=2 and rek(i - 2, 0)+ c[i] - c[i - 2]<d:
                d = rek(i - 2, 0)+ c[i] - c[i - 2]
                t=2
            if i>2 and rek(i - 3, 0)+ c[i] - c[i - 3]<d:
                d = rek(i - 3, 0)+ c[i] - c[i - 3]
                t=3
            osoba=0
            if i - t - 1<0:
                break
            res.append(przesiadkowe[i-t-1][2])
            i=i-t
    # print(res)
    res.reverse()
    # print(res)





    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )