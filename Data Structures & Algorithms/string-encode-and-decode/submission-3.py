class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded+= str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            length = 0
            while s[p2] != '#':
                length = length*10 + int(s[p2])
                p2+=1
            p1 = p2+1
            p2 = p1 + length
            decoded.append(s[p1:p2])
            p1 = p2
        
        return decoded


        
