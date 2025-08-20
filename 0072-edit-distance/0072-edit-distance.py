class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            dp[i+1][0] = i+1

        for i in range(m):
            dp[0][i+1] = i+1

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j])+1



        return dp[-1][-1]