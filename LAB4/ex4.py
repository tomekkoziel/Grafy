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
    s_adjmatrix, s_weight_adjmatrix = add_s(adjmatrix, weight_adjmatrix)
    n = len(s_adjmatrix)
    if belman_ford(s_adjmatrix,s_weight_adjmatrix, n-1)[0] == False:
        sys.exit("G zawiera cykl o ujemnej wadze.")
    else:
        _, ds = belman_ford(s_adjmatrix,s_weight_adjmatrix, n-1)
        nodes = get_nodes_from_adjmatrix(s_adjmatrix)
        h = []
        for node in nodes:
            h.append(ds[node-1])
        positive_weights_adjmatrix = np.zeros((n+1,n+1), dtype=int)
        for i in range(n):
            for j in range(n):
                if s_adjmatrix[i][j] == 1:
                    positive_weights_adjmatrix[i][j] = s_weight_adjmatrix[i][j] + h[i] - h[j]
        D = np.zeros((n,n), dtype=int)
        nodes = get_nodes_from_adjmatrix(adjmatrix)
        for node in nodes:
            du, _ = dijkstra(adjmatrix, weight_adjmatirx, node-1)
            for v in nodes:
                D[node-1][v-1] = du[v-1] - h[node-1] + h[v-1]
        return D, s_adjmatrix, positive_weights_adjmatrix




def add_s(adjmatrix, weight_adjmatrix):
    n = len(adjmatrix)
    s_adjmatrix = np.zeros((n+1,n+1), dtype=int)
    s_weight_adjmatrix = np.zeros((n+1,n+1), dtype=int)
    for i in range(n):
        for j in range(n):
            s_adjmatrix[i][j] = adjmatrix[i][j]
            s_weight_adjmatrix[i][j] = weight_adjmatrix[i][j]
    for i in range(n):
        s_adjmatrix[n][i] = 1
    return s_adjmatrix, s_weight_adjmatrix


if __name__ == "__main__":
    adjmatrix = strong_cohernet_digraph(7,0.4)
    weight_adjmatirx = add_weights_to_adjmatrix(10,-5,adjmatrix)
    print(weight_adjmatirx)
    D, s_adjmatrix, positive_weight_adjmatirx = johnson(adjmatrix,weight_adjmatirx)
    print(D)
    draw_digraph_from_adjmatrix(s_adjmatrix, weights=positive_weight_adjmatirx)