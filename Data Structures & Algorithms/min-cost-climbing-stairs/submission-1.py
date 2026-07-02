class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # base case: 1 floor
        if len(cost) == 1:
            return cost[0]

        # recursive case: min cost of getting to floor n
        # = min cost to get to floor from n-1 or n-2
        
        cost.append(0) # this extra 0 is for reaching the top floor
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        print(dp)
        return dp[-1]