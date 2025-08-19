class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        dp = cost[:2]

        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2])+cost[i])

        return min(dp[-1], dp[-2])