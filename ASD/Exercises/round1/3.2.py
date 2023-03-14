# Quicksort bez rekurencji
def partition(T,p,k):
    l=p-1
    for i in range(p,k):
        if T[i]<=T[k]:
            l+=1
            T[l],T[i]=T[i],T[l]
    T[l+1],T[k]=T[k],T[l+1]
    return l+1

def quicksort(T,p,k):
    tab=[]
    tab.append((p,k))
    while tab: #while len(T)>0:
        a,b=tab.pop()
        if (b-a)>1:
            q=partition(T, a,b)
            tab.append((a,q-1))
            tab.append((q+1,b))
#znajdowanie k-tego elementu w tablicy
def find_k(tab,k):
    left,right=0,len(tab)-1
    while left<right:
        q=partition(tab,left,right)
        if q>k:
            right=q
        else:
            left=q
    return tab[left]