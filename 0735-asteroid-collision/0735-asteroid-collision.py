class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        collapsed = False

        for i in asteroids:
            collapsed = False
            while stack and stack[-1] > 0 and i < 0:
                if abs(stack[-1]) > abs(i):
                    collapsed = True
                    break
                elif abs(stack[-1]) == abs(i):
                    stack.pop()
                    collapsed = True
                    break
                else:
                    stack.pop()

            if not collapsed:
                stack.append(i)

        return stack