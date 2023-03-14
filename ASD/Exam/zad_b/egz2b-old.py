from egz2btesty import runtests
def fun(ind,  zapas,C,n):
    maxW = 0
    for j in range(1, 4):
        if C[ind][j][1] != -1:
            maxW = max(maxW, fun(C[ind][j][0], zapas,C,n))
            if C[ind][0] >= C[ind][j][1]:
                maxW = max(maxW, fun(C[ind][j][0], zapas + min(C[ind][0] - C[ind][j][1], 10,C,n)))
            if zapas + C[ind][0] >= C[ind][j][1]:
                d = zapas + C[ind][0] - C[ind][j][1]
                maxW = max(maxW, fun(C[ind][j][0], d,C,n))
    if ind==n-1:
        print(maxW)
        return maxW
def magic( C ):
    # tu prosze wpisac wlasna implementacje
    n=len(C)
    print(fun(n-1,0,C,n))

    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
