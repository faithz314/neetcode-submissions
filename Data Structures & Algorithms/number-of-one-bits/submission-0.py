class Solution:
    def hammingWeight(self, n: int) -> int:
        # n_string= str(n)
        # count=0
        # for item in n_string:
        #     if item == '0':
        #         count= count+1
        # return count
        return bin(n).count('1')
