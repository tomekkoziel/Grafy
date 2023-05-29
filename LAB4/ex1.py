import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys


def make_rand_digraph_adjmatrix(n, p):
    if(p < 0 or p > 1):
        sys.exit("Prawdopodobieństwo musi być z przedziału [0,1].")
    if(n<=0):
        sys.exit("Liczba wierzchołków musi być większa od zera.")
    adjmatrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if not i == j:
                adjmatrix[i][j] = random.choices([0, 1],weights=[1-p, p], k=1)[0]    
    return adjmatrix

def draw_digraph_from_adjmatrix(adjmatrix, colors = '#ffa059', weights = []):
    G = nx.DiGraph()

    # Dodawanie wierzchołków do grafu
    nodes = len(adjmatrix)
    G.add_nodes_from(range(1, nodes + 1))

    # Dodawanie krawędzi do grafu na podstawie macierzy sąsiedztwa
    for i in range(nodes):
        for j in range(nodes):
            # Jeśli graf bez wag to nie dodajemy wag
            if adjmatrix[i][j] == 1 and len(weights) == 0:
                G.add_edge(i + 1, j + 1)
            # Jeśli graf z wagami to dodajemy wagi
            elif adjmatrix[i][j] == 1 and len(weights) > 0:
                G.add_edge(i+1, j+1, weight = weights[i][j])
   
    # Rysowanie grafu
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True, node_color = colors)
    # Jeśli graf z wagami to dodajemy wagi
    if len(weights) != 0:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Wyświetlanie grafu
    # print(nx.is_strongly_connected(G))
    plt.show()
    return G
    

if __name__ == '__main__':
    adjmatrix = make_rand_digraph_adjmatrix(8, 0.1)
    print(adjmatrix)
    draw_digraph_from_adjmatrix(adjmatrix)
    