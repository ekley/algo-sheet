def find_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# inputs
nums = [-5, -1, 0, 3, 9, 12]
target = 9

# output
res = find_target(nums, target)

print(res)