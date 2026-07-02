class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        s = ''
        for c in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][c] != strs[-1][c]:
                return s
            s+= strs[0][c]
        
        return s
        