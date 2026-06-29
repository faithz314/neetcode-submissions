class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1

        while p1 < p2:
            if s[p1] != s[p2]:
                skipL = s[p1+1: p2+1]
                skipR = s[p1:p2]
                # will return False if skipL and skipR are both not palindromes
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            p1+=1
            p2-=1
        
        return True



        # # this greedy solution doesn't work because you could select the 
        # wrong letter first
        # s = '0' + s + '0'

        # p1, p2 = 0, len(s)-1
        # life = False
        # while p1 < p2:
        #     if s[p1] != s[p2]:
        #         if life == True:
        #             return False
        #         life = True

        #         if s[p1+1] == s[p2]:
        #             p1+=1
        #         elif s[p1] == s[p2-1]:
        #             p2 -=1
        #         else:
        #             return False
        #     p1+=1
        #     p2-=1
        
        # return True

        