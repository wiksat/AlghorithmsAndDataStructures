"""najkrótsza ścieżka po malejących wagach

jeśli ścieżka któa nas interesuje jest malejąca to


sortujemy krawędzie malejąco i w tej kolejności relaksujemy


"""
"""w grafie zorientowanym sprawdzamy czy wierzchołka da sie dojsc bezpośrednio do każdego innego

"""
def FloydWarshall(G,):
    n=len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][k]==1 and G[k][j]==1:
                    G[i][j]=1


"""
mamy informacje o kursach walut i dla kazdej pary mamy kurs kupna i sprzedazy (
szukamy kombinacji sprzedaza i kupna ktore nam pozwola zarobic) trzeba to zrobic wymnożeniem wartości, a potem logarytm z tego i do grafu

szukam ujemnego cyklu belmanem fordem (po zrobieniu iteracji po wierzchołkach robimy weryfikacje)


"""
"""
prowadzą ciężarówke Bob i Alicja, Alicja chce prowadzic jak najmniej , przesiadaja sie na punktach przesiadkowych
jadą z A do B po grafie i szukamy ścieżki
nie wiemy kto startuje

robimy transformacje grafu kazdy wierzcholek na 2 (a i b) na krzyż krawędzie, potem wagi tylko gdy jedzie Bob, przy alicji 0


na początku i końcu robimy superwierzchołek
na nowym grafie odpalamy normalną dikstre
"""

"""
mamy drzewo graf ważony
szukamy taki wierzchołek od ktorego makx odleglosc do liscia najdalszego jest najmniejsza ze wszystkich wierzhcolkow

można to zrobić za pomocom 2 przeszukiwać grafu


"""