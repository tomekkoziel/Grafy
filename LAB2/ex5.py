import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import random
from operator import itemgetter
import numpy as np

<<<<<<< Updated upstream
from LAB1.ex2 import draw_circular_graph
from LAB1.ex3 import get_edges_from_adjmatrix, get_nodes_from_adjmatrix
=======
from LAB1.ex2 import drawCircularGraph
from LAB1.ex3 import get_edges_from_adjmatrix, get_nodes_from_adjmatrix, make_rand_graph_edges
>>>>>>> Stashed changes
from ex123 import randomize_graph
import utility

            
def randomize_graph(edges, n):
    while(n != 0):
        is_edge_in_graph = False
        is_loop = False
        # Losowanie indexów krawędzi do zmiany
        idx = np.random.choice(len(edges),size=2, replace=False)
        # Przypisanie krawędzi oraz zamiana ich wierzchołków
        edge1 = edges[idx[0]]
        edge2 = edges[idx[1]]
        edge1,edge2 = (edge1[0], edge2[1]), (edge1[1], edge2[0])
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

# def generate_k_regular_graph(nodes, k):
#     if k > nodes:
#         sys.exit("Stopień większy niż ilość wierzchołków") 

#     if k % 2 == 1 and nodes % 2 == 1:
#         sys.exit("Jeżeli k nieparzyste, to n parzyste") 

#     G = nx.Graph()
#     adjmatrix = make_rand_graph_edges(nodes, )
#     G.add_nodes_from(get_nodes_from_adjmatrix(adjmatrix))
#     edges = get_edges_from_adjmatrix(adjmatrix)
#     G.add_edges_from(edges)

#     print(edges)

#     drawCircularGraph(G)

#     edgescopy = edges.copy()

    # while True:
    #     if any(len(utility.find_neighbors_edges(edgescopy, node)) != k for node in G.nodes):
    #         edgescopy = randomize_graph(edgescopy, 1)
    #         print("x")
    #     else:
    #         break
        

#     print("Feeling lucky")
    
    # if any((G.degree(node) % 2) == 1 for node in G.nodes):

<<<<<<< Updated upstream
    draw_circular_graph(G)
=======
# def generate_k_regular_graph(n, k):
#     if k >= n:
#         raise ValueError("K should be lower than n")
    
#     # If k is odd and n is even, we cannot create a k-regular graph
#     if k % 2 == 1 and n % 2 == 0:
#         raise ValueError("Cannot create a k-regular graph with odd k and even n.")
    
#     # Initialize a graph with n nodes
#     G = nx.Graph()
#     G.add_nodes_from(range(n))
    
#     # Create a list of all possible edges
#     all_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    
#     # Initialize a list of edges to add to the graph
#     edges_to_add = []
    
#     # Repeat until the graph is k-regular
#     while any(G.degree(node) != k for node in G.nodes):
#         # Randomly shuffle the list of edges
#         random.shuffle(all_edges)
#         print("xd")
        
#         # Try adding each edge to the graph
#         for edge in all_edges:
#             if len(edges_to_add) >= n*k/2:
#                 break  # Stop if we've added enough edges
                
#             # Add the edge if it doesn't create a degree-2 vertex or a parallel edge
#             if G.degree(edge[0]) < k and G.degree(edge[1]) < k and not G.has_edge(*edge):
#                 edges_to_add.append(edge)
                
#         # Add the edges to the graph
#         G.add_edges_from(edges_to_add)
        
#         # Clear the list of edges to add
#         edges_to_add = []
        
#     return G
>>>>>>> Stashed changes

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
            print(G.degree(nodes[i]))
            j = random.choice(range(n))
            if i != j and G.degree(nodes[j]) < k:
                G.add_edge(nodes[i], nodes[j])
            else:
                counter += 1
            if counter == 1000:
                print("if")
                G.remove_edges_from(G.edges)
                G.remove_nodes_from(range(n))
                counter = 0
                G = find_the_edges(n, k)

    return G
        
        

if __name__ == '__main__':
    drawCircularGraph(generate_k_regular_graph(7, 2))