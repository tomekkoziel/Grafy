import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex1 import draw_digraph_from_adjmatrix
from ex3 import belman_ford, strong_cohernet_digraph, add_weights_to_adjmatrix
from LAB1.ex3 import get_nodes_from_adjmatrix
from LAB3.ex2 import dijkstra


def johnson(adjmatrix, weight_adjmatrix):
    # Dodanie wierzchołka s
    s_adjmatrix, s_weight_adjmatrix = add_s(adjmatrix, weight_adjmatrix)
    n = len(s_adjmatrix)
    # Sprawdzenie czy istnieje ujemny cykl
    if belman_ford(s_adjmatrix,s_weight_adjmatrix, n-1)[0] == False:
        sys.exit("G zawiera cykl o ujemnej wadze.")
    else:
        # Wywołanie algorytmu belmana forda dla wierzchołka s
        _, ds = belman_ford(s_adjmatrix,s_weight_adjmatrix, n-1)
        nodes = get_nodes_from_adjmatrix(s_adjmatrix)
        h = []
        # Przesalowanie wag
        for node in nodes:
            h.append(ds[node-1])
        positive_weights_adjmatrix = np.zeros((n+1,n+1), dtype=int)
        for i in range(n):
            for j in range(n):
                if s_adjmatrix[i][j] == 1:
                    positive_weights_adjmatrix[i][j] = s_weight_adjmatrix[i][j] + h[i] - h[j]
        # Utworzenie tablicy D
        D = np.zeros((n,n), dtype=int)
        nodes = get_nodes_from_adjmatrix(adjmatrix)
        # Wywołanie algorytmu dijkstry i przeskalowanie powrotne wag
        for node in nodes:
            du, _ = dijkstra(adjmatrix, weight_adjmatrix, node-1)
            for v in nodes:
                D[node-1][v-1] = du[v-1] - h[node-1] + h[v-1]
        return D, s_adjmatrix, positive_weights_adjmatrix


def add_s(adjmatrix, weight_adjmatrix):
    n = len(adjmatrix)
    s_adjmatrix = np.zeros((n+1,n+1), dtype=int)
    s_weight_adjmatrix = np.zeros((n+1,n+1), dtype=int)
    # Kopia adjmatrix
    for i in range(n):
        for j in range(n):
            s_adjmatrix[i][j] = adjmatrix[i][j]
            s_weight_adjmatrix[i][j] = weight_adjmatrix[i][j]
    # Dodanie wierzchołka s
    for i in range(n):
        s_adjmatrix[n][i] = 1
    return s_adjmatrix, s_weight_adjmatrix


if __name__ == "__main__":
    adjmatrix = strong_cohernet_digraph(7,0.4)
    weight_adjmatrix = add_weights_to_adjmatrix(10,-5,adjmatrix)
    # adjmatrix = [[0, 1, 1, 0, 1, 0, 0],
    #          [1, 0, 1, 1, 1, 0, 1],
    #          [0, 0, 0, 0, 0, 1, 0],
    #          [0, 1, 0, 0, 0, 0, 1],
    #          [0, 0, 0, 0, 0, 0, 1],
    #          [0, 1, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 1, 0]]
    # print(adjmatrix)
    # weight_adjmatrix = [[0, 6, 1, 2, -1, -1, -5],
    #          [10, 0, -5, -4, 4, -3, 0],
    #          [21, 11, 0, 7, 15, 2, 11],
    #          [15, 5, 0, 0, 9, 2, 5],
    #          [19, 9, 4, 5, 0, 0, -4],
    #          [19, 9, 4, 5, 13, 0, 9],
    #          [23, 13, 8, 9, 17, 4, 0]]
    # print(weight_adjmatrix)
    D, s_adjmatrix, positive_weight_adjmatirx = johnson(adjmatrix,weight_adjmatrix)
    print(D)
    G = draw_digraph_from_adjmatrix(adjmatrix=adjmatrix, weights=weight_adjmatrix)