class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            res = num ^ res  # ^ is an exclusive or operator
            # used on bit manipulation
        
        return res
        