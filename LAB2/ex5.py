import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random

from LAB1.ex2 import draw_circular_graph

# Funkcja szukająca k-regularnego grafu
def generate_k_regular_graph(n, k):
    if k % 2 == 1 and n % 2 == 1:
        raise ValueError("Cannot create a k-regular graph with both k and n odd")
    
    if k >= n:
        raise ValueError("k must be less than n")
    
    G = find_the_edges(n, k)
    
    return G

def find_the_edges(n, k):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    nodes = list(G.nodes())
    counter = 0
    for i in range(n):
        while G.degree(nodes[i]) < k:
            j = random.choice(range(n))
            if i != j and G.degree(nodes[j]) < k:
                G.add_edge(nodes[i], nodes[j])
            else:
                counter += 1
            if counter == 1000:
                G.remove_edges_from(G.edges)
                G.remove_nodes_from(range(n))
                G = find_the_edges(n, k)

    return G
        
        

if __name__ == '__main__':
    draw_circular_graph(generate_k_regular_graph(7, 4))