class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        #brute force is literally checking every substring


        #optimal solution is a sliding window

        dict = {}

        l=0
        res= 0

        for r in range(len(s)):
            if s[r] in dict:
                l= max(dict[s[r]]+1, l)
            dict[s[r]]= r
            res = max(res, r-l+1)
        
        return res
