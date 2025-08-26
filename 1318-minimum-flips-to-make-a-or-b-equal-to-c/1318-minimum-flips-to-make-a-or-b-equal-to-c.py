class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        cnt = 0

        while a > 0 or b > 0 or c > 0:
            if c % 2 == 0:
                cnt = cnt + a%2 + b%2
            else:
                if a%2 == 0 and b%2==0:
                    cnt+=1
            
            a >>= 1
            b >>= 1
            c >>= 1


        return cnt