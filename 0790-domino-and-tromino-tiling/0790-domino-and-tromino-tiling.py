class Solution:
    def numTilings(self, n: int) -> int:
        mod = pow(10, 9)+7

        arr = [1, 2, 5]

        for i in range(3, 1000):
            arr.append((arr[i-1]*2+arr[i-3])%mod)
        
        return arr[n-1]