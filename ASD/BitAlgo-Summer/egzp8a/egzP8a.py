from egzP8atesty import runtests
def binSearchRight(D,i,l,h):
    while l<=h:
        m=l+(h-l)//2
        if D[m]==i:
            return m
        if D[m]>i:
            h=m-1
        elif D[m]<i:
            l=m+1
    return h+1
def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if hi is None:
        hi = len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    return lo
def bisect_right(a, x, lo=0, hi=None, *, key=None):
    if hi is None:
        hi = len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            # if x < a[mid]:
            if a[mid] <= x:
                # hi = mid
                lo = mid + 1
            else:
                # lo = mid + 1
                hi = mid
    return lo
def reklamy ( T, S, o ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], S[i])
    T = sorted(T, key=lambda x: x[0])
    BEST_RIGHT=[0 for _ in range(n)]
    BEST_RIGHT[n-1]=T[n-1][2]
    for i in range(n-2,-1,-1):
        BEST_RIGHT[i]=max(T[i][2],BEST_RIGHT[i+1]) #wartość najlepszego przedziału od prawej strony do obecnego
    STARTS=[i[0] for i in T]
    result=0
    for i in range(n):
        end=T[i][1]
        idx=bisect_right(STARTS,end,i+1)
        second=0
        if idx<n and STARTS[idx]!=end:
            second=BEST_RIGHT[idx]
        result=max(result,T[i][2]+second)
    return result

runtests ( reklamy, all_tests=True )