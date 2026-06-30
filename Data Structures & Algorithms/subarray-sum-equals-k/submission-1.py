from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # very similar to two sum!
        count = 0
        curSum = 0

        prefixSums = defaultdict(int)
        prefixSums[0] = 1 #prefixSums = {curSum : frequency}

        for num in nums:
            curSum += num
            count += prefixSums[curSum - k]
            prefixSums[curSum] += 1

        return count







        # brute force, time limit will exceed
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    res+=1
        return res

        