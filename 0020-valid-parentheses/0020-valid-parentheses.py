class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            
            if i == '(' or i=='{' or i=='[':
                stack.append(i)
            elif (i==')' or i=='}' or i==']') and len(stack)==0:
                return False
            elif (i==')' and stack[-1] == '(') or (i=='}' and stack[-1] == '{') or (i==']' and stack[-1] == '['):
                stack = stack[:-1]
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False