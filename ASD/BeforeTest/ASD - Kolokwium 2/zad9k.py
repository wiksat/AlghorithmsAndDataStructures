from zad9ktesty import runtests
from math import inf

def rek(P,F,i,l1,l2):
    if i>len(P)-1:
        return 0
    if F[i][l1][l2]!=-1:
        return F[i][l1][l2]
    if P[i]>l1 and P[i]>l2:
        F[i][l1][l2]=0
        return 0
    if P[i]>l1:
        F[i][l1][l2]=rek(P,F,i+1,l1,l2-P[i])+1
    elif P[i]>l2:
        F[i][l1][l2]=rek(P,F,i+1,l1-P[i],l2)+1
    else:
        F[i][l1][l2]=max(rek(P,F,i+1,l1,l2-P[i]),rek(P,F,i+1,l1-P[i],l2))+1
    return F[i][l1][l2]

def prom(P, g, d):
    n=len(P)
    F=[[[-1 for i in range(d+1)] for i in range(g+1)] for i in range(n)]
    w=rek(P,F,0,g,d)
    # print(F)
    i=0
    l1=g
    l2=d
    sol=[]
    sol2=[]
    while i<len(P) and (l1>=P[i] or l2>=P[i]):
        if P[i]>l1:
            w1=0
            w2=1
        elif P[i]>l2:
            w1=1
            w2=0
        else:
            w1=rek(P,F,i+1,l1-P[i],l2)
            w2 = rek(P, F, i + 1, l1, l2 - P[i])
        if w1>w2:
            sol.append(i)
            l1=l1-P[i]
        else:
            sol2.append(i)
            l2=l2-P[i]
        i+=1
    if w-1 in sol:
        return sol
    else:
        return sol2
    # return []

runtests ( prom )