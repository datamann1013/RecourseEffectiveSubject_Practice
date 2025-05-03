def dfs_recursive(graph, start):
    if start not in graph:
        raise KeyError(f"Start node '{start}' not in graph")
    visited = []

    def dfs(node):
        visited.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr)

    dfs(start)
    return visited

def dfs_iterative(graph, start):
    if start not in graph:
        raise KeyError(f"Start node '{start}' not in graph")
    visited, stack = [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for nbr in reversed(graph[node]):
                if nbr not in visited:
                    stack.append(nbr)
    return visited