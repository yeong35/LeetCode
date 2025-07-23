class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        stack = []
        if x > y:
            for i in s:
                if stack and stack[-1] == 'a' and i == 'b':
                    score += x
                    stack.pop()
                else:
                    stack.append(i)
            
            s = "".join(stack)
            stack = []

            for i in s:
                if stack and stack[-1] == 'b' and i == 'a':
                    score += y
                    stack.pop()
                else:
                    stack.append(i)

        else:
            for i in s:
                if stack and stack[-1] == 'b' and i == 'a':
                    score += y
                    stack.pop()
                else:
                    stack.append(i)
            
            s = "".join(stack)
            stack = []

            for i in s:
                if stack and stack[-1] == 'a' and i == 'b':
                    score += x
                    stack.pop()
                else:
                    stack.append(i)

        return score