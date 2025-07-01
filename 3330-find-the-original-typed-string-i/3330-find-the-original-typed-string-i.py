class Solution:
    def possibleStringCount(self, word: str) -> int:
        word = word+" "
        c = word[0]
        cnt = 0
        result = 0

        for i in word:
            if c != i:
                result += cnt-1
                c = i
                cnt = 0

            cnt += 1


        return result + 1