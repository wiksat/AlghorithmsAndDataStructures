#WIKTOR SATORA
#Najpierw tworzę n/4 pustych bucketów, później dodaję kolejne elementy z tablicy do odpowiednich bucketów.
#Następnie sortuje InsertSortem i QuickSortem w zależności od ilości elementów w kubełku
#Na koniec dodaję elementy do nowej tablicy i ją returnuje
#Złożoność algorytu to O(n), a pamięciowa także O(n)
from zad3testy import runtests
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def quick_sort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
def SortTab(T,P):
    n=int(len(T)/4)
    if n==0:
        n=1
    buckets=[[]for _ in range(n)]
    for num in T:
        # w=int(num / 4)
        # if w != n:
        #     buckets[w].append(num)
        # else:
        #     buckets[w-1].append(num)
        buckets[int(num/4)-1].append(num)
    res=[]
    for x in buckets:
        dl=len(x)
        # print(dl)
        if (dl == 1):
            res.append(x[0])
        elif(dl>0 and dl<=40):
            #INSERTSORT
            for i in range(1,dl):
                el=x[i]
                j=i-1
                while j>=0 and el<x[j]:
                    x[j+1]=x[j]
                    j-=1
                x[j+1]=el
            for w in x:
                res.append(w)
        elif(dl>40):
            #QUICKSORT
            quick_sort(x, 0, dl - 1)
            for w in x:
                res.append(w)
    return res
    pass

# T = [1.1,3,2.2]
# P = [(4, 8, 0.75) , (1, 5, 0.25)]
# print(SortTab(T,P))
runtests( SortTab )