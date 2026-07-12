class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a)-1
        j = len(b)-1
        overflow = 0

        while i >= 0 or j >= 0 or overflow > 0:
            if i >= 0:
                digitA = int(a[i])
            else:
                digitA = 0
            
            if j >= 0:
                digitB = int(b[j])
            else:
                digitB = 0
            
            total = digitA + digitB + overflow
            # % and // are the hacks here
            res.append(total % 2)
            overflow = total // 2

            i-=1
            j-=1
        
        res.reverse()
        return ''.join(map(str, res))
        
        


