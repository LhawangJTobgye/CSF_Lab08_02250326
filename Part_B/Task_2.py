def display_graph(graph):
    print("Graph Representation:")
    for vertex in sorted(graph):
        print(f"  {vertex} -> {graph[vertex]}")

def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []
 
def add_edge(graph, u, v):
    add_vertex(graph, u)
    add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)
 
graph_b = {}
for v in ['A', 'B', 'C', 'D']:
    add_vertex(graph_b, v)
for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D')]:
    add_edge(graph_b, u, v)
display_graph(graph_b)
