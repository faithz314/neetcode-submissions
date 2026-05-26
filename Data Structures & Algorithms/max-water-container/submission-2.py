class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers: always move the shorter side inward
        best = 0
        l = 0
        r = len(heights) -1

        while l < r:
            currentWidth = min(heights[r], heights[l]) * (r-l)
            best = max(best, currentWidth)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
        return best













        