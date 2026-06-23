from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need = Counter(s1)

        # for l in range(len(s2) - len(s1) + 1):
        #     window = Counter(s2[l:l+len(s1)])

        #     if window == need:
        #         return True

        # return False


# without counter:
        k = len(s1)

        target = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1

        for l in range(len(s2) - k + 1):
            window = [0] * 26

            for i in range(l, l + k):
                window[ord(s2[i]) - ord('a')] += 1

            if window == target:
                return True

        return False


# FIRST ATTEMPT
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1_set = set(s1)
#         print(s1_set)
#         l = 0

#         for r in range(len(s2)):
#             if s2[r] not in s1:
#                 l+=1
#                 continue

#             # while loop: while we're exploring a potentially new permutation
#             while s2[l] in s1:
#                 s1_set.remove(s2[l])
#                 l+=1
#             if not s1_set:
#                 return True
#             else:
#                 l = r
#                 s1_set = set(s1)

#         return False
        