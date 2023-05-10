import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random

from LAB1.ex1 import draw_circular_graph
from utility import is_bridge, find_neighbors
from ex123 import get_nodes_from_graphical, get_edges_from_graphical, check_if_graphical

def is_euler(G):
    if any((G.degree(node) % 2) == 1 for node in G.nodes):
        return False
    
    return True

# Tworzenie grafu eulerowskiego z losowej sekwencji 
def create_random_euler_graph(v_count):
    flag = True

    while(flag == True):
        # Losowanie sekwencji funkcją
        sequence = create_sequence_graph(v_count)

        # Sprawdzenie czy sekwencja jest graficzna
        if check_if_graphical(sequence):

            # Kreacja grafu
            nodes = get_nodes_from_graphical(sequence)
            edges = get_edges_from_graphical(sequence, nodes)

            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)
        
            # Sprawdzenie czy graf jest eulerowski i ewentualne zwrócenie grafu
            if is_euler(G):
                flag = False
                return G


def fleury(G):
    # Sprawdzenie czy graf jest eulerowski
    if not is_euler(G):
        sys.exit("This is not an eulerian graph")
    
    # Kopia grafu, żeby nie psuć oryginalnego
    Gc = G.copy()
    
    # Ustalenie stosu do zapisywania cyklu eulera oraz początkowego wierzchołka
    euler_cycle = []
    current_node = 1

    while len(Gc.edges) > 0:
        # Ustalenie następnego wierzchołka na podstawie sąsiadów aktualnego wierzchołka
        next_node = None
        for neighbor in find_neighbors(Gc, current_node):
            # Sprawdzenie czy dany sąsiad tworzy z aktualnym wierzchołkiem most
            if not is_bridge(Gc, current_node, neighbor):
                next_node = neighbor
                break

        # Jeśli zostały tylko mosty, wybieramy dowolny dostępny z sąsiadów
        if next_node is None:
            next_node = next(iter(find_neighbors(Gc, current_node)))

        # Usunięcie krawędzi z grafu, dla łatwiejszego szukania cyklu
        Gc.remove_edge(current_node, next_node)
        # Dodanie krawędzi do cyklu
        euler_cycle.append((current_node, next_node))

        # Update the current node
        current_node = next_node
    
    return euler_cycle

# Losowanie sekwencji dla grafu
def create_sequence_graph(size):
    sequence = [random.randrange(2, size, 2) for _ in range(size)]
    # print('graph sequence: ', sequence)
    return sequence


def task4():
    # G = read_from_file("data4.txt")
    # print("True" if is_euler(G) else "False")
    
    G = create_random_euler_graph(9)
    # print(list(nx.eulerian_circuit(G)))
    print(fleury(G))

    draw_circular_graph(G)


if __name__ == '__main__':
    task4()