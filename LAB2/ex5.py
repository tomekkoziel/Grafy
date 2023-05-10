import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random
from operator import itemgetter
import numpy as np

from LAB1.ex2 import draw_circular_graph
from LAB1.ex3 import get_edges_from_adjmatrix, get_nodes_from_adjmatrix
from ex123 import randomize_graph


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
            
def randomize_graph(edges):
    while(n != 0):
        is_edge_in_graph = False
        is_loop = False
        # Losowanie indexów krawędzi do zmiany
        idx = np.random.choice(len(edges),size=2, replace=False) 
        # Przypisanie krawędzi oraz zamiana ich wierzchołków
        edge1 = edges[idx[0]]
        edge2 = edges[idx[1]]
        edge1,edge2 = (edge1[0],edge2[1]),(edge1[1],edge2[0])  
        # Sprawdzanie czy nowe krawędzie nie istnieją już w grafie oraz czy nie ma pętli
        for edge in edges:
            if(edge1[0] == edge1[1] or edge2[0] == edge2[1]):
                is_loop = True
                break
            if(((edge[0] == edge1[0]) and (edge[1] == edge1[1])) or ((edge[1] == edge1[0]) and (edge[0] == edge1[1]))):
                is_edge_in_graph = True
                break
            elif(((edge[0] == edge2[0]) and (edge[1] == edge2[1])) or ((edge[1] == edge2[0]) and (edge[0] == edge2[1]))):
                is_edge_in_graph = True
                break
        # Zmiana krawędzi gdy nie ma takiej w grafie oraz nie ma petli
        if((not is_edge_in_graph) and (not is_loop)):
            edges[idx[0]] = edge1
            edges[idx[1]] = edge2
            n -= 1

    # print(edges)        
    return edges

def generate_k_regular_graph(nodes, k):
    if k > nodes or k % 2 == 1 and nodes % 2 == 1:
        sys.exit("Wrong arguments")

    G = nx.Graph()
    adjmatrix = generate_random_np(nodes, k / nodes)
    G.add_nodes_from(get_nodes_from_adjmatrix(adjmatrix))
    G.add_edges_from(get_edges_from_adjmatrix(adjmatrix))

    if any(G.degree(node) % k for node in G.nodes):
        return
    
    if any((G.degree(node) % 2) == 1 for node in G.nodes):

    draw_circular_graph(G)



if __name__ == '__main__':
    generate_k_regular_graph(6, 3)