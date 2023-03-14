from egzP6atesty import runtests
def mergeSort(array,tablicaKlucz):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]
        Lklucz=tablicaKlucz[:r]
        Mklucz=tablicaKlucz[r:]
        mergeSort(L,Lklucz)
        mergeSort(M,Mklucz)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if Lklucz[i] < Mklucz[j]:
                array[k] = L[i]
                tablicaKlucz[k] = Lklucz[i]
                i += 1
            else:
                array[k] = M[j]
                tablicaKlucz[k] = Mklucz[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            tablicaKlucz[k] = Lklucz[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            tablicaKlucz[k] = Mklucz[j]
            j += 1
            k += 1
def partition(tab,p,r,dane):
    x=dane[r][0]
    y=dane[r][1]
    i=p-1
    for j in range(p,r):
        if dane[j][0]<x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
            dane[i], dane[j] = dane[j], dane[i]
        if dane[j][0]==x:
            if dane[j][1]<=y:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
                dane[i], dane[j] = dane[j], dane[i]

    tab[i+1],tab[r]=tab[r],tab[i+1]
    dane[i + 1], dane[r] = dane[r], dane[i + 1]
    return i+1

def quickSort(tab,p,r,dane):
    if p<r:
        q=partition(tab,p,r,dane)
        quickSort(tab,p,q-1,dane)
        quickSort(tab,q+1,r,dane)
def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    n=len(H)
    dane=[0 for _ in range(n)]
    for i,slowo in enumerate(H):
        litery=0
        for znak in slowo:
            if ord(znak)>96 and ord(znak)<123:
                litery+=1

        # dane[i]=int(str(len(slowo))+str(litery))
        dane[i] = (len(slowo),litery)

    # mergeSort(H,dane)
    quickSort(H,0,n-1,dane)
    return H[n-s]


runtests ( google, all_tests=True )