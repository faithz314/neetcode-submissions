class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        s= sorted(s)
        t= sorted(t)

        for idx in range(len(s)):
            if s[idx] != t[idx]:
                return False
        return True

    