class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0 #pointer to the word "implementation"
        p2 = 0 #pointer to the abbr "i12n"

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2] == '0':
                return False
            if word[p1] == abbr[p2]:
                p1+=1
                p2+=1
            else:
                if abbr[p2].isalpha(): #if they don't match and it's a string
                    return False
                else:
                    # number case
                    num = ""
                    while p2 < len(abbr) and abbr[p2].isnumeric():
                        num+=abbr[p2]
                        p2+=1
                    p1 += int(num)
        if p1 == len(word) and p2 == len(abbr):
            return True
        return False



                


  