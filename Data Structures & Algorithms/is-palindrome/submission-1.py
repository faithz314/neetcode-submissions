class Solution:
    def isPalindrome(self, s: str) -> bool:

        str2= ''

        for char in s:
            if char.isalpha() or char.isnumeric():
                str2= str2+ char.lower()

        p2 = len(str2) -1

        for p1 in range(len(str2)//2):
            if str2[p1]!= str2[p2]:
                return False
            p2= p2-1
        
        return True
