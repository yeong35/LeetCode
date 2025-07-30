class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        crushed = False

        for i in asteroids:
            crushed = False

            while stack and stack[-1] > 0 and i < 0:
                if abs(stack[-1]) > abs(i):
                    crushed = True
                    break
                elif abs(stack[-1]) == abs(i):
                    stack.pop()
                    crushed = True
                    break
                else:
                    stack.pop()
            
            if not crushed:
                stack.append(i)


        return stack
                