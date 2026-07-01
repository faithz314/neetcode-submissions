class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # cycle sort: place each number at it's actually correct index
        # this effectively ignores negatives, since we don't care about those anyways

        # value 1 -> index 0

        # nums = [1,2,4,5,6,3,-1] becomes nums = [1,2,3,4,5,6,-1]
        # 1 2 4 5 6 3 -1
        # 1 2 5 4 6 3 -1
        # 1 2 6 4 5 3 -1
        # 1 2 3 4 5 6 -1
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > len(nums):
                i+=1
            else:
                num = nums[i]
                nums[i], nums[num-1]= nums[num-1], nums[i]
                # duplicate check for [1, 1] case; we want to move i forward
                if nums[i] == nums[num-1]:
                    i+=1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1



        