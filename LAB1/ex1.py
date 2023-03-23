import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def adj_matrix_to_adj_list(matrix):
    adjlist = []

    for i in range(len(matrix)):
        adjlist.append([i])
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjlist[i].append(j + 1)

    return adjlist

def adj_matrix_to_incidence_matrix(adjmatrix):
    edges = get_edges_from_adjmatrix(adjmatrix)
    number_of_edges = len(edges)
    number_of_nodes = len(adjmatrix)

    incmatrix = np.zeros((number_of_nodes, number_of_edges), dtype = int)

    for j in range(number_of_edges):
        for i in (edges[j]):
            incmatrix[i - 1][j] = 1

    return incmatrix
            

def adj_list_to_adj_matrix(list):
    adjmatrix = np.zeros((len(list), len(list)), dtype = int)

    for i in range(len(list)):
        for j in (list[i][1:]):
            adjmatrix[i][j - 1] = 1

    return adjmatrix
                

def print_adjacency_list(adjlist):
    print("\nAdjacency list:")
    for i in range(len(adjlist)):
        print(str(adjlist[i][0] + 1) + ": ", end = "")
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


def get_nodes_from_adjmatrix(adjmatrix):
    nodes = []
    for i in range(1, len(adjmatrix) + 1):
        nodes.append(i)

    return nodes

def get_edges_from_adjmatrix(adjmatrix):
    edges = []
    
    for i in range(len(adjmatrix)):
        for j in range(i, len(adjmatrix[i])):
            if adjmatrix[i][j] == 1:
                e = (i + 1, j + 1)
                edges.append(e)

    return edges


def task1():
    G = nx.Graph()
    input = np.loadtxt('input/adjmatrix.txt', delimiter = ' ', dtype = 'int')


    adjmatrix = input
    print_adjacency_matrix(adjmatrix)

    adjlist = adj_matrix_to_adj_list(adjmatrix)
    print_adjacency_list(adjlist)
    print_incidence_matrix(adj_matrix_to_incidence_matrix(adjmatrix))
    

    # add all nodes to the graph
    nodes = get_nodes_from_adjmatrix(adjmatrix)
    G.add_nodes_from(nodes)

    edges = get_edges_from_adjmatrix(adjmatrix)
    G.add_edges_from(edges)
    print(edges)

    
    nx.draw(G, pos = nx.circular_layout(G), with_labels=True, node_color = '#ffa059',
            node_size = [1000] * len(adjmatrix), edgecolors = '#ff6d01')
    # plt.show()


task1()

