import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LAB1.ex2 import draw_circular_graph

# Zamiana macierzy sąsiedztwa na listę sąsiedztwa
def adj_matrix_to_adj_list(matrix):
    adjlist = []

    # Jeśli 
    for i in range(len(matrix)):
        adjlist.append([i + 1])
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjlist[i].append(j + 1)

    return adjlist

# Zamiana macierzy sąsiedztwa na macierz incydencji
def adj_matrix_to_incidence_matrix(adjmatrix):
    edges = get_edges_from_adjmatrix(adjmatrix)
    number_of_edges = len(edges)
    number_of_nodes = len(adjmatrix)

    # Inicjalizacja macierzy incydencji od odpowiednich rozmiarach zerami 
    incmatrix = np.zeros((number_of_nodes, number_of_edges), dtype = int)

    # Dla każdej krawędzi jeśli wierzchołek jest z nią incydentny - zapisujemy w tym miejscu jedynkę
    for j in range(number_of_edges):
        for i in (edges[j]):
            incmatrix[i - 1][j] = 1

    return incmatrix
            
#  Zamiania listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(list):
    adjmatrix = np.zeros((len(list), len(list)), dtype = int)

    for i in range(len(list)):
        for j in (list[i][1:]):
            adjmatrix[i][j - 1] = 1

    return adjmatrix

# Zamiana macierzy incydencji na listę sąsiedztwa
def incidence_matrix_to_adj_list(incmatrix):

    # Ustalenie ilości wierzchołków
    vertices_number = len(incmatrix)

    # Zapisanie wszystkich krawędzi na podstawie macierzy incydencji, dedykowaną funkcją
    edges = get_edges_from_incmatrix(incmatrix)

    adjlist = [ [i + 1] for i in range(vertices_number) ]
    
    # Dla każdego wierzchołka dodaj drugi koniec krawędzi, z którą jest incydentny
    for i in range(vertices_number):
        for pair in edges:
            if pair[0] == i + 1:
                if pair[1] != -3:
                    adjlist[i].append(pair[1])
                    adjlist[pair[1] - 1].append(i + 1)

    return adjlist


                
# print functions
def print_adjacency_list(adjlist):
    print("\nAdjacency list:")
    for i in range(len(adjlist)):
        print(str(adjlist[i][0]) + ": ", end = "")
        print(*adjlist[i][1:], sep = ", ")
    print()

def print_adjacency_matrix(adjmatrix):
    print("\nAdjacency matrix:")
    for i in range(len(adjmatrix)):
        print(*adjmatrix[i], sep = "  ")
    print()

def print_incidence_matrix(incmatrix):
    print("\nIncidence matrix:")
    for i in range(len(incmatrix)):
        print(*incmatrix[i], sep = "  ")
    print()


# Zczytywanie wierzchołków z macierzy sąsiedztwa
def get_nodes_from_adjmatrix(adjmatrix):
    nodes = []
    for i in range(1, len(adjmatrix) + 1):
        nodes.append(i)

    return nodes

# Zczytywanie krawędzi z macierzy sąsiedztwa
def get_edges_from_adjmatrix(adjmatrix):
    edges = []
    
    for i in range(len(adjmatrix)):
        for j in range(i, len(adjmatrix[i])):
            if adjmatrix[i][j] == 1:
                e = (i + 1, j + 1)
                edges.append(e)

    return edges

# Zczytywanie krawędzi z macierzy incydencji
def get_edges_from_incmatrix(incmatrix):
    edges = []

    vertices_number = len(incmatrix)
    edges_number = len(incmatrix[0])
    
    for i in range(edges_number):
        v1 = -4
        v2 = -4
        for j in range(vertices_number):
            if incmatrix[j][i] == 1:
                if v1 == -4:
                    v1 = j
                else:
                    v2 = j
        e = (v1 + 1, v2 + 1)
        edges.append(e)
    return edges

def task1():
    G = nx.Graph()

    match sys.argv[2]:
        case 'am':
            # macierz sąsiedztwa
            adjmatrix = np.loadtxt(sys.argv[1], delimiter = ' ', dtype = 'int')
            print_adjacency_matrix(adjmatrix)

            # lista sąsiedztwa
            adjlist = adj_matrix_to_adj_list(adjmatrix)
            print_adjacency_list(adjlist)

            # macierz incydencji
            print_incidence_matrix(adj_matrix_to_incidence_matrix(adjmatrix))

            # dodanie wierzchołków
            nodes = get_nodes_from_adjmatrix(adjmatrix)
            G.add_nodes_from(nodes)

            # dodanie krawędzi
            edges = get_edges_from_adjmatrix(adjmatrix)

            # wyświetlenie krawędzi
            G.add_edges_from(edges)
            print("All edges:")
            print(edges)

            # wyświetlenie grafu
            draw_circular_graph(G)

        case 'al':
            # lista sąsiedztwa
            with open(sys.argv[1], 'r') as f:
                lines = f.readlines()
                
            adjlist = []
            
            for line in lines:
                nodes = list(map(int, line.split()))
                adjlist.append(nodes)

            print_adjacency_list(adjlist)

            # macierz sąsiedztwa
            adjmatrix = adj_list_to_adj_matrix(adjlist)
            print_adjacency_matrix(adjmatrix)

            # macierz incydencji
            incmatrix = adj_matrix_to_incidence_matrix(adjmatrix)
            print_incidence_matrix(incmatrix)

            nodes = get_nodes_from_adjmatrix(adjmatrix)
            G.add_nodes_from(nodes)

            edges = get_edges_from_adjmatrix(adjmatrix)
            G.add_edges_from(edges)
            
            print("All edges:")
            print(edges)

            draw_circular_graph(G)
            
        case 'im':
            # macierz incydencji
            incmatrix = np.loadtxt(sys.argv[1], delimiter = ' ', dtype = 'int')

            print_incidence_matrix(incmatrix)
            
            # lista sąsiedztwa
            adjlist = incidence_matrix_to_adj_list(incmatrix)
            print_adjacency_list(adjlist)
            
            # macierz sąsiedztwa
            adjmatrix = adj_list_to_adj_matrix(adjlist)
            print_adjacency_matrix(adjmatrix)
            
            nodes = get_nodes_from_adjmatrix(adjmatrix)
            G.add_nodes_from(nodes)

            edges = get_edges_from_adjmatrix(adjmatrix)
            G.add_edges_from(edges)
            
            print("All edges:")
            print(edges)

            draw_circular_graph(G)
            
        case _:
            print("Please specify input type")

    #####################
    # input musi byc typu: python ex1.py input/adjmatrix.txt "am"
    #####################
    
if __name__ == '__main__':
    task1()

