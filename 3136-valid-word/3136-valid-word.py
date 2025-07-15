class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        vowels = ['a','e','i','o','u']

        vowel = False
        consonant = False
        cnt = 0

        for i in word:
            if i.isdigit() or i.isalpha():
                if i in vowels:
                    vowel = True
                elif i.isalpha():
                    consonant = True
            else:
                return False
        
        return vowel and consonant and len(word) > 2


