def absolute(T):
    n=len(T)
    F=[[0 for _ in range(n)]for _ in range(n)]
    S=[0 for _ in range(n+1)]
    for i in range(n):
        S[i+1]=S[i]+T[i]
    # print(S)
    for i in range(n-1):
        F[i][i+1]=abs(S[i+2]-S[i])
    for l in range(2,n):
        for i in range(n-l):
            j=i+l
            F[i][j]=max(abs(S[j+1]-S[i]),min(F[i][j-1],F[i+1][j]))
    return F[0][n-1]

T=[1,-5,2]
print(absolute(T))