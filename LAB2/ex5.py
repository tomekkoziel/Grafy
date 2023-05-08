import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random
from operator import itemgetter
import numpy as np

from LAB1.ex2 import drawCircularGraph
from LAB1.ex3 import make_rand_graph_propability, get_edges_from_adjmatrix, get_nodes_from_adjmatrix


def generate_random_np(n, prob):
    if(prob < 0 or prob > 1):
        sys.exit("Prawdopodobieństwo musi być z przedziału [0,1].")
    if(n < 0):
        sys.exit("Liczba wierzchołków musi być większa od zera.")

    while True:
        adjmatrix = np.zeros((n, n), dtype=int)
        # Losowanie krawędzi grafu
        for i in range(n):
            for j in range(i+1, n):
                adjmatrix[i][j] = random.choices([0, 1], weights=[1-prob, prob], k=1)[0]
                adjmatrix[j][i] = adjmatrix[i][j]
        # print(adjmatrix)
        edges = get_edges_from_adjmatrix(adjmatrix)

        if edges != []:
            if max(map(max, edges)) == n:
                return adjmatrix

def generate_k_regular_graph(nodes, k):
    if k > nodes or k % 2 == 1 and nodes % 2 == 1:
        sys.exit("Wrong arguments")

    G = nx.Graph()
    adjmatrix = generate_random_np(nodes, k / nodes)
    G.add_nodes_from(get_nodes_from_adjmatrix(adjmatrix))
    G.add_edges_from(get_edges_from_adjmatrix(adjmatrix))


    drawCircularGraph(G)

if __name__ == '__main__':
    generate_k_regular_graph(6, 3)