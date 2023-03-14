#WIKTOR SATORA
#Algorytm najpierw sortuje przedziały wielkością (od największych do najmniejszych) heapsortem.
#Później przechodząc po tablicy porównuje przedziały, bierze jeden i porównuje z kolejnymi
#Jeśli kolejny nie mieści się w poprzednim zmienia nowy na bierzący i sprawdza poprzednie
#Złożoność obliczeniowa na heapsorta to O(n*log(n)),
#a porównywanie przedziałów optymistycznie n, średnio n*log(n), a w najgorszym przypadku n*n
from zad2testy import runtests

def heapify(A,n,i):
    l=2*i+1
    r=2*i+2
    max_ind=i
    w=A[max_ind][1]-A[max_ind][0]
    if l<n and A[l][1]-A[l][0]<w:
        max_ind=l
    if r<n and A[r][1]-A[r][0]<w:
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,n,max_ind)
def build_heap(A,n):
    for i in range((n-2)//2,-1,-1):
        heapify(A,n,i)
def heap_sort(A,n):
    build_heap(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)

def partition(A,p,r):
    x = A[r][1]-A[r][0]
    i=p-1
    for j in range(p,r):
        # if A[j]<=x:
        if A[j][1]-A[j][0] >= x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def quick_sort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

def depth(L):
    # print(L)
    # quick_sort(L,0,len(L)-1)
    heap_sort(L,len(L))
    # print(L)
    tab=[]
    counter=[]
    tab.append(L[0])
    counter.append(0)
    for l in range(1,len(L)):
        flag = 0
        for a in range(len(tab)):
            if L[l][0]>=tab[a][0] and L[l][1]<=tab[a][1]:
                counter[a]+=1
                flag=1
        if flag==0:
            tab.append(L[l])
            counter.append(0)
    return max(counter)
    pass

#porównanie z wszystko ze waszystkim
# def depth(L):
#     countMax=0
#     for l in range(len(L)):
#         new=0
#         for y in range(len(L)):
#             if L[l][0] <= L[y][0] and L[l][1] >= L[y][1]:
#                 new+=1
#         if countMax<new:
#             countMax=new
#     return countMax-1
#     pass

runtests( depth )
