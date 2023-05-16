import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
from ex1 import make_rand_digraph_adjmatrix, draw_digraph_from_adjmatrix

def kosajaru(adjmatrix):
    comp = []
    d = np.zeros(len(adjmatrix), dtype=int)
    f = np.zeros(len(adjmatrix), dtype=int)
    nodes = np.zeros(len(adjmatrix), dtype=int)
    for i in range(len(d)):
        nodes[i] = i
        d[i] = -1
        f[i] = -1
    t = [0]
    # print(nodes)
    for node in nodes:
        if d[node] == -1:
            dfs_visit(node, adjmatrix, d, f, t)
            # print(t)
    transposed_adjmatrix = np.transpose(adjmatrix)
    # print(f)
    # print(d)
    nr = 0
    comp = np.zeros(len(transposed_adjmatrix), dtype=int)
    tmp_nodes, f = bubble_sort(nodes, f)
    # print("\n")
    # print(f)
    # print(tmp_nodes)
    for i in range(len(comp)):
        comp[i] = -1
    for node in tmp_nodes:
        if comp[node] == -1:
            nr += 1
            comp[node] = nr
            components_r(nr,node,transposed_adjmatrix,comp)
    return comp

def dfs_visit(node, adjmatrix, d, f, t):
    t[0] += 1
    d[node] = t[0]
    # stack.append(node)
    # print(adjmatrix[node])
    for v in range(len(adjmatrix[node])):
        if adjmatrix[node][v] == 1 and d[v] == -1:
            dfs_visit(v,adjmatrix,d,f,t)
            break
    t[0] += 1
    f[node] = t[0]


def components_r(nr,node,adjmatrix,comp):
    for v in range(len(adjmatrix[node])):
        if adjmatrix[node][v] == 1 and comp[v] == -1:
            comp[v] = nr
            components_r(nr,v,adjmatrix,comp)


def bubble_sort(nodes, f):
    for i in range(len(nodes)):
        for j in range(len(nodes) - 1 - i):
            if f[j] < f[j+1]:
                f[j], f[j + 1] = f[j + 1], f[j]
                nodes[j], nodes[j + 1] = nodes[j + 1], nodes[j]
    return nodes, f



if __name__ == "__main__":
    adjmatrix = make_rand_digraph_adjmatrix(8,0.4)
    # adjmatrix = [[0, 1, 1, 0, 1, 0, 0],
    #              [1, 0, 1, 1, 1, 0, 1],
    #              [0, 0, 0, 0, 0, 1, 0],
    #              [0, 1, 0, 0, 0, 0, 1],
    #              [0, 0, 0, 0, 0, 0, 1],
    #              [0, 1, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 1, 0]]
    # print(adjmatrix)
    comp = kosajaru(adjmatrix)
    print(comp)
    draw_digraph_from_adjmatrix(adjmatrix, colors=comp)