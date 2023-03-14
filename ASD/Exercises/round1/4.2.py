def unique(A):
    B=[]
    for i in range(len(A)):
        if A[i] not in B:
            insert(B,A[i])
        return B

def counting(A):
    B=unique(A)
    C=[0]*len(B)
    D=[0]*len(A)
    for i in range(len(B)):
        j=index(B,A[i])
        C[j]+=1
        for i in range(1,len(C)):
            C[i]+=C[i-1]
        for i in range(len(A)-1,-1,-1):
            D[C[A[i]]-1]=A[i]
            C[A[i]]-=1
    return D
A=[1,20,7,9]
n=4
A=counting(A)
print(A)