# Two Sum for un-sorted array

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i

    return None

res = two_sum_2([2, 3, 4, 7, 11, 15], 9)
print(res)


# Two Sum for sorted array

def sorted_two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        elif sum < target:
            left +=1
        elif sum > target:
            right -=1 
    return None

res = sorted_two_sum([1, 2, 5, 6, 7, 11, 15], 9)
print(res)



