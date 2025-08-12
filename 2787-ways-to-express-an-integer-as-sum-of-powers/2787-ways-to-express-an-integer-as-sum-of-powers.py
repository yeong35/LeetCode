class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def powers(target, x, n):
            if target < 0:
                return 0
            elif target > 0:
                cnt = 0

                for i in range(n+1, target+1):
                    cnt += powers(target-pow(i,x), x, i)
                
                return cnt
            else:
                return 1

        return powers(n, x, 0)