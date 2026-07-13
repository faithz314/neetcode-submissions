class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) and O(1)
        # Use XOR cancel out property => if a number is missing it won't cancel out
        res = 0
        for i in range(len(nums)):
            res = (i+1)^nums[i]^res
        return res










        # sorting brute force
        # nums.sort()
        # if nums[0] != 0:
        #     return 0
        # cur = 0
        # for i in range(len(nums)):
        #     if nums[i] != cur:
        #         return cur
        #     cur+=1
        # return cur
        