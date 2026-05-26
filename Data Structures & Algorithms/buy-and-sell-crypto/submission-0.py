class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # residual = 0

        # lowest = prices[0]
        
        # for price in prices:
        #     if price < lowest:
        #         lowest = price
        #     residual= max(residual, price-lowest)

        # return residual 


        #1: brute force solution would be to fix left pointer on an item and
        #compare it to each item in front of it. Keep track of the max profit. 

        max_profit= 0;
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if (prices[j]-prices[i])> max_profit:
                    max_profit= prices[j]-prices[i]
        return max_profit
        



