from collections import deque

def display_graph(graph):
    print("Graph Representation:")
    for vertex in sorted(graph):
        print(f"  {vertex} -> {graph[vertex]}")

graph_cd = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
}
 
def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order
 
print("BFS Traversal starting from A:")
print(" ", " ".join(bfs(graph_cd, 'A')))