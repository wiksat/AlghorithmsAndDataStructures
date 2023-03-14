def partition(tab,p,r):
    x=tab[r]
    i=p-1
    for j in range(p,r):
        if tab[j]<=x:
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
tab=[3,6,2,6,4,44,7,1,76,4365,76,437,6,5,2,2,365,88,0,65,45]
print(select(tab,0,len(tab)-1,20))