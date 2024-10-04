def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)  
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)  
        stack.append(node)  

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

order = topological_sort(graph)
print("Topological Sort:", order)
