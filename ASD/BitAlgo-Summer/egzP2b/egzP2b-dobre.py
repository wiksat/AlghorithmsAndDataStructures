import bisect

from egzP2btesty import runtests
from math import log10
def binSearchLeft(D,i,l,h):
    while l<=h:
        m=l+(h-l)//2
        if D[m]==i:
            return m
        elif D[m]>i:
            h=m-1
        elif D[m]<i:
            l=m+1
    return l
def binSearchRight(D,i,l,h):
    while l<=h:
        m=l+(h-l)//2
        if D[m]==i:
            return m
        if D[m]>i:
            h=m-1
        elif D[m]<i:
            l=m+1
    return h+1
def radixSort(tab,x):
    if x==-1:
        return tab
    it=x
    output_0=[]
    output_1=[]
    for i in tab:
        if len(i)<=it:
            output_0=[i]+output_0
        elif i[it]=="0":
            output_0.append(i)
        else:
            output_1.append(i)
    return radixSort(output_0+output_1,x-1)

def kryptograf( D, Q ):
    #tutaj proszę wpisać własną implementację
    maxi=0
    for i in range(len(D)):
        D[i]=D[i][::-1]
        maxi=max(maxi,len(D[i]))
    for i in range(len(Q)):
        Q[i]=Q[i][::-1]
    print(D)
    # sortowanie radixsort
    D=radixSort(D,maxi)
    print(D)
    print(sorted(D))
    output=0
    for i in Q:
        low=binSearchLeft(D,i,0,len(D)-1)
        high=binSearchRight(D,i+"2",0,len(D)-1)
        output+=log10(high-low)

    return output

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 0)