class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            middle = (low+high)//2
            
            if middle*middle > x:
                high = middle-1
            else:
                low = middle+1

        
        return high
