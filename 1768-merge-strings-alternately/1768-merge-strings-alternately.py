class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        result = ""

        n1 = len(word1)
        n2 = len(word2)

        while n1 > idx or n2 > idx:
            if idx < n1:
                result += word1[idx]
            if idx < n2:
                result += word2[idx]
            idx+=1

        return result