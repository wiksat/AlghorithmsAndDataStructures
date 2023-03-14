"""
    Mamy tablce liczb naturalnych A[n] szukamy zbioru sumującego się do T{T,F}
    1) Tworzymy funkcję f(i,t) która zwraca True lub False dla tablicy A funkcją dającą wynik będzie f(A,n-1,T)
    2) Dla przypadku f(n-x, 0) n-x >= 0 funkcja zwraca True
    3) Dla przypadku f(0,x) x < t funkcja zwraca False
"""
A=[1,3,6,7]
# T=6
T=17
def sum_to_target(A,t):
    n=len(A)

    f=[[False for _ in range(t+1)] for _ in range(n)]
    # f[0][A[0]] = True
    for i in range(n):
        f[i][0]=True
    for i in range(1,n):
        for j in range(t+1):
            if j-A[i]>=0:
                f[i][j]=f[i-1][j-A[i]] or f[i-1][j]
            else:
                f[i][j]=f[i-1][j]
    return f[n-1][t]
print(sum_to_target(A,T))