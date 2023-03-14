def g(i):
    if i==0:
        return 0
    if G[i]==-1:
        G[i]=max(f(i-1),g(i-1))
    return G[i]
def f(i):
    if i==0:
        return 0
    if F[i]==-1:
        F[i] = T[i]+g(i-1)
    return F[i]
T=[0,2,7,5,3,19,11,13]
n=len(T)
F=[-1 for _ in range(n)]
G=[-1 for _ in range(n)]
print(max(f(n-1),g(n-1)))



#w pętli
F=[0 for _ in range(n)]
G=[0 for _ in range(n)]
for i in range(1,n):
    F[i]=T[i]+G[i-1]
    G[i]=max(F[i-1],G[i-1])
zysk=max(G[n-1],F[n-1])
print(zysk)
#odczytywanie wyników to cofanie sie po tablicy i wybieranie wiekszej i flaga