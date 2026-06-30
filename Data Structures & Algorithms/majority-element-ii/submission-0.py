from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1
        
        res = []
        for key, value in hm.items():
            if value > k:
                res.append(key)
        
        return res
