class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            alphabet = [0]*26

            for w in word:
                alphabet[ord(w)-ord('a')] += 1
            
            return alphabet

        answer = []
        b = [0]*26

        for word in words2:
            for i, c in enumerate(count(word)):
                b[i] = max(b[i], c)
        
        for word in words1:
            if all(x >= y for x,y in zip(count(word), b)):
                answer.append(word)

        return answer