class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # BRUTE FORCE- O(n^2)
        # order_list = list(order)
        # for i in range(len(words)-1):
        #     cur, next = words[i], words[i+1]
        #     for char in range(min(len(cur), len(next))):
        #         if cur[char] == next[char]:
        #             continue
        #         else:
        #             curi = order_list.index(cur[char])
        #             nexti = order_list.index(next[char])
        #             if curi > nexti:
        #                 return False
        #             else:
        #                 break
        #     # note the startwsith function
        #     # this stops the case where "neetcode" comes before "neet"
        #     if cur.startswith(next) and len(cur) > len(next):
        #         return False
        # return True
        

        # SORTING O(nmlogn)
        order_index = {c: i for i, c in enumerate(order)}
        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)