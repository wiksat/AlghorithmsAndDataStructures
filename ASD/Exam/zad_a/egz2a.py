"""
WIKTOR SATORA 411502
ALgorytm jest w O(n^2)
Idąc kolejno po dostawach węgla i kolejno po magazynach wybieram ten pierwszy gdzie sie da umieścić węgiel.
Gdy sie nie da dodaje na koncu nowy magazyn
"""
from egz2atesty import runtests

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    n=len(A)
    magazyny=[]
    magazyny.append(0)
    iloscMag=1
    last=-1
    for i in range(n):
        flaga=0
        for j in range(iloscMag):
            if magazyny[j]+A[i]<=T:
                magazyny[j]+=A[i]
                flaga=1
                last=j
                break
        if flaga==0:
            magazyny.append(A[i])
            iloscMag += 1
            last=iloscMag-1

    return last

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
