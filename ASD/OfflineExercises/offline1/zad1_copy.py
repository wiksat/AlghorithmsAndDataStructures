#WIKTOR SATORA
#Program opiera się na sortowaniu SelectSort w zastosowaniu do list odsyłaczowych
#Złożoność obliczeniowa dla:
# k = Θ(1) to n
# k = Θ(log n) to n*log(n)
# k = Θ(n) to n^2
from zad1testy import Node, runtests

def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

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
#     while current is not None:
#         A.append(current)
#         current=current.next
#     build_heap(A)
#     n = len(A)
#     p = None
#     for i in range(n - 1, 0, -1):
#         if i == n - 1:
#             A[0].next = None
#         else:
#             A[0].next = p
#         p = A[0]
#         A[0], A[i] = A[i], A[0]
#         heapify(A, i, 0)
#     A[0].next = p
#     p = A[0]
#     # current = p
#     # while current is not None:
#     #     print(current.val, "-->", end="")
#     #     current = current.next
#     return p
#     pass

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
#         A[0]=current
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
#         heapify(A,i,0)
#     pierw.next = A[0]
#     pierw = pierw.next
#     pierw.next=None
#
#     return zwrot
#     pass


# def SortH(p,k):
#     if k==1:
#         q=p
#         while p.next.next is not None:
#             if p.val > p.next.val:
#                 p.val,p.next.val=p.next.val,p.val
#             p=p.next
#         return q
#     e = p
#     prev_minim = None
#     prev_p = None
#     f = 0
#     while p is not None:
#         w = p
#         minim = p
#         wyn = 0
#         flag = 0
#         for n in range(1, 1 + k):
#             if w.next is not None:
#                 s = w
#                 w = w.next
#                 if minim.val > w.val:
#                     prev_minim = s
#                     minim = w
#                     wyn = n
#                     flag = 1
#
#         if flag == 1:
#             if wyn != 1:
#                 # print_node(e)
#                 copy_min_next = minim.next
#                 minim.next = p.next
#                 p.next = copy_min_next
#                 # print(copy_min_next.val)
#                 if prev_minim is not None:
#                     prev_minim.next = p
#                 if prev_p is not None:
#                     prev_p.next = minim
#                 # print_node(e)
#             else:
#                 copy_min_next = minim.next
#                 p.next = copy_min_next
#                 if prev_p is not None:
#                     prev_p.next = minim
#                 minim.next = p
#         p = minim
#
#         if f == 0:
#             e = p
#         prev_p = p
#         p = p.next
#         f = 1
#     return e
#     pass




runtests( SortH ) 
