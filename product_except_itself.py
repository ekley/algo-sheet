def productExceptSelf(nums):
    result = [1] * len(nums)

    # product of nums on the left side of current num
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # product of nums on the right side of current num
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

print(productExceptSelf([1, 2, 3, 4]))

# Time complexity O(n)
# Space complexity O(n)