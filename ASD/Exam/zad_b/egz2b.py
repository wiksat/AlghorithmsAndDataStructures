"""
WIKTOR SATORA 411502
Jest to algorytm dynamiczny gdzie:
    f(i)=największy zysk sztabek złota gdy dochodzimy do komnaty i
Zysk przy pierszej komnacie to 0, Dla każdej koljenej komanty obliczamy funkcję. W niej sprawdzamy możliwości przejścia
do kolejnych komnat (gdy nie ma -1 w polu C[i][k][1]) oraz czy da sie zwiekszyć lub zostac z tym samym zyskiem,
na koniec porównanie wiekszej wartości i jeśli trzeba to podmienienie.
Jeśli dojście jest niemożliwe to wartość -1 zostanie zwrócona z tablicy DP (bo jest tam domyślnie)
Złożonośc obliczeniowa to O(n)
"""
from egz2btesty import runtests


def magic(C):
    n=len(C)
    DP=[-1]*n
    DP[0]=0
    for i in range(n-1):
        if DP[i] != -1:
            for k in range(1, 4):
                if C[i][k][1] != -1 and C[i][0] - C[i][k][0] <= 10:
                    if C[i][0] - C[i][k][0] + DP[i]>DP[C[i][k][1]]:
                        DP[C[i][k][1]]=C[i][0] - C[i][k][0] + DP[i]
    return DP[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
