"""
wydawanie monet

f(i,c)={Njamniejsza liczba monet o nominałach spośród M[0],....,M[i]
        przy pomocy któych możńa wydać kwotę C}

f(i,c)=min(f(i-1,c),f(i,c-M[i]))
                        jesli c-M[i]>=0
f(i,0)=0
f(0,c)={c/M[0] jeśli M[0]%C==0,
        inf w przeciwnym przypadku




"""
M=[1,3,13]
C=19
def exch(M,C):
    n=len(M)
    F=[[float("inf") for _ in range(C+1)] for _ in range(n)]
    A = [[0 for _ in range(C + 1)] for _ in range(n)]
    for j in range(int(C/M[0])+1):
        F[0][j*M[0]]=j
        # A[0][j * M[0]] = 1
    # for i in range(C+1):
    #     F[0][]
    # F[0] = range(C + 1)
    print(F)
    for i in range(1,n):
        for c in range(C+1):
            if c-M[i]<0:
                F[i][c]=F[i-1][c]
            else:
                # F[i][c]=min(F[i-1][c],1+F[i][c-M[i]])
                if(F[i-1][c]<1+F[i][c-M[i]]):
                    F[i][c]=F[i-1][c]
                    A[i][c]=A[i-1][c]
                else:
                    F[i][c]=1+F[i][c-M[i]]
                    A[i][c]=i
    # print(F)
    i=n-1
    j=C
    # print(A)
    while A[i][j]!=0:
        print(A[i][j])
        i=A[i][j]-1
        j=j-M[i]
    return F[n-1][C]
print(exch(M,C))