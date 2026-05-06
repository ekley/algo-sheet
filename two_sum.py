# Two Sum for un-sorted array

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums, start=1):
        need = target - num

        if need in seen:
            return [seen[num], i]

        seen[need] = i

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
            return [left + 1 , right + 1]
        elif sum < target:
            left +=1
        elif sum > target:
            right -=1 
    return None

res = sorted_two_sum([1, 2, 5, 6, 7, 11, 15], 9)
print(res)



