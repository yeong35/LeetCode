class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        n, m = 0, 0

        while n < len(word1) or m < len(word2):
            if n < len(word1):
                ans.append(word1[n])
                n+=1
            
            if m < len(word2):
                ans.append(word2[m])
                m+=1
        
        return "".join(ans)
            
            