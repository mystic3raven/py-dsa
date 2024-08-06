from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Usage
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
print("BFS traversal:")
bfs(graph, 0)
# Output: BFS traversal:
# 0 1 2 3
