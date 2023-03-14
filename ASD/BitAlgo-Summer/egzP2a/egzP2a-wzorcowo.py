from egzP2atesty import runtests
def partition(tab,p,r,indeksy):
    x=tab[indeksy[r]][1]
    i=p-1
    for j in range(p,r):
        if tab[indeksy[j]][1]>=x:
            i+=1
            tab[indeksy[i]],tab[indeksy[j]]=tab[indeksy[j]],tab[indeksy[i]]
    tab[indeksy[i+1]],tab[indeksy[r]]=tab[indeksy[r]],tab[indeksy[i+1]]
    return i+1
def select(tab,p,r,k,indeksy):
    if p<r:
        q=partition(tab,p,r,indeksy)
        if q<k:
            select(tab,q+1,r,k,indeksy)
        else:
            select(tab,p,q-1,k,indeksy)
def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    indeksy=[0 for _ in range(n)]
    starts=[0 for _ in range(m)]
    ends=[0 for _ in range(m)]
    items=0
    width=m+k-1
    currEnd=-1
    for i in range(m):
        starts[i]=currEnd+1
        currEnd+=width
        ends[i]=currEnd
        width-=1
    kolumna=0
    rzad=0
    while items<n:
        if starts[rzad]+kolumna<=ends[rzad]:
            indeksy[starts[rzad]+kolumna]=items
            items+=1
        rzad+=1
        if rzad>=m:
            rzad=0
            kolumna+=1

    lastEnd=ends[m-1]
    for i in range(m-2,-1,-1):
        select(T,0,lastEnd,ends[i],indeksy)
        lastEnd=ends[i]-1
    return None


runtests ( zdjecie, all_tests=False )