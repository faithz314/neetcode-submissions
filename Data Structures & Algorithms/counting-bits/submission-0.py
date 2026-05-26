class Solution:
    def countBits(self, n: int) -> List[int]:
        onecount_array= []
        onecount=0
        for num in range(n+1):
            onecount= bin(num).count('1')
            onecount_array.append(onecount)

        return onecount_array