class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ""
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                
                stack.pop()

                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop()+n
                if n != "":
                    stack.append(int(n)*temp)
                else:
                    stack.append(temp)
                
        return "".join(stack)