from zad3ktesty import runtests

def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    F=[9999 for _ in range(n)]
    for i in range(k):
        F[i]=T[i]
    for i in range(k,n):
        mini=9999999999999999
        for j in range(i-k,i):
            mini=min(mini,F[j])
        F[i]=mini+T[i]
    mini = 99999999999999
    for j in range(n-k,n):
        mini=min(mini,F[j])
    # print(F)
    return mini

runtests ( ksuma )
# T=[1, 2, 3, 4, 6, 15, 8, 7]
# k=4
# print(ksuma(T,k))