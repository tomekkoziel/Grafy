import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from LAB1.ex1 import  draw_circular_graph
from utility import read_from_file

def is_hamilton(G):
    n = G.number_of_nodes()
    
    # Twierdzenie Diraca
    if n >= 3 and not (any(G.degree(node) < n / 2 for node in G.nodes)):
        print("Graf jest hamiltonowski.")
    

if __name__ == '__main__':
    G = nx.Graph()
    G = read_from_file('data_ex6.txt')
    draw_circular_graph(G)
    
    is_hamilton(G)