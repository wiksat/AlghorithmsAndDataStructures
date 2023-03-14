def partition(tab,p,r):
    x=tab[r]
    i=p-1
    for j in range(p,r):
        if tab[j]<=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1

def quickSort(tab,p,r):
    if p<r:
        q=partition(tab,p,r)
        quickSort(tab,p,q-1)
        quickSort(tab,q+1,r)
tab=[3,6,2,6,4,44,7,1]
quickSort(tab,0,len(tab)-1)
print(tab)