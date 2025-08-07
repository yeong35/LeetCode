class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]

        curr = 1
        for i in range(1, 201):
            curr*=i
            dp.append(curr)

        return dp[m+n-2]//(dp[m-1]*dp[n-1])