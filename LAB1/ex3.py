import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# Funckja tworząca macierz sąsiedztwa grafu o l krawędziach i n wierzchołkach
def make_rand_graph_edges(n, l):
    # Sprawdzenie warunków początkowych
    if(l<0 or l > n*(n-1)/2):
        print("Liczba krawędzi musi być z przedziału [0,(n*(n-1))/2]")
        return 0
    if(n<0):
        print("Liczba wierzchołków musi być większa od zera.")
        return 0
    adjmatrix = np.zeros((n,n),dtype=int)
    i = 0
    # Losowanie krawędzi grafu
    while(i<l):
        row, col = np.random.choice(range(n), size=2, replace=False)
        if(row > col and adjmatrix[row][col] != 1):
            adjmatrix[row][col] = 1
            adjmatrix[col][row] = 1
            i = i+1
    # print(adjmatrix) 
    return adjmatrix

# Funckja tworząca macierz sąsiedztwa grafu o n wierzchołkach oraz p prawdopodobieństwie istnienia krawędzi
def make_rand_graph_propability(n, p):
    # Sprawdzenie warunków początkowych
    if(p < 0 or p > 1):
        print("Prawdopodobieństwo musi być z przedziału [0,1].")
        return 0
    if(n<0):
        print("Liczba wierzchołków musi być większa od zera.")
        return 0
    adjmatrix = np.zeros((n,n),dtype=int)
    # Losowanie krawędzi grafu
    for i in range(n):
        for j in range(i+1,n):
            adjmatrix[i][j] = random.choices([0,1],weights=[1-p,p],k=1)[0]
            adjmatrix[j][i] = adjmatrix[i][j]
    # print(adjmatrix)
    return adjmatrix

# Funkcja zwracająca wierzchołki grafu
def get_nodes_from_adjmatrix(adjmatrix):
    nodes = []
    for i in range(1, len(adjmatrix) + 1):
        nodes.append(i)

    return nodes

# Funkcja zwracająca krawędzie grafu
def get_edges_from_adjmatrix(adjmatrix):
    edges = []
    for i in range(len(adjmatrix)):
        for j in range(i, len(adjmatrix[i])):
            if adjmatrix[i][j] == 1:
                e = (i + 1, j + 1)
                edges.append(e)

    return edges

# Funkcja rysująca graf z macierzy sąsiedztwa
def draw_graph_from_adjmatrix(adjmatrix):
    G = nx.Graph()
    G.add_edges_from(get_edges_from_adjmatrix(adjmatrix))
    G.add_nodes_from(get_nodes_from_adjmatrix(adjmatrix))
    nx.draw(G,pos=nx.circular_layout(G),with_labels=True, node_color= '#ffa059',node_size = [1000] * len(adjmatrix), edgecolors = '#ff6d01')


def task3(n, l = 0, p = 0):
    if(l==0):
        adjmatrix = make_rand_graph_propability(n,p)
    elif(p==0):
        adjmatrix = make_rand_graph_edges(n,l)
    draw_graph_from_adjmatrix(adjmatrix)
    plt.show()

if __name__ == '__main__':
    task3(n = 5, p = 0.1)   
    task3(n = 5, l = 9) 