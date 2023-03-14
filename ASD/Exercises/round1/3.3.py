# budowanie kopca
def parent(n):
    return (n-1)//2
def insert(T,value):
    T.append(value)
    child=len(T)-1
    while child!=0 and T[child]>T[parent(child)]:
        T[child],T[parent(child)]=T[parent(child)],T[child]
        child=parent(child)

#6.algorytm scalający k posortowanych list
#7.struktura insert, removeINT, removeMAX w O(logN)
#8. struktura insert, removeMedian w O(logN)
# kopiec min i max i slot na medianę,(mniejsze od mediany do kopca max , przeciwne do min), pry parzyste to mediana na szczytach kopców