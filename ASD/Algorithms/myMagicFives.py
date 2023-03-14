def insertionSort(tab, l, r):
    dl = len(tab)
    for i in range(l + 1, r + 1):
        klucz = tab[i]
        j = i - 1
        while j >= 0 and klucz < tab[j]:
            tab[j + 1], tab[j] = tab[j], tab[j + 1]
            j -= 1
        tab[j + 1] = klucz

# It searches for x in arr[l..r],
# and partitions the array around x.
def partition(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            arr[i],arr[r]=arr[r],arr[i]
            break

    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1
def findMedian(arr, l, n):
    lis = []
    for i in range(l, l + n):
        lis.append(arr[i])
    insertionSort(lis,0,len(lis)-1)
    return lis[n // 2]

def magic(tab,l,r,k):
    n = r - l + 1
    median = []
    i = 0
    while (i < n // 5):
        median.append(findMedian(tab, l + i * 5, 5))
        i += 1
    if (i * 5 < n):
        median.append(findMedian(tab, l + i * 5,n % 5))
        i += 1
    # print("median",l,r, median)
    if i == 1:
        medOfMed = median[i - 1]
    else:
        medOfMed = magic(median, 0,i - 1, i // 2)
    if l==r:
        return tab[l]
    if l<r:
        q=partition(tab,l,r,medOfMed)
        if q==k:
            return tab[k]
        elif q<k:
            return magic(tab,q+1,r,k)
        else:
            return magic(tab,l,q-1,k)

tab=[3,6,2,6,4,44,7,1,76,4365,76,437,6,5,2,2,365,88,0,65,45]
print(magic(tab,0,len(tab)-1,20))