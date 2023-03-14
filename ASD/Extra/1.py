import math

R=10
tab=[(1,2),(1,1),(4,4),(6,3),(2,1)]
n=len(tab)
buckets=[[]for _ in range(n)]
for odl in tab:
    dl=math.sqrt(odl[0]**2+odl[1]**2)
    x=0
    for i in range(n):
        x=math.sqrt((R*R/n)+x*x)
        if dl<=x:
            buckets[i].append(odl)
            break
print(buckets)