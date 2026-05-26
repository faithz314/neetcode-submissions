class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Option 1: lowkey brute force check every substring

        # Option 2: two pointers with a map
        hm = {}
        maxL = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hm:
                l = max(l, hm[s[r]]+1) 
            hm[s[r]]=r
            maxL= max(maxL, r-l+1)
        return maxL