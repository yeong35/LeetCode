class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        exploded = False
        for a in asteroids:
            exploaded = False
            while stack and stack[-1] > 0 and a < 0:
                if -stack[-1] < a:
                    exploaded = True
                    break
                elif -stack[-1] > a:
                    stack.pop()
                else:
                    stack.pop()
                    exploaded =True
                    break
            if not exploaded:
                stack.append(a)
        
        return stack