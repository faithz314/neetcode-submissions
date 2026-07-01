class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # solution:
        # go backwards
        # if nums2 < nums1 number, then move the nums1 number to the 0 slot


        p1 = len(nums1)-1
        p2 = len(nums2)-1
        i = m-1

        # start at the first non-zero number len(nums1) -len(nums2)
        while i >= 0 or p1 >= 0 or p2 >= 0:
            if i >= 0 and p2 >= 0:
                if nums1[i] > nums2[p2]:
                    nums1[p1] = nums1[i]
                    nums1[i] = 0
                    p1 -=1
                    i-=1
                elif nums1[i] <= nums2[p2]:
                    nums1[p1] = nums2[p2]
                    p1-=1
                    p2-=1
            else:
                if p2 >=0:
                    nums1[p1] = nums2[p2]
                    p1 -=1
                    p2 -=1
                else:
                    break
                    
