import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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
    plt.show()




def task1(path):
    matrix = np.loadtxt(path, delimiter=" ", dtype=int)
    if(check_if_graphical(matrix)):
        print("Ciąg jest graficzny")
        draw_graph(matrix)
    else:
        print("Ciąg nie jest graficzny")
        print(matrix)
    #plt.show()



task1("./data.txt")

