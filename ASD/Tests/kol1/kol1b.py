#WIKTOR SATORA
#Algorytm segreguje elementy na kubełki ze względu na długość słów, później sumuje kody ascii i zamienia te elementy na te kody
#(tylko anaramy będą miały takie same kody ascii)
#Następnie bucket sortem sortuję te tablice i szukam najdłuższego ciągu takih samych elementów
#Złożoność algorytmu to O(N), złożoność pamięciowa to O(N)
from kol1btesty import runtests

def f(T):
    # tu prosze wpisac wlasna implementacje
    ile=0
    for x in T:
        if len(x)>ile:
            ile=len(x)
    # print(ile)
    tab=[[]for _ in range(ile)]
    for x in T:
        tab[len(x)-1].append(x)
    for ind_kosz in range(len(tab)):
        for ind_slowo in range(len(tab[ind_kosz])):
            sum = 0
            for ind_litera in range(len(tab[ind_kosz][ind_slowo])):
                sum+=ord(tab[ind_kosz][ind_slowo][ind_litera])
            tab[ind_kosz][ind_slowo]=sum
            # print(sum)
    for ind_kosz in range(len(tab)):
        if len(tab[ind_kosz])>0:
            dl=len(tab[ind_kosz])
            buckety=[[]for _ in range(dl)]
            norm=max(tab[ind_kosz])
            for el in tab[ind_kosz]:
                # print(int((el/norm)*dl)-1)
                buckety[int((el/norm)*dl)-1].append(el)
            for bucket in buckety:
                dl=len(bucket)
                if dl>0:
                    for i in range(1,dl):
                        klucz=bucket[i]
                        j=i-1
                        while j>=0 and klucz<bucket[j]:
                            bucket[i],bucket[j]=bucket[j],bucket[i]
                            j=-1
                        bucket[j]=klucz

                    out=[]
                    for bucket in buckety:
                        for el in bucket:
                            out.append(el)
                    tab[ind_kosz]=out
    # print(tab)
    sumaa=1
    for ind_kosz in range(len(tab)):
        if len(tab[ind_kosz])>0:
            prev = tab[ind_kosz][0]
        else:
            prev=None
        cur_sum=1
        for ind_el in range(1,len(tab[ind_kosz])):
            # print(tab[ind_kosz][ind_el],sumaa)
            if prev==tab[ind_kosz][ind_el]:
                cur_sum+=1
            else:
                if cur_sum>sumaa:
                    sumaa=cur_sum
                cur_sum = 1
            if cur_sum > sumaa:
                sumaa = cur_sum
            prev=tab[ind_kosz][ind_el]
    return sumaa
    # print(sumaa)



# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
