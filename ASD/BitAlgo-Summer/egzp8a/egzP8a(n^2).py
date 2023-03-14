from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    for i in range(n):
        T[i]=(T[i][0],T[i][1],S[i])
    T=sorted(T,key=lambda x:x[1])
    maxZ=0
    for i in range(n):
        maxZ=max(maxZ,T[i][2])
        for y in range(i,n):
            if T[y][0]>T[i][1]:
                maxZ=max(maxZ,T[y][2]+T[i][2])
    # print(T)
    return maxZ

runtests ( reklamy, all_tests=True )