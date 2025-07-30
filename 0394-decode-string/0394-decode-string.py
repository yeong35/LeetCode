class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ']':
                temp = ""
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()

                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop()+n
                
                if n != '':
                    stack.append(temp * int(n))
                else:
                    stack.append(temp)

            else:
                stack.append(i)

        return "".join(stack)