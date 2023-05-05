import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def drawCircularGraph(G):
    # Liczba wierzchołków
    n = G.number_of_nodes()
    
    # Kąt pomiędzy wirzchołkami grafu
    alpha = 2 * np.pi / n
    
    # Pozycja startowa i promień
    x_0, y_0, r = 0, 0, 20
    
    # Słownik przechowywujący posycje kolejnych wierzchołków
    positions = {}
    
    for i in range(n):
        positions.update(
            {(i ): np.array([x_0 + r * np.cos(i * alpha), y_0 + r * np.sin(i * alpha)])})

    # Rysowanie
    nx.draw(G, pos=positions)
    plt.show()