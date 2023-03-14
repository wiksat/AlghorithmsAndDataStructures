from kol2atesty import runtests

def drivers( P, B ):
    n = len(P)
    counter=1
    for i in P:
        if i[1]==True:
            counter+=1
    W=[]
    for i in range(n):
        W.append((P[i][0],P[i][1],i))
    W.sort()
    # print(W)
    przesiadkowe=[]
    for i in range(n):
        if W[i][1]==True:
            przesiadkowe.append(W[i])
    c=[]
    c.append(0)
    t_sum=0
    for i in W:
        if i[1]==True:
            c.append(t_sum)
        else: t_sum+=1
    c.append(t_sum)
    print(c)
    F=[[-1 for _ in range(2)] for _ in range(counter+1)]
    odczyt = [[None for _ in range(2)] for _ in range(counter + 1)]
    F[0][0]=99999999999999999
    F[0][1] = 0
    for i in range(1,counter+1):
        for j in range(2):
            if i==1:
                F[i][j]=F[i-1][1-j]
                odczyt[i][j]=(i-1,j-1)
            elif i==2:
                if j == 0:
                    if F[i - 1][1]<F[i - 2][1]:
                        F[i][j]=F[i - 1][1]
                        odczyt[i][j]=(i-1,1)
                    else:
                        F[i][j]=F[i - 2][1]
                        odczyt[i][j] = (i - 2, 1)
                    # F[i][j] = min(F[i - 1][1], F[i - 2][1])
                if j == 1:
                    if F[i - 1][0] + c[i] - c[i - 1]<F[i - 2][0] + c[i] - c[i - 2]:
                        F[i][j] = F[i - 1][0] + c[i] - c[i - 1]
                        odczyt[i][j] = (i - 1, 0)
                    else:
                        F[i][j]=F[i - 2][0] + c[i] - c[i - 2]
                        odczyt[i][j] = (i - 2, 0)
                    # F[i][j] = min(F[i - 1][0] + c[i] - c[i - 1], F[i - 2][0] + c[i] - c[i - 2])
            elif i>2:
                if j == 0:
                    d = min(F[i - 1][1], F[i - 2][1], F[i - 3][1])
                    if d==F[i - 1][1]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 1, 1)
                    elif d== F[i - 2][1]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 2, 1)
                    elif d==F[i - 3][1]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 3, 1)
                if j == 1:
                    d = min(F[i - 1][0] + c[i] - c[i - 1], F[i - 2][0] + c[i] - c[i - 2],
                            F[i - 3][0] + c[i] - c[i - 3])
                    if d==F[i - 1][0] + c[i] - c[i - 1]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 1, 0)
                    elif d==F[i - 2][0] + c[i] - c[i - 2]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 2, 0)
                    elif d==F[i - 3][0] + c[i] - c[i - 3]:
                        F[i][j] = d
                        odczyt[i][j] = (i - 3, 0)
    # for i in F:
    #     print(i)
    # print(min(F[counter][1],F[counter][0]))
    # print(przesiadkowe)
    # print(len(przesiadkowe),counter)
    res=[]
    if F[counter][1]<F[counter][0]:
        d=odczyt[counter][1]
        flag=1
    else:
        d=odczyt[counter][0]
        flag=0
    while d!=None and d[0]>0:
        if d[1]!=flag:
            flag=not flag
            # print("d",d[0],przesiadkowe[d[0]-1][2])
            res.append(przesiadkowe[d[0]-1][2])
        d=odczyt[d[0]][d[1]]
    res.reverse()
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )