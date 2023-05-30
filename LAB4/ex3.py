import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex1 import make_rand_digraph_adjmatrix, draw_digraph_from_adjmatrix
from ex2 import kosajaru
from LAB3.ex2 import init, relax

def strong_cohernet_digraph(n, p):
    adjmatrix = []
    counter = 0
    # Sprawdzenie czy graf jest silnie spójny
    while True:
        adjmatrix = make_rand_digraph_adjmatrix(n, p)
        if all(el == 1 for el in kosajaru(adjmatrix)):
            break
        counter += 1
        if counter > 100000:
            sys.exit("Ponad 100000 losowań, brak grafu silnie spójnego")
    return adjmatrix

def add_weights_to_adjmatrix(max, min, adjmatrix):
    weight_adjmatrix = np.copy(adjmatrix)
    # Dodanie wag do grafu skierowanego
    for i in range(len(adjmatrix)):
        for j in range(len(adjmatrix)):
            if(weight_adjmatrix[i][j] == 1):
                weight_adjmatrix[i][j] = random.randint(min,max)
    return weight_adjmatrix

def belman_ford(adjmatrix, weight_adjmatrix, s):
    # Alokacja pamięci
    ds, ps = init(adjmatrix,s)
    # Relaksacja 
    for i in range(1,len(adjmatrix)):
        for u in range(len(adjmatrix)):
            for v in range(len(adjmatrix)):
                if adjmatrix[u][v] == 1:
                    relax(u,v,weight_adjmatrix, ds, ps)
    # Znajdowanie najktotszych sciezek
    for i in range(1,len(adjmatrix)):
        for u in range(len(adjmatrix)):
            for v in range(len(adjmatrix)):
                if adjmatrix[u][v] == 1:
                    if ds[v] > ds[u] + weight_adjmatrix[u][v]:
                        return False, ds
    return True, ds

if __name__ == "__main__":
    adjmatrix = strong_cohernet_digraph(7,0.1)
    # adjmatrix = [[0, 1, 1, 0, 1, 0, 0],
    #          [1, 0, 1, 1, 1, 0, 1],
    #          [0, 0, 0, 0, 0, 1, 0],
    #          [0, 1, 0, 0, 0, 0, 1],
    #          [0, 0, 0, 0, 0, 0, 1],
    #          [0, 1, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 1, 0]]
    # print(adjmatrix)
    weight_adjmatrix = add_weights_to_adjmatrix(10, -5, adjmatrix)
    # weight_adjmatrix = [[0, 6, 1, 2, -1, -1, -5],
    #          [10, 0, -5, -4, 4, -3, 0],
    #          [21, 11, 0, 7, 15, 2, 11],
    #          [15, 5, 0, 0, 9, 2, 5],
    #          [19, 9, 4, 5, 0, 0, -4],
    #          [19, 9, 4, 5, 13, 0, 9],
    #          [23, 13, 8, 9, 17, 4, 0]]
    is_negative_cycle = not belman_ford(adjmatrix, weight_adjmatrix, 0)
    if is_negative_cycle:
        print("Istnieje negatywny cykl")
    else:
        print("Brak negatwynego cyklu")
    draw_digraph_from_adjmatrix(adjmatrix,weights=weight_adjmatrix)
