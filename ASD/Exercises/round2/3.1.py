s=[0,20,40,55,80,120]
k=[0,15,8,7,11,6]
B=50
def Orlen(B,k,s):
    b=B
    prev_i=0
    suma_kosztow=0
    for i in range(1,len(s)):
        b=b-(s[i]-s[prev_i])
        min_koszt=i
        for j in range(i+1,len(s)):
            if b-(s[j]-s[i])>=0:
                if k[min_koszt]>k[j]:
                    min_koszt=j
            else:
                break
        if min_koszt==i:
            for k in range(j,len(s)):
                if B-(s[k]-s[i])>=0:
                    if k[i]>k[k]:
                        suma_kosztow+=((s[k]-s[i])-b)*k[k]
                        i=k
                        prev_i=i

#tankujemy do pełna zawsze to trzeba dynamicznie