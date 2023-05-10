import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from LAB1.ex1 import  draw_circular_graph
from utility import read_from_file

# Funkcja wyszukiwująca cykl Hamiltona
def is_hamilton(G):
    n = G.number_of_nodes()
    # Tablica przechowująca cykl Hamiltona
    cycle = []
    
    # Twierdzenie Diraca
    if n >= 3 and not (any(G.degree(node) < n / 2 for node in G.nodes)):
        print("Spełnione twierdzenie Diraca, graf jest hamiltonowski.")
    
    # Początkowy wierzchołek
    first_node = list(G.nodes)[0]
    hamilton_cycle_recursive(G, first_node, cycle)
    
    if len(cycle) == n:
        # Jeżeli wszystko się zgadza dodajemy pierwszy wierzchołek na koniec cyklu
        cycle.append(first_node)
        print("Cykl Hamiltona:", cycle)
    else:
        print("Graf nie jest hamiltonowski.")
    
# Rekursywna funkcja znajdująca cykl Hamiltona
def hamilton_cycle_recursive(G, node, cycle):    
    cycle.append(node)
    
    if len(cycle) == G.number_of_nodes():
        # Sprawdzenie czy ostatni element cykl jest połączony krawędzią z pierwszym elementem w cyklu
        # G.neighbors(node) - funkcja zwracająca sąsiadów wierzchołka node
        if cycle[-1] in G.neighbors(cycle[0]):
            return True
        
        # Jeżeli nie jest usuwamy ostatni element i dalej szukamy
        cycle.pop()
        return False
    
    # Rekrsywne przejście po nieodwiedzonych sąsiadach
    for neighbor in G.neighbors(node):
        if neighbor not in cycle:
            if hamilton_cycle_recursive(G, neighbor, cycle):
                return True
    
    # Jeżeli nie znaleziono cyklu czyścimy tablice cycle 
    cycle.pop()
    return False
            
if __name__ == '__main__':
    G = nx.Graph()
    G = read_from_file('data_ex6.txt')
    draw_circular_graph(G)
    
    is_hamilton(G)