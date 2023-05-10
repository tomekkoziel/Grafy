import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import random
from LAB1.ex3 import make_rand_graph_edges, get_nodes_from_adjmatrix, get_edges_from_adjmatrix

def is_connected(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    
    # Funkcja pomocnicza Przeszukiwanie w głąb
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if adj_matrix[v][i] == 1 and not visited[i]:
                dfs(i)
    
    # Znajdowanie pierwszego nieodwiedzonego wierzchołka i przeszukiwanie grafu DFS
    dfs(0)
    
    # Jeżeli po przeszukiwaniu wgłą któryś wierzchołek jest nieodwiedzony, to graf ten nie jest spójny
    for i in range(n):
        if not visited[i]:
            return False
    
    # Zwraca True jeżeli graf jest spójny, w przeciwnym wypadku False
    return all(visited)

def generate_connected_graph(n):
    
    # Pętla do wyszukania spójnego grafu
    while True:
        adjmatrix = make_rand_graph_edges(n, random.randint(n-1, (n*(n-1))/2))
        if is_connected(adjmatrix):
            break
        
    # Konwersja na obiekt typu nx.Graph()
    G = nx.Graph()
    G.add_nodes_from(get_nodes_from_adjmatrix(adjmatrix))
    for node1, node2 in get_edges_from_adjmatrix(adjmatrix):
        G.add_edge(node1, node2, weight = random.randint(1, 10))
    
    return G

def draw_weighted_graph(G):
    # Rysowanie
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    
    # Testowanie
    # plt.savefig('graph.png')
        
if __name__ == '__main__':
    # Wygenerowany graf
    G = nx.Graph()
    G = generate_connected_graph(5)
    draw_weighted_graph(G)