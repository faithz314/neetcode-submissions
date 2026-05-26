class Solution:
    def findMin(self, nums: List[int]) -> int:

        # binary search with two pointers
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r)// 2 # same as mid = (l+r) //2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        