from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # two strings must share the same repeating base in order to even be considered for gcd
        # example that doesn't work: "ABCD" and "ABAB" since you have to have s = t+t+t..+t

        if str1 + str2 != str2 + str1:
            return ""
        
        lesser = min(len(str1), len(str2))
        greater = max(len(str1), len(str2))
        while lesser != 0:
            greater, lesser = lesser, greater % lesser
        
        return str1[:greater]

        # convert each string to a number and find gcd between both numbers
        length = gcd(len(str1), len(str2))

        return str1[:length]