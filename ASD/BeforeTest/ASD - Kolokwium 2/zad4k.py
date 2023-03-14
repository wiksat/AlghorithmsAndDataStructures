from zad4ktesty import runtests

def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    F=[[9999 for _ in range(n)] for _ in range(n)]
    F[0][0]=T[0][0]
    for i in range(1,n):
        F[0][i]=F[0][i-1]+T[0][i]
        F[i][0]=F[i-1][0]+T[i][0]
    for i in range(1,n):
        for j in range(1,n):
            F[i][j]=min(F[i-1][j],F[i][j-1])+T[i][j]
    # print(F)
    return F[n-1][n-1]

runtests ( falisz )
