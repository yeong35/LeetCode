class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        count = 0
        result = 0
        for i in range(0, k):
            if s[i] in vowels:
                count+=1
        
        result = max(count, result)
        
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            result = max(count, result)
        

        return result