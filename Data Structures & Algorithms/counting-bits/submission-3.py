class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n+1):
            # output.append(bin(i).count('1'))
            res=0
            for j in range(32):
                if (i >> j) & 1:
                    res+=1
            output.append(res)
        return output
        