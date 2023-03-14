def countingSort(a,k):
    n=len(a)
    b=[0]*n
    c=[0]*k
    for x in a:
        c[x]+=1
    for i in range(1,k):
        c[i]=c[i]+c[i-1]
    for i in range(n-1,-1,-1):
        b[c[a[i]]-1]=a[i]
        c[a[i]]-=1
    for i in range(n):
        a[i]=b[i]
tab=[3,6,2,6,4,7,1]
countingSort(tab,8)
print(tab)