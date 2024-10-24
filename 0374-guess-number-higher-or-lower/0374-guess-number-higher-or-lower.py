# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        guessed = guess(n)

        low = 0
        high = 2**31 - 1


        while guessed != 0:
            if guessed > 0:
                low = n+1
                n = (low+high)//2

            else:
                high = n-1
                n = (low+high)//2
            
            guessed = guess(n)
    
        return n
