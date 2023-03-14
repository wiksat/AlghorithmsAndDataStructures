from egz2btesty import runtests

def fun(ind, ile_odwiedzonych, zapas):
    maxW = 0
    for j in range(1, 4):
        if C[ind][j][1] != -1:
            maxW = max(maxW, fun(C[ind][j][0], ile_odwiedzonych - 1, zapas))
            if C[ind][0] >= C[ind][j][1]:
                maxW = max(maxW, fun(C[ind][j][0], ile_odwiedzonych - 1, zapas + min(C[ind][0] - C[ind][j][1], 10)))
            if zapas + C[ind][0] >= C[ind][j][1]:
                d = zapas + C[ind][0] - C[ind][j][1]
                maxW = max(maxW, fun(C[ind][j][0], ile_odwiedzonych - 1, d))
return maxW
def magic( C ):
    # tu prosze wpisac wlasna implementacje
    n = len(C)



    # D=[[-1 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         D[i][j]=max(D[i-1][j-1],)
    print(fun())

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
