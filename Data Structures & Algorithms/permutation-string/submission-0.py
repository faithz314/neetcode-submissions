from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        k = len(s1)

        for l in range(len(s2) - k + 1):
            window = Counter(s2[l:l+k])

            if window == need:
                return True

        return False