import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from LAB3.ex1 import generate_connected_graph, draw_weighted_graph

def init(G, s):
    n = len(G)
    
    ds = np.array([np.inf for i in range(n)])
    ps = np.array([-1 for i in range(n)])
    ds[s] = 0
    
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = np.inf
    
    return ds, ps
    
def relax(u, v, w, ds, ps):
    if ds[v] > ds[u] + w[u][v]:
        ds[v] = ds[u] + w[u][v]
        ps[v] = u
        
def dijkstra(G, w, s):
    s = s-1
    n = len(G)
    ds, ps = init(G, s)
    S = set()
    Q = {i: ds[i] for i in range(n)}
    
    while Q:
        u = min(Q, key=Q.get)
        if ds[u] == np.inf:
            break
        del Q[u]
        S.add(u)
        
        for v in range(n):
            if G[u][v] != 0 and v not in S:
                relax(u, v, w, ds, ps)
                Q[v] = ds[v]
                
    return ds, ps

def print_shortest_paths(ds, ps, s):
    for i in range(len(ds)):
        path = [i]
        j = i
        while j != -1:
            j = ps[j]
            path.insert(0, j)
        print(f'd({i+1}) = {ds[i]} ==> {path}')
        
if __name__ == '__main__':
    
    G_temp = generate_connected_graph(10)
    draw_weighted_graph(G_temp)
    
    G = nx.to_numpy_array(G_temp)
    print(G)
    ds, ps = dijkstra(G, G, 1)
    print(ds)
    print(ps)
    
    print_shortest_paths(ds, ps, 1)