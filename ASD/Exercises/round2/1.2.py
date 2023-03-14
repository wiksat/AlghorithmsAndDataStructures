"""

A[n]-zbiór nominałów
zwracamy liczby monet
f(t)-w ilu min monetach
f(t)=min(f(t-A[0]),f(t-A[1]),...)+1
T=[...],dl=t+1




"""
def mins(A,t):
    T=[-1 for _ in range(t+1)]
    T[0]=0
    for el in A:
        T[el]=1
    def