"""
słaba żaba

f(i,x)=minimalna liczba skoków aby dotrzeć do pola i-tego z zapasem x(jednostek energii)
f(0,x)=0
f(0,0)=


f(i,x)=min(f(j,x+(i-j)-T[j])+1)
        j<i
        gdy (x+(i-j)-T[j])>=0
"""
T=[]
n=len(T)
F=[0 for _ in range(n)]
x=None
for i in range(1,n):
    m=999999999
    for j in range(i):
        if x+(i-j)-T[j]>=0:
            m=min(m,)
def f(i,x):
    if i==0:
        return 0
    m=999999999
    for j in range():
        pass
        