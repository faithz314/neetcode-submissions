class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # loop backwards and remove any occurrences
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

        # can also just use list comprehension if not modifying in place:
        filtered_list = [item for item in nums if item != val]
        return len(filtered_list)

        