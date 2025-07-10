class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)+1):
                t = s[i:j]
                if t == t[::-1] and len(t) > len(result):
                    result = t
        return result