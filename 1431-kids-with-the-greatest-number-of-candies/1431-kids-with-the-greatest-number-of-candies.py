class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies)
        temp = 0

        for i, n in enumerate(candies):
            temp = candies[i] + extraCandies
            if greatest <= temp:
                result.append(True)
            else:
                result.append(False)    

        return result