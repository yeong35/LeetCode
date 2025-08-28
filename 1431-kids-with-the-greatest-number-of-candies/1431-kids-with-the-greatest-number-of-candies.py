class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        maxCandies = max(candies)
        ans = [False]*n

        for i in range(n):
            ans[i] = True if candies[i]+extraCandies >= maxCandies else False

        return ans