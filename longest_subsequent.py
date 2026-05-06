class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_sub = 1
        
        for num in num_set:
            if num - 1 in num_set:
                continue
            
            current_num = num
            current_sub = 1
            
            while current_num + 1 in num_set:
                current_sub += 1
                current_num += 1
            
            longest_sub  = max(longest_sub, current_sub)
        
        return longest_sub



sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
