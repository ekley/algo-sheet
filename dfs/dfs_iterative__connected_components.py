def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs_iterative(graph, node, visited)
            count += 1

    return count


def dfs_iterative(graph, start, visited):
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            stack.append(neighbor)


# Example
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

print(connected_components_count(graph))  # 2