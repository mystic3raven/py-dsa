

# Bellman-Ford algorithm in Python

def bellman_ford(graph, start):
    # Initialize distances
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Check for negative weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances

# Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    #'C': {'A': 4, 'B': 2, 'D': 1},
    
    'D': {'B': 5, 'C': 1}
}
distances = bellman_ford(graph, 'A')
print("Shortest distances:", distances)
# Output: Shortest distances: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
