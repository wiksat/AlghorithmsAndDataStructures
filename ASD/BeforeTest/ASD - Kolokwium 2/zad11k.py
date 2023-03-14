from zad11ktesty import runtests


def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    def rek(i, p1,s):
        nonlocal F,T
        if i == len(T):
            return abs(p1-(s-p1))
        if i > len(T) - 1:
            return 0
        if F[i][p1] != -1:
            return F[i][p1]
        d = min(rek(i + 1, p1 + T[i],s+T[i]), rek( i + 1, p1,s+T[i]))
        F[i][p1] = d
        return F[i][p1]
    n=len(T)
    s=sum(T)
    F=[[-1 for _ in range(s+1)] for _ in range(n)]
    w=rek(0,0,0)

    # print(w)
    # print(T)
    # print(F)
    return w

runtests ( kontenerowiec )
    