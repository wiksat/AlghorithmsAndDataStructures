def insertionSort(tab):
    dl=len(tab)
    for i in range(1,dl):
        klucz=tab[i]
        j=i-1
        while j>=0 and klucz<tab[j]:
            tab[j+1],tab[j]=tab[j],tab[j+1]
            j-=1
        tab[j+1]=klucz
# tab=[3,6,2,6,4,44,7,1]
tab=[3,6,2,6,4,44,7,1,76,4365,76,437,6,5,2,2,365,88,0,65,45]
insertionSort(tab)
print(tab)

# def insertionSort(tab,l,r):
#     dl=len(tab)
#     for i in range(l+1,r+1):
#         klucz=tab[i]
#         j=i-1
#         while j>=0 and klucz<tab[j]:
#             tab[j+1],tab[j]=tab[j],tab[j+1]
#             j-=1
#         tab[j+1]=klucz
