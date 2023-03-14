"""
Drzewa binarne

"""


class Node():
    def __init__(self):
        P = None
        l = None
        r = None
        val = None

# wstawianie do drzewa
def f(Tree, x):
    if Tree == None:
        Tree = x
        return Tree
    u = Tree, prev = None
    while u is not None:
        if u.val < x.val:
            prev=u
            u = u.r
        else:
            prev=u
            u=u.l
    if prev.val<x.val:
        prev.r=x
    else:
        prev.l=x
    x.p=prev
    return Tree


#minimum w drzewie to trzeba isc caly czas w lewo

#wyszukiwanie nastęnika
# idziemy do prawego dziecka i maksymalnie w lewo
# gdy sie nie da to idziemy w gore dopoki wierzcholek na ktorym jestesmy jest prawym synem...
def next(Tree,x):
    if x.r is not None:
        return t_min(x.r)#ta funkcja zwraca węzeł
    v=x
    # if v==x.p.l:
    #     return x.p
    while v.p is not None and v!=v.p.l:
        v=v.p
    return v.p

# sekwencja kodów dna GATC chcemy sprawdzić czy sie powtarzają słowa drzewa trie


"""
mamy dwa drzewa BST ile takich samych kluczy znajduje sie w obu drzewach

zaczynamy od minimum w odydwu drzewach, szukamy następnika i znajdujemy wspolny element
potem next gdy znaleźliśmy wspolnego to next w obu drzewach

"""



"""
znajywanie i-tego min w drzewie
można niby z minimum i nextować,
ale
dla kazdego wezla sprawdzamy ile w lewym poddrzewie jest elementów,
np chcemy znalezx 5 wierzcholek, sprawdzamy ile jest w lewym poddrzewie korzenia i jesli jest wiecej lub rowno to idziemy w lewo i odejmujemy


oraz jaki ma numer dany element
"""


"""
jak zaimplementowac drzewa czerwono czarne tak aby obliczenie sum przedzialu od x do y dzialalo w czasie log
dobrze jest trzymac w kazdym wierzchoku sumy poddrzewa

"""