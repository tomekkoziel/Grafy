import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_circular_graph(G):
    # Liczba wierzchołków
    n = G.number_of_nodes()
    
    # Kąt pomiędzy wirzchołkami grafu
    alpha = 2 * np.pi / n
    
    # Pozycja startowa i promień
    x_0, y_0, r = 0, 0, 20
    
    # Słownik przechowywujący pozycje kolejnych wierzchołków
    positions = {}
    
    for i in range(n+1):
        positions.update(
            {(i ): np.array([x_0 + r * np.cos(i * alpha), y_0 + r * np.sin(i * alpha)])})

    # Rysowanie
    nx.draw(G, pos=positions, node_color="#ff6d01", node_size=600, with_labels=True)
    plt.show()
    
    # Testowanie
    # plt.savefig("graph.png")