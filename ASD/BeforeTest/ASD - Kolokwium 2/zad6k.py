from zad6ktesty import runtests

def haslo ( S ):
    n=len(S)
    print(S,n)
    F=[-1 for _ in range(n)]
    F[0]=1
    if int(S[0])>2 or (S[0]==2 and(S[0]=="2" and S[1]!="7")or(S[0]=="2" and  S[1]!="8")or(S[0]=="2" and S[1]!="9")):
        F[1] = 1
    else:
        F[1] = 2

    def rek(i):
        nonlocal S,F
        if i<0:
            return 0
        if F[i]!=-1:
            return F[i]
        w=rek(i-1)
        w2=0
        if S[i]=="0":
            F[i]=rek(i-1)
            return F[i]
        if (S[i-1]=="1")or(S[i-1]=="2" and S[i]!="7")or(S[i-1]=="2" and  S[i]!="8")or(S[i-1]=="2" and S[i]!="9"):
            w2=rek(i-2)
        F[i]=w+w2
        return F[i]

    w=rek(n-1)
    print(F)
    return w

runtests ( haslo )