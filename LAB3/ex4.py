import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from LAB3.ex3 import get_length_matrix
from LAB3.ex1 import draw_weighted_graph

def get_center_minmax(n):
    # Wykorzystanie zadania 3 do uzyskania macierzy odległości
    len_matrix, G = get_length_matrix(n)
    len_sum = np.zeros(n, dtype=int)
    len_max = np.zeros(n, dtype=int)
    # Znalezienie sumy i maximum odległości dla każdego wierzchołka
    for i in range(n):
        len_sum[i] = np.sum(len_matrix[i])
        len_max[i] = np.max(len_matrix[i])
    # print(len_matrix)
    # Znalezienie minimum z sum oraz maximów wierzchołków
    min_sum_center = np.min(len_sum)
    min_max_center = np.min(len_max)
    return min_max_center, min_sum_center, G

if __name__ == '__main__':
    min_max_center, min_sum_center, G = get_center_minmax(5)
    print(min_max_center)
    print(min_sum_center)
    draw_weighted_graph(G)

