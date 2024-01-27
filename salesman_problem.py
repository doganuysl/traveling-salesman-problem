import itertools
import math

#distance between two points (cities)
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

#total distance of a path
def total_distance(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += distance(cities[path[i]], cities[path[i + 1]])
    return total

#the shortest path using brute force
def tsp_brute_force(cities):
    shortest_path = None
    shortest_distance = float('inf')
    all_paths = itertools.permutations(range(len(cities)))

    for path in all_paths:
        d = total_distance(path, cities)
        if d < shortest_distance:
            shortest_distance = d
            shortest_path = path

    return shortest_path, shortest_distance

#Example cities (coordinates)
cities = [(0, 0), (1, 2), (2, 4), (5, 2)]

#Find the shortest path using brute force
shortest_path, shortest_distance = tsp_brute_force(cities)
print("Shortest Tour Indices:", shortest_path)
print("Shortest Total Distance:", shortest_distance)
