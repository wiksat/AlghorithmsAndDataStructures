def insertionSort(tab,l,r):
    dl=len(tab)
    for i in range(l+1,r+1):
        klucz=tab[i]
        j=i-1
        while j>=0 and klucz<tab[j]:
            tab[j+1],tab[j]=tab[j],tab[j+1]
            j-=1
        tab[j+1]=klucz
def partition(tab,p,r):
    x=tab[r]
    i=p-1
    for j in range(p,r):
        if tab[j]<=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1
def select_five(L, left, right, k):
    # 1. Jeżeli jest mało elementów, to sortuj.
    # p powinno być co najmniej 5, aby ustawiło się i > 0.
    p = 5   # może być kilkadziesiąt
    if (right-left+1) < p:
        insertionSort(L, left, right)
        return left+k-1   # zwracam indeks
    # 2. Podziel listę na 5-elementowe podzbiory, najwyżej jeden 4-elementowy.
    # 3. Posortuj podzbiory.
    left2 = left
    right2 = left + 4
    i = left   # pierwszy wolny
    while right2 <= right:
        insertionSort(L, left2, right2)
        print(left2,right2,L)
        # Przerzucamy mediany na początek tablicy.
        # swap(L, i, left2+2)
        L[i], L[left2 + 2] = L[left2 + 2], L[i]
        i += 1
        left2 += 5
        right2 += 5
    # Tu można posortować zbiory mniej niż 5-elementowe.
    if right2 == right+1 or right2 == right+2:
        insertionSort(L, left2, right)
        # swap(L, i, left2+1)
        L[i], L[left2+1] = L[left2+1], L[i]
        i += 1
    # 5. Wyznaczamy medianę median rekurencyjnie.
    median_idx = select_five(L, left, i-1, (i-left+1) // 2)

    L[median_idx],L[right]=L[right],L[median_idx]

    if left==right:
        return L[left]
    pivot = partition(L, left, right)
    if k == pivot:
        return L[pivot]   # zwracam indeks
    elif pivot < k:
        return select_five(L, pivot+1, right, k)
    else:
        return select_five(L, left, pivot-1, k)
# tab=[3,6,2,6,4,44,7,1]
tab=[3,6,2,6,4,44,7,1,76,4365,76,437,6,5,2,2,365,88,0,65,45]
# print(len(tab)-1)
print(select_five(tab,0,len(tab)-1,8))