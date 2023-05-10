import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
import random
import networkx as nx
from LAB1.ex3 import make_rand_graph_edges, get_nodes_from_adjmatrix, get_edges_from_adjmatrix
from LAB3.ex1 import draw_weighted_graph, is_connected

def has_cycle(edges, nodes):
    visited = [False] * len(nodes)
    finished = [False] * len(nodes)

    def dfs(node, parent):
        visited[node - 1] = True
        # Szukanie sąsiadów wierzchołka
        for edge in edges:
            if node in edge:
                neighbour = edge[1] if edge[0] == node else edge[0]
                # Sprawdzenie czy był już odwiedzony
                if not visited[neighbour - 1]:
                    if dfs(neighbour, node):
                        return True
                # Sprawdzenie czy nie jest rodzicem
                elif neighbour != parent:
                    return True

        finished[node - 1] = True
        return False

    # Wywołanie dfs dla nieodwiedzonych wierzchołków
    for node in nodes:
        if not visited[node - 1]:
            if dfs(node, -1):
                return True

    return False

def bubble_sort(edges, weights):
    for i in range(len(weights)):
            for j in range(0,len(weights)-i-1):
                if(weights[j] > weights[j+1]):
                    weights[j], weights[j+1] = weights[j+1], weights[j]
                    edges[j], edges[j+1] = edges[j+1], edges[j]

def find_smallest_tree(n):
    # Tworzenie grafu spójnego
    while True:
        adjmatrix = make_rand_graph_edges(n, random.randint(n-1, (n*(n-1))/2))
        if is_connected(adjmatrix):
            break
    edges = get_edges_from_adjmatrix(adjmatrix)
    # Odsortowanie krawędzi
    random.shuffle(edges)
    nodes = get_nodes_from_adjmatrix(adjmatrix)
    # Dodanie wag do krawędzi
    weights = np.zeros(len(edges), dtype=int)
    for i in range(len(edges)):
        weights[i] = random.randint(1,10)
    # Posortowanie według wag
    bubble_sort(edges, weights)
    tree_edges = []
    tree_weights = []
    counter = 0
    # print(edges)
    # print(weights)
    while True:
        tmp_tree_edges = tree_edges.copy()
        tmp_tree_edges.append(edges[counter])
        # Sprawdzenie czy nie tworzy sie cykl
        if(not has_cycle(tmp_tree_edges, nodes)):
            tree_edges.append(edges[counter])
            tree_weights.append(weights[counter])
            print(tree_edges)
        # Koniec funkcji przy znalezieniu n-1 krawędzi
        if(len(tree_edges) == n-1):
            break
        counter += 1
    # Dodanie krawędzi do grafu
    G = nx.Graph()
    G.add_nodes_from(nodes)
    counter = 0
    for edge in tree_edges:
        G.add_edge(edge[0],edge[1], weight = tree_weights[counter])
        counter += 1
    return G

if __name__ == "__main__":
    G = find_smallest_tree(19)
    draw_weighted_graph(G)
