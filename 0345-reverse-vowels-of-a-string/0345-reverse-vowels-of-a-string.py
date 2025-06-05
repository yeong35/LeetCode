class Solution:
    def reverseVowels(self, s: str) -> str:
        def vowel(c):
            check = ['a', 'e', 'i', 'o', 'u']
            if c.lower() in check:
                return True
            return False

        head = 0
        rear = len(s)-1
        s = list(s)

        while head < rear:
            v1 = vowel(s[head])
            v2 = vowel(s[rear])
            print(s[head], s[rear])
            if v1 and v2:
                temp = s[head]
                s[head] = s[rear]
                s[rear] = temp
                head += 1
                rear -= 1

            if not v1:
                head += 1
            if not v2:
                rear -= 1
        
        return "".join(s)