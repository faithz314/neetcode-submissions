class Solution:
    def findMin(self, nums: List[int]) -> int:



        #the solution is a binary search with 2 pointers

        p1 = 0
        p2 = len(nums)-1

        while p1 < p2:
            mid = p1 + (p2 -p1) //2
            if nums[mid] < nums[p2]:
                p2 = mid
            else:
                p1 = mid + 1

        return nums[p1]




        