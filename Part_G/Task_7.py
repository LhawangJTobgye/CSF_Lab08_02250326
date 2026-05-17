from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
}

vertices = list(graph.keys())
edges = sum(len(v) for v in graph.values()) // 2
degrees = {v: len(neighbours) for v, neighbours in graph.items()}

visited = set()
queue = deque([vertices[0]])
visited.add(vertices[0])
while queue:
    node = queue.popleft()
    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            queue.append(n)
connected = len(visited) == len(vertices)

print(f"Number of vertices: {len(vertices)}")
print(f"Number of edges:    {edges}")
print("Degree of each vertex:")
for v in sorted(degrees):
    print(f"  {v}: {degrees[v]}")
print(f"The graph is {'connected' if connected else 'not connected'}.")
print("The graph is undirected.")