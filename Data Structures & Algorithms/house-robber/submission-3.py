class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case: 1 house or 2 houses
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # recursive case
        # you can rob indices 1 3 5 7... or 0 2 4 6... or some combination: 1 4 6 ... etc
        # because of the combination, you will still need dp
        
        dp = [0]* len(nums)
        # best robbery combo at index i = best robbery combos of all indices before it (skip the one right before it)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[:i-1]) + nums[i]
        
        print(dp)
        return max(dp)


        