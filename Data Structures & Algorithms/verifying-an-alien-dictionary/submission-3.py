class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # My solution but slightly more optimized
        # order_list = list(order)
        # for i in range(len(words)-1):
        #     cur, next = words[i], words[i+1]
        #     for char in range(len(cur)):
        #         # if neetcode comes before neet
        #         if char == len(next):
        #             return False
                
        #         if cur[char] != next[char]:
        #             if order_list.index(cur[char]) > order_list.index(next[char]):
        #                 return False
        #             break
        # return True
        

        # SORTING O(nmlogn)
        order_index = {c: i for i, c in enumerate(order)}
        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)