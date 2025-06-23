class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatestNum = max(candies)

        for i in candies:
            if i+extraCandies >= greatestNum:
                result.append(True)
            else:
                result.append(False)
        return result
