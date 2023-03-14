#counting sort
def countingSort(arr,base,key):
    c=[0]*(base+1)
    # c = [0] * ((max(arr))//base+1)
    b=[0]*len(arr)
    for i in arr:
        print(key(i))
        c[key(i)]+=1
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    for i in range(len(arr)-1,-1,-1):
        b[c[key(arr[i])]-1]=arr[i]
        c[key(arr[i])]-=1
    return b

def radix(arr):
    base=len(arr)
    res=countingSort(arr,base,lambda x:x%base)
    # res = countingSort(res, base, lambda x: x//base)
    res = countingSort(res, base, lambda x: x%(base**2)//base)
    res = countingSort(res, base, lambda x: x // base**2)
    return res
A=[1,20,7,9]
n=4
A=radix(A)
print(A)