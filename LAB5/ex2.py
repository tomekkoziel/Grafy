import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from collections import deque 
from LAB5.ex1 import generate_random_flow_network, draw_flow_network

def bfs(G, source, target):
    # Inicjalizacja BFS
    visited = {source}
    # Skorzystano z degue, ponieważ umożliwia usuwanie elementów z początku oraz końca (użyto popleft)
    Q = deque([(source, [])])

    # Przeszukiwanie BFS
    while Q:
        v, path = Q.popleft()
        for u in G.neighbors(v):
            # Sprawdzenie czy krawędź ma dostępną przepustowość (czy nie jest ujemna oraz czy wierzchołek u nie został już odwiedzony)
            if G.edges[v, u]['capacity'] - G.edges[v, u]['flow'] > 0 and u not in visited:
                visited.add(u)
                new_path = path + [(v, u)]
                if u == target:
                    return new_path
                Q.append((u, new_path))

    return None

def ford_fulkerson(G, s, t):
    # Zerowanie przepływów
    for u, v in G.edges:
        G.edges[u, v]['flow'] = 0

    # Generowanie sieci residualnej znalezienie ścieżki rozszerzającej "path"
    path = bfs(G, s, t)
    while path:
        # przepustowość rezydualna ścieżki = najmniejsza przepustowość rezydualna jej krawędzi
        min_capacity = min(G.edges[u, v]['capacity'] - G.edges[u, v]['flow'] for u, v in path)

        # Zwiększanie/kasowanie przepływu wzdłuż ścieżki "path"
        for u, v in path:
            if (u, v) in G.edges:
                G.edges[u, v]['flow'] += min_capacity
            else:
                G.edges[v, u]['flow'] -= min_capacity
        
        path = bfs(G, s, t)

    # Obliczenie całkowitego przepływu z źródła
    total_flow = sum(G.edges[s, v]['flow'] for v in G.successors(s))

    return total_flow

# Pomocnicza funkcja wypisująca wszystkie krawędzie wraz z wagami oraz przepływem
def print_edges(G):
    print("Krawędzie z wagami oraz przepływem:")
    for u, v, key in G.edges(data=True):
        capacity = key['capacity']
        flow = key['flow']
        print(f"Edge ({u}, {v}) - Capacity: {capacity}, Flow: {flow}")
    print()

if __name__ == '__main__':
    number_of_layers = 2  
    G = generate_random_flow_network(number_of_layers)
    draw_flow_network(G)
    
    print()
    
    max_flow = ford_fulkerson(G, 0, len(G) - 1)
    print_edges(G)
    print("Maksymalny przepływ:", max_flow)