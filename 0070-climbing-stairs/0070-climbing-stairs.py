class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        for i in range(2, 45):
            arr.append(arr[i-2]+arr[i-1])
        return arr[n-1]