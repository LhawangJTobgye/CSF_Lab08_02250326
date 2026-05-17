from collections import deque

graph = {
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

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbour in graph[start]:
        if neighbour not in visited:
            order.extend(dfs(graph, neighbour, visited))
    return order

bfs_order = " ".join(bfs(graph, 'A'))
dfs_order = " ".join(dfs(graph, 'A'))

print(f"{'Algorithm':<12} {'Data Structure':<20} {'Traversal Order':<20} {'Best For'}")
print("-" * 80)
print(f"{'BFS':<12} {'Queue':<20} {bfs_order:<20} Shortest path in unweighted graph")
print(f"{'DFS':<12} {'Stack / Recursion':<20} {dfs_order:<20} Exploring deep paths / cycle detection")