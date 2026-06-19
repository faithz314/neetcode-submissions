class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        currentSet = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                currentSet.remove(nums[l])
                l+=1
            if nums[r] in currentSet:
                return True
            currentSet.add(nums[r])
        
        return False
        