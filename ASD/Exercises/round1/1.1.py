# sortowania proste
# bubbleSort
def sort(tab):
    n=len(tab)
    for j in range(n):
        for i in range(n-1):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
    return tab



def sort2(tab):
    n=len(tab)
    for j in range(n):
        swapped=False
        for i in range(n-1-j):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
                swapped=True
        if not swapped:
            break
    return tab