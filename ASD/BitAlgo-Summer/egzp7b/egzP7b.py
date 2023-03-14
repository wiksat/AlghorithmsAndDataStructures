from egzP7btesty import runtests 


def ogrod( S, V ):
    #Tutaj proszę wpisać własną implementację
    n=len(S)
    m=len(V)
    for i in range(n):
        S[i]-=1

    maxi=0
    suma = 0
    for i in range(n):
        tab = [0 for _ in range(m)]
        suma = 0
        for j in range(i,n):
            if tab[S[j]]==0:
                suma+=V[S[j]]
                tab[S[j]] =1
            elif tab[S[j]]==1:
                maxi=max(maxi,suma)
                suma -= V[S[j]]
                tab[S[j]] = -1
        maxi = max(maxi, suma)
    return maxi
    
runtests(ogrod, all_tests = True)