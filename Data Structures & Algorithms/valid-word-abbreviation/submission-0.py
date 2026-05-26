class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        p2 = 0

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2] == '0':
                return False
            
            # if they both match, move both pointers forward
            if word[p1] == abbr[p2]:
                p1 = p1 + 1
                p2 = p2 + 1
            # if they don't match but abbr is a letter
            elif abbr[p2].isalpha():
                return False
            # look for the complete integer substring (like 12 or 57)
            else:
                strLen = 0
                # find the complete length of the integer substring
                while p2 < len(abbr) and abbr[p2].isdigit():
                    strLen = strLen * 10 + int(abbr[p2])
                    p2+=1
                p1+= strLen

        if p1 == len(word) and p2 == len(abbr):
            return True
        return False        


        