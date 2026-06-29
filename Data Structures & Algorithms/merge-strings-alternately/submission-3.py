class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # an even better solution:
        n, m = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)

        # my solution:
        res = ''
        for i in range(min(len(word1), len(word2))):
            res+= word1[i]
            res+= word2[i]
        
        if len(word1) < len(word2):
            res+= word2[len(word1):]
        elif len(word1) > len(word2):
            res+= word1[len(word2):]

        return res

        