from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hm = defaultdict(int)

        for bill in bills:
            hm[bill]+=1

            if bill == 20:
                # three 5s
                # one 5 and one 10
                if hm[5] >= 3:
                    hm[5]-=3
                elif hm[5] >=1 and hm[10]>=1:
                    hm[5]-=1
                    hm[10]-=1
                else:
                    return False
            
            if bill == 10:
                # one 5
                if hm[5] >= 1:
                    hm[5]-=1
                else:
                    return False
        return True
                

        