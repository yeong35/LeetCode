class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        
        for i in range(31):
            if c%2 == 1 and a%2==0 and b%2==0:
                cnt+=1
            elif c%2 == 0:
                if a%2 == 1 and b%2==1:
                    cnt+=2
                elif a%2==1 or b%2==1:
                    cnt+=1
                
            a = a>>1
            b = b>>1
            c = c>>1

        return cnt