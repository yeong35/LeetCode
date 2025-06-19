class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        result = []

        while idx < len(word1) or idx < len(word2):
            if idx < len(word1):
                result.append(word1[idx])
            if idx < len(word2):
                result.append(word2[idx])
            
            idx+=1
        
        return "".join(result)