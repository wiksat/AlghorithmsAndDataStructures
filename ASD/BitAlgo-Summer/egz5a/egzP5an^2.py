from egzP5atesty import runtests 
# dynamik
def inwestor ( T ):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    F=[[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i]=T[i]
    maxi=0
    for l in range(1,n):
        for i in range(n-l):
            j=i+l
            F[i][j]=min(F[i+1][j],T[i],F[i][j-1],T[j])
            maxi=max(maxi,F[i][j]*(j-i+1))
    # for i in F:
    #     print(i)
    return maxi

runtests ( inwestor, all_tests=True )