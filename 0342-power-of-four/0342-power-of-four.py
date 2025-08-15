class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        temp = 1
        while temp <= n:
            if temp == n:
                return True
            temp *= 4

        return False