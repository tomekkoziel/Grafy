import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Funkcja sprawdzająca czy ciąg jest graficzny
def check_if_graphical(matrix):
    while(True):
        sum = 0
        matrix = sorted(matrix,reverse=True)
        # Sprawdzenie czy ciąg nie jest już wyzerowany
        for num in matrix:
            sum += num
        if(sum == 0):
            return True
        # Sprawdzenie czy pierwsza liczba ciągu nie jest za duża
        if(matrix[0] >= len(matrix)):
            return False
        # Sprawdzenie czy nie ma liczb ujemnych
        for num in matrix:
            if(num < 0):
                return False
        # Redukowanie kolejnych n elementów, n = pierwszy wyraz ciągu
        for i in range(1,matrix[0]+1):
            matrix[i] -= 1
        matrix[0] = 0

# Funkcja zwracająca wierzchołki ciągu graficznego
def get_nodes_from_graphical(matrix):
    nodes = []
    for i in range(len(matrix)):
        nodes.append(i+1)
    
    # print(nodes)
    return nodes


# Funkcja zwracająca krawędzie ciągu graficznego
def get_edges_from_graphical(matrix, nodes):
    matrix = sorted(matrix, reverse=True)
    edges = []
    sum = 0
    while(True):
        # Sprawdzenie czy ciąg nie jest już wyzerowany
        sum = 0
        for num in matrix:
            sum += num
        if(sum == 0):
            break
        # Sortowanie ciągu z zachowaniem kolejności wierzchołków
        for i in range(len(matrix)):
            for j in range(0,len(matrix)-i-1):
                if(matrix[j] < matrix[j+1]):
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                    nodes[j], nodes[j+1] = nodes[j+1], nodes[j]
         # Redukowanie kolejnych n elementów, n = pierwszy wyraz ciągu
        for i in range(1,matrix[0]+1):
            matrix[i] -= 1
            edges.append((nodes[0],nodes[i]))
        matrix[0] = 0
    
    # print(edges)
    return edges

# Funkcja rysująca graf
def draw_graph(nodes, edges, colors = '#ffa059'):
    G = nx.Graph()
    # Posortowanie wierzchołków (dla lepszego wyglądu grafu)
    nodes = sorted(nodes)
    # Dodanie wierzchołków do grafu
    G.add_nodes_from(nodes)
    # Dodanie krawędzi do grafu
    G.add_edges_from(edges)
    # Rysowanie grafu
    nx.draw(G, nx.circular_layout(G), with_labels = True, node_color = colors, edgecolors = '#ff6d01')
    
# Funkcja zmieniająca krawędzie n razy
def randomize_graph(edges, n):
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


def components(nodes, edges):
    nr = 0
    # Dodanie wszystkich wierzchołków jako nieodwiedzone
    comp = np.zeros(len(nodes), dtype=int)
    for i in range(len(comp)):
        comp[i] = -1
    # Odwiedzanie wszystkich nieodwiedzonych wierzchołków
    for node in nodes:
        if comp[node - 1] == -1:
            nr += 1
            comp[node - 1] = nr
            components_R(nr, node, comp, edges)
    
    # print(comp)
    return comp

def components_R(nr, node, comp, edges):
    neighbours = []
    # Znalezienie wszystkich sąsiadów dla wierzchołka node
    for edge in edges:
        if(node == edge[0]):
            neighbours.append(edge[1])
        elif(node == edge[1]):
            neighbours.append(edge[0])
    # Odwiedzenie sąsiadów wszystkich sąsiadów dla wierzchołka node, jeśli nieodwiedzeni
    for neighbour in neighbours:
        if(comp[neighbour - 1] == -1):
            comp[neighbour - 1] = nr
            components_R(nr, neighbour, comp, edges)

    
def task1(path):
    matrix = np.loadtxt(path, delimiter=" ", dtype=int)
    if(check_if_graphical(matrix)):
        print("Ciąg jest graficzny")
        nodes = get_nodes_from_graphical(matrix)
        edges = get_edges_from_graphical(matrix, nodes)
        draw_graph(nodes, edges)
        # print(nodes, edges)
    else:
        print("Ciąg nie jest graficzny")
        # print(matrix)
    plt.show()

def task2(path):
    with open(path) as file:
        n = int(file.readline())
        matrix = []
        row = list(map(int, file.readline().split()))
        matrix.append(row)
    matrix = matrix[0]
    if(check_if_graphical(matrix)):
        print("Ciąg jest graficzny")
        nodes = get_nodes_from_graphical(matrix)
        edges = get_edges_from_graphical(matrix, nodes)
        # draw_graph(nodes, edges)
        edges = randomize_graph(edges, n)
        draw_graph(nodes, edges)
    else:
        print("Ciąg nie jest graficzny")
    plt.show()


def task3(path):
    matrix = np.loadtxt(path, delimiter=" ", dtype=int)
    if(check_if_graphical(matrix)):
        print("Ciąg jest graficzny")
        nodes = get_nodes_from_graphical(matrix)
        edges = get_edges_from_graphical(matrix, nodes)
        comp = components(nodes, edges)
        draw_graph(nodes, edges, colors = comp)
        counter = 1
        while(True):
            if(max(comp) + 1 == counter):
                break
            print(str(counter) + ")", end=" ")
            for i in range(len(comp)):
                if(comp[i] == counter):
                    print(str(i+1),end=" ")
            print("\n")
            counter += 1
            
    else:
        print("Ciąg nie jest graficzny")
    plt.show()

if __name__ == '__main__':
    task1("./data_ex1.txt")
    task2("./data_ex2.txt")
    task3("./data_ex3.txt")



