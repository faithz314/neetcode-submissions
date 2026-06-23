class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        numElem = 0
        best = float('inf')
        l = 0
        
        for r in range(len(nums)):
            total += nums[r]
            numElem +=1

            while total >= target:
                best = min(best, numElem)
                total -= nums[l]
                numElem -=1
                l+=1
            
        
        return 0 if best == float('inf') else best        




        