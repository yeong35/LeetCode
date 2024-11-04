class Solution:
    def makeFancyString(self, s: str) -> str:

        if len(s) < 3:
            return s

        result = [s[0], s[1]]

        for i in range(2, len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            else:
                result.append(s[i])

        return "".join(result)