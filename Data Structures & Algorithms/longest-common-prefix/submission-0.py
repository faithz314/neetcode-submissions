class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the list
        strs.sort()

        # compare similarity for first and last word (most different)
        prefix = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                prefix+= strs[0][i]
            else:
                break

        return prefix
        