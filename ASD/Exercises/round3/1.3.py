"""
ścieżka hamiltona

sortowanie topologiczne

mhm
gdy każde dwa nie mają bezpośredniego połączenia, po posortowaniu top.  to sie nie da wykonać takiej ścieżki

"""
"""
jak znaleźć taki wierzchołek z którego można dojść do wszystkich innych w grafie skierowanym
(dobry początek)
na pewno do silnie spojnej składowej bedzie 
1.sortowanie topologiczne spójnych składowych
2.potem sprawdzamy z początku czy da sie dojsc do wszystkich innych

lub lepiej

zwykłe przeszukiwanie w głąb, kiedy jest tak że przy kolejnym wyborze nowego elementu przeszukaliśmy wszytskich pozostałych,
to odpalamy dfs od niego i jeśli sie zgadza to ok, a jeśli nie to nie ma dobrego początku



"""
"""
najkrótsza ścieżka w grafie z wagami skierowanym bez cykli

sortujemy topologicznie
relaksacja wierzchołków w kolejności z sortowania




"""
"""
znaleźć w grafie graf o min iloczynie wag

logarytmy wszystkich wag a potem dijkstra



"""