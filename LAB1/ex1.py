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


def print_adjacency_list(adjlist):
    print("Adjacency list:")
    for i in range(len(adjlist)):
        print(str(adjlist[i][0] + 1) + ": ", end = "")
        print(*adjlist[i][1:], sep = ", ")


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

    adjlist = adj_matrix_to_adj_list(adjmatrix)
    print_adjacency_list(adjlist)

    # add all nodes to the graph
    nodes = get_nodes_from_adjmatrix(adjmatrix)
    G.add_nodes_from(nodes)

    edges = get_edges_from_adjmatrix(adjmatrix)
    G.add_edges_from(edges)
    
    nx.draw(G, pos = nx.circular_layout(G), with_labels=True, node_color = '#ffa059',
            node_size = [1000] * len(adjmatrix), edgecolors = '#ff6d01')
    plt.show()


task1()

