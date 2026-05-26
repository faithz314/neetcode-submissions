class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_list = list(order)

        for i in range(len(words)-1):
            cur, next = words[i], words[i+1]

            for char in range(min(len(cur), len(next))):
                if cur[char] == next[char]:
                    continue
                else:
                    curi = order_list.index(cur[char])
                    nexti = order_list.index(next[char])
                    if curi > nexti:
                        return False
                    else:
                        break
            if cur.startswith(next) and len(cur) > len(next):
                return False
            
        
        return True
        