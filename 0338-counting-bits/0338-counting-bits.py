class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        if n == 0:
            return [0]

        temp = 1

        for i in range(1, n+1):
            if i == temp:
                ans.append(1)
                temp *= 2
            else:
                ans.append(1+ans[i-temp//2])

        return ans