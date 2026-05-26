class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        p1= 0

        #edge case
        if nums[0] != 0:
            return 0
        if nums[-1]!= len(nums):
            return len(nums)        

        for p2 in range(1, len(nums)):
            if nums[p2]-nums[p1]>1:
                return (nums[p1]+1)
            p1= p1 +1

        

        return 0