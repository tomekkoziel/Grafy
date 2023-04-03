import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def check_if_graphical(matrix):
    # print(matrix)
    adjmatrix = np.zeros((len(matrix),len(matrix)),dtype=int)
    while(True):
        counter = 0
        matrix = sorted(matrix,reverse=True)
        for num in matrix:
            if(num == 0):
                counter = counter +1
        if(counter == len(matrix)):
            return True
        if(matrix[0] >= len(matrix)):
            return False
        for num in matrix:
            if(num < 0):
                return False
        for i in range(1,matrix[0]+1):
            matrix[i] -= 1
        matrix[0] = 0
        #print(matrix)

def draw_graph(matrix):
    matrix = sorted(matrix,reverse=True)
    nodes = np.zeros(len(matrix),dtype=int)
    keep_going = True
    sum = 0
    G = nx.Graph()
    for i in range(len(matrix)):
        nodes[i] = i + 1
        G.add_node(i+1)
    while(keep_going):
        for num in matrix:
            sum += num
        if(sum == 0):
            keep_going = False
        sum = 0
        for i in range(len(matrix)):
            for j in range(0,len(matrix)-i-1):
                if(matrix[j] < matrix[j+1]):
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                    nodes[j], nodes[j+1] = nodes[j+1], nodes[j]
        for i in range(1,matrix[0]+1):
            matrix[i] -= 1
            G.add_edge(nodes[0],nodes[i])
        matrix[0] = 0
    
    nx.draw(G, pos = nx.circular_layout(G), with_labels=True, node_color = '#ffa059', edgecolors = '#ff6d01')


def draw_randomize_graph(matrix, n):
    matrix = sorted(matrix,reverse=True)
    nodes = np.zeros(len(matrix),dtype=int)
    edges = []
    keep_going = True
    sum = 0
    G = nx.Graph()
    G_rand = nx.Graph()
    for i in range(len(matrix)):
        nodes[i] = i + 1
        G.add_node(i+1)
        G_rand.add_node(i+1)
    while(keep_going):
        for num in matrix:
            sum += num
        if(sum == 0):
            keep_going = False
        sum = 0
        for i in range(len(matrix)):
            for j in range(0,len(matrix)-i-1):
                if(matrix[j] < matrix[j+1]):
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                    nodes[j], nodes[j+1] = nodes[j+1], nodes[j]
        for i in range(1,matrix[0]+1):
            matrix[i] -= 1
            G.add_edge(nodes[0],nodes[i])
            edges.append((nodes[0],nodes[i]))
        matrix[0] = 0
    print(edges)
    
    while(n != 0):
        is_edge_in_graph = False
        idx = np.random.choice(len(edges),size=2, replace=False)
        edge1 = edges[idx[0]]
        edge2 = edges[idx[1]]
        #print(edge1)
        #print(edge2)
        edge1,edge2 = (edge1[0],edge2[1]),(edge1[1],edge2[0])
        #print(edge1)
        #print(edge2)                             
        for edge in edges:
            if(edge1[0] == edge1[1] or edge2[0] == edge2[1]):
                break
            if(((edge[0] == edge1[0]) and (edge[1] == edge1[1])) or ((edge[1] == edge1[0]) and (edge[0] == edge1[1]))):
                is_edge_in_graph = True
            elif(((edge[0] == edge2[0]) and (edge[1] == edge2[1])) or ((edge[1] == edge2[0]) and (edge[0] == edge2[1]))):
                is_edge_in_graph = True
            if(is_edge_in_graph == False):
                edges[idx[0]] = edge1
                edges[idx[1]] = edge2
                n -= 1
                break
        print(idx)
        print(edge2)
        print(edge1)
        print(edges)
    G_rand.add_edges_from(edges)
    plt.figure("Graph")
    nx.draw(G, pos = nx.circular_layout(G), with_labels=True, node_color = '#ffa059', edgecolors = '#ff6d01')
    plt.figure("Rand Graph")
    nx.draw(G_rand, pos = nx.circular_layout(G_rand), with_labels=True, node_color = '#ffa059', edgecolors = '#ff6d01')



def task1(path):
    matrix = np.loadtxt(path, delimiter=" ", dtype=int)
    if(check_if_graphical(matrix)):
        print("Ciąg jest graficzny")
        draw_graph(matrix)
    else:
        print("Ciąg nie jest graficzny")
        print(matrix)
    plt.show()

def task2(path):
    with open(path) as file:
        n = int(file.readline())
        matrix = []
        row = list(map(int, file.readline().split()))
        matrix.append(row)
    matrix = matrix[0]
    if(check_if_graphical(matrix)):
        print(matrix)
        print(n)
        print("Ciąg jest graficzny")
        #draw_graph(matrix)
        draw_randomize_graph(matrix, n)
    else:
        print("Ciąg nie jest graficzny")
    plt.show()


#task1("./data_ex1.txt")
task2("./data_ex2.txt")




