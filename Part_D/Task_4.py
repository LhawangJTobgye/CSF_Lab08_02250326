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

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbour in graph[start]:
        if neighbour not in visited:
            order.extend(dfs(graph, neighbour, visited))
    return order
 
print("DFS Traversal starting from A:")
print(" ", " ".join(dfs(graph_cd, 'A')))