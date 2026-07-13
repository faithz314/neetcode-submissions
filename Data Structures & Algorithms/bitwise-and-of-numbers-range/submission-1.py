class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Bit manipulation optimized
        while left < right:
            right &= right - 1
        return right

        # Brute force solution
        res = left
        for i in range(left+1, right+1):
            res = res & i
        return res
        