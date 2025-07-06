class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        crushed = False

        for a in asteroids:
            crushed = False
            while stack and (stack[-1] > 0 and a < 0):
                # print(stack)
                if -stack[-1] == a:
                    stack.pop()
                    crushed = True
                    break
                elif -stack[-1] < a:
                    crushed = True
                    break
                else:
                    stack.pop()
            if not crushed:
                stack.append(a)
                
        return stack