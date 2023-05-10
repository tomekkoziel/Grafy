import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random

from LAB1.ex2 import draw_circular_graph

# Funkcja szukająca k-regularnego grafu
def generate_k_regular_graph(n, k):
    # Warunki początkowe
    if k % 2 == 1 and n % 2 == 1:
        raise ValueError("Cannot create a k-regular graph with both k and n odd")
    
    if k >= n:
        raise ValueError("k must be less than n")
    
    # Losowanie grafu
    G = find_the_edges(n, k)
    
    return G

# Funkcja do losowania grafu
def find_the_edges(n, k):

    # Stworzenie grafu na podstawie podanej ilości wierzchołków
    G = nx.Graph()
    G.add_nodes_from(range(n))
    nodes = list(G.nodes())

    # Licznik do optymalizacji
    counter = 0

    # Losowanie krawędzi dla każdego wierzchołka
    for i in range(n):
        # Jesli stopień wierzchołka mniejszy niż k to losujemy dla niego krawędź
        while G.degree(nodes[i]) < k:
            j = random.choice(range(n))
            # Jeśli wylosowany wierzchołek nie jest samym sobą (inaczej powoduje pętle) 
            # i jego stopień jest mniejszy niż k, możemy dodać krawędź
            if i != j and G.degree(nodes[j]) < k:
                G.add_edge(nodes[i], nodes[j])
            # W przeciwnym wypadku poprawienie licznika i przejsćie dalej
            else:
                counter += 1
            # Jeśli licznik dobije do 1000 prób, usunięcie krawędzi, wierzchołków i restart funkcji
            if counter == 1000:
                G.remove_edges_from(G.edges)
                G.remove_nodes_from(range(n))
                G = find_the_edges(n, k)

    return G
        
        

if __name__ == '__main__':
    draw_circular_graph(generate_k_regular_graph(8, 3))