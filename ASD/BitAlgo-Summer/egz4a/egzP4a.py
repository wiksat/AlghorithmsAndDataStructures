from egzP4atesty import runtests 
# def bstLewy():
def binSearchLeft(D,i,l,h):
    while l<=h:
        m=l+(h-l)//2
        if D[m]==i:
            return m
        elif D[m]>i:
            h=m-1
        elif D[m]<i:
            l=m+1
    return l
def mosty ( T ):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    T=sorted(T, key=lambda el: (el[0],el[1]))
    T2=[T[i][1] for i in range(n)]
    print(T,T2)
    # lis dynamicznie n^2

    # F=[1 for _ in range(n)]
    # maxi=0
    # for i in range(1,n):
    #     for j in range(i):
    #         if T2[i]>=T2[j]:
    #             F[i]=max(F[i],F[j]+1)
    #     if F[i]>maxi:
    #         maxi=F[i]



    # lis w n*lon(n)
    S=[]
    S.append(T2[0])
    for i in range(1,n):
        if T2[i]>=S[len(S)-1]:
            S.append(T2[i])
        else:
            S[binSearchLeft(S,T2[i],0,len(S)-1)]=T2[i]
    maxi=len(S)
    return maxi

runtests ( mosty, all_tests=True )