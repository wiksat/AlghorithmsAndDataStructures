#quicksort, pamięć O(logn)
def partition(T,p,k):
    l=p-1
    for i in range(p,k):
        if T[i]<=T[k]:
            l+=1
            T[l],T[i]=T[i],T[l]
    T[l+1],T[k]=T[k],T[l+1]
    return l+1

def quick_sort(T,p,k):
    if p<k:
        q=partition(T,p,k)
        quick_sort(T,p,q-1)
        quick_sort(T,q+1,k)

def quick_sort(T,p,k):
    while p<k:
        q=partition(T,p,k)
        quick_sort(T,p,q-1)
        p=q+1

def quick_sort(T,p,k):
    while p<k:
        q=partition(T,p,k)
        if (q-p)>(k-q):
            quick_sort(T,q+1,k)
            k=q-1
        else:
            quick_sort(T,p,q-1)
            p=q+1