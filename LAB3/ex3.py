import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import numpy as np
from LAB3.ex1 import generate_connected_graph, draw_weighted_graph
from LAB3.ex2 import dijkstra

def get_length_matrix(n):
    G_temp = generate_connected_graph(n)
    G = nx.to_numpy_array(G_temp)
    # Alokacja pamięci na tablice odległości 
    len_matrix = np.zeros((n,n), dtype=int)
    # Wykorzystanie algorytmu dijkstry dla każdego wierzchołka
    for i in range(n):
        ds, ps = dijkstra(G, G, i)
        del ps
        # Zapisanie odległości od wierzczhołka do macierzy
        len_matrix[i-1] = ds
    return len_matrix, G_temp

if __name__ == '__main__':
    len_matrix ,G = get_length_matrix(5)
    print(len_matrix)
    draw_weighted_graph(G)



