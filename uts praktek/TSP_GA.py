import random
import numpy as np

# Contoh koordinat kota (x, y)
cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 4),
    'D': (1, 6),
    'E': (7, 2)
}

# Hitung jarak Euclidean antar dua kota
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Hitung total jarak rute
def route_distance(route):
    dist = 0
    for i in range(len(route)):
        dist += distance(route[i], route[(i + 1) % len(route)])
    return dist

# Inisialisasi populasi
def initial_population(pop_size):
    city_list = list(cities.keys())
    return [random.sample(city_list, len(city_list)) for _ in range(pop_size)]

# Seleksi berdasarkan fitness (jarak terpendek)
def selection(population):
    sorted_pop = sorted(population, key=route_distance)
    return sorted_pop[:len(population)//2]

# Crossover: Order Crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    fill = [city for city in parent2 if city not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child

# Mutasi: Tukar dua kota
def mutate(route, mutation_rate=0.1):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route

# Algoritma GA utama
def genetic_algorithm(generations=100, pop_size=20):
    population = initial_population(pop_size)
    for gen in range(generations):
        selected = selection(population)
        children = []
        while len(children) < pop_size:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            children.append(child)
        population = children
        best_route = min(population, key=route_distance)
        print(f"Gen {gen+1}: Jarak = {route_distance(best_route):.2f}, Rute = {best_route}")
    return best_route

# Jalankan algoritma
optimal_route = genetic_algorithm()
print("\nRute optimal:", optimal_route)
