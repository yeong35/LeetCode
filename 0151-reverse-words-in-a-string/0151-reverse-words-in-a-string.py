class Solution:
    def reverseWords(self, s: str) -> str:

        result = ""
        temp = s.split()

        for i in temp[::-1]:
            result += i
            result += " "

        return result[:-1]