class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        #brute force is to check every pairing

        maxsum= 0
        width=0
        length =0
        product = 0

        for p1 in range(len(heights)):
            for p2 in range(p1, len(heights)):
                width= p2 -p1
                length = min(heights[p1], heights[p2])
                product = width * length

                if product > maxsum:
                    maxsum= product
        return maxsum

