def display_graph(graph):
    print("Graph Representation:")
    for vertex in sorted(graph):
        print(f"  {vertex} -> {graph[vertex]}")

graph_a = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C'],
}

display_graph(graph_a)
