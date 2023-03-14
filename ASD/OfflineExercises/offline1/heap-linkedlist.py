def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2
class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
    print()
def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q
    return p
def heapify(A,n,i):
    l=left(i)
    r=right(i)
    min_ind=i
    if l<n and A[l].val<A[min_ind].val:
        min_ind=l
    if r<n and A[r].val<A[min_ind].val:
        min_ind=r
    if min_ind!=i:
        A[i],A[min_ind]=A[min_ind],A[i]
        heapify(A,n,min_ind)
def build_heap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)


# def SortH(p,k):
#     # tu prosze wpisac wlasna implementacje
#     current=p
#     A=[]
#     for i in range(0,k+1):
#         if current is not None:
#             A.append(current)
#             current=current.next
#
#     build_heap(A)
#     pierw=A[0]
#     zwrot=pierw
#     while current is not None:
#         # print("pop", A[0].val)
#         A.pop(0)
#         A.append(current)
#         current=current.next
#         build_heap(A)
#         pierw.next=A[0]
#         pierw=pierw.next
#
#     A.pop(0)
#     build_heap(A)
#     for i in range(len(A) - 1, 0, -1):
#         pierw.next = A[0]
#         A[0],A[i]=A[i],A[0]
#         pierw = pierw.next
#         # A.pop(0)
#         heapify(A,i,0)
#     pierw.next = A[0]
#     pierw = pierw.next
#     pierw.next=None
#
#     return zwrot
#     pass


def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    current=p
    A=[]
    for i in range(0,k+1):
        if current is not None:
            A.append(current)
            current=current.next

    build_heap(A)
    pierw=A[0]
    zwrot=pierw
    while current is not None:
        A[0]=current
        current=current.next
        heapify(A,k+1,0)
        pierw.next=A[0]
        pierw=pierw.next
    dl=len(A)
    A[0],A[dl-1]=A[dl-1],A[0]
    build_heap(A)
    for i in range(dl - 1, 0, -1):
        pierw.next = A[0]
        A[0],A[i]=A[i],A[0]
        pierw = pierw.next
        heapify(A,i,0)
    pierw.next = A[0]
    pierw = pierw.next
    pierw.next=None

    return zwrot
    pass


tab=[4,1,3,2,7,9,6,5]
# tab=[9,3,4,2,5,7,6,1]
# selSort(tab,2)
print(tab)
lista=tab2list(tab)
print_node(lista)
print()
lista=SortH(lista,3)
print_node(lista)