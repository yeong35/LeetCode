class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        elif n == 3:
            return 5
        
        modulo = 10**9+7

        arr = [1, 2, 5]

        for i in range(3, n):
            arr.append((arr[i-3]+arr[i-1]*2)%modulo)

        return arr[-1]


