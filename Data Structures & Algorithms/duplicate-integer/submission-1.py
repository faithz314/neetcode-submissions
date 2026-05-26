class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         nums2= set()

         for item in nums:
            if item in nums2:
                return True
            else:
                nums2.add(item)
        
         return False