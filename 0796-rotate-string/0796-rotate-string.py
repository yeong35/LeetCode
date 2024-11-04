class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = []

        for i in range(len(s)):
            temp.append(s[i:]+s[:i])

        return goal in temp