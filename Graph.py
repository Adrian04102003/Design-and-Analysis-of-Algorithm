graph = {

'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': [],
}

def display_graph(graph):
    for node in graph:
        print(node, "->", graph[node])
        
        display_graph(graph)