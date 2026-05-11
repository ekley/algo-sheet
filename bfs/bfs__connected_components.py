from collections import deque

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1

    return count


def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)


# Example graph (adjacency list)
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

print(connected_components_count(graph))  # 2