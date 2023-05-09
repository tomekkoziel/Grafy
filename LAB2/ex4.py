import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random
from operator import itemgetter

from LAB1.ex1 import drawCircularGraph
from LAB1.ex3 import make_rand_graph_edges
from utility import read_from_file, is_bridge, find_neighbors
from ex123 import get_nodes_from_graphical, get_edges_from_graphical, check_if_graphical

def is_euler(G):
    if any((G.degree(node) % 2) == 1 for node in G.nodes):
        return False
    
    return True

# Tworzenie grafu eulerowskiego z losowej sekwencji 
def create_random_euler_graph(v_count):
    flag = True

    while(flag == True):
        sequence = create_sequence_graph(v_count)
        if check_if_graphical(sequence):
            nodes = get_nodes_from_graphical(sequence)
            edges = get_edges_from_graphical(sequence, nodes)

            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)
        
            if is_euler(G):
                flag = False
                return G


def fleury(G):
    if not is_euler(G):
        print("This is not an eulerian graph")
        return
    
    Gc = G.copy()
    
    euler_cycle = []
    current_node = 1

    while len(Gc.edges) > 0:

        next_node = None
        for neighbor in find_neighbors(Gc, current_node):
            if not is_bridge(Gc, current_node, neighbor):
                next_node = neighbor
                break

        if next_node is None:
            next_node = next(iter(find_neighbors(Gc, current_node)))

        Gc.remove_edge(current_node, next_node)
        euler_cycle.append((current_node, next_node))

        # Update the current node
        current_node = next_node
    
    return euler_cycle


def task4():
    # G = read_from_file("data4.txt")
    # print("True" if is_euler(G) else "False")

    # print(list(nx.eulerian_circuit(G)))
    # print(fleury(G))

    # drawCircularGraph(G)
    G = create_random_euler_graph(9)

    # print(list(nx.eulerian_circuit(G)))
    print(fleury(G))
    drawCircularGraph(G)


def create_sequence_graph(size):
    sequence = [random.randrange(2, size, 2) for _ in range(size)]
    # print('graph sequence: ', sequence)
    return sequence

def set_euler_path(matrix):
        # https://cp-algorithms.com/graph/euler_path.html#algorithm
        stack = [0]
        answer = []
        while len(stack) != 0:
            v = stack[-1]
            if 1 not in matrix[v]:
                answer.append(v)
                stack.pop()
            else:
                edge = matrix[v].index(1)
                matrix[v][edge] = 0
                matrix[edge][v] = 0
                stack.append(edge)
        print([[i+1] for i in answer])


if __name__ == '__main__':
    # G1 = nx.Graph()
    # G1.add_nodes_from([1, 2, 3, 4])
    # G1.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4)])
    # is_hamilton(G1)

    # G2 = nx.Graph()
    # G2.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
    # print(G2.nodes)
    task4()