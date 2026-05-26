class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = nums[::]
        nums_final = nums + nums_copy
        return nums_final