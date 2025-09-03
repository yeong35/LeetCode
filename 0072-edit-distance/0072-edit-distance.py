class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            dp[i+1][0] = i+1
        for i in range(n):
            dp[0][i+1] = i+1

        for i in range(m):
            for j in range(n):

                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1

        return dp[-1][-1]