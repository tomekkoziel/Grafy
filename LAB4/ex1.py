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

def draw_digraph_from_adjmatrix(adjmatrix):
    G = nx.DiGraph()

    # Dodawanie wierzchołków do grafu
    nodes = len(adjmatrix)
    G.add_nodes_from(range(1, nodes + 1))

    # Dodawanie krawędzi do grafu na podstawie macierzy sąsiedztwa
    for i in range(nodes):
        for j in range(nodes):
            if adjmatrix[i][j] == 1:
                G.add_edge(i + 1, j + 1)

    # Rysowanie grafu
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)

    # Wyświetlanie grafu
    plt.show()

if __name__ == '__main__':
    adjmatrix = make_rand_digraph_adjmatrix(8, 0.2)
    print(adjmatrix)
    draw_digraph_from_adjmatrix(adjmatrix)
    