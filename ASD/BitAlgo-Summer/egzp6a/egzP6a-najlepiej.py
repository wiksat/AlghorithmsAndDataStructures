from egzP6atesty import runtests
def partition(tab,p,r):
    x=tab[r][2]
    i=p-1
    for j in range(p,r):
        if tab[j][2]>=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1
def select(tab,p,r,k):
    if p==r:
        return tab[p]
    if p<r:
        q=partition(tab,p,r)
        if q==k:
            return tab[k]
        elif q<k:
            return select(tab,q+1,r,k)
        else:
            return select(tab,p,q-1,k)
def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    n=len(H)
    maxiLen=0
    for i, slowo in enumerate(H):
        w = len(slowo)
        maxiLen = max(maxiLen, w)
    buckets=[[] for _ in range(maxiLen+1)]
    for el in H:
        buckets[len(el)].append(el)

    summed=0
    goalID=0

    for i in range(maxiLen,-1,-1):
        summed+=len(buckets[i])
        if s <=summed:
            goalID=i
            break
    T=buckets[goalID]
    for i in range(len(T)):
        letters=0
        for letter in T[i]:
            if ord(letter) > 96 and ord(letter) < 123:
                letters += 1
        T[i]=(T[i],len(T[i]),letters)
    startIndex=0
    endIndex=len(T)-1
    searchIndex=s-(summed-len(T))-1
    select(T, startIndex, endIndex, searchIndex)
    print(T)
    return T[searchIndex][0]


runtests ( google, all_tests=True )