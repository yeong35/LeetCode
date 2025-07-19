class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        crushed = False

        for i in asteroids:
            crushed = False
            
            if stack and stack[-1] > 0 and i < 0:

                while stack and stack[-1] > 0 and stack[-1] < -i:
                    stack.pop()
                if stack and stack[-1] == -i:
                    stack.pop()
                    crushed=True
                elif stack and stack[-1] > -i:
                    crushed=True
            

            if not crushed:
                stack.append(i)

        return stack