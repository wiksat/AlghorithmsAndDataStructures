from egzP1atesty import runtests

def titanic( W, M, D ):
    n=len(W)
    # print(M)
    s=""
    dict={}
    for i in D:
        dict[M[i][1]]=True
    for i in range(n):
       s=s+M[ord(W[i])-ord('A')][1]
    n2=len(s)
    DP = [10 ** 10 for _ in range(n2)]
    DP[0]=1
    tes=s[0]
    for i in range(1,4):
        if i>n2-1:
            break
        tes=tes+s[i]
        if dict.get(tes) is not None:
            DP[i] = 1
    for i in range(1,n2):
        temp=DP[i]
        pot=""
        for j in range(i,i-5,-1):
            if j<0:
                break
            pot=s[j]+pot
            if dict.get(pot) is not None:
                temp=min(temp,DP[j-1]+1)
        DP[i]=temp
    # print(DP)
    return DP[n2-1]

runtests ( titanic, recursion=False )