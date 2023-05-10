import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import numpy as np
from LAB3.ex1 import generate_connected_graph, draw_weighted_graph

# Funkcja inicjalizująca zmienne 
# - ds - tablica dystansów najkrótszej ścieżki s → ustalonego wierzchołka
# - ps - tablica poprzedników ustalonego wierzchołka na najkrótszej ścieżce s → ustalonego wierzchołka
# na koniec ustawia dystans do startującego wierzchołka na 0
def init(G, s):
    n = len(G)
    ds = np.array([np.inf for i in range(n)])
    ps = np.array([-1 for i in range(n)])
    ds[s] = 0
    
    return ds, ps
    
# Funkcja relax sprawdza czy z s do v można przejść krócej przez 
# krawędź (u, v) (względem aktualnego oszacowania ds[v]).
def relax(u, v, w, ds, ps):
    if ds[v] > ds[u] + w[u][v]:
        ds[v] = ds[u] + w[u][v]
        ps[v] = u
     
# Algorytm Dijkstry   
def dijkstra(G, w, s):
    n = len(G)
    ds, ps = init(G, s)
    
    # Pusty set do przechowywania odwiedzonych wierzchołków
    S = set()
    
    # Słownik zawierający nieodwiedzone wierzchołki i ich minimalnych dystansów
    Q = {i: ds[i] for i in range(n)}
    
    # Pętla wykonująca się dopóki są nieodwiedzone wierzchołki w Q
    while Q:
        # Znajdujemy wierzchołek o najmniejszym dystansie
        u = min(Q, key=Q.get)
        
        # Jeżeli dystans z s do u jest równy np.inf to przerwij
        if ds[u] == np.inf:
            break
        
        # Usuń u z Q, a dodaj do S
        del Q[u]
        S.add(u)
        
        for v in range(n):
            
            # Jeżeli u i v są połączone krawędzią i v nie został jeszcze odwiedzony
            if G[u][v] != 0 and v not in S:
                # Relaksacja
                relax(u, v, w, ds, ps)
                
                # Aktalizacja dystansu w słowniku Q
                Q[v] = ds[v]
                
    return ds, ps

# Wypisanie najkrótszych ścieżek składających się z poprzedników znajdujących się w tablicy ps 
# oraz dystansów znajdujących się w tablicy ds
def print_shortest_paths(ds, ps):
    for i in range(len(ds)):
        path = [i]
        j = i
        while j != -1 and j != 0:
            j = ps[j]
            
            # Używamy insert zamiast append bo chcemy dodawać na początek
            path.insert(0, j)
            
        path = [node + 1 for node in path]
        print(f'd({i+1}) = {ds[i]} ==> {path}')
        
if __name__ == '__main__':
    # Generowanie grafu oraz pomocniczy rysunek
    G_temp = generate_connected_graph(7)
    draw_weighted_graph(G_temp)
    
    # Konwersja nx.Graph na np.array
    G = nx.to_numpy_array(G_temp)
    ds, ps = dijkstra(G, G, 0)
    
    print_shortest_paths(ds, ps)