from egzP5atesty import runtests 
# dynamik
def inwestor ( T ):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    maxi=0
    s=[-1,0]

    LS=[-1 for _ in range(n)]
    RS=[n for _ in range(n)]

    for i in range(1,n):
        while s[len(s)-1]!=-1 and T[s[len(s)-1]]>T[i]:
            RS[s[len(s)-1]]=i
            s.pop()
        if T[i]==T[i-1]:
            LS[i]=LS[i-1]
        else:
            LS[i]=s[len(s)-1]
        s.append(i)
    for j in range(n):
        maxi=max(maxi,T[j]*(RS[j]-LS[j]-1))
    return maxi

runtests ( inwestor, all_tests=True )