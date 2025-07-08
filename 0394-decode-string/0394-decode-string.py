class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = []
        n = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = []
                n = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()

                while stack and stack[-1].isdigit():
                    n.append(stack.pop())
                
                stack = stack + temp[::-1]*int("".join(n[::-1]))

        return "".join(stack)