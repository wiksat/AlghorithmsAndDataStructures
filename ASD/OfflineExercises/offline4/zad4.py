#WIKTOR SATORA
#Algorytm działa na zasadzie dymanicznego algorytmu z problemem plecakowym, ale rozbudowany o sprawdzanie zawierania się przedziałów. Najpierw tablica wejściowa jest
#modyfikowana o dodatkowe miejsce na przechowywanie pierwotnego indeksu, poźniej tablica zostaje posortowana po wartości b. Następnie w pętli sprawdzamy n przedziałów,
#szukamy dla niego najbliższego z lewej strony rozłącznego i w drugiej pętli postępujemy jak w problemie plecakowym. Na koniec odzyskanie wyniku odbywa się poprzez
#cofanie po tablicy dwuwymiarowej złożoność obliczeniowa to n+nlogn+n*(p+n)+n, więc O(n*p), a pamięciowa to n*p
from zad4testy import runtests

def konflikty(T,n):
    # for i in reversed(range(n)):
    # # for i in range(n,-1,-1):
    # # szukamy najbliższego od zachodzącego na siebie!!!!!!
    #     if T[i][2] < T[n][1]:
    #         return i
    # return -1
    l = 0
    h = n
    while l <= h:
        sr = (l + h) // 2
        if T[sr][2] < T[n][1]:
            # szukamy najbliższego od zachodzącego na siebie!!!!!!
            if T[sr + 1][2] < T[n][1]:
                l = sr + 1
            else:
                return sr
        else:
            h = sr - 1
    else:
        return -1
def select_buildings(T,p):
    n = len(T)
    for i in range(n):
        T[i]=[T[i][0],T[i][1],T[i][2],T[i][3],i]
    T = sorted(T, key=lambda el: el[2])
    F=[[0 for _ in range(p+1)] for _ in range(n)]
    for pi in range(T[0][3],p + 1):
        F[0][pi]=T[0][0]*(T[0][2]-T[0][1])

    for i in range(1, n):
        ind = konflikty(T, i)
        z=T[i][0] * (T[i][2] - T[i][1])
        for pi in range(p+1):
            zawartosc_studentow = z
            if pi>=T[i][3]:
                if ind != -1:
                    zawartosc_studentow += F[ind][pi-T[i][3]]
                if F[i-1][pi]<zawartosc_studentow:
                    F[i][pi]=zawartosc_studentow
                else:
                    F[i][pi] = F[i - 1][pi]
            else:
                F[i][pi] = F[i - 1][pi]

    i=n-1
    pi=p
    res=[]
    while F[i][pi]!=0and i>=0 :
        while F[i][pi]==F[i-1][pi]and i>0:
            i-=1
        res.append(T[i][4])
        ind = konflikty(T, i)
        # if ind==-1:
        #     break
        pi-=T[i][3]
        i = ind
    return res

runtests( select_buildings )