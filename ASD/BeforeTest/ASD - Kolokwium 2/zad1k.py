from zad1ktesty import runtests

def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    # n=len(S)
    # arr=[0 for i in range(n)]
    # for i in range(n):
    #     arr[i] = 1 if S[i] == '0' else -1
    # F=[[0 for _ in range(2)] for _ in range(n)]
    # F[0][0]=0
    # F[0][1]=arr[0]
    # # print(F)
    # for i in range(1,n):
    #     F[i][1] = max(F[i - 1][1] + arr[i], arr[i])
    #     F[i][0]=max(F[i-1][0],F[i - 1][1] + arr[i])
    #
    # print(F)
    # return F[n-1][0]
    n=len(S)

    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i]=1 if S[i] == '0' else -1
    maxi = 0
    for a in range(n):
        for b in range(a+1,n):
            if S[b]=='1':
                F[a][b]=F[a][b-1]-1
            if S[b]=='0':
                F[a][b]=F[a][b-1]+1
            maxi=max(maxi,F[a][b])
    return maxi




    # print(F)
    # print(przewaga)

runtests ( roznica )