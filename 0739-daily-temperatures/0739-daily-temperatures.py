class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        n = len(temperatures)
        ans = [0]*n

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                prev = stack.pop()[1]
                ans[prev] = i-prev
            stack.append([temperatures[i], i])

        return ans