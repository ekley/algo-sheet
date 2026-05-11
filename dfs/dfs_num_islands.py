def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(row, col):
        stack = [(row, col)]

        while stack:
            x, y = stack.pop()

            if (x < 0 or x >= rows or
                y < 0 or y >= cols):
                continue

            if grid[x][y] == 0 or (x, y) in visited:
                continue

            visited.add((x, y))

            # add 4-directional neighbors
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                count += 1

    return count