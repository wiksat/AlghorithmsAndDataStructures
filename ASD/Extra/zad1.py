def setBorder(tab, start, pivot, n):
    border = start

    for i in range(start, pivot):
        if tab[i//n][i % n] < tab[pivot//n][pivot % n]:
            tab[border//n][border % n], tab[i//n][i % n] = tab[i//n][i % n], tab[border // n][border % n]
            border += 1
    tab[border // n][border % n], tab[pivot//n][pivot % n] = tab[pivot//n][pivot % n], tab[border // n][border % n]
    return border

def quickSort(tab, start, end, n):
    while start < end:
        border = setBorder(tab, start, end, n)
        quickSort(tab, start, border - 1, n)
        start = border + 1

def Median(T):
    n = len(T)
    quickSort(T, 0, n * n - 1, n)
    print(T)
    toReturn = []
    interval = int((n * n - n) / 2)
    # print(interval)
    left_id = 0
    middle_id = interval
    right_id = interval + n

    for i in range(n):
        tab = []
        for j in range(n):
            if i > j:
                tab.append(T[left_id // n][left_id % n])
                left_id += 1
            elif i == j:
                tab.append(T[middle_id // n][middle_id % n])
                middle_id += 1
            else:
                tab.append(T[right_id // n][right_id % n])
                right_id += 1
        print(tab)
        toReturn.append(tab)

    return toReturn

T=[[2,6,3,8],[88,5,2,9],[55,67,7,3],[11,32,23,35]]
Median(T)