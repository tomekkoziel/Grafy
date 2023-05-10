import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx

from LAB1.ex1 import draw_circular_graph
from LAB1.ex3 import make_rand_graph_edges
from utility import read_from_file, is_bridge, find_neighbors
from ex123 import get_nodes_from_graphical, get_edges_from_graphical, check_if_graphical

edges = [[1,0,2], [4,2,3]]

print(edges[1][2])

stack = [0]
print(stack[-1])

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])

G.add_edges_from([(1, 2), (2, 3), (3, 1), (5, 2)])
G.remove_edges_from([(1, 2), (2, 3), (3, 1), (5, 2)])

G.update(edges=[(1, 2)])

draw_circular_graph(G)

