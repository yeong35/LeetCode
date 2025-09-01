class Solution:
    def countBits(self, n: int) -> List[int]:
        power = 1

        ans = [0] * (n+1)

        for i in range(1, n+1):
            if power == i:
                ans[i] = 1
                power *= 2
            else:
                ans[i] = ans[i-power//2]+1
        return ans
