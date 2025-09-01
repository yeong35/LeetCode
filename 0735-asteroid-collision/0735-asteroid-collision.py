class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        collapsed = False

        for i in asteroids:
            collapsed = False

            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < -i:
                    stack.pop()
                elif stack[-1] > -i:
                    collapsed = True
                    break
                else:
                    stack.pop()
                    collapsed = True
                    break
            if not collapsed:
                stack.append(i)


        return stack