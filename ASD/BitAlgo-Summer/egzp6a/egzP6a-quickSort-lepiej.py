from egzP6atesty import runtests
# def countingSort(arr, exp1):
#

def radixSort(arr,exp1,n):
    # n = len(arr)
    output = [0] * (n)
    count = [0] * (exp1 + 1)
    for i in range(0, n):
        index = arr[i][0]
        count[index] += 1
    for i in range(1, exp1 + 1):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i][0]
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    n=len(H)
    dane=[0 for _ in range(n)]
    maxi=0
    maxiLen=0
    for i,slowo in enumerate(H):
        litery=0
        for znak in slowo:
            if ord(znak)>96 and ord(znak)<123:
                litery+=1
        maxi=max(maxi,litery)
        w=len(slowo)
        maxiLen=max(maxiLen,w)
        dane[i] = (w,litery)
    maksus=[[0,0] for _ in range(maxiLen+1)]
    tablice=[[] for _ in range(maxiLen+1)]
    # print(H)
    # print(maxiLen)
    for i,slowo in enumerate(H):
        # print(dane[i][0])
        tablice[dane[i][0]].append((dane[i][1],slowo))
        maksus[dane[i][0]][0]+=1
        maksus[dane[i][0]][1]=max(maksus[dane[i][0]][1],dane[i][1])
    # print(tablice)
    for i,tablica in enumerate(tablice):
        # tablica.sort()
        radixSort(tablica,maksus[i][1],maksus[i][0])
    arr=[]
    for tablica in tablice:
        for el in tablica:
            arr.append(el[1])

    # print(tablice)
    # print(arr)
    return arr[n-s]


runtests ( google, all_tests=True )