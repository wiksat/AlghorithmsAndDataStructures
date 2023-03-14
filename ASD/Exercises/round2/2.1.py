"""
T=[0,2,7,5,3,19,11,13]
f(i)-max zysk gdy wytniemy drzewo i
g(i)-max zysk gdy nie wytniemy drzewa i
f(0)=0
g(0)=0
f(i)=T[i]+g(i-1)
g(i)=max(g(i-1),f(i-1))

podobne do imprezy firmowej
"""
def g(i):
    if i==0:
        return 0
    return max(f(i-1),g(i-1))
def f(i):
    if i==0:
        return 0
    return T[i]+g(i-1)



T=[0,2,7,5,3,19,11,13]
n=len(T)
print(max(f(n-1),g(n-1)))