class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        s = set()
        temp = 1
        while temp <= 2**31-1:
            s.add(temp)
            temp *= 3

        return n in s