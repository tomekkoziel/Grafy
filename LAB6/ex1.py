import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

# Funkcja wyszukiwująca cykl Hamiltona
def is_hamilton(G):
    n = G.number_of_nodes()
    # Tablica przechowująca cykl Hamiltona
    cycle = []
    
    # Twierdzenie Diraca
    if n >= 3 and not (any(G.degree(node) < n / 2 for node in G.nodes)):
        print("Spełnione twierdzenie Diraca, graf jest hamiltonowski.")
    
    # Początkowy wierzchołek
    first_node = list(G.nodes)[0]
    hamilton_cycle_recursive(G, first_node, cycle)
    
    if len(cycle) == n:
        # Jeżeli wszystko się zgadza dodajemy pierwszy wierzchołek na koniec cyklu
        cycle.append(first_node)
        print("Cykl Hamiltona:", cycle)
    else:
        print("Graf nie jest hamiltonowski.")
    
# Rekursywna funkcja znajdująca cykl Hamiltona
def hamilton_cycle_recursive(G, node, cycle):    
    cycle.append(node)
    
    if len(cycle) == G.number_of_nodes():
        # Sprawdzenie czy ostatni element cykl jest połączony krawędzią z pierwszym elementem w cyklu
        # G.neighbors(node) - funkcja zwracająca sąsiadów wierzchołka node
        if cycle[-1] in G.neighbors(cycle[0]):
            return True
        
        # Jeżeli nie jest usuwamy ostatni element i dalej szukamy
        cycle.pop()
        return False
    
    # Rekrsywne przejście po nieodwiedzonych sąsiadach
    for neighbor in G.neighbors(node):
        if neighbor not in cycle:
            if hamilton_cycle_recursive(G, neighbor, cycle):
                return True
    
    # Jeżeli nie znaleziono cyklu czyścimy tablice cycle 
    cycle.pop()
    return False

def create_digraph_from_file(file_path):
    G = nx.DiGraph()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            node = line[0]
            neighbors = line[1].split(',')

            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

    return G

def create_digraph_from_adjlist(adjacency_list):
    G = nx.DiGraph()
    
    for node, neighbors in adjacency_list.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    return G

def pagerank_randomwalk(G):
    num_nodes = G.number_of_nodes()
    ranks = {node: 1 / num_nodes for node in G.nodes()}

    d = 0.15
    num_iterations = 100

    for _ in range(num_iterations):
        new_ranks = {}
        for node in G.nodes():
            rank_sum = sum(ranks[neighbor] / G.out_degree(neighbor) for neighbor in G.predecessors(node))
            new_ranks[node] = (1 - d) * rank_sum + d / num_nodes
        ranks = new_ranks

    return ranks

def pagerank_matrix(G, d=0.15, epsilon=1e-8, max_iterations=100):
    n = G.number_of_nodes()  # liczba wierzchołków
    p = {node: 1 / n for node in G.nodes()}  # inicjalizacja wektora obsadzeń p0

    iteration = 1
    for _ in range(max_iterations):
        p_next = {node: 0 for node in G.nodes()}
        for j in G.nodes():
            sum_p = sum((1 - d) * p[i] / G.out_degree(i) for i in G.predecessors(j))
            p_next[j] = sum_p + d / n
        if sum(abs(p_next[node] - p[node]) for node in G.nodes()) < epsilon:
            break
        p = p_next
        iteration += 1

    print(iteration)

    return p_next


if __name__ == '__main__':

    # Przykładowa lista sąsiedztwa
    adj_list = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': ['D']  
    }

    # Wczytanie ścieżki do pliku
    file_path = 'data/adjlist.txt'

    # Tworzenie digrafu na podstawie ścieżki/listy sąsiedztwa
    G = create_digraph_from_file(file_path)
    G1 = create_digraph_from_adjlist(adj_list)

    # Narysowanie grafu
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color = "#ff6d01", node_size = 500)
    nx.draw_networkx_labels(G, pos)
    plt.show()

    ranks_method1 = pagerank_randomwalk(G)
    sorted_nodes = sorted(ranks_method1, key=ranks_method1.get, reverse=True)

    # Wyniki metody korzystającej z błądzenia losowego
    print("Metoda 1 - Wierzchołki w porządku malejącym:")
    for node in sorted_nodes:
        print(f"Node: {node}, Rank: {ranks_method1[node]}")

    ranks_method2 = pagerank_matrix(G)
    sorted_nodes = sorted(ranks_method2, key=ranks_method2.get, reverse=True)

    # Wyniki metody korzystającej z macierzy
    print("Metoda 2 - Wierzchołki w porządku malejącym:")
    for node in sorted_nodes:
        print(f"Node: {node}, Rank: {ranks_method2[node]}")


