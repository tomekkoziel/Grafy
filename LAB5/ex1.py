import networkx as nx
import matplotlib.pyplot as plt
import random
    
def generate_random_flow_network(N):
    
    # Warunki dotyczące ilości warstw
    if N < 2:
        raise ValueError("Zbyt mało warstw pośrednich, minimalna ilość to dwie.")
    elif N > 4:
        raise ValueError("Zbyt wiele warstw pośrednich, maksymalna ilość to cztery.")
    
    G = nx.DiGraph()
    
    # Inicjalizacja warstw pośrednich wraz z ilością wierzchołków w każdej warstwie
    layers = [random.randint(2, N) for _ in range(N)]
    
    # Źródło (source node)
    node = 0
    G.add_node(node, layer = 0)
    
    # Wierzchołki w warstwach, gdzie layer określa warstwę (numerowany od 1)
    for i, num_nodes in enumerate(layers):
        layer = i + 1
        for _ in range(num_nodes):
            node += 1
            G.add_node(node, layer=layer)
            
    # Ujście (target node)
    G.add_node(node + 1, layer = N + 1)
    
    # Połączenie źródła (source) z wierzchołkami w pierwszej warstwie
    for i in range(layers[0]):
        G.add_edge(0, i + 1)
    
    # Połącznenie wierzchołków w N warstwie z ujściem (target)
    for i in range(layers[-1]):
        G.add_edge(len(G) - (i + 2), len(G) - 1) 
            
    for i in range(N - 1):
        current_layer = i + 1
        next_layer = i + 2
        
        current_layer_nodes = [node for node in G.nodes if G.nodes[node]['layer'] == current_layer]
        next_layer_nodes = [node for node in G.nodes if G.nodes[node]['layer'] == next_layer]

        # Połączenie losowego wierzchołka z warstwy i z losowym wierzchołkiem z warstwy i + 1
        source_nodes = random.sample(current_layer_nodes, k=len(current_layer_nodes))
        target_nodes = random.sample(next_layer_nodes, k=len(next_layer_nodes))

        for source_node in source_nodes:
            target_node = random.choice(target_nodes)
            G.add_edge(source_node, target_node)

        # Upewnienie się, że z każdego wierzchołka warstwy i wychodzi co najmniej jeden łuk
        for source_node in current_layer_nodes:
            if not G.out_edges(source_node):
                target_node = random.choice(next_layer_nodes)
                G.add_edge(source_node, target_node)

        # Upewnienie się, że do każdego wierzchołka warstwy i + 1 wchodzi co najmniej jeden łuk
        for target_node in next_layer_nodes:
            if not G.in_edges(target_node):
                source_node = random.choice(current_layer_nodes)
                G.add_edge(source_node, target_node)
        
    # Dodanie 2N krawędzi do niepołączonych wierzchołków, obsługiwany jest również przypadek pesymistyczny, kiedy wszystkie krawędzie są już dodane, wtedy po 1000 próbach pętla się kończy
    added_edges = 0
    checker = 0
    while added_edges < 2 * N:
        checker += 1
        i, j = random.randint(1, len(G) - 2), random.randint(1, len(G) - 2)
        if (i != j) and (i != 0) and (j != len(G) - 1) and not G.has_edge(i, j) and not G.has_edge(j, i):
            G.add_edge(i, j)
            
        if checker == 1000:
            break
            
    # Dodanie wagi z przedziału [1, 10] do każdej krawędzi
    for edge in G.edges:
        G.edges[edge]['capacity'] = random.randint(1, 10)  

    return G

def draw_flow_network(G):
    # Multipartite layout rozkłada wierzchołki w prostych liniach za pomocą subset_key, w naszym przypadku to warstwy
    pos = nx.multipartite_layout(G, subset_key="layer")
    node_labels = {node: str(node) for node in G.nodes}
    edge_labels = {(u, v): G.edges[u, v]['capacity'] for u, v in G.edges}

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()
    
    # Testowanie
    # plt.savefig("network.jpg")

if __name__ == '__main__':
    number_of_layers = 2  
    G = generate_random_flow_network(number_of_layers)
    draw_flow_network(G)