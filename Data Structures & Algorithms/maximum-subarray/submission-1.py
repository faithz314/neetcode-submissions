class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best = min(nums)
        for i in range(len(nums)):

            sm = 0
            for j in range(i, len(nums)):
                sm+= nums[j]
                best = max(sm, best)
        
        return best

        