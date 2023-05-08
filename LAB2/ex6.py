import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from utility import read_from_file

def is_hamilton(G):
    n = G.number_of_nodes()
    
    if n > 3 and not (any(G.degree(node) < n / 2 for node in G.nodes)):
        print("Graf jest hamiltonowski.")
    

if __name__ == '__main__':
    # G1 = nx.Graph()
    # G1.add_nodes_from([1, 2, 3, 4])
    # G1.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4)])
    # is_hamilton(G1)

    # G2 = nx.Graph()
    # G2.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
    # print(G2.nodes)
    G = nx.Graph()
    G = read_from_file('data_ex6.txt')
    is_hamilton(G)