class Solution:
    def makeFancyString(self, s: str) -> str:
        prevCharacter = s[0]
        cnt = 0

        result = []

        for i in s:
            if i == prevCharacter:
                cnt += 1
            else:
                prevCharacter = i
                cnt = 1
            
            if cnt < 3:
                result.append(i)
            else:
                continue

        return "".join(result)

