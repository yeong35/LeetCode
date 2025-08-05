class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s)-1
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        while left < right:
            while s[left].lower() not in vowels and left < right:
                left += 1
            while s[right].lower() not in vowels and left < right:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)