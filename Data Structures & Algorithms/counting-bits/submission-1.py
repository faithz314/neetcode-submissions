class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        # hamming weight but modified
        for i in range(n+1):
            output.append(bin(i).count('1'))
        
        return output
            

        