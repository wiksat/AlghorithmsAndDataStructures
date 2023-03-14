from zad5ktesty import runtests

def garek ( A ):
    #Tutaj proszę wpisać własną implementację
    n=len(A)
    F=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i]=A[i]
    for l in range(1,n):
        for i in range(n-l):
            j=i+l
            if i+2<n and j-2>=0:
                F[i][j]=max(A[i]+min(F[i+2][j],F[i+1][j-1]),A[j]+min(F[i+1][j-1],F[i][j-2]))
            elif i+2<n and j-1>=0:
                F[i][j]=max(A[i]+min(F[i+2][j],F[i+1][j-1]),A[j])
            elif i+1<n and j-2>=0:
                F[i][j]=max(A[i],A[j]+min(F[i+1][j-1],F[i][j-2]))
            # print(i,j)
    #
    # for el in F:
    #     print(el)
    return F[0][n-1]

runtests ( garek )