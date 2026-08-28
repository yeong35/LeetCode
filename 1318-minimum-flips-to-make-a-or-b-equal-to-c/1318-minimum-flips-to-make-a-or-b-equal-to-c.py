class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0

        while c>0 or a>0 or b>0:

            if c%2 == 0:
                cnt += a%2+b%2
            else:
                if a%2 == 0 and b%2 == 0:
                    cnt += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return cnt