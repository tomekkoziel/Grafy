import random
import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_distance(point1, point2):
    """Funkcja oblicza odległość między dwoma punktami na płaszczyźnie"""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_path_length(path, distances):
    """Funkcja oblicza długość ścieżki"""
    length = 0
    n = len(path)
    for i in range(n - 1):
        length += distances[path[i]][path[i+1]]
    length += distances[path[-1]][path[0]]  # Odległość między ostatnim a pierwszym wierzchołkiem
    return length

def calculate_path_distance(points, path):
    """Oblicza całkowitą długość ścieżki przechodzącej przez punkty."""
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(points[path[i]], points[path[i + 1]])
    distance += calculate_distance(points[path[-1]], points[path[0]])
    return distance

def generate_initial_solution(n):
    """Funkcja generuje losowe początkowe rozwiązanie"""
    path = list(range(n))
    random.shuffle(path)
    return path

def metropolis_hastings_acceptance(distance_current, distance_new, temperature):
    """Oblicza prawdopodobieństwo akceptacji nowej ścieżki na podstawie algorytmu Metropolisa-Hastingsa."""
    if distance_new < distance_current:
        return True
    acceptance_probability = np.exp((distance_current - distance_new) / temperature)
    return np.random.rand() < acceptance_probability

def two_opt_swap(path, i, j):
    """Funkcja zamienia dwa wierzchołki na ścieżce przy użyciu operacji 2-opt"""
    new_path = path[:i] + path[i:j+1][::-1] + path[j+1:]
    return new_path



def simulated_annealing(points, max_iterations, initial_temperature):
    """Główna funkcja implementująca algorytm symulowanego wyżarzania"""
    # n = len(points)
    
    # # Obliczanie macierzy odległości między punktami
    # distances = [[calculate_distance(points[i], points[j]) for j in range(n)] for i in range(n)]
    
    # # Generowanie losowego początkowego rozwiązania
    # current_path = generate_initial_solution(n)
    # best_path = current_path.copy()
    
    # # Obliczanie długości aktualnej i najlepszej ścieżki
    # current_length = calculate_path_length(current_path, distances)
    # best_length = current_length
    
    # # Parametry symulowanego wyżarzania
    # temperature = initial_temperature
    temperature_decay = 0.99
    
    # Główna pętla algorytmu
    num_points = len(points)
    current_path = generate_initial_solution(num_points)
    best_path = current_path.copy()
    current_distance = calculate_path_distance(points, current_path)
    best_distance = current_distance
    temperature = initial_temperature

    for iteration in range(max_iterations):

        i = np.random.randint(0, len(current_path) - 1)
        j = np.random.randint(i + 1, len(current_path))

        new_path = two_opt_swap(current_path, i, j)
        new_distance = calculate_path_distance(points, new_path)

        if metropolis_hastings_acceptance(current_distance, new_distance, temperature):
            current_path = new_path
            current_distance = new_distance

        if current_distance < best_distance:
            best_path = current_path.copy()
            best_distance = current_distance

        temperature *= temperature_decay

    return best_path, best_distance

# Wczytywanie współrzędnych wierzchołków z pliku .dat
def read_points_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = line.strip().split(' ')
            points.append((float(x), float(y)))
    return points

# Rysowanie wszystkich wierzchołków na planszy kwadratowej


def plot_points(points, path=None):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)
    if path:
        path_x = [points[i][0] for i in path + [path[0]]]
        path_y = [points[i][1] for i in path + [path[0]]]
        plt.plot(path_x, path_y, color='red', linestyle='-', linewidth=1)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wierzchołki')
    plt.grid(True)
    plt.show()

# Przykładowe użycie algorytmu

file_path = 'data/input_150.dat'  # Ścieżka do pliku .dat
points = read_points_from_file(file_path)

max_iterations = 20000  # Maksymalna liczba iteracji
initial_temperature = 100.0  # Początkowa temperatura

best_path, best_length = simulated_annealing(points, max_iterations, initial_temperature)

print("Najkrótsza ścieżka:", best_path)
print("Długość ścieżki:", best_length)

plot_points(points, best_path)