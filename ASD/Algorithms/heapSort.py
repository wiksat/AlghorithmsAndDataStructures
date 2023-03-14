def heapify_max(tab,n,i):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and tab[l]>tab[max_ind]:
        max_ind=l
    if r<n and tab[r]>tab[max_ind]:
        max_ind=r
    if i!=max_ind:
        tab[max_ind],tab[i]=tab[i],tab[max_ind]
        heapify_max(tab,n,max_ind)
def heapify_min(tab,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < n and tab[l] < tab[max_ind]:
        max_ind = l
    if r < n and tab[r] < tab[max_ind]:
        max_ind = r
    if i != max_ind:
        tab[max_ind], tab[i] = tab[i], tab[max_ind]
        heapify_min(tab, n, max_ind)
#jest juz ddane na ostatnim elemencie tablicy
def heapify_max_wypychanie(tab,n,i):
    parent=(i-1)//2
    max_ind=i
    if parent>=0 and tab[parent]<tab[max_ind]:
        max_ind=parent
    if i!=max_ind:
        tab[max_ind], tab[i] = tab[i], tab[max_ind]
        heapify_max_wypychanie(tab,n,max_ind)

def build_heap(tab):
    n=len(tab)
    for i in range((n-2)//2,-1,-1):
        heapify_max(tab,n,i)
def heap_sort(A):
    n=len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify_max(A,i,0)

tab=[3,6,2,6,4,44,7,1]
# build_heap(tab)
heap_sort(tab)
print(tab)
# tab.append(380)
# print(tab)
# heapify_max_wypychanie(tab,9,8)
# print(tab)