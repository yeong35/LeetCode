class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

        for i in range(1, 1+len(s1)):
            dp[0][i] = ord(s1[i-1])+dp[0][i-1]
        for i in range(1, 1+len(s2)):
            dp[i][0] = ord(s2[i-1])+dp[i-1][0]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1]==s2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(ord(s1[i-1])+dp[j][i-1], ord(s2[j-1])+dp[j-1][i])
        
        return dp[-1][-1]