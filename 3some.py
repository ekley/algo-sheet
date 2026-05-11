# return all the triplets that i != j, i != k , and j != k, and (num[i] + num[j] + num[k]) == 0

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0: # since nums array  is sorted if first element of the triple is greater than 0 then all the other elements of tiple will be greater than zero
                break

            if i == 0 or nums[i] != nums[i - 1]: # if two sibling elements are equal they will generated duplicate triple
                self.two_sum(nums, i, result)

        return result

    def two_sum(self, nums, i, result):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
          
nums = [-4, -1, -1, 0, 1, 2]
sol = Solution();
print(sol.threeSum(nums))

