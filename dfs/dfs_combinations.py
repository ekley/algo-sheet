def dfs_iterative_combinations(nums):
    result = []
    stack = [(0, [])]

    while stack:
        index, path = stack.pop()
    
        if path:
            result.append(path)

        for i in range(len(nums) - 1, index - 1, -1):
            stack.append((i + 1, path + [nums[i]]))

    return result


nums = [1, 2, 3]

print(dfs_iterative_combinations(nums))