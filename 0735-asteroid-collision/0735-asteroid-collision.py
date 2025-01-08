class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        boom = False

        for i in asteroids:
            boom = False
            if len(result) == 0:
                result.append(i)
            else:
                # positive
                if i > 0:
                    result.append(i)
                
                # asteroid is negative
                else:
                    while len(result) > 0 and result[-1] > 0:
                        # same speed
                        if result[-1] == abs(i):
                            result = result[:-1]
                            boom = True
                            break
                        # small
                        elif result[-1] < abs(i):
                            result = result[:-1]
                        # big
                        else:
                            boom = True
                            break
                    if not boom:
                        result.append(i)
        return result