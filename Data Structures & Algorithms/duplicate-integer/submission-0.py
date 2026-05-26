class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         nums2= []

         for item in nums:
            if item in nums2:
                return True
            else:
                nums2.append(item)
        
         return False