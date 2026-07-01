class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        # greedy algorithm -> buy on day i and sell on day i+1
        l = 0
        r = 0
        best = 0

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            if prices[r] > prices[l]:
                best += prices[r]-prices[l]
                l = r
            r+=1
        return best