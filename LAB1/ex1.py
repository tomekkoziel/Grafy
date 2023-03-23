import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def task1():
    G = nx.Graph()
    adjmatrix = np.loadtxt('input/adjmatrix.txt', delimiter = ' ', dtype = 'int')

    # add all nodes to the graph
    nodes = []
    edges = []
    for i in range(1, len(adjmatrix) + 1):
        nodes.append(i)

    G.add_nodes_from(nodes)

    adjlist = []
    # # print the adjacency matrix
    # for row in adjmatrix:
    #     print(row)
    for i in range(len(adjmatrix)):
        adjlist.append([i])
        for j in range(len(adjmatrix[i])):
            if adjmatrix[i][j] == 1:
                adjlist[i].append(j + 1)

    # printing the adjacency list
    print("Adjacency list:")
    for i in range(len(adjlist)):
        print(str(adjlist[i][0] + 1) + ": ", end = "")
        print(*adjlist[i][1:], sep = ", ")

    # add all the edges of the graph
    for i in range(len(adjmatrix)):
        for j in range(i, len(adjmatrix[i])):
            if adjmatrix[i][j] == 1:
                e = (i + 1, j + 1)
                edges.append(e)


    G.add_edges_from(edges)
    nx.draw(G, pos = nx.circular_layout(G), with_labels=True, node_color = '#ffa059',
            node_size = [1000] * len(adjmatrix), edgecolors = '#ff6d01')
    plt.show()


task1()

