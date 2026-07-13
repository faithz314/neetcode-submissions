class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        
        cur = 0
        for i in range(len(nums)):
            if nums[i] != cur:
                return cur
            cur+=1

        return cur
        