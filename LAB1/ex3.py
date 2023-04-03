import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def make_rand_graph_edges(n, l):
    if(l<0 or l > n*(n-1)/2):
        print("Liczba krawędzi musi być z przedziału [0,(n*(n-1))/2]")
        return 0
    if(n<0):
        print("Liczba wierzchołków musi być większa od zera.")
        return 0
    matrix = np.zeros((n,n),dtype=int)
    i = 0
    while(i<l):
        row, col = np.random.choice(range(n), size=2, replace=False)
        if(row > col and matrix[row][col] != 1):
            matrix[row][col] = 1
            matrix[col][row] = 1
            i = i+1
    print(matrix) 
    return matrix

def make_rand_graph_propability(n, p):
    if(p < 0 or p > 1):
        print("Prawdopodobieństwo musi być z przedziału [0,1].")
        return 0
    if(n<0):
        print("Liczba wierzchołków musi być większa od zera.")
        return 0
    matrix = np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j] = random.choices([0,1],weights=[1-p,p],k=1)[0]
            matrix[j][i] = matrix[i][j]
    print(matrix)
    return matrix

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

def task3(n,l,p):

    if(l==0):
        matrix = make_rand_graph_propability(n,p)
    elif(p==0):
        matrix = make_rand_graph_edges(n,l)
    else:
        return 0
    G = nx.Graph()
    G.add_edges_from(get_edges_from_adjmatrix(matrix))
    G.add_nodes_from(get_nodes_from_adjmatrix(matrix))
    nx.draw(G,pos=nx.circular_layout(G),with_labels=True, node_color= '#ffa059',node_size = [1000] * len(matrix), edgecolors = '#ff6d01')
    plt.show()

task3(5,0,0.5)
task3(5,10,0)