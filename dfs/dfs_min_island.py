def min_island(grid):
    visited = set()
    smallest = float('inf')

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):

            size = dfs_iterative(grid, r, c, visited)

            if size > 0:
                smallest = min(smallest, size)

    return smallest
            
    


def dfs_iterative(grid, start_row, start_col, visited):
    # bound check
    if start_row < 0 or start_row > len(grid) or start_col < 0 or start_col > len(grid[0]):
        return 0
    
    # water check
    if grid[start_row][start_col] == 'w':
        return 0
    
    # visited check
    if (start_row, start_col) in visited:
        return 0
        
    stack = [(start_row, start_col)]
    size = 0
    
    while stack:
        r, c = stack.pop()

        # bound check
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        
        # water check
        if grid[r][c] == 'w':
            continue
        
        # visited check
        if (r, c) in visited:
            continue
        
        visited.add((r, c))
        size += 1
        
        # push neighbors
        stack.append((r - 1, c))  # up
        stack.append((r + 1, c))  # down
        stack.append((r, c - 1))  # left
        stack.append((r, c + 1))  # right
        
    return size
        


# Example
grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w'],
]

print(min_island(grid))  # 2