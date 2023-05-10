import networkx as nx
import matplotlib.pyplot as plt

from LAB1.ex1 import adj_list_to_adj_matrix, get_nodes_from_adjmatrix, get_edges_from_adjmatrix, draw_circular_graph
from ex123 import components

def read_from_file(path):
    # Konwersja pliku z adjacency list do nx.Graph()
    G = nx.Graph()
    
    with open(path, 'r') as f:
        lines = f.readlines()
                
    adjlist = []
    
    for line in lines:
        nodes = list(map(int, line.split()))
        adjlist.append(nodes)

    adjmatrix = adj_list_to_adj_matrix(adjlist)
    nodes = get_nodes_from_adjmatrix(adjmatrix)
    G.add_nodes_from(nodes)
    edges = get_edges_from_adjmatrix(adjmatrix)
    G.add_edges_from(edges)
    
    # Testowanie
    # print("All edges:")
    # print(edges)
    # draw_circular_graph(G)
    
    return G

# Sprawdzanie czy dana krawędź w grafie jest mostem
def is_bridge(G, u, v):

    # Kopia grafu i usunięcie z niej zadanej krawędzi
    Gcopy = G.copy()
    Gcopy.remove_edge(u, v)

    if max(components(Gcopy.nodes, Gcopy.edges)) == 1:
        return False
    
    return True

# Znajdowanie wszystkich sąsiadów danego wierzchołka
def find_neighbors(G, node):
    neighbors = []

    for edge in G.edges:
        if(node == edge[0]):
            neighbors.append(edge[1])
        elif(node == edge[1]):
            neighbors.append(edge[0])

    return neighbors