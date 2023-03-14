def partition(tab,p,r):
    x=tab[r]
    i=p-1
    for j in range(p,r):
        if tab[j]<=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1
def select(tab,p,r,k):
    if p==r:
        return tab[p]
    if p<r:
        q=partition(tab,p,r)
        if q==k:
            return tab[k]
        elif q<k:
            return select(tab,q+1,r,k)
        else:
            return select(tab,p,q-1,k)
def Median(T):
    n = len(T)
    new=[]
    for i in range(n):
        for j in range(n):
            new.append(T[i][j])
    uno=int((n*n-n)/2)
    select(new,0,len(new)-1,uno)
    secundo = int((n * n + n) / 2)
    select(new,0,len(new)-1,secundo)
    res=[]
    left_id = 0
    middle_id = uno
    right_id = secundo
    for i in range(n):
        tab=[]
        for j in range(n):
            if i > j:
                tab.append(new[left_id])
                left_id += 1
            elif i == j:
                tab.append(new[middle_id])
                middle_id += 1
            else:
                tab.append(new[right_id])
                right_id += 1
        # print(tab)
        res.append(tab)
    print()
    for i in res:
        print(i)


    return []

T=[[2,6,3,8],
   [88,5,2,9],
   [55,67,7,3],
   [11,32,23,35]]
Median(T)