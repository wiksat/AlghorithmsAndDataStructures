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
def partition(tab,p,r,dane,mnoznik):
    x=dane[r]
    # y=dane[r][1]
    i=p-1
    for j in range(p,r):
        if dane[j]<=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
            dane[i], dane[j] = dane[j], dane[i]

    tab[i+1],tab[r]=tab[r],tab[i+1]
    dane[i + 1], dane[r] = dane[r], dane[i + 1]
    return i+1

def quickSort(tab,p,r,dane,mnoznik):
    if p<r:
        q=partition(tab,p,r,dane,mnoznik)
        quickSort(tab,p,q-1,dane,mnoznik)
        quickSort(tab,q+1,r,dane,mnoznik)
def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    n=len(H)
    dane=[0 for _ in range(n)]
    maxi=0
    for i,slowo in enumerate(H):
        litery=0
        for znak in slowo:
            if ord(znak)>96 and ord(znak)<123:
                litery+=1
        maxi=max(maxi,litery)

        # dane[i]=int(str(len(slowo))+str(litery))
        dane[i] = (len(slowo),litery)
        # print(len(slowo),litery,)
    # print(maxi)
    mnoznik=len(str(maxi))
    for i in range(n):
        dane[i]=(dane[i][0])*(10**mnoznik)+dane[i][1]
    # print(mnoznik)
    # mergeSort(H,dane)
    # print(H)
    quickSort(H,0,n-1,dane,mnoznik)
    # print(H)
    return H[n-s]


runtests ( google, all_tests=True )