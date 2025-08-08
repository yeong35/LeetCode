class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        arr = cost[:2]

        for i in range(2, len(cost)):
            arr.append(cost[i]+min(arr[i-2], arr[i-1]))

        return min(arr[-1], arr[-2])