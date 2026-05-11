def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs_recursive(graph, node, visited)
            count += 1

    return count


def dfs_recursive(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)


# Example
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

print(connected_components_count(graph))  # 2